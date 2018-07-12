#! /venv/bin/python
from flask import Blueprint
from models import *
from book import *

red = Blueprint('data', __name__, template_folder='templates')

@red.route('/book_add', methods=['POST', 'GET'])
def book_add():
    book = Book(request.form['b_name'], request.form['author'], request.form['price'])
    db.session.add(book)
    db.session.commit()
    books = Book.query.all()
    return render_template('add_book.html', books=books)

@red.route('/getBook', methods=['POST', 'GET'])
def getBook():
    id=request.args.get('book_details')
    data = db.session.query(Book).filter_by(id=id).first()
    print(id)
    print(data.b_name)
    return render_template('update.html', data_id = data.id, data_title=data.b_name, data_author=data.author, data_price=data.price)

@red.route('/update', methods=['GET','POST'])
def update():
    id = request.form.get('data_id')
    final_title = request.form.get('b_name')
    final_author = request.form.get('oldauthor')
    print(final_author)
    final_price = request.form.get('oldprice')
    book = db.session.query(Book).filter_by(id=id).first()
    book.b_name = final_title
    book.author = final_author
    book.price = final_price
    print(id)
    print(book.b_name)
    db.session.commit()

    return render_template('add_book.html')

@red.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    id = request.args.get('del_book')
    print(id)
    book = Book.query.filter_by(id=id).delete()
    db.session.commit()
    return render_template('add_book.html')
