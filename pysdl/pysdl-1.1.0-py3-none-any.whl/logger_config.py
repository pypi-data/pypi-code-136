import sys

logging_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "json": {
            '()': "pysdl.stackdriverjsonlogger.StackdriverJsonFormatter",
            'format': "%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)s %(process)s %(thread)s %(message)s"
        },
        "medium": {
            'format': '%(levelname)s %(asctime)s [%(correlation_id)s] %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'stream': sys.stdout
        },
    },
    'loggers': {
        # Root Logger
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # DB events and sql
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        # Celery tasks will duplicate WARNING and ERROR logs here but it also helps us to catch celery issues
        # IMO duplication of ERROR and WARNING logs aren't a big deal
        'celery': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'celery.beat': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    }
}