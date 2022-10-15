import datetime
import logging
import re
import string
from dataclasses import dataclass
from typing import List, Optional

from rich.color import ANSI_COLOR_NAMES
from rich.default_styles import DEFAULT_STYLES

from timetable_cli.colorscheme import DEFAULT_COLORSCHEME

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def now(global_timedelta: Optional[datetime.timedelta] = None):
    _now = datetime.datetime.now()
    if global_timedelta:
        return _now + global_timedelta
    return _now


def time_from_time_str(time_str) -> datetime.time:
    return datetime.time(*[int(x) for x in re.findall(r"\d\d", time_str)])


def uppercase_letters_list() -> List[str]:
    return list(string.ascii_uppercase)[::-1]


def remove_tags(input_str: str) -> str:
    return re.sub(r"\[/?[^\ ]]*\]", "", input_str)


def tag(input_str: str, tag: str) -> str:
    return f"[{tag}]{input_str}[/{tag}]"


def compose_datetime(
    input_date: datetime.date, input_time: datetime.time
) -> datetime.datetime:
    return datetime.datetime(
        year=input_date.year,
        month=input_date.month,
        day=input_date.day,
        hour=input_time.hour,
        minute=input_time.minute,
        second=input_time.second,
        microsecond=input_time.microsecond,
    )


def check_colorscheme(colorscheme: dict):
    for key, val in colorscheme.items():
        if not isinstance(val, str):
            raise TypeError
        if key not in DEFAULT_COLORSCHEME:
            raise ValueError(
                f"Key '{key}' not in 'DEFAULT_COLORSCHEME'")
        for element in val.split():
            if (
                element not in ANSI_COLOR_NAMES.keys()
                and element not in DEFAULT_STYLES.keys()
            ):
                raise ValueError(
                    f"Key '{element}' not in 'ANSI_COLOR_NAMES' or 'DEFAULT_STYLES'"
                )


@dataclass
class TimedeltaParsed:
    days: int
    hours: int
    minutes: int
    seconds: int
    microseconds: int

    def format(self) -> str:
        data = {
            "day": self.days,
            "hour": self.hours,
            "minute": self.minutes,
            "second": self.seconds,
            "microseconds": self.microseconds,
        }
        elements = []
        for key, val in data.items():
            if val:
                elements.append(f"{val} {key}(s)")
        return ", ".join(elements)

    def format_short(self) -> str:
        data = {
            "d": self.days,
            "h": self.hours,
            "m": self.minutes,
            "s": self.seconds,
            # "m": self.microseconds,
        }
        elements = []
        for key, val in data.items():
            if val:
                elements.append(f"{val}{key}")
        return " ".join(elements)

    def format_minutes(self) -> str:
        minutes = 0
        minutes += self.days * 24 * 60
        minutes += self.hours * 60
        minutes += self.minutes
        return str(minutes) + "m"


def parse_timedelta(data: datetime.timedelta):
    total_minutes = int(data.seconds / 60)
    kwargs = {
        "days": data.days,
        "hours": int(total_minutes / 60),
        "minutes": total_minutes % 60,
        "seconds": data.seconds % 60,
        "microseconds": int(data.microseconds % 100000),
    }
    return TimedeltaParsed(**kwargs)


def parse_timedelta_str(input_str: str) -> datetime.timedelta:
    data = {
        "d": "days",
        "h": "hours",
        "m": "minutes",
        "s": "seconds",
    }
    kwargs = {}
    for key, val in data.items():
        m = re.search(r"-?\d+(?=" + key + r")", input_str)
        if not m:
            continue
        kwargs.update({val: int(m.group())})
    return datetime.timedelta(**kwargs)
