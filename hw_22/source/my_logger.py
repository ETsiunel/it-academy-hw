"""Logger"""

import logging


def setup_logging():
    formatter = logging.Formatter('\n[%(asctime)s] '
                                  '- %(levelname)s - %(message)s')

    # file_handler = logging.FileHandler('hw_22.hw_22.log')
    # file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    # logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    return logger
