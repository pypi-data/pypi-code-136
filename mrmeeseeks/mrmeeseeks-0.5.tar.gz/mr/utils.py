import os
import logging
from rich.logging import RichHandler

logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    level=os.environ.get("LOGLEVEL", "INFO"),
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger('Mr.Meeseeks')


class OhNo(Exception):
    "Something bad happened, maybe another Meeseeks could solve the problem?"

    def __init__(self, message, level=logging.ERROR):

        if level == logging.CRITICAL:
            f = log.critical
        elif level == logging.ERROR:
            f = log.error
        elif level == logging.WARNING:
            f = log.warning
        elif level == logging.INFO:
            f = log.info
        elif level == logging.DEBUG:
            f = log.debug
        else:
            f = log.info

        print('\n')
        f('／￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣＼')
        f('|　I am Mr. Meeseeks, maybe I need some help?   |')
        f('|　Something really bad happened:               |')
        f('＼＿　 ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿／')
        f('     ∨')
        f(message)

        self.message = message
