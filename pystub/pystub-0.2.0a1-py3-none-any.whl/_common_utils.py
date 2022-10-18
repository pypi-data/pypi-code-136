import logging
import sys

LOG = logging.getLogger(__name__)


def exit_with_code(code, msg=""):
    if msg:
        LOG.error(msg)
    sys.exit(code)
