import logging


def get_logger(logger_name: str) -> logging.Logger:
    return logging.getLogger(logger_name)


__all__ = ["get_logger"]
