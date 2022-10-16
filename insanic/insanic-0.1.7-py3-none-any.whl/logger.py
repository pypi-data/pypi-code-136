import logging
import sys

from loguru import logger as log
from sanic import Sanic


LOGURU_PROD_FORMAT = "{message}"
LOGURU_DEBUG_FORMAT = ' | '.join([
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>",
    "<level>{level: <8}</level>",
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
])

class StdLoggingInterceptor(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Getting corresponding loguru level according to stdlogging level if it exists
        try:
            level = log.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Get original caller from message
        # https://github.com/Delgan/loguru#entirely-compatible-with-standard-logging
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # @TODO: Enable exceptions logging?
        # logger.opt(depth=depth, exception=record.exc_info)
        log.opt(depth=depth).log(level, record.getMessage())


def init_logger() -> None:
    # Setting up interceptor to `logging` to redirect all records to loguru and removing default stderr handler
    logging.basicConfig(handlers=[StdLoggingInterceptor()], level=0, force=True)
    log.remove()

    # Settings log level according to loaded configuration
    application = Sanic.get_app()
    app_in_debug = application.config.APPLICATION_DEBUG

    # @TODO: Implement custom serializer for JSON log format
    # https://loguru.readthedocs.io/en/stable/resources/recipes.html#serializing-log-messages-using-a-custom-function
    handler_config = {
        'level': logging.DEBUG if app_in_debug else logging.WARNING,
        'format': LOGURU_DEBUG_FORMAT if app_in_debug else LOGURU_PROD_FORMAT,
        'serialize': not app_in_debug,
        'colorize': app_in_debug,
    }
    log.add(sys.stdout, enqueue=True, **handler_config)
