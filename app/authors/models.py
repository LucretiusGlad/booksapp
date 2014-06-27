#-*-coding: utf-8-*-
from app import db
from flaskext.babel import gettext as _

books = db.Table(
    'authors_books',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')))

class Author(db.Model):
    
    __tablename__ = 'authors_author'
    
    id = db.Column(
        db.Integer, 
        primary_key=True)
    
    name = db.Column(
        db.String(255))
    
    books = db.relationship('books.Book', secondary=books,
        backref=db.backref('authors', lazy='dynamic'))
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Author {0}>'.format(self.name)    
    