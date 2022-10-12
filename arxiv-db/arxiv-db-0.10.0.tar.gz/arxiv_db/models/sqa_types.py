from typing import Union
from sqlalchemy import Integer
from sqlalchemy.types import TypeDecorator
from datetime import datetime

from arxiv_db import arxiv_business_tz


class EpochIntArxivTz(TypeDecorator):
    """Epoch in arXiv offices TZ represted as an Integer in the db."""
    impl = Integer

    def __init__(self):
        TypeDecorator.__init__(self)

    def process_bind_param(self, dt:Union[datetime, int], dialect):
        if type(dt) == datetime:
            return int(dt.astimezone(arxiv_business_tz).timestamp())
        else:
            return dt


    def process_result_value(self, value:int, dialect):
        if value is not None:
            return datetime.fromtimestamp(value, tz=arxiv_business_tz)
        else:
            return None
