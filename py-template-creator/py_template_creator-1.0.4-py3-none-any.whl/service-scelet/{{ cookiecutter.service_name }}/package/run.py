from mrkutil.communication import listen
from mrkutil.logging import get_logging_config
from package.app import handlers  # noqa importing handlers

import os
import sys
import logging
import logging.config


log_level = os.getenv("LOG_LEVEL", "DEBUG")
json_format = bool('true' == str(os.getenv("JSON_FORMAT", 'false')).lower())

logging.config.dictConfig(get_logging_config(log_level, json_format, False))

logger = logging.getLogger("main")


def main():
    """
    App starting point
    """
    pid = str(os.getpid())
    pidfile = "./running/service.pid"

    if os.path.isfile(pidfile):
        logger.warning("Service is already running")
        sys.exit(1)
    with open(pidfile, 'w') as file:
        file.write(pid)
        file.write("\n")
    try:
        logger.info("Starting ...")
        listen(
            exchange=os.getenv("EXCHANGE_EXAMPLE"),
            exchange_type=os.getenv("EXCHANGE_TYPE_EXAMPLE"),
            queue=os.getenv("QUEUE_EXAMPLE"),
        )
        sys.exit(0)
    finally:
        os.unlink(pidfile)


if __name__ == "__main__":
    main()
