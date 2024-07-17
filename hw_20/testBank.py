"""Homework_20"""

import unittest
import logging
from hw_20.bank import Deposit, Bank

formatter = logging.Formatter('\n[%(asctime)s] - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class TestDeposit(unittest.TestCase):
    """Deposit methods unit tests"""
    def setUp(self):
        self.deposit1 = Deposit(1000, 12, 0.10)
        self.deposit2 = Deposit(50000, 12, 0.08)
        self.deposit3 = Deposit(2000, 6, 0.05)
        self.deposit4 = Deposit(1000, 12)   # default percent 10%
        self.bank1 = Bank()

    def tearDown(self):
        del self.deposit1
        del self.deposit2
        del self.deposit3
        del self.deposit4
        del self.bank1

    def test_total_amount(self):
        """Test finish amount calculating"""
        # N = 1000, R = 12, percent = 10
        logger.info('Testing total amount: initial 1000 RUB, 12 months, 10%')
        expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
        calculated_amount = self.deposit1.total_amount()
        self.assertAlmostEqual(calculated_amount, expected_amount, places=2)
        logger.info(f'Expected amount = {expected_amount:.4f}, '
                    f'Calculated amount = {calculated_amount:.4f}')

        # N = 50000 RUB, R = 12 month, percent = 8%
        logger.info('Testing total amount: initial 50000 RUB, 12 months, 8%')
        expected_amount = 50000 * ((1 + 0.08 / 12) ** 12)
        calculated_amount = self.deposit2.total_amount()
        self.assertAlmostEqual(calculated_amount, expected_amount, places=2)
        logger.info(f'Expected amount = {expected_amount:.4f}, '
                    f'Calculated amount = {calculated_amount:.4f}')

        # N = 2000 RUB, R = 6 month, percent = 5%
        logger.info('Testing total amount: initial 2000 RUB, 6 months, 5%')
        expected_amount = 2000 * ((1 + 0.05 / 12) ** 6)
        calculated_amount = self.deposit3.total_amount()
        self.assertAlmostEqual(calculated_amount, expected_amount, places=2)
        logger.info(f'Expected amount = {expected_amount:.4f}, '
                    f'Calculated amount = {calculated_amount:.4f}')

    def test_default_percent(self):
        """Test finish amount calculating with default percent"""
        # N = 1000, R = 12, default percent = 10%
        logger.info('Testing total amount: initial 1000 RUB, 12 months, '
                    'default percent 10%')
        expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
        calculated_amount = self.deposit4.total_amount()
        self.assertAlmostEqual(calculated_amount, expected_amount, places=2)
        logger.info(f'Expected amount = {expected_amount:.4f}, '
                    f'Calculated amount = {calculated_amount:.4f}')

    def test_deposit_is_instance(self):
        """Test deposit is instance of class Deposit"""
        self.assertIsInstance(self.deposit1, Deposit)
        logger.info('Testing deposit1 is instance of class Deposit')
        self.assertIsInstance(self.deposit2, Deposit)
        logger.info('Testing deposit2 is instance of class Deposit')
        self.assertIsInstance(self.deposit3, Deposit)
        logger.info('Testing deposit3 is instance of class Deposit')
        self.assertIsInstance(self.deposit4, Deposit)
        logger.info('Testing deposit4 is instance of class Deposit')

    def test_deposit_more_than_amount(self):
        """Test deposit amount > initial amount"""
        self.assertGreater(self.deposit1.total_amount(), self.deposit1.amount)
        logger.info('Testing deposit amount > initial amount')


class TestBank(unittest.TestCase):
    """Bank methods unit tests"""
    def setUp(self):
        self.bank1 = Bank()
        self.bank2 = Bank()

    def tearDown(self):
        del self.bank1
        del self.bank2

    def test_deposit(self):
        N = 1000
        R = 12
        expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
        calculated_amount = self.bank1.deposit(N, R)
        self.assertAlmostEqual(calculated_amount, expected_amount, places=2)


if __name__ == '__main__':
    unittest.main()
