import sys

import structlog
from django.utils.log import DEFAULT_LOGGING


def get_default_logging_conf(log_level: str, console_formatter: str, own_apps: list[str]) -> dict:
    formatters = {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(
                key_order=['microservice', 'timestamp', 'level', 'event', 'logger']
            ),
        },
    }

    if console_formatter not in formatters:
        raise NotImplementedError("formatter not supported")

    configuration = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': formatters,
        'handlers': {
            'console': {
                'level': log_level,
                'class': 'logging.StreamHandler',
                'formatter': console_formatter,
                'stream': sys.stdout,
            },
            'django.server': DEFAULT_LOGGING['handlers']['django.server'],
        },
        "root": {
            "level": log_level,
            "handlers": ["console"],
            "propagate": False,
        },
        'loggers': {
            '': {
                'level': log_level,
                'handlers': ['console'],
                "propagate": False,
            },
            'django.request': {
                'level': log_level,
                'handlers': ['console'],
                "propagate": False,
            },
            "django.security.DisallowedHost": {
                'level': log_level,
                'handlers': ['console'],
                "propagate": False,
            },
            'django.server': DEFAULT_LOGGING['loggers']['django.server'],
            "celery.task": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "celery": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            # Setup loggers for each app
            **{
                app.split('.', maxsplit=1)[0]: {
                    "handlers": ["console"],
                    "level": log_level,
                    "propagate": False,
                }
                for app in own_apps
            },
        },
    }

    return configuration
