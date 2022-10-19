# max_logger/main.py
import os
from functools import wraps
from pathlib import Path
from time import perf_counter

from loguru import logger as log
from rich import print
from rich.panel import Panel
from rich.text import Text
from ujson import dump, load

from max_logger.color import *


# _. BASE
def generate_base():
    """Generate base directory for the project."""
    BASE = Path.cwd()
    return BASE


BASE = generate_base()


# . First Run Tasks

# Make JSON Directory
JSON_DIR = BASE / "json"
if not JSON_DIR.exists():
    os.mkdir(f"{BASE}/json")

# Make JSON Directory
LOGS_DIR = BASE / "logs"
if not LOGS_DIR.exists():
    os.mkdir(f"{BASE}/logs")

# Create Dictionary to keep track of runs
RUN_DICT = BASE / "json" / "run.json"
if not RUN_DICT.exists():
    run_dict = {"run": 0}
    with open(RUN_DICT, "w") as outfile:
        dump(run_dict, outfile, indent=4)


# _. Every Run → Get Current Run
def get_last_run() -> int:
    """
    Get the last run of the script.
    """
    with open(RUN_DICT, "r") as infile:
        last_run_dict = dict(load(infile))
    return int(last_run_dict["run"])


def increment_run(last_run: int) -> int:
    """
    Increment the last run of the script.
    """
    run = last_run + 1
    return run


def record_run(run: int) -> None:
    """
    Record the last run of the script.
    """
    run = {"run": run}  # type: ignore
    with open(RUN_DICT, "w") as outfile:
        dump(run, outfile, indent=4)


def new_run() -> int:
    """
    Create a new run of the script.
    """
    # > RUN
    last_run = get_last_run()
    run = increment_run(last_run)
    record_run(run)

    # > Clear and initialize console
    console.clear()
    run_title = rainbow(f"Run {run}", 2)
    console.rule(title=run_title, style="bold bright_white")
    return run


current_run = new_run()


# _. Configure Loguru Logger Sinks
sinks = log.configure(
    handlers=[
        dict(  # debug.log
            sink=f"{BASE}/logs/debug.log",
            level="DEBUG",
            format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
            rotation="10 MB",
        ),
        dict(  # info.log
            sink=f"{BASE}/logs/info.log",
            level="INFO",
            format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
            rotation="10 MB",
        ),
        dict(  # Rich Console Log > INFO
            sink=(
                lambda msg: console.log(
                    msg, markup=True, highlight=True, log_locals=False
                )
            ),
            level="INFO",
            format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: ^8} ﰲ  {message}",
            diagnose=True,
            catch=True,
            backtrace=True,
        ),
        dict(  # Rich Console Log > ERROR
            sink=(
                lambda msg: console.log(
                    msg, markup=True, highlight=True, log_locals=True
                )
            ),
            level="ERROR",
            format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: ^8} ﰲ  {message}",
            diagnose=True,
            catch=True,
            backtrace=True,
        ),
    ],
    extra={"run": current_run},  #  Current Run
)

log.debug("Initialized Logger")
# _, End of handlers


# _. Decorators
@log.catch
def check(
    *,
    entry=True,
    exit=True,
    level="DEBUG",
):
    """Create a decorator that can be used to record the entry, *args, **kwargs,as well ass the exit and results of a decorated function.

    Args:
        entry (bool, optional):
            Should the entry , *args, and **kwargs of given decorated function be logged? Defaults to True.

        exit (bool, optional):
            Should the exit and the result of given decorated function be logged? Defaults to True.

        level (str, optional):
            The level at which to log to be recorded.. Defaults to "DEBUG".
    """

    def wrapper(func):
        name = func.__name__
        log.debug(f"Checking function {name}.")

        @wraps(func)
        def wrapped(*args, **kwargs):
            check_log = log.opt(depth=1)
            if entry:
                check_log.log(
                    level,
                    f"Entering '{name}'\n<code>\nargs:\n{args}'\nkwargs={kwargs}</code>",
                )
            result = func(*args, **kwargs)
            if exit:
                check_log.log(
                    level, f"Exiting '{name}'<code>\nresult:\n<{result}</code>"
                )
            return result

        return wrapped

    return wrapper


def time(*, level="DEBUG"):
    """Create a decorator that can be used to record the entry and exit of a decorated function.
    Args:
        level (str, optional):
            The level at which to log to be recorded.. Defaults to "DEBUG".
    """

    def wrapper(func):
        name = func.__name__
        log.debug(f"Timing function {name}.")

        @wraps(func)
        def wrapped(*args, **kwargs):
            time_log = log.opt(depth=1)
            start = perf_counter()
            result = func(*args, **kwargs)
            end = perf_counter()
            time_log.log(level, f"{name} took {end - start} seconds.")
            return result

        return wrapped

    return wrapper


def logpanel(msg: str, level: str = "INFO") -> None:
    """Log a message to loguru sinks and print to a panel.
    Args:
        msg (str):
            The message to be logged.
    """
    match level:
        case "DEBUG" | "debug" | "d":
            panel = Panel(
                Text(msg, style="bold bright_white"),
                title=Text(
                    "DEBUG",
                    style="debug",
                ),
                title_align="left",
                border_style="debug",
                expand=False,
            )
            console.log(panel, markup=True, highlight=True, log_locals=False)
            log.debug(msg)
        case "INFO" | "info" | "i":
            panel = Panel(
                Text(msg, style="bold bright_white"),
                title=Text(
                    "INFO",
                    style="info",
                ),
                title_align="left",
                border_style="info",
                expand=False,
            )
            console.log(panel, markup=True, highlight=True, log_locals=False)
            log.info(msg)
        case "WARNING" | "warning" | "w":
            panel = Panel(
                Text(msg, style="bold bright_white"),
                title=Text(
                    "WARNING",
                    style="warning",
                ),
                title_align="left",
                border_style="warning",
                expand=False,
            )
            console.log(panel, markup=True, highlight=True, log_locals=False)
            log.warning(msg)
        case "ERROR" | "error" | "e":
            panel = Panel(
                Text(msg, style="bold bright_white"),
                title=Text(
                    "ERROR",
                    style="error",
                ),
                title_align="left",
                border_style="error",
                expand=False,
            )
            console.log(panel, markup=True, highlight=True, log_locals=True)
            log.error(msg)
        case "CRITICAL" | "critical" | "c":
            panel = Panel(
                Text(msg, style="bold bright_white"),
                title=Text(
                    "CRITICAL",
                    style="critical",
                ),
                title_align="left",
                border_style="critical",
                expand=False,
            )
            console.log(panel, markup=True, highlight=True, log_locals=True)
            log.critical(msg)
        case _:
            console.log(msg, markup=True, highlight=True, log_locals=False)
            log.info(msg)


# _, End of Decorators
