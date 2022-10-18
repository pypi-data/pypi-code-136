import logging.config

from chalk.utils.log_with_context import Logger

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {"()": "chalk.utils.json_log_formatter.JSONFormatter"},
        },
        "handlers": {
            "console": {
                "formatter": "json",
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "": {"handlers": ["console"], "level": "DEBUG"},
        },
    }
)

chalk_logger = Logger(__name__)
