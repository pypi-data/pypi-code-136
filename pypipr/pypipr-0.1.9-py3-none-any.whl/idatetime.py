IDATETIME = True

"""PYPIPR Module"""


"""PYTHON Standard Module"""
import datetime


"""PYPI Module"""
import pytz


def datetime_now(timezone=None):
    """
    Datetime pada timezone tertentu
    """
    tz = pytz.timezone(timezone) if timezone else None
    return datetime.datetime.now(tz)
