import pytz
from datetime import datetime

from .domain import ICity


class City(ICity):

    def get_utcoffset(self) -> str:
        timezone = pytz.timezone(self.timezone)
        return str(timezone.localize(datetime.now()))[-6:]
