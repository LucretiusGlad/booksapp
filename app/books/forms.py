#-*-coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField 
from wtforms.validators import DataRequired
from app.authors.models import Author

REQUIRED_MESSAGE = u"Поле обязательно для заполнения"

class BookForm(Form):
    id = HiddenField()
    
    name = StringField(
        label=u'Название', validators=[DataRequired(message=REQUIRED_MESSAGE)])
    
    authors = QuerySelectMultipleField(
        label=u'Авторы',
        query_factory=lambda: Author.query.all(),
        get_label=lambda a: a.name,
        validators=[])