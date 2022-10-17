from __future__ import annotations
from typing import (Optional, Any)
from ...fable_library.date import now
from ...fable_library.string import (to_text, printf)
from ...fable_library.types import Array
from ..context import (Context, Profile__get_parseJourneyLeg)
from ..lib.transformations import (RawDep_FromRawStopL, RawArr_FromRawStopL, ToTrip_FromLeg)
from ..types_hafas_client import (Leg, Trip)
from ..types_raw_hafas_client import (RawJny, RawStop, RawSec)

def parse_trip(ctx: Context, j: RawJny) -> Trip:
    match_value: Optional[Array[RawStop]] = j.stop_l
    (pattern_matching_result, stop_l_1) = (None, None)
    if match_value is not None:
        if len(match_value) > 1:
            pattern_matching_result = 0
            stop_l_1 = match_value

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        raw_sec_l: RawSec = RawSec("JNY", None, RawDep_FromRawStopL(stop_l_1[0]), RawArr_FromRawStopL(stop_l_1[len(stop_l_1) - 1]), j, None, None, None)
        date_1: str
        match_value_1: Optional[str] = j.date
        if match_value_1 is None:
            dt: Any = now()
            arg_2: int = (dt.day) or 0
            arg_1: int = (dt.month) or 0
            arg: int = (dt.year) or 0
            date_1 = to_text(printf("%04d%02d%02d"))(arg)(arg_1)(arg_2)

        else: 
            date_1 = match_value_1

        leg: Leg = Profile__get_parseJourneyLeg(ctx.profile)(ctx)(raw_sec_l)(date_1)
        match_value_2: Optional[str] = leg.trip_id
        if match_value_2 is not None:
            return ToTrip_FromLeg(match_value_2, leg)

        else: 
            raise Exception("parseTrip failed")


    elif pattern_matching_result == 1:
        raise Exception("parseTrip failed")



__all__ = ["parse_trip"]

