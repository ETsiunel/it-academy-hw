"""Homework_11"""

# # # Библиотека # # #
# Создайте класс book с именем книги, автором, кол-м страниц,
# ISBN, флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь,
# который может брать книгу, возвращать, бронировать.
# Если другой пользователь хочет взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).

from hw_20.my_logger import logger as log


class Book:
    """Определение класса Book"""
    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.in_use = False

    def __str__(self):
        return self.title


class User:
    """Определение класса User"""
    def __init__(self, name):
        self.name = name
        self.taken_books = []
        self.returned_books = []
        self.reserved_books = []

    def __str__(self):
        return self.name

    def reserve_book(self, book):
        """Метод резервирования книги"""
        if book.in_use:
            log.warning("Sorry, book %s is in use" % book.title)
        elif book.reserved:
            log.warning("Sorry, book %s is reserved" % book.title)
        else:
            book.reserved = True
            self.reserved_books.append(book)
            log.info("You have reserved book %s" % book.title)

    def take_book(self, book):
        """Метод взятия книги"""
        if book.in_use:
            log.warning("Sorry, book %s is in use" % book.title)
        elif book.reserved and book not in self.reserved_books:
            log.warning("Sorry, book %s is reserved" % book.title)
        else:
            book.in_use = True
            if book in self.reserved_books:
                book.reserved = False
                self.reserved_books.remove(book)
            self.taken_books.append(book)
            log.info("You have taken book %s" % book.title)

    def return_book(self, book):
        """Метод возврата книги"""
        if book in self.taken_books:
            book.in_use = False
            self.taken_books.remove(book)
            log.info("You have returned book %s" % book.title)
        else:
            log.warning("You do not have book %s taken" % book.title)


book1 = Book("Book_1", "Author_1", 100, "12345")
book2 = Book("Book_2", "Author_2", 200, "23456")

user1 = User("Kate")
user2 = User("Anna")

user1.reserve_book(book1)
user2.take_book(book1)
user1.take_book(book1)
user2.take_book(book2)
user2.return_book(book1)
user1.return_book(book1)
user2.reserve_book(book1)
user2.take_book(book1)
user1.take_book(book2)
