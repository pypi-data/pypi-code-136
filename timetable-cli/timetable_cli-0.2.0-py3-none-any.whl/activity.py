import datetime
import logging
from dataclasses import dataclass, field
from typing import Any, Optional

from timetable_cli.category import ActivityCategory
from timetable_cli.enums import ActivityTimeStatus
from timetable_cli.utils import format_time, parse_timedelta

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass(kw_only=True)
class Activity:
    start: datetime.datetime
    title: str
    variation: str = ""
    category: Optional[ActivityCategory] = None
    colorscheme: dict = field(default_factory=dict)
    _timetable: Optional[Any] = None

    def get_status(self, application: Any):
        """The status property."""
        cur = application.connection.cursor()
        cur.execute(
            f"""
SELECT status FROM records WHERE title='{self.title}' AND date='{self._timetable.date.isoformat()};'"""
        )
        return cur.fetchone()

    def set_status(self, application: Any, value):
        application.connection.cursor().execute(
            f"""
INSERT INTO records (title='{self.title}', date='{self._timetable.date.isoformat()}', status='{value}');"""
        )

    def next(self):
        if not self._timetable:
            raise ValueError
        index = self._timetable.index(self)
        if index == len(self._timetable) - 1:
            return self._timetable[0]
        return self._timetable[index + 1]

    def total_time(self) -> datetime.timedelta:
        result = self.next().start - self.start
        if result.days < 0:
            result = datetime.timedelta(seconds=result.seconds)
        return result

    def total_time_str(self) -> str:
        return parse_timedelta(self.total_time()).format_minutes()

    def eta(self, application) -> str:
        return parse_timedelta(self.start - application.now()).format_minutes()

    def start_str(self):
        return format_time(self.start.time())

    def time_status(self, datetime_input: datetime.datetime) -> ActivityTimeStatus:
        if datetime_input > self.start and datetime_input > self.next().start:
            result = ActivityTimeStatus.BEFORE
        elif datetime_input > self.start and datetime_input < self.next().start:
            result = ActivityTimeStatus.NOW
        else:
            result = ActivityTimeStatus.AFTER
        logger.debug(result)
        return result
