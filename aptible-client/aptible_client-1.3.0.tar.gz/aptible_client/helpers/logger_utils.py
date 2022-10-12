import logging
import time
from typing import Optional


def setup_root_logger(name_prefix: Optional[str] = ""):
    if name_prefix:
        name_prefix += "-"
    logging.basicConfig(
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(levelname)-8s %(message)s',
        encoding='utf-8',
        handlers=[
            logging.FileHandler(f'{name_prefix}{time.time_ns()}.log'),
            logging.StreamHandler()
        ],
        level=logging.DEBUG
    )
