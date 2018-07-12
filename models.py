#! /venv/bin/python
#from book import db
from book import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
#BookStore = db.Table('BookStore',
#                  db.Column('id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
#                  db.Column('id', db.Integer, db.ForeignKey('store.id'), primary_key=True)
#)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    b_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
#    BookStore = db.relationship('Store', secondary=BookStore, lazy='subquery',
#                          backref=db.backref('book', lazy=True))

    def __init__(self, b_name, author, price):
        self.b_name = b_name
        self.author = author
        self.price = price

    def __repr__(self):
        return '<Book %r>' % self.b_name

#class Store(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    store_name = db.Column(db.String(40), unique=True, nullable=False)
#    location = db.Column(db.String(50), nullable=False)
