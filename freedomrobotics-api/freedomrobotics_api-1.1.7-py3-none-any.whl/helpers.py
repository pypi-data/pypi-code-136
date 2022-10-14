import re
import time
import logging

date_short_relative_regex = re.compile(r'^[+-]\d+[smdhwMY]$')

logger = logging.getLogger(__name__)


def to_struct_time(t):
    """Converts a UNIX time, a time string, or a struct_time to a struct_time.
    """

    if t is None:
        return t

    if type(t) == float:
        return time.gmtime(t)
    elif type(t) == int:
        return time.gmtime(t)
    elif type(t) == str:
        return time.strptime(t, "%Y-%m-%d %H:%M:%S")
    elif type(t) == time.struct_time:
        return t

    logger.debug("parse_time: could not parse time: ", t)
    return None


def to_time_query_param(value):
    """Parse value to API time query parameter"""
    if isinstance(value, str) and is_short_relative_date(value):
        return value
    else:
        return to_unix_time(value)


def to_unix_time(t):
    """Converts a UNIX time, a time string, or a struct_time to a UNIX time.
    """

    if t is None:
        return t

    if type(t) == float:
        return t
    elif type(t) == int:
        return float(t)
    elif type(t) == str:
        return time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S"))
    elif type(t) == time.struct_time:
        return time.mktime(t)

    logger.debug("parse_time: could not parse time: ", t)
    return None


def is_short_relative_date(value):
    """Checks if the value matches with short relative dates used for API time ranges
    Examples:
    * 25s: 25 seconds
    * 10m: 10 minutes
    * 3h: 3 hours
    * 5d: 5 days
    * 1w: 1 week
    """
    if value.lower() == 'now':
        return True
    return date_short_relative_regex.match(value) is not None
