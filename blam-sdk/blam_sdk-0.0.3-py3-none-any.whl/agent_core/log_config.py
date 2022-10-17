import logging
import sys


def configure_logger(level, use_file=False):
    if use_file:
        logging.basicConfig(
            filename="agent.log",
            filemode="w",
            format="%(name)s - %(levelname)s - %(message)s",
            level=level,
        )
    else:
        logging.basicConfig(level=level, stream=sys.stdout)

    logging.getLogger("botocore").setLevel(logging.WARNING)
    logging.getLogger("boto3").setLevel(logging.WARNING)
