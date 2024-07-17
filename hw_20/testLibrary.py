"""Homework_20"""

import unittest
import logging
from hw_20.library import Book, User


formatter = logging.Formatter(' [%(asctime)s] - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class TestLibrary(unittest.TestCase):
    """Book and User methods unit tests"""
    def setUp(self):
        self.book1 = Book("Book_1", "Author_1", 100, "12345")
        self.book2 = Book("Book_2", "Author_2", 200, "23456")
        self.user1 = User("Kate")
        self.user2 = User("Anna")

    def tearDown(self):
        del self.book1
        del self.book2
        del self.user1
        del self.user2

    def test_reserve_book_already_in_use(self):
        """Reserve book already in use"""
        logger.info(f'{self.user1} tries to reserve_book {self.book1}'
                    f'which is already in_use')
        self.book1.in_use = True
        self.user1.take_book(self.book1)
        self.assertFalse(self.book1.reserved)
        self.assertFalse(self.user2.reserve_book(self.book1))
        self.assertNotIn(self.book1, self.user1.reserved_books)
        logger.warning(f"Sorry, book {self.book1} is already in use")

    def test_reserve_book_already_reserved(self):
        """Reserve book already reserved"""
        logger.info(f'{self.user1} tries to reserve_book {self.book1}'
                    f'which is already reserved')
        self.book1.reserved = True
        self.user1.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)
        self.assertNotIn(self.book1, self.user1.reserved_books)
        logger.warning(f"Sorry, book {self.book1} is already reserved")

    def test_reserve_book_positive(self):
        """Reserve book"""
        logger.info(f'{self.user1} tries to reserve_book {self.book1}')
        self.user1.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)
        self.assertIn(self.book1, self.user1.reserved_books)
        logger.info(f"You have successfully reserved book {self.book1}")

    def test_take_book_already_in_use(self):
        """Take book already in use"""
        logger.info(f'{self.user1} tries to take_book {self.book1} '
                    f'which is already in_use')
        self.book1.in_use = True
        self.user1.take_book(self.book1)
        self.assertNotIn(self.book1, self.user1.taken_books)
        logger.warning(f"Sorry, book {self.book1} is already in use")

    def test_take_book_already_reserved(self):
        """Take book already reserved"""
        logger.info(f'{self.user1} tries to take_book {self.book1} '
                    f'which is already reserved')
        self.book1.reserved = True
        self.user2.reserved_books.append(self.book1)
        self.user1.take_book(self.book1)
        self.assertNotIn(self.book1, self.user1.taken_books)
        self.assertTrue(self.book1.reserved)
        self.assertFalse(self.user1.take_book(self.book1))
        logger.warning(f"Sorry, book {self.book1} is already reserved")

    def test_take_book_positive(self):
        """Take book"""
        logger.info(f'{self.user1} tries to take_book {self.book1}')
        self.user1.take_book(self.book1)
        self.assertTrue(self.book1.in_use)
        self.assertIn(self.book1, self.user1.taken_books)
        self.assertFalse(self.book1.reserved)
        logger.info(f"You have successfully taken book {self.book1}")

    def test_return_book_not_taken(self):
        """Return book not taken"""
        logger.info(f'{self.user1} tries to return_book {self.book1} '
                    f'which is not taken by him')
        self.user1.return_book(self.book1)
        self.assertNotIn(self.book1, self.user1.taken_books)
        logger.warning(f"You do not have book {self.book1} taken")

    def test_return_book_positive(self):
        """Return book"""
        logger.info(f'{self.user1} tries to return_book {self.book1}')
        self.user1.take_book(self.book1)
        self.user1.return_book(self.book1)
        self.assertFalse(self.book1.in_use)
        self.assertNotIn(self.book1, self.user1.taken_books)
        logger.info(f"You have successfully returned book {self.book1}")

    def test_multiple_users(self):
        """Multiple users test"""
        self.user1.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)
        self.user2.take_book(self.book1)
        self.assertFalse(self.book1.in_use)
        self.assertIn(self.book1, self.user1.reserved_books)
        self.assertNotIn(self.book1, self.user2.taken_books)
        self.user1.take_book(self.book1)
        self.assertTrue(self.book1.in_use)
        self.user1.return_book(self.book1)
        self.user2.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)
        self.user2.take_book(self.book1)
        self.assertTrue(self.book1.in_use)
        self.assertIn(self.book1, self.user2.taken_books)
        self.assertNotIn(self.book1, self.user2.reserved_books)


if __name__ == '__main__':
    unittest.main()
