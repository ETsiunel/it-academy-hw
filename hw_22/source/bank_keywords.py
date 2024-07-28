"""Bank keywords"""

from robot.api.deco import keyword
from bank import Deposit, Bank
from my_logger import setup_logging

log = setup_logging()


@keyword
def create_bank():
    return Bank()


@keyword
def deposit_money(amount, term, percent):
    deposit = Deposit(amount, term, percent)
    deposit.total_amount()
    return deposit.total_amount()


@keyword
def should_be_none(value, msg=None):
    if value is not None:
        if not msg:
            msg = f"Expected None, but got {value}"
        raise AssertionError(msg)


@keyword
def should_not_be_none(value, msg=None):
    if value is None:
        if not msg:
            msg = f"Expected value not to be None, but got {value}"
        raise AssertionError(msg)


@keyword
def log_message(message):
    log.info(message)
