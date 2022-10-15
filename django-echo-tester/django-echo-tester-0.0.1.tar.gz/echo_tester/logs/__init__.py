import logging
import sys
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s', '%m-%d-%Y %H:%M:%S'
)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)


location = os.path.join(os.path.dirname(__file__), 'echo_tester.log')
file_handler = logging.FileHandler(location)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

