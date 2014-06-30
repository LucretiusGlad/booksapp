#-*-coding: utf-8 -*-
from flask import (Blueprint, render_template, request, jsonify, url_for)
from app import db
from app.views import BaseTableView

from app.authors.models import Author
from app.authors.forms import AuthorForm

mod = Blueprint('authors', 
                __name__, 
                url_prefix='/authors', 
                template_folder='templates')

@mod.route('/')
def author_list():
    return render_template("authors/author_list.html")

@mod.route('/author_table/')
def author_table():
    table_view = AuthorTableView()
    return table_view.render_to_response()

class AuthorTableView(BaseTableView):
    model = Author
    
    columns_map = {
        '0': 'id',
        '1': 'name',
    }

def render_form(form, path):
    context = {
        'form': form,
        'path': path
    }
    form_html = render_template('authors/_add_form.html', **context)
    return form_html

@mod.route('/get_add_form/')
def get_add_form():
    form = AuthorForm()
    path = url_for('authors.add_author')
    return render_form(form, path)
    
@mod.route('/add_author/', methods=['POST'])
def add_author():
    form = AuthorForm(request.form)
    if form.validate_on_submit():
        author = Author(name=form.name.data)
        author.books.extend(form.books.data)
        db.session.add(author)
        db.session.commit()
        return jsonify({'status': 'success'})
    
    path = url_for('authors.add_author')
    return jsonify({'status': 'fail', 'form_html':render_form(form, path)})        

@mod.route('/author_info/')
def author_info():
    author_id = int(request.args.get('item_id'))
    author = Author.query.get(author_id)
    context = {'author': author}
    return render_template('authors/author_info.html', **context)
    
@mod.route('/remove_author/', methods=['POST'])
def remove_author():
    author_id = int(request.form.get('item_id'))
    author = Author.query.get(author_id)
    db.session.delete(author)
    db.session.commit()
    return ''

@mod.route('/get_edit_form/')
def get_edit_form():
    item_id = int(request.args.get('item_id'))
    book = Author.query.get(item_id)
    form = AuthorForm(obj=book)
    path = url_for('authors.edit_author')
    return render_form(form, path)

@mod.route('/edit_author/', methods=['POST'])
def edit_author():
    book_id = request.form.get('id')
    book = Author.query.get(book_id)
    form = AuthorForm(request.form, obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        return jsonify({'status': 'success'})
    
    path = url_for('author.edit_book')
    return jsonify({'status': 'fail', 'form_html':render_form(form, path)})        
    
    
    

    
    
    