"""Conftest"""

from hw_21.tests.my_logger import logger as log
from constants import LOG_LEVELS


def pytest_addoption(parser):
    """Function adds a command-line option to set the HTML log level"""
    parser.addoption(
        "--html-log-level",
        action="store",
        default="DEBUG",
        help="Set the logging level for html report"
    )


def pytest_configure(config):
    """Function configures logging based on the command-line option"""
    log_level = config.getoption("--html-log-level").upper()
    if log_level_numeric := LOG_LEVELS.get(log_level):
        log.setLevel(log_level_numeric)


# To run:
#   pytest test_library.py --log-cli-level=ERROR --html=report_library.html
#       - вывод уровня ERROR и выше в консоль, в html-отчете уровни по дефолту
#   pytest test_library.py --log-level=ERROR --html=report_library.html
#       - вывод уровня ERROR и выше в html-отчет, в консоли уровни по дефолту
#   pytest test_bank.py --html-log-level=ERROR --html=report_bank.html
#       - вывод уровня ERROR и выше везде
