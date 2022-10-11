import abc
from datetime import datetime
from typing import Optional


class ABCMessager(abc.ABC):
    @abc.abstractmethod
    def report(self, checker: str, target: str, status: bool, start: datetime, end: Optional[datetime] = None) -> bool:
        ...
