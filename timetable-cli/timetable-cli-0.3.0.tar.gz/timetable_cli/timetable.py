import datetime
import logging
from collections import UserList
from typing import List, Optional

from timetable_cli.activity import Activity

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Timetable(UserList):
    data: List[Activity]
    date: Optional[datetime.date] = None

    def __init__(self, activities: List[Activity]):
        super().__init__(activities)

    def for_datetime(self, input_datetime: datetime.datetime):
        result = None
        for i, activity in enumerate(self.data):
            if i == 0:
                result = self.data[-1]
                continue
            if i == len(self.data) - 1:
                return activity
            if activity.start > input_datetime:
                return result
            else:
                result = activity

    def centered(self, activity) -> List[Activity]:
        index = self.data.index(activity)
        return self.data[index:] + self.data[:index]

    def get_by_title(self, title: str) -> Activity:
        for x in self.data:
            if x.title == title:
                return x
        raise KeyError

    def __str__(self) -> str:
        return f"Timetable(activities: {len(self.data)}, date: {self.date})"

    def __repr__(self) -> str:
        return self.__str__()

    def __post__init__(self):
        self.data.sort(key=lambda x: x.start)
