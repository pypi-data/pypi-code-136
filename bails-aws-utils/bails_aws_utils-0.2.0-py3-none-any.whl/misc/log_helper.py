import logging
import sys


def configure_logging():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.getLogger("botocore").setLevel(logging.WARNING)
    logging.getLogger("boto3").setLevel(logging.WARNING)
