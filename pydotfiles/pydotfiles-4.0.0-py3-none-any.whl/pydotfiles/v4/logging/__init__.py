# General imports
from logging import getLogger
from logging import StreamHandler, Formatter, Filter
from logging import WARNING, DEBUG, INFO, ERROR, FATAL
from logging import root as root_logger

from sys import stderr, stdout
from sys import exit as sys_exit

##
# Public method
##

logger = getLogger(__name__)


def set_logging(is_quiet: bool, is_verbose: bool) -> None:
    if is_quiet:
        logging_level = WARNING
    elif is_verbose:
        logging_level = DEBUG
    else:
        logging_level = INFO

    # Enables normal logging to stdout and errors to stderr
    stderr_handler = StreamHandler(stderr)
    stderr_handler.setLevel(WARNING)
    stderr_handler.setFormatter(PrettyLogFormatter())
    root_logger.addHandler(stderr_handler)

    # See https://github.com/Robpol86/sphinxcontrib-versioning/blob/master/sphinxcontrib/versioning/setup_logging.py
    stdout_handler = StreamHandler(stdout)
    stdout_handler.setLevel(logging_level)
    stdout_handler.setFormatter(PrettyLogFormatter())
    stdout_handler.addFilter(type('', (Filter,), {'filter': staticmethod(lambda r: r.levelno < WARNING)}))
    root_logger.addHandler(stdout_handler)

    root_logger.setLevel(logging_level)

##
# Helper classes and methods
##


class PrettyLogFormatter(Formatter):
    """
    Presentation-layer pretty printing, enabling
    clear guides to an end-user via ANSI escape
    sequences. Should be attached to a logger.

    For more information see:
    https://stackoverflow.com/questions/1343227/can-pythons-logging-format-be-modified-depending-on-the-message-log-level/27835318#27835318
    """

    DEBUG_BLUE = "\033[94m"
    INFO_GREEN = "\033[92m"
    WARNING_YELLOW = "\033[0;33m"
    ERROR_ORANGE = "\033[38:2:255:165:0m"
    FATAL_RED = "\033[31m"

    END_COLOUR = '\033[0m'

    def __init__(self):
        super().__init__()
        self.formatters = {
            DEBUG: Formatter(f"%(asctime)s [{self.DEBUG_BLUE}DEBUG::%(name)s{self.END_COLOUR}]: %(message)s", datefmt=self.date_format),
            INFO: Formatter(f"%(asctime)s [{self.INFO_GREEN}%(levelname)s::%(name)s{self.END_COLOUR}]: %(message)s", datefmt=self.date_format),
            WARNING: Formatter(f"%(asctime)s [{self.WARNING_YELLOW}WARN::%(name)s{self.END_COLOUR}]: %(message)s", datefmt=self.date_format),
            ERROR: Formatter(f"%(asctime)s [{self.ERROR_ORANGE}ERROR::%(name)s{self.END_COLOUR}]: %(message)s", datefmt=self.date_format),
            FATAL: Formatter(f"%(asctime)s [{self.FATAL_RED}FATAL::%(name)s{self.END_COLOUR}]: %(message)s", datefmt=self.date_format),
        }

        self.default_format = Formatter("%(levelname)s: %(name)s: %(message)s")

    @property
    def date_format(self):
        return "%Y-%m-%d %I:%M:%S %p"

    def format(self, record):
        return self.formatters.get(record.levelno, self.default_format).format(record)


class PrettyPrint:
    """
    Presentation-layer pretty printing, enabling
    clear guides to an end-user via ANSI escape
    sequences
    """

    SUCCESS_GREEN = '\033[92m'
    INFO_BLUE = '\033[94m'
    USER_YELLOW = '\033[0;33m'
    WARN_ORANGE = '\033[38:2:255:165:0m'
    FAIL_RED = '\033[31m'

    # Other settings not turned on yet
    # HEADER = '\033[95m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

    END_COLOUR = '\033[0m'

    @staticmethod
    def success(message):
        print(f"[ {PrettyPrint.SUCCESS_GREEN}OK{PrettyPrint.END_COLOUR} ] {message}")

    @staticmethod
    def info(message):
        print(f"[{PrettyPrint.INFO_BLUE}INFO{PrettyPrint.END_COLOUR}] {message}")

    @staticmethod
    def user(message):
        print(f"[{PrettyPrint.USER_YELLOW}USER{PrettyPrint.END_COLOUR}] {message}")

    @staticmethod
    def warn(message):
        print(f"[{PrettyPrint.WARN_ORANGE}WARN{PrettyPrint.END_COLOUR}] {message}")

    @staticmethod
    def fail(message):
        sys_exit(f"[{PrettyPrint.FAIL_RED}FAIL{PrettyPrint.END_COLOUR}] {message}")
