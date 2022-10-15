from datetime import date

from timetable_cli.colorscheme import DEFAULT_COLORSCHEME
from timetable_cli.selectors import DEFAULT_SHORTCUTS
from timetable_cli.timetable import Timetable


def get_timetable(date: date) -> Timetable:
    return Timetable([])


def get_shortcuts() -> dict:
    return DEFAULT_SHORTCUTS


def get_colorscheme() -> dict:
    return DEFAULT_COLORSCHEME
