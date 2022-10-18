import datetime
from typing import Optional, Union

from sqlalchemy import DateTime, TypeDecorator


class UtcDateTime(TypeDecorator):
    """A timestamp, converted to UTC before DB insertion, optionally as a timezoned timestamp.

    The local orm value must be a :class:`datetime.datetime` with a the ``tzinfo`` set.

    Upon return from the database, the timezone of the python object will be converted to UTC.
    If the database does not store the timezone, then the raw value will be interpreted with the UTC timezone.
    (This should generally be a no-op, since we convert to UTC upon inserting into the database.)
    """

    impl = DateTime

    cache_ok = True

    def process_bind_param(self, value: Optional[Union[datetime.datetime, datetime.timedelta]], dialect):
        if value is not None:
            if not isinstance(value, datetime.datetime):
                raise TypeError("expected datetime, not " + repr(value))
            elif value.tzinfo is None:
                raise ValueError("unzoned datetime is disallowed")

            return value.astimezone(datetime.timezone.utc)
        return None

    def process_result_value(self, value: Optional[Union[datetime.datetime, datetime.timedelta]], dialect):
        if value is not None:
            if value.tzinfo is None:
                value = value.replace(tzinfo=datetime.timezone.utc)
            elif isinstance(value, datetime.datetime):
                assert value == value.astimezone(
                    datetime.timezone.utc
                ), "If a timezone is set in the DB, it must be UTC."
            else:
                raise TypeError(f"Unexpected datetime type: {type(value).__name__}")

        return value
