# This file is named app_logging to avoid name collision with system logging package

import sys

from logging.config import dictConfig


LEVELS = [
    'critical',
    'error',
    'warning',
    'info',
    'debug',
]
DEFAULT_LEVEL = "warning"


def init_logging(log_level: str):
    console_format = "{log_color}{message}{reset}"
    log_level = log_level.upper()

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "colored": {
                    "()": "colorlog.ColoredFormatter",
                    "format": console_format,
                    "style": "{",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                    "level": log_level,
                    "stream": sys.stdout,
                },
            },
            "loggers": {
                "": {
                    "handlers": ["console"],
                    "level": log_level,
                },
            },
        }
    )

