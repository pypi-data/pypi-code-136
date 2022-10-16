import logging
import signal
from typing import Callable, Optional

logger = logging.getLogger(__name__)
exiting = False
sigint_callback: Optional[Callable[[int], None]] = None


def _sigint_handler(signum, frame):
    logger.info(f'Received sigint: {signum}')

    global exiting
    if exiting:
        logger.warning('Double sigint received, forcing exit')
        exit(1)

    exiting = True
    if sigint_callback is not None:
        sigint_callback(signum)


signal.signal(signal.SIGINT, _sigint_handler)
