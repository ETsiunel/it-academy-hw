"""Homework_20"""

import unittest
from hw_20.my_logger import logger as log
from hw_20.bank import Deposit, Bank


class TestDeposit(unittest.TestCase):
    """Deposit methods unit tests"""
    def setUp(self):
        self.deposit_valid = Deposit(1000, 12, 0.10)
        self.deposit_default = Deposit(1000, 12)  # default percent 10%
        self.bank1 = Bank()

    def tearDown(self):
        del self.deposit_valid
        del self.deposit_default
        del self.bank1

    def test_total_amount(self):
        """Test total amount calculating"""
        log.info('Testing total amount: initial 1000 RUB, 12 months, 10%')
        expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
        self.deposit_valid.total_amount()
        self.assertAlmostEqual(self.deposit_valid.total_amount(),
                               expected_amount, places=2)
        log.info(f'Expected amount = {expected_amount:.4f}, '
                 f'Calculated amount = '
                 f'{self.deposit_valid.total_amount():.4f}')

    def test_default_percent(self):
        """Test total amount calculating with default percent"""
        log.info('Testing total amount: initial 1000 RUB, 12 months, '
                 'default percent 10%')
        expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
        self.deposit_default.total_amount()
        self.assertAlmostEqual(self.deposit_default.total_amount(),
                               expected_amount, places=2)
        log.info(f'Expected amount = {expected_amount:.4f}, '
                 f'Calculated amount = '
                 f'{self.deposit_default.total_amount():.4f}')

    def test_deposit_is_instance(self):
        """Test deposit is instance of class Deposit"""
        self.assertIsInstance(self.deposit_valid, Deposit)
        log.info('Testing deposit1 is instance of class Deposit')

    def test_deposit_more_than_amount(self):
        """Test deposit amount > initial amount"""
        self.assertGreater(self.deposit_valid.total_amount(),
                           self.deposit_valid.amount)
        log.info('Testing deposit amount > initial amount')

    def test_invalid_amount(self):
        """Test deposit with invalid amount"""
        with self.assertLogs(log, level='ERROR') as cm:
            invalid_deposit = Deposit(-1000, 12, 0.10)
            self.assertFalse(invalid_deposit.valid)
            self.assertIsNone(invalid_deposit.total_amount())
        self.assertIn("Сумма вклада должна быть положительной", cm.output[0])

    def test_invalid_term(self):
        """Test deposit with invalid term"""
        with self.assertLogs(log, level='ERROR') as cm:
            invalid_deposit = Deposit(1000, -12, 0.10)
            self.assertFalse(invalid_deposit.valid)
            self.assertIsNone(invalid_deposit.total_amount())
        self.assertIn("Срок вклада должен быть больше нуля", cm.output[0])

    def test_invalid_percent(self):
        """Test deposit with invalid percent"""
        with self.assertLogs(log, level='ERROR') as cm:
            invalid_deposit = Deposit(1000, 12, 1.5)
            self.assertFalse(invalid_deposit.valid)
            self.assertIsNone(invalid_deposit.total_amount())
        self.assertIn("Процентная ставка должна быть "
                      "в пределах (0, 1]", cm.output[0])

        with self.assertLogs(log, level='ERROR') as cm:
            invalid_deposit = Deposit(1000, 12, -0.1)
            self.assertFalse(invalid_deposit.valid)
            self.assertIsNone(invalid_deposit.total_amount())
        self.assertIn("Процентная ставка должна быть "
                      "в пределах (0, 1]", cm.output[0])


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

    def test_invalid_deposit_amount(self):
        """Test Bank deposit with invalid amount"""
        with self.assertLogs(log, level='ERROR') as cm:
            invalid_amount = self.bank1.deposit(-1000, 12)
            self.assertIsNone(invalid_amount)
        self.assertIn("Сумма вклада должна быть положительной", cm.output[0])

    def test_invalid_deposit_term(self):
        """Test Bank deposit with invalid term"""
        with self.assertLogs(log, level='ERROR') as cm:
            invalid_term = self.bank1.deposit(1000, -12)
            self.assertIsNone(invalid_term)
        self.assertIn("Срок вклада должен быть больше нуля", cm.output[0])


if __name__ == '__main__':
    unittest.main()
