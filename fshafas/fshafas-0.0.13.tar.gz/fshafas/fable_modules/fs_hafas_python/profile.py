from __future__ import annotations
from typing import (Optional, Any, Literal)
from ..fable_library.types import Array
from .context import (Profile__ctor_Z4BA06F5C, Context, CommonData, Platform, ParsedWhen, Profile)
from .extra_types import (Icon, IndexMap_2)
from .parse.arrival_or_departure import (parse_arrival, parse_departure)
from .parse.common import parse_common
from .parse.date_time import parse_date_time
from .parse.hint import parse_hint
from .parse.icon import parse_icon
from .parse.journey import parse_journey
from .parse.journey_leg import (parse_journey_leg, parse_platform)
from .parse.line import parse_line
from .parse.location import parse_locations
from .parse.movement import parse_movement
from .parse.operator import parse_operator
from .parse.polyline import parse_polyline
from .parse.products_bitmask import parse_bitmask
from .parse.prognosis_type import parse_prognosis_type
from .parse.stopover import (parse_stopover, parse_stopovers)
from .parse.trip import parse_trip
from .parse.warning import parse_warning
from .parse.when import parse_when
from .types_hafas_client import (JourneysOptions, Alternative, FeatureCollection, Line, Journey, Leg, Movement, Operator, StopOver, Trip, Warning)
from .types_raw_hafas_client import (TripSearchRequest, RawCommon, RawJny, RawRem, RawIco, RawPoly, RawLoc, RawProd, RawOutCon, RawSec, RawOp, RawStop, RawHim)

def default_profile(__unit: Literal[None]=None) -> Profile:
    def _arrow457(x: str) -> str:
        return x

    def _arrow458(_arg: Optional[JourneysOptions], q: TripSearchRequest) -> TripSearchRequest:
        return q

    def _arrow459(ctx: Context, c: RawCommon) -> CommonData:
        return parse_common(ctx, c)

    def _arrow460(ctx_1: Context, d: RawJny) -> Alternative:
        return parse_arrival(ctx_1, d)

    def _arrow461(ctx_2: Context, d_1: RawJny) -> Alternative:
        return parse_departure(ctx_2, d_1)

    def _arrow462(ctx_3: Context, h: RawRem) -> Optional[Any]:
        return parse_hint(ctx_3, h)

    def _arrow463(ctx_4: Context, i: RawIco) -> Optional[Icon]:
        return parse_icon(ctx_4, i)

    def _arrow464(ctx_5: Context, poly: RawPoly) -> FeatureCollection:
        return parse_polyline(ctx_5, poly)

    def _arrow465(ctx_6: Context, loc_l: Array[RawLoc]) -> Array[Any]:
        return parse_locations(ctx_6, loc_l)

    def _arrow466(ctx_7: Context, p: RawProd) -> Line:
        return parse_line(ctx_7, p)

    def _arrow467(ctx_8: Context, j: RawOutCon) -> Journey:
        return parse_journey(ctx_8, j)

    def _arrow468(ctx_9: Context, pt: RawSec, date: str) -> Leg:
        return parse_journey_leg(ctx_9, pt, date)

    def _arrow469(ctx_10: Context, m: RawJny) -> Movement:
        return parse_movement(ctx_10, m)

    def _arrow470(ctx_11: Context, a: RawOp) -> Operator:
        return parse_operator(ctx_11, a)

    def _arrow471(ctx_12: Context, platf_s: Optional[str]=None, platf_r: Optional[str]=None, cncl: Optional[bool]=None) -> Platform:
        return parse_platform(ctx_12, platf_s, platf_r, cncl)

    def _arrow472(ctx_13: Context, st: RawStop, date_1: str) -> StopOver:
        return parse_stopover(ctx_13, st, date_1)

    def _arrow473(ctx_14: Context, stop_l: Optional[Array[RawStop]], date_2: str) -> Optional[Array[StopOver]]:
        return parse_stopovers(ctx_14, stop_l, date_2)

    def _arrow474(ctx_15: Context, j_1: RawJny) -> Trip:
        return parse_trip(ctx_15, j_1)

    def _arrow475(ctx_16: Context, date_3: str, time_s: Optional[str]=None, time_r: Optional[str]=None, tz_offset: Optional[int]=None, cncl_1: Optional[bool]=None) -> ParsedWhen:
        return parse_when(ctx_16, date_3, time_s, time_r, tz_offset, cncl_1)

    def _arrow476(ctx_17: Context, date_4: str, time: Optional[str]=None, tz_offset_1: Optional[int]=None) -> Optional[str]:
        return parse_date_time(ctx_17, date_4, time, tz_offset_1)

    def _arrow477(ctx_18: Context, bitmask: int) -> IndexMap_2[str, bool]:
        return parse_bitmask(ctx_18, bitmask)

    def _arrow478(ctx_19: Context, w: RawHim) -> Warning:
        return parse_warning(ctx_19, w)

    def _arrow479(ctx_20: Context, p_1: Optional[str]=None) -> Optional[str]:
        return parse_prognosis_type(ctx_20, p_1)

    return Profile__ctor_Z4BA06F5C("de-DE", "Europe/Berlin", _arrow457, _arrow458, _arrow459, _arrow460, _arrow461, _arrow462, _arrow463, _arrow464, _arrow465, _arrow466, _arrow467, _arrow468, _arrow469, _arrow470, _arrow471, _arrow472, _arrow473, _arrow474, _arrow475, _arrow476, _arrow477, _arrow478, _arrow479)


__all__ = ["default_profile"]

