from __future__ import annotations
from datetime import timedelta
from typing import (ByteString, Any, Optional, Literal, Callable)
from ...fable_library.array import (map, fold as fold_1, sum_by, choose)
from ...fable_library.date import (create, to_string)
from ...fable_library.int32 import parse
from ...fable_library.option import default_arg
from ...fable_library.range import range_double
from ...fable_library.seq import (to_array, fold)
from ...fable_library.string import substring
from ...fable_library.types import (uint8, Uint8Array, Array)
from ..context import (Context, Profile__get_parseJourneyLeg)
from ..extra_types import (IndexMap_2, IndexMap_2__set_Item_541DA560, IndexMap_2__ctor_2B594)
from ..lib.transformations import Default_Journey
from ..types_hafas_client import (Leg, Cycle, Journey, FeatureCollection)
from ..types_raw_hafas_client import (RawOutCon, RawSec, RawFreq, RawRecon)
from .common import msg_lto_remarks
from .polyline import distance_of_feature_collection

def mapping(x: int) -> uint8:
    value: int = (1 << (7 - x)) or 0
    return int(value+0x100 if value < 0 else value) & 0xFF


bytes: ByteString = map(mapping, to_array(range_double(0, 1, 7)), Uint8Array)

def parse_scheduled_days(ctx: Context, s_days: str, year: int) -> IndexMap_2[str, bool]:
    dt: Any = create(year, 1, 1)
    source: ByteString = bytes.fromhex(s_days)
    def folder_1(m: IndexMap_2[str, bool], d: uint8, ctx: Context=ctx, s_days: str=s_days, year: int=year) -> IndexMap_2[str, bool]:
        def folder(m_1: IndexMap_2[str, bool], b: uint8, m: IndexMap_2[str, bool]=m, d: uint8=d) -> IndexMap_2[str, bool]:
            nonlocal dt
            IndexMap_2__set_Item_541DA560(m_1, to_string(dt, "yyyy-MM-dd"), (d & b) != uint8(0))
            dt = dt+timedelta(days=1)
            return m_1

        return fold_1(folder, m, bytes)

    return fold(folder_1, IndexMap_2__ctor_2B594(False), source)


def parse_journey(ctx: Context, j: RawOutCon) -> Journey:
    def mapping(l: RawSec, ctx: Context=ctx, j: RawOutCon=j) -> Leg:
        return Profile__get_parseJourneyLeg(ctx.profile)(ctx)(l)(j.date)

    legs: Array[Leg] = map(mapping, j.sec_l, None)
    remarks: Optional[Array[Any]] = default_arg(msg_lto_remarks(ctx, j.msg_l), [0] * 0) if ctx.opt.remarks else None
    scheduled_days: Optional[IndexMap_2[str, bool]]
    matchValue_1: Optional[str] = j.s_days.s_days_b
    (pattern_matching_result,) = (None,)
    if ctx.opt.scheduled_days:
        if matchValue_1 is not None:
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        scheduled_days = parse_scheduled_days(ctx, matchValue_1, parse(substring(j.date, 0, 4), 511, False, 32))

    elif pattern_matching_result == 1:
        scheduled_days = None

    cycle: Optional[Cycle]
    match_value_1: Optional[RawFreq] = j.freq
    if match_value_1 is None:
        cycle = None

    else: 
        freq: RawFreq = match_value_1
        matchValue_2: Optional[int] = freq.min_c
        matchValue_3: Optional[int] = freq.max_c
        def _arrow444(__unit: Literal[None]=None, ctx: Context=ctx, j: RawOutCon=j) -> Optional[Cycle]:
            max_c: int = matchValue_3 or 0
            min_c: int = matchValue_2 or 0
            return Cycle(min_c * 60, max_c * 60, freq.num_c)

        def _arrow445(__unit: Literal[None]=None, ctx: Context=ctx, j: RawOutCon=j) -> Optional[Cycle]:
            min_c_1: int = matchValue_2 or 0
            return Cycle(min_c_1 * 60, None, None)

        cycle = (_arrow444() if (matchValue_3 is not None) else _arrow445()) if (matchValue_2 is not None) else None

    def _arrow446(__unit: Literal[None]=None, ctx: Context=ctx, j: RawOutCon=j) -> Optional[str]:
        match_value_4: Optional[RawRecon] = j.recon
        return None if (match_value_4 is None) else match_value_4.ctx

    return Journey(Default_Journey.type, legs, _arrow446() if (j.ctx_recon is None) else j.ctx_recon, remarks, Default_Journey.price, cycle, scheduled_days)


def distance_of_journey(j: Journey) -> float:
    def _arrow447(fc: FeatureCollection, j: Journey=j) -> float:
        return distance_of_feature_collection(fc)

    def chooser(l: Leg, j: Journey=j) -> Optional[FeatureCollection]:
        return l.polyline

    class ObjectExpr450:
        @property
        def GetZero(self) -> Callable[[], float]:
            def _arrow448(__unit: Literal[None]=None) -> float:
                return 0.0

            return _arrow448

        @property
        def Add(self) -> Callable[[float, float], float]:
            def _arrow449(x: float, y: float) -> float:
                return x + y

            return _arrow449

    return sum_by(_arrow447, choose(chooser, j.legs, None), ObjectExpr450())


__all__ = ["bytes", "parse_scheduled_days", "parse_journey", "distance_of_journey"]

