import logging
from typing import Any, Dict

LOG_TYPE = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "FATAL": logging.FATAL,
}

logging.basicConfig(
    handlers=[logging.StreamHandler()],
    format='{"datetime": "%(asctime)s", "level_name": "%(levelname)s", "message": "%(message)s"}',
    level=LOG_TYPE["INFO"],
)


class Logging:
    @staticmethod
    def get_logger():
        return logging

    @staticmethod
    def formatting_message(msg: Any) -> Dict[str, Any]:
        """formatting message to get better logs
        :param msg: message that want to print
        :return: dictionary message
        """
        return msg

    @staticmethod
    def info(message: Any):
        """Print logging info message
        :param message: any message
        :return: None
        """
        logging.info(Logging.formatting_message(message))

    @staticmethod
    def debug(message: Any):
        """Print logging debug message
        :param message: any message
        :return: None
        """
        logging.debug(Logging.formatting_message(message))

    @staticmethod
    def error(message: Any):
        """Print logging error message
        :param message: any message
        :return: None
        """
        logging.error(Logging.formatting_message(message))

    @staticmethod
    def warning(message: Any):
        """Print logging warning message
        :param message: any message
        :return: None
        """
        logging.warning(Logging.formatting_message(message))

    @staticmethod
    def exception(message: Any):
        """Print logging exception() message
        :param message: any message
        :return: None
        """
        logging.exception(Logging.formatting_message(message))
