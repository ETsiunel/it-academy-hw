"""Homework_21"""

from hw_21.my_logger import logger as log
import pytest
from hw_21.source.bank import Deposit, Bank


@pytest.fixture
def deposit():
    deposit = Deposit(1000, 12, 0.10)
    yield deposit


@pytest.fixture
def bank():
    bank = Bank()
    yield bank


def test_deposit_initialization(deposit):
    assert deposit.amount == 1000
    assert deposit.term == 12
    assert deposit.percent == 0.10


def test_deposit_total_amount(deposit):
    expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
    assert deposit.total_amount() == pytest.approx(expected_amount, rel=1e-4)


def test_bank_deposit(bank):
    N = 1000
    R = 12
    total_amount = bank.deposit(N, R)
    expected_amount = 1000 * ((1 + 0.10 / 12) ** 12)
    assert total_amount == pytest.approx(expected_amount, rel=1e-4)


def test_bank_deposit_custom_percent():
    deposit = Deposit(50000, 12, 0.08)
    expected_amount = 50000 * ((1 + 0.08 / 12) ** 12)
    assert deposit.total_amount() == pytest.approx(expected_amount, rel=1e-4)


def test_negative_amount(caplog):
    with caplog.at_level(log.ERROR):
        deposit = Deposit(-1000, 12, 0.10)
        assert deposit.total_amount() is None
        assert "Сумма вклада должна быть положительной" in caplog.text


def test_zero_term(caplog):
    with caplog.at_level(log.ERROR):
        deposit = Deposit(1000, 0, 0.10)
        assert deposit.total_amount() is None
        assert "Срок вклада должен быть больше нуля" in caplog.text


def test_excessive_percent(caplog):
    with caplog.at_level(log.ERROR):
        deposit = Deposit(1000, 12, 2.0)
        assert deposit.total_amount() is None
        assert "Процентная ставка должна быть в пределах (0, 1]" in caplog.text


def test_bank_deposit_negative_amount(bank, caplog):
    with caplog.at_level(log.ERROR):
        total_amount = bank.deposit(-1000, 12)
        assert total_amount is None
        assert ("Failed to create deposit with amount=-1000 "
                "and term=12") in caplog.text


def test_bank_deposit_zero_term(bank, caplog):
    with caplog.at_level(log.ERROR):
        total_amount = bank.deposit(1000, 0)
        assert total_amount is None
        assert ("Failed to create deposit with amount=1000 "
                "and term=0") in caplog.text


def test_bank_deposit_excessive_percent(caplog):
    with caplog.at_level(log.ERROR):
        deposit = Deposit(1000, 12, 2.0)
        total_amount = deposit.total_amount()
        assert total_amount is None
        assert "Процентная ставка должна быть в пределах (0, 1]" in caplog.text
