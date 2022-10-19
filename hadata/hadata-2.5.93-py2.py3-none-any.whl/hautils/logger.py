import logging
import os

from uvicorn.logging import ColourizedFormatter

log_level = os.getenv("LOG_LEVEL", "INFO")
logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(log_level))
standard = logging.StreamHandler()
standard.setLevel(logging.getLevelName(log_level))

formatter = ColourizedFormatter(fmt=(
    "%(levelprefix)-8s %(asctime)-15s - "
    "%(filename)10s:%(lineno)-3d - %(message)s"))

standard.setFormatter(formatter)
logger.addHandler(standard)