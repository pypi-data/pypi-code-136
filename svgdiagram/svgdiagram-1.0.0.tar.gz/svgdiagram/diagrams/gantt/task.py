from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime, date


class Task(BaseModel):
    name: str
    start_date: Union[datetime, date]
    end_date: Union[datetime, date]
    progress: Optional[float] = 0.0
    id: Optional[str] = None

    @property
    def done(self):
        return self.progress >= 1.0

    @property
    def duration(self):
        return self.end_date - self.start_date

    def __post_init__(self):
        assert self.end_date > self.start_date,\
            f"End date {self.end_date} lies before start date {self.start_date}!"
