from __future__ import unicode_literals

import copy
import logging
import logging.handlers
import os.path
import re
from datetime import datetime
import sys
from pythonagent import config
from pythonagent.lib import default_log_formatter, mkdir

LOGGING_MAX_BYTES = 10 * 1024 * 1024
LOGGING_MAX_NUM_FILES = 5


def get_log_level():
    default_logging_level = logging.WARNING
    allowed_logging_levels = {'DEBUG': logging.DEBUG,
                              'INFO': logging.INFO,
                              'WARNING': logging.WARNING,
                              'ERROR': logging.ERROR,         # Added for testing
                              'CRITICAL': logging.CRITICAL    # Added for testing
                              }

    level = config.LOGGING_LEVEL.upper()
    ret_val = allowed_logging_levels.get(level, default_logging_level)
    # NOTSET=0
    # DEBUG=10
    # INFO=20
    # WARN=30
    # ERROR=40
    # CRITICAL=50
    return allowed_logging_levels.get(level, default_logging_level)


def get_log_filename():
    non_alphanumeric = re.compile(r'\W+')
    sanitize = lambda x: non_alphanumeric.sub('_', x)
    filename = '-'.join(
        map(sanitize, [config.APP_NAME, config.TIER, config.SERVER, '{:%Y-%m-%d}'.format(datetime.now())])) + '.log'
    return os.path.join(config.LOGS_DIR, filename)


def debug_enabled(logger):
    for handler in logger.handlers:
        if handler.__class__ is logging.StreamHandler:
            return True
    return False


def enable_debug(logger):
    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(default_log_formatter)
    logger.addHandler(stream_handler)


def disable_debug(logger):
    level = get_log_level()
    logger.setLevel(level)

    handlers = copy.copy(logger.handlers)
    logger.handlers = []
    for handler in handlers:
        if handler.__class__ is not logging.StreamHandler:
            handler.setLevel(level)
            logger.addHandler(handler)


def configure_logging():
    try:
        logger = logging.getLogger('pythonagent.agent')
        level = get_log_level()
        print("Logging level:", level)
        logger.setLevel(level)
        path = get_log_filename()

        print("Logging file path name", path)

        agent_env = None

        if "CAV_APP_AGENT_Env" in os.environ:
            if os.environ['CAV_APP_AGENT_Env'] == "AWS_LAMBDA":
                agent_env = "AWS_LAMBDA"
            elif os.environ['CAV_APP_AGENT_Env'] == "NATIVE":
                agent_env = "NATIVE"
        else:
            agent_env = "AWS_LAMBDA"

        if agent_env == "AWS_LAMBDA":
            consolHandler = logging.StreamHandler(sys.stdout)
            consolHandler.setLevel(level)
            consolHandler.setFormatter(default_log_formatter)
            logger.addHandler(consolHandler)

        else:
            mkdir(os.path.dirname(path))
            rotating_file_handler = logging.handlers.RotatingFileHandler(path, maxBytes=LOGGING_MAX_BYTES,
                                                                         backupCount=LOGGING_MAX_NUM_FILES - 1)
            # logging.getLogger('pythonagent.agent').addHandler()
            rotating_file_handler.setLevel(level)
            rotating_file_handler.setFormatter(default_log_formatter)
            logger.addHandler(rotating_file_handler)

        if config.DEBUG_LOG:
            enable_debug(logger)

        has_handlers = logger.hasHandlers()
        logger.warning("has handlers {}".format(str(has_handlers)))
        logger.propagate = False
        logger.warning("has handlers {}".format(str(has_handlers)))


    except:
        logging.getLogger('pythonagent.agent').exception('Logging configuration failed.')
