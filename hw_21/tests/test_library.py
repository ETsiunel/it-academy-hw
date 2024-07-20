"""Homework_21"""

import pytest
from hw_21.source.library import Book, User
from hw_21.tests.my_logger import logger as log


@pytest.fixture
def book1():
    return Book("Book_1", "Author_1", 100, "12345")


@pytest.fixture
def book2():
    return Book("Book_2", "Author_2", 200, "23456")


@pytest.fixture
def user1():
    return User("Kate")


@pytest.fixture
def user2():
    return User("Anna")


def test_book_initialization(book1):
    assert book1.title == "Book_1"
    assert book1.author == "Author_1"
    assert book1.pages == 100
    assert book1.isbn == "12345"
    assert not book1.reserved
    assert not book1.in_use
    log.info("test_book_initialization passed")


def test_user_initialization(user1):
    assert user1.name == "Kate"
    assert user1.taken_books == []
    assert user1.returned_books == []
    assert user1.reserved_books == []
    log.info("test_user_initialization passed")


def test_reserve_book(user1, book1):
    user1.reserve_book(book1)
    assert book1.reserved
    assert book1 in user1.reserved_books
    log.info("test_reserve_book passed")


def test_reserve_book_already_reserved(user1, user2, book1):
    user1.reserve_book(book1)
    user2.reserve_book(book1)
    assert len(user2.reserved_books) == 0
    log.info("test_reserve_book_already_reserved passed")


def test_take_book(user1, book1):
    user1.take_book(book1)
    assert book1.in_use
    assert book1 in user1.taken_books
    log.info("test_take_book passed")


def test_take_book_already_reserved(user1, book1):
    user1.reserve_book(book1)
    user1.take_book(book1)
    assert book1.in_use
    assert not book1.reserved
    assert book1 not in user1.reserved_books
    assert book1 in user1.taken_books
    log.info("test_take_reserved_book passed")


def test_take_book_already_in_use(user1, user2, book1):
    user1.take_book(book1)
    user2.take_book(book1)
    assert len(user2.taken_books) == 0
    log.info("test_take_book_already_in_use passed")


def test_return_book(user1, book1):
    user1.take_book(book1)
    user1.return_book(book1)
    assert not book1.in_use
    assert book1 not in user1.taken_books
    log.info("test_return_book passed")


def test_return_book_not_taken(user1, book1):
    user1.return_book(book1)
    assert not book1.in_use
    assert book1 not in user1.taken_books
    log.info("test_return_book_not_taken passed")


def test_take_reserved_book_by_other_user(user1, user2, book1):
    user1.reserve_book(book1)
    user2.take_book(book1)
    assert not book1.in_use
    assert book1.reserved
    assert book1 in user1.reserved_books
    assert book1 not in user2.taken_books
    log.info("test_take_reserved_book_by_other_user passed")
