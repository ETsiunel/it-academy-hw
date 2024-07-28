"""Library keywords"""

from library import User, Book
from my_logger import setup_logging

log = setup_logging()


books = {}
users = {}


def create_book(title, author, pages, isbn):
    books[title] = Book(title, author, pages, isbn)


def create_user(name):
    users[name] = User(name)


def reserve_book(user_name, book_title):
    user = users[user_name]
    book = books[book_title]
    user.reserve_book(book)


def take_book(user_name, book_title):
    user = users[user_name]
    book = books[book_title]
    user.take_book(book)


def return_book(user_name, book_title):
    user = users[user_name]
    book = books[book_title]
    user.return_book(book)


def book_should_be_reserved(book_title):
    book = books[book_title]
    assert book.reserved, f"Book {book_title} is not reserved"


def book_should_not_be_reserved(book_title):
    book = books[book_title]
    assert not book.reserved, f"Book {book_title} is reserved"


def book_should_be_in_use(book_title):
    book = books[book_title]
    assert book.in_use, f"Book {book_title} is not in use"


def book_should_not_be_in_use(book_title):
    book = books[book_title]
    assert not book.in_use, f"Book {book_title} is in use"


def user_should_have_book(user_name, book_title):
    user = users[user_name]
    book = books[book_title]
    assert book in user.taken_books, (f"User {user_name} "
                                      f"does not have book {book_title}")


def user_should_not_have_book(user_name, book_title):
    user = users[user_name]
    book = books[book_title]
    assert book not in user.taken_books, (f"User {user_name} "
                                          f"has book {book_title}")
