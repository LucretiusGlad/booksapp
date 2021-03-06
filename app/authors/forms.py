#-*-coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField 
from wtforms.validators import DataRequired
from app.books.models import Book

REQUIRED_MESSAGE = u"Поле обязательно для заполнения"

class AuthorForm(Form):
    id = HiddenField()
    
    name = StringField(
        label=u'Название', validators=[DataRequired(message=REQUIRED_MESSAGE)])
    
    books = QuerySelectMultipleField(
        label=u'Книги',
        query_factory=lambda: Book.query.all(),
        get_label=lambda a: a.name,
        validators=[])