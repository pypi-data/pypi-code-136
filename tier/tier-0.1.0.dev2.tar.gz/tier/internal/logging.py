# std
import logging
import os
import sys
import traceback

# constants
_FMT = '%(asctime)s (%(name)s) [%(levelname)s] %(message)s'
_DEFAULT_LOG_LEVEL = 'WARNING'
_ENVIRONMENT_LOG_LEVEL = os.environ.get('LOG_LEVEL', '').upper()


def _get_logger(
        name: str,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.propagate = False

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(fmt=_FMT))
    logger.addHandler(handler)

    log_level = _ENVIRONMENT_LOG_LEVEL or _DEFAULT_LOG_LEVEL

    try:
        logger.setLevel(log_level)
    except ValueError as e:
        logger.warning(f'Unknown log level: {_ENVIRONMENT_LOG_LEVEL}\n{e}\n{traceback.format_exc()}')
    return logger


def _convert_verbosity_to_level(verbosity: int) -> int:
    if verbosity <= 0:
        return logging.WARNING
    elif verbosity == 1:
        return logging.INFO
    elif verbosity >= 2:
        return logging.DEBUG
    else:
        return logging.WARNING


log = _get_logger('tier')


def set_verbosity(verbosity: int):
    global log
    log.setLevel(_convert_verbosity_to_level(verbosity))
