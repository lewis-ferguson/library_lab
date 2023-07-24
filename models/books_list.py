from models.book import Book


book1 = Book("Harry Potter", "J.K Rowling", "Fantasy")
book2 = Book("Percy Jackson", "Rick Riordan", "Adventure")

books =[book1, book2]

def add_new_book(book):
    books.append(book)
    
def remove_book(title):
    for book in books:
        if book.title == title:
            books.remove(book)    