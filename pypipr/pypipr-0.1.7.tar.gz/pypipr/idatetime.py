import datetime
import pytz


def datetime_now(timezone=None):
    """
    Datetime pada timezone tertentu
    """
    tz = pytz.timezone(timezone) if timezone else None
    return datetime.datetime.now(tz)
