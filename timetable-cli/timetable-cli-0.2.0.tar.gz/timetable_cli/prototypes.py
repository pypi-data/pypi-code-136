import datetime
import hashlib
import logging
from collections import UserList
from dataclasses import dataclass
from typing import List, Optional

from timetable_cli.activity import Activity
from timetable_cli.category import ActivityCategory
from timetable_cli.timetable import Timetable
from timetable_cli.utils import compose_datetime, time_from_time_str

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass(kw_only=True)
class ActivityPrototype:
    def get(self, date: datetime.date) -> List[Activity]:
        pass


@dataclass(kw_only=True)
class DailyActivityPrototype(ActivityPrototype):
    start: datetime.time
    title: str
    variation: Optional[str] = None
    category: Optional[ActivityCategory] = None

    def __init__(
        self,
        start: datetime.time | str,
        title: str,
        variation: Optional[str] = None,
        *args,
        category: Optional[ActivityCategory] = None
    ):
        if not isinstance(start, datetime.time):
            start = time_from_time_str(start)
        self.title = title
        self.start = start
        self.variation = variation
        self.category = category

    def get(self, date: datetime.date) -> List[Activity]:
        return [
            Activity(
                start=compose_datetime(date, self.start),
                title=self.title,
                variation=self.variation,
                category=self.category,
            )
        ]


@dataclass(kw_only=True)
class ActivitiesGroup(ActivityPrototype):
    activities: List[ActivityPrototype]
    title: Optional[str]

    def get(self, date: datetime.date) -> List[Activity]:
        result = []
        for activity_prototype in self.activities:
            result.extend(activity_prototype.get(date))
        return result


@dataclass(kw_only=True)
class WeeklyActivityPrototype(ActivityPrototype):
    mon: Optional[ActivityPrototype] = None
    tue: Optional[ActivityPrototype] = None
    wed: Optional[ActivityPrototype] = None
    thu: Optional[ActivityPrototype] = None
    fri: Optional[ActivityPrototype] = None
    sat: Optional[ActivityPrototype] = None
    sun: Optional[ActivityPrototype] = None
    default: Optional[ActivityPrototype] = None

    _WEEK_DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    def get(self, date: datetime.date) -> List[Activity]:
        week_day_number = date.weekday()
        activity = getattr(self, self._WEEK_DAYS[week_day_number])
        if not activity:
            if self.default:
                activity = self.default
            else:
                raise TypeError
        return activity.get(date)

    def __post__init__(self):
        self._check()

    def _check(self):
        for val in self._WEEK_DAYS + ["default"]:
            if getattr(self, val):
                return
        raise ValueError


class TimetablePrototype(UserList):
    data: List[ActivityPrototype]
    date: Optional[datetime.date] = None

    def get(self, date: datetime.date) -> Timetable:
        activities = []
        for prototype in self.data:
            activities.extend(prototype.get(date))
        timetable = Timetable(activities)
        for activity in timetable:
            activity._timetable = timetable
        timetable.date = date
        return timetable
