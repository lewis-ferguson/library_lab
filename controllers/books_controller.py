from flask import render_template, Blueprint, request, redirect
from models.books_list import books, add_new_book, remove_book
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    return render_template('index.jinja', title = 'Books', books = books)


@books_blueprint.route('/books/<index>')
def show(index):
  chosen_book = books[int(index)]
  return render_template('book.jinja', title="{{book.title}}", book = chosen_book)

@books_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return render_template('index.jinja', title='Books', books = books)

@books_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
  remove_book(title)
  return redirect('/books')    