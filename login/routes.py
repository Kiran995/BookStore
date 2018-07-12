#! /usr/bin/python
from flask import Blueprint
from flask import request, render_template
from models import *

blue = Blueprint('login', __name__, template_folder='templates')

@blue.route('/home')
def home():
    return render_template('home_page.html')

@blue.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        books = Book.query.all()
        return render_template('add_book.html', books=books)
    else:
        return render_template('home_page.html')
