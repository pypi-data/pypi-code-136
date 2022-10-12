# Manages logging for the SDK.
# This configuration sends all INFO level messages to stdout,
# and all WARNING, ERROR, CRITICAL messages to stderr.
# Ignores DEBUG level messages.
import logging
import sys

LOG = logging.getLogger(__name__)
# To enable DEBUG level messages, change logging.INFO to
# logging.DEBUG. This will also allow DEBUG messages to be
# sent to stdout.
LOG.setLevel(logging.INFO)

info_handler = logging.StreamHandler(sys.stdout)
info_handler.setLevel(logging.INFO)
LOG.addHandler(info_handler)

err_handler = logging.StreamHandler(sys.stderr)
err_handler.setLevel(logging.WARNING)
LOG.addHandler(err_handler)
