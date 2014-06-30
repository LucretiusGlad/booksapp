#-*-coding: utf-8-*-
from app import db

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
        return u'<Book {0}>'.format(self.id)
    