import datetime
from typing import Optional, Union

from sqlalchemy import DateTime, TypeDecorator
from sqlalchemy.engine import Dialect


class UtcDateTime(TypeDecorator):
    """A timestamp, converted to UTC before DB insertion, optionally as a timezoned timestamp.

    The local orm value must be a :class:`datetime.datetime` with a the ``tzinfo`` set.

    Upon return from the database, the timezone of the python object will be converted to UTC.
    If the database does not store the timezone, then the raw value will be interpreted with the UTC timezone.
    (This should generally be a no-op, since we convert to UTC upon inserting into the database.)
    """

    impl = DateTime

    cache_ok = True

    def process_bind_param(
        self, value: Optional[Union[datetime.datetime, str]], dialect: Dialect
    ) -> Optional[datetime.datetime]:
        if value is not None:
            if isinstance(value, str):
                if dialect.name == "bigquery":
                    if value.lower() in ("infinity", "inf", "+inf", "+infinity"):
                        return datetime.datetime.max
                    elif value.lower() in ("-infinity", "-inf"):
                        return datetime.datetime.min
                value = datetime.datetime.fromisoformat(value)
            if not isinstance(value, datetime.datetime):
                raise TypeError("expected datetime, not " + repr(value))
            elif value.tzinfo is None:
                raise ValueError("unzoned datetime is disallowed")

            return value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
        return None

    def process_result_value(self, value: Optional[datetime.datetime], dialect: Dialect) -> Optional[datetime.datetime]:
        if value is not None:
            if not isinstance(value, datetime.datetime):
                raise TypeError(f"Unexpected datetime type: {type(value).__name__}")
            if value.tzinfo is not None:
                raise TypeError(f"DB datetime should not have a timezone")
            return value.replace(tzinfo=datetime.timezone.utc)
        return value

    def process_literal_param(self, value: Optional[Union[datetime.datetime, str]], dialect: Dialect) -> Optional[str]:
        # Need to override how to process a literal param, as the built-in SQLAlcehmy DateTime object
        # does not have a literal processor
        bind_value = self.bind_processor(dialect)(value)
        if bind_value is None:
            return "NULL"
        else:
            assert isinstance(bind_value, datetime.datetime)
            return f'"{bind_value.isoformat()}"'
