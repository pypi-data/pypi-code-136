from __future__ import annotations
from datetime import timedelta
import datetime
from dateutil import tz as tz_1
from typing import (Any, Optional)
from ...fable_library.date import create
from ...fable_library.reflection import (TypeInfo, class_type)
from ...fable_library.string import (to_console, printf)
from ..context import Profile

def _expr295() -> TypeInfo:
    return class_type("FsHafas.Extensions.DateTimeOffsetEx.DateTimeOffsetEx", None, DateTimeOffsetEx)


class DateTimeOffsetEx:
    def __init__(self, dt: Any, tzoffset_arg: Optional[int]=None, tz_arg: Optional[str]=None) -> None:
        self.dt: Any = dt
        self.tzoffset_arg: Optional[int] = tzoffset_arg
        self.tz_arg: Optional[str] = tz_arg


DateTimeOffsetEx_reflection = _expr295

def DateTimeOffsetEx__ctor_26581FE8(dt: Any, tzoffset_arg: Optional[int]=None, tz_arg: Optional[str]=None) -> DateTimeOffsetEx:
    return DateTimeOffsetEx(dt, tzoffset_arg, tz_arg)


def DateTimeOffsetEx__get_DateTime(__: DateTimeOffsetEx) -> Any:
    return DateTimeOffsetEx__getDateTime(__)


def DateTimeOffsetEx__AddDays_5E38073B(__: DateTimeOffsetEx, days: float) -> DateTimeOffsetEx:
    return DateTimeOffsetEx__ctor_26581FE8(__.dt+timedelta(days=int(days)), __.tzoffset_arg, __.tz_arg)


def DateTimeOffsetEx__getDateTime(this: DateTimeOffsetEx) -> Any:
    matchValue: Optional[int] = this.tzoffset_arg
    matchValue_1: Optional[str] = this.tz_arg
    if matchValue is not None:
        tzoffset_arg: int = matchValue or 0
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.tzoffset(None, tzoffset_arg)))

    elif matchValue_1 is not None:
        tz: str = matchValue_1
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.gettz(tz)))

    else: 
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.gettz("Europe/Berlin")))



def parse_date_time_with_offset(profile: Profile, year: int, month: int, day: int, hour: int, minute: int, seconds: int, tz_offset: Optional[int]=None) -> DateTimeOffsetEx:
    try: 
        dt: Any = create(year, month, day, hour, minute, seconds)
        return DateTimeOffsetEx__ctor_26581FE8(dt, None, None) if (tz_offset is None) else DateTimeOffsetEx__ctor_26581FE8(dt, tz_offset * 60, None)

    except Exception as ex:
        arg: str = str(ex)
        to_console(printf("error parseDateTimeWithOffset: %s"))(arg)
        raise Exception(str(ex))



def ToIsoString(dto: DateTimeOffsetEx) -> str:
    dt: Any = DateTimeOffsetEx__get_DateTime(dto)
    return dt.isoformat()


__all__ = ["DateTimeOffsetEx_reflection", "DateTimeOffsetEx__get_DateTime", "DateTimeOffsetEx__AddDays_5E38073B", "DateTimeOffsetEx__getDateTime", "parse_date_time_with_offset", "ToIsoString"]

