"display / terminal color handling functions"
import sys

from e2j2 import cache

BRIGHT_RED = "\033[1;31m"
RESET_ALL = "\033[00m"
YELLOW = "\033[93m"
GREEN = "\033[0;32m"
LIGHTGREEN = "\033[1;32m"
WHITE = "\033[0;37m"


class Colorize:
    red = BRIGHT_RED
    reset = RESET_ALL
    yellow = YELLOW
    green = GREEN
    lightgreen = LIGHTGREEN
    white = WHITE


COLORS = Colorize()


def get_colors():
    return COLORS


def colorize():
    global COLORS
    COLORS = Colorize()


def no_colors():
    global COLORS
    COLORS = Colorize()
    COLORS.red = ""
    COLORS.reset = ""
    COLORS.yellow = ""
    COLORS.green = ""
    COLORS.lightgreen = ""
    COLORS.white = ""


def write(msg):
    print_at = cache.print_at
    increment = cache.increment
    counter = cache.log_repeat_log_msg_counter

    if cache.last_log_line != msg:
        sys.stderr.write(msg)
        cache.log_repeat_log_msg_counter = 0
    elif counter == print_at:
        sys.stderr.write(f"({print_at}x) {msg}")
        cache.print_at += increment
        cache.log_repeat_log_msg_counter = 0

    cache.log_repeat_log_msg_counter += 1
    cache.last_log_line = msg
