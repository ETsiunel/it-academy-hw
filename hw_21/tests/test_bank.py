"""Homework_21"""

import pytest
from hw_21.source.bank import Deposit, Bank
# from hw_21.tests.my_logger import logger as log
import logging


@pytest.fixture
def deposit():
    dep = Deposit(1000, 12, 0.10)
    yield dep


@pytest.fixture
def bank():
    bnk = Bank()
    yield bnk


def test_deposit_initialization(deposit):
    assert deposit.amount == 1000
    assert deposit.term == 12
    assert deposit.percent == 0.10


def test_deposit_total_amount(deposit):
    expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
    assert deposit.total_amount() == pytest.approx(expected_amount, rel=1e-4)


@pytest.mark.parametrize(
    "amount, months, percent, expected",
    [
        (1000, 12, 0.10, 1000 * ((1 + 0.10 / 12) ** 12)),
        (5000, 24, 0.05, 5000 * ((1 + 0.05 / 12) ** 24)),
        (2000, 6, 0.07, 2000 * ((1 + 0.07 / 12) ** 6))
    ]
)
def test_bank_deposit(bank, amount, months, percent, expected):
    deposit = Deposit(amount, months, percent)
    total_amount = deposit.total_amount()
    assert total_amount == pytest.approx(expected, rel=1e-4)


def test_bank_deposit_custom_percent():
    deposit = Deposit(50000, 12, 0.08)
    expected_amount = 50000 * ((1 + 0.08 / 12) ** 12)
    assert deposit.total_amount() == pytest.approx(expected_amount, rel=1e-4)


def test_negative_amount(caplog):
    with caplog.at_level(logging.ERROR):
        deposit = Deposit(-1000, 12, 0.10)
        assert deposit.total_amount() is None
        assert "Сумма вклада должна быть положительной" in caplog.text


def test_zero_term(caplog):
    with caplog.at_level(logging.ERROR):
        deposit = Deposit(1000, 0, 0.10)
        assert deposit.total_amount() is None
        assert "Срок вклада должен быть больше нуля" in caplog.text


def test_excessive_percent(caplog):
    with caplog.at_level(logging.ERROR):
        deposit = Deposit(1000, 12, 2.0)
        assert deposit.total_amount() is None
        assert "Процентная ставка должна быть в пределах (0, 1]" in caplog.text


def test_bank_deposit_negative_amount(bank, caplog):
    with caplog.at_level(logging.ERROR):
        total_amount = bank.deposit(-1000, 12)
        assert total_amount is None
        assert "Failed to create deposit with amount=-1000 and term=12" in caplog.text


def test_bank_deposit_zero_term(bank, caplog):
    with caplog.at_level(logging.ERROR):
        total_amount = bank.deposit(1000, 0)
        assert total_amount is None
        assert "Failed to create deposit with amount=1000 and term=0" in caplog.text


def test_bank_deposit_excessive_percent(caplog):
    with caplog.at_level(logging.ERROR):
        deposit = Deposit(1000, 12, 2.0)
        total_amount = deposit.total_amount()
        assert total_amount is None
        assert "Процентная ставка должна быть в пределах (0, 1]" in caplog.text
