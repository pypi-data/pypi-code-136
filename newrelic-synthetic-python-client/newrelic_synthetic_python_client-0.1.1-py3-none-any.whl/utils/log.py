import os
import sys

from loguru import logger as log

env = "NR_LOG_LEVEL"

level = "INFO" if env not in os.environ else os.environ[env]

log.remove()
log.add(
    sink=sys.stdout,
    level=level,
)
