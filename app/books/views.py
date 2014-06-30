#-*-coding: utf-8 -*-
from flask import (Blueprint, render_template, request, jsonify, url_for)
from app import db
from app.views import BaseTableView

from app.books.models import Book
from app.books.forms import BookForm

mod = Blueprint('books', 
                __name__, 
                url_prefix='/books', 
                template_folder='templates')

@mod.route('/')
def book_list():
    return render_template("books/book_list.html")

@mod.route('/book_table/')
def book_table():
    table_view = BookTableView()
    return table_view.render_to_response()

class BookTableView(BaseTableView):
    model = Book
    
    columns_map = {
        '0': 'id',
        '1': 'name',
    }

def render_form(form, path):
    context = {
        'form': form,
        'path': path
    }
    form_html = render_template('books/_add_form.html', **context)
    return form_html

@mod.route('/get_add_form/')
def get_add_form():
    form = BookForm()
    path = url_for('books.add_book')
    return render_form(form, path)
    
@mod.route('/add_book/', methods=['POST'])
def add_book():
    form = BookForm(request.form)
    if form.validate_on_submit():
        book = Book(name=form.name.data)
        book.authors.extend(form.authors.data)
        db.session.add(book)
        db.session.commit()
        return jsonify({'status': 'success'})
    
    path = url_for('books.add_book')
    return jsonify({'status': 'fail', 'form_html':render_form(form, path)})        

@mod.route('/book_info/')
def book_info():
    book_id = int(request.args.get('item_id'))
    book = Book.query.get(book_id)
    context = {'book': book}
    return render_template('books/book_info.html', **context)
    
@mod.route('/remove_book/', methods=['POST'])
def remove_book():
    book_id = int(request.form.get('item_id'))
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return ''

@mod.route('/get_edit_form/')
def get_edit_form():
    item_id = int(request.args.get('item_id'))
    book = Book.query.get(item_id)
    form = BookForm(obj=book)
    path = url_for('books.edit_book')
    return render_form(form, path)

@mod.route('/edit_book/', methods=['POST'])
def edit_book():
    book_id = request.form.get('id')
    book = Book.query.get(book_id)
    form = BookForm(request.form, obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        return jsonify({'status': 'success'})
    
    path = url_for('books.edit_book')
    return jsonify({'status': 'fail', 'form_html':render_form(form, path)})        
    
    
    

    
    
    