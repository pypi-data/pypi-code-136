import datetime
import logging
import re
from typing import Any, List, Optional, Type

from timetable_cli.activity import Activity
from timetable_cli.timetable import Timetable

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

DEFAULT_SHORTCUTS = {
    "now": "0",
    "nownext": "0..1",
    "all": "#0..",
    "after": "0..",
    "next": "1",
    "previous": "-1",
}


class WrongSelectorType(Exception):
    pass


class ActivityNotFound(Exception):
    pass


class _SelectorType:
    pass


class SimpleSelector(_SelectorType):
    _examples: List[str]
    RE: str
    FULL_RE: str
    _VALUE_TYPE: Type
    value: Any

    def __init__(self, selector: str):
        parsed = re.search(self.RE, selector)
        if parsed is None:
            raise WrongSelectorType
        value_str = parsed.group()
        if self._VALUE_TYPE:
            value = self._VALUE_TYPE(value_str)
        else:
            value = value_str
        logger.debug(
            "%s, %s, %s", self.__class__.__name__, selector, value)
        self.value = value

    def get(
        self, timetable: Timetable, datetime_input: datetime.datetime
    ) -> List[Activity]:
        pass


class ComplexSelector(SimpleSelector):
    def solve(self, timetable: Timetable) -> List[_SelectorType]:
        return [self]


class SelectorNumber(SimpleSelector):
    _examples = ["#123", "#0", "#-123"]
    RE = r"(?<=^#)-?\d+$"
    FULL_RE = r"^#-?\d+$"
    _VALUE_TYPE = int

    def get(self, timetable, datetime_input) -> List[Activity]:
        return [timetable[self.value]]


class SelectorCentered(SimpleSelector):
    _examples = ["123", "0", "-123"]
    _VALUE_TYPE = int
    RE = r"^-?\d+$"
    FULL_RE = r"^-?\d+$"

    def get(self, timetable, datetime_input) -> List[Activity]:
        center = timetable.for_datetime(datetime_input)
        return [timetable.centered(center)[int(self.value)]]


simple_selectors = [SelectorNumber, SelectorCentered]
simple_selectors_re = [x.FULL_RE for x in simple_selectors]
simple_selectors_re_all = (
    ")|(".join(simple_selectors_re).replace("^", "").replace("$", "")
)
_SIMPLE_SELECTOR_RE = f"({simple_selectors_re_all})"


class RangeSelector(ComplexSelector):
    _examples = ["now..123", "-123..", "#0..#123"]
    # RE = "^" + _SIMPLE_SELECTOR_RE + r"\.\." + _SIMPLE_SELECTOR_RE + "$"
    _VALUE_TYPE = str
    RE = r"^.*\.\..*$"
    FULL_RE = r"^.*\.\..*$"

    def get(self, timetable, datetime_input) -> List[Activity]:
        logger.debug(self.value)
        re_1 = _SIMPLE_SELECTOR_RE.replace("(", "(^")
        re_2 = _SIMPLE_SELECTOR_RE.replace(")", "$)")
        match_1 = re.search(re_1, self.value)
        match_2 = re.search(re_2, self.value)
        logger.debug(re_1)
        logger.debug(re_2)

        def get_activity(re_match) -> Optional[Activity]:
            logger.debug(re_match)
            if not re_match:
                return None
            selector = parse_selector(re_match.group())
            activity = selector.get(timetable, datetime_input)
            return activity

        activity_1 = get_activity(match_1)
        activity_2 = get_activity(match_2)

        def get_index(activity: Optional[Activity]):
            if not activity:
                return None
            if isinstance(activity, list):
                if len(activity) != 1:
                    raise ValueError
                activity = activity[0]
            return timetable.index(activity)

        i_1 = get_index(activity_1)
        i_2 = get_index(activity_2)
        if i_2:
            i_2 += 1
        result = list(timetable[i_1:i_2])
        return result


class TitleSelector(SimpleSelector):
    RE = r"^.*$"
    FULL_RE = r"^.*$"
    _VALUE_TYPE = str

    def get(self, timetable, datetime_input) -> List[Activity]:
        value = self.value
        for activity in timetable:
            if activity.title == value:
                return [activity]
        raise ActivityNotFound(f"'{value}'")


class TitleSelectorMultipleActivities(TitleSelector):
    RE = r"^.*(?=\+$)"
    FULL_RE = r"^.*\+$"
    _VALUE_TYPE = str

    def get(self, timetable, datetime_input):
        value = self.value
        result = []
        for activity in timetable:
            if activity.title == value:
                result.append(activity)
        return result


class ShortcutSelector(ComplexSelector):
    shortcuts = DEFAULT_SHORTCUTS
    _VALUE_TYPE = str

    @property
    def RE(self):
        shortcuts = "|".join(self.shortcuts.keys())
        return f"^({shortcuts})$"

    def get(self, timetable, datetime_input) -> List[Activity]:
        selectors = self.solve(timetable)
        result = []
        for selector in selectors:
            result.extend(selector.get(timetable, datetime_input))
        return result

    def solve(self, timetable) -> List[SimpleSelector]:
        solved = parse_selector(self.shortcuts[self.value])
        result = []
        if isinstance(solved, ComplexSelector):
            result.extend(solved.solve(timetable))
        else:
            result.append(solved)
        return result

    def solve_no_recursion(self, timetable):
        return parse_selector(self.shortcuts[self.value])


SELECTORS = [
    SelectorNumber,
    SelectorCentered,
    RangeSelector,
    ShortcutSelector,
    TitleSelectorMultipleActivities,
    TitleSelector,
]


def parse_selector(selector) -> _SelectorType:
    for x in SELECTORS:
        try:
            return x(selector)
        except WrongSelectorType:
            pass
    raise ValueError


def parse_selectors(selectors) -> List[_SelectorType]:
    return [parse_selector(x) for x in selectors]
