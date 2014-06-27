#-*-coding: utf-8-*-
from app import db
from flaskext.babel import gettext as _

class Book(db.Model):
    
    __tablename__ = 'books_book'
    
    id = db.Column(
        db.Integer, 
        primary_key=True)
    
    name = db.Column(
        db.String(255))
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Book {0}>'.format(self.name)    
    