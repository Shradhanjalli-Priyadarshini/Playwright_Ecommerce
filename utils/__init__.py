import logging
import os


def get_logger(name):

    os.makedirs(
        "logs",
        exist_ok=True
    )

    logger = logging.getLogger(name)

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )

        console_handler = (
            logging.StreamHandler()
        )

        console_handler.setFormatter(
            formatter
        )

        file_handler = (
            logging.FileHandler(
                "logs/test_execution.log"
            )
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            console_handler
        )

        logger.addHandler(
            file_handler
        )

    return logger