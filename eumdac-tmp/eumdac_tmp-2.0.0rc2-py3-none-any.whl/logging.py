"""module that is used for logging in eumdac"""
import logging
import platform
import sys
from pathlib import Path
from typing import Callable, Iterable, Tuple


def gen_table_printer(
    print_func: Callable[[str], None],
    columns: Iterable[Tuple[str, int]],
    header_sep: str = "-",
    column_sep: str = " ",
) -> Callable[[Iterable[str]], None]:
    headings = [x[0] for x in columns]
    colwidths = [x[1] for x in columns]

    fmt_string = column_sep.join(["{:<" + str(x) + "}" for x in colwidths])
    contentseps = [header_sep * x for x in colwidths]

    print_func(fmt_string.format(*headings))
    print_func(fmt_string.format(*contentseps))

    return lambda c: print_func(fmt_string.format(*[str(x) for x in c]))


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    def __init__(self, fmt: str, color: bool):
        super().__init__()
        self.fmt = fmt
        self.formats = {
            logging.INFO: colorize(self.fmt, "grey", not color),
            logging.DEBUG: colorize(self.fmt, "blue", not color),
            logging.WARNING: colorize(self.fmt, "yellow", not color),
            logging.ERROR: colorize(self.fmt, "bold_red", not color),
            logging.CRITICAL: colorize(self.fmt, "bold_red_underline", not color),
        }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def colorize(txt: str, color: str, no_color: bool = False) -> str:
    known_colors = {
        "grey": "\x1b[37;1m",
        "blue": "\x1b[94;1m",
        "yellow": "\x1b[93;1m",
        "bold_red": "\x1b[31;1m",
        "bold_red_underline": "\x1b[31;1;4m",
    }
    reset = "\x1b[0m"
    if no_color:
        return txt
    return known_colors[color] + txt + reset


class LevelFilter(logging.Filter):
    def __init__(self, levels: Iterable[str]):
        self.levels = levels

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in self.levels


class TraceFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        filename = Path(record.pathname).parts[-1]
        record.func_trace = f"{filename}:{record.lineno} {record.funcName}()"
        return True


logger = logging.getLogger(__package__)


def init_logger(level: str = "INFO") -> None:
    """
    initialize global logger
    note: this is not threadsafe
    """
    loglevels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    global logger

    logger = logging.getLogger(__package__)
    logger.handlers.clear()
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.addFilter(LevelFilter(["INFO"]))
    stdout_handler.addFilter(TraceFilter())

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.addFilter(
        LevelFilter(
            [
                "WARNING",
                "DEBUG",
                "ERROR",
                "CRITICAL",
            ]
        )
    )
    stderr_handler.addFilter(TraceFilter())

    colorize = (sys.stdout.isatty() and sys.stderr.isatty()) and not platform.system() == "Windows"

    if level in ["DEBUG"]:
        formatter = CustomFormatter(
            "%(asctime)s | %(threadName)s | " "%(func_trace)-40s - %(levelname)-8s - %(message)s",
            color=colorize,
        )
    else:
        formatter = CustomFormatter("%(message)s", color=colorize)

    stdout_handler.setFormatter(formatter)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    logger.setLevel(loglevels[level])
