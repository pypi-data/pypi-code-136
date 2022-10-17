from __future__ import annotations
from typing import (Any, Optional, Callable)
from ...fable_library.array import (map, filter)
from ...fable_library.option import default_arg
from ...fable_library.types import Array
from ..context import (Context, Profile__get_parseWhen, ParsedWhen, Profile__get_parsePlatform, Platform, Profile__get_parsePrognosisType, Profile__get_parseStopover)
from ..lib.transformations import U2StationStop_FromSomeU3StationStopLocation
from ..types_hafas_client import StopOver
from ..types_raw_hafas_client import (RawStop, RawPltf)
from .common import (get_element_at, msg_lto_remarks)

default_stopover: StopOver = StopOver(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

def parse_stopover(ctx: Context, st: RawStop, date: str) -> StopOver:
    stop: Optional[Any] = U2StationStop_FromSomeU3StationStopLocation(get_element_at(st.loc_x, ctx.common.locations))
    dep: ParsedWhen = Profile__get_parseWhen(ctx.profile)(ctx)(date)(st.d_time_s)(st.d_time_r)(st.d_tzoffset)(st.d_cncl)
    arr: ParsedWhen = Profile__get_parseWhen(ctx.profile)(ctx)(date)(st.a_time_s)(st.a_time_r)(st.a_tzoffset)(st.a_cncl)
    def match_platf_s(a_platf_s: Optional[str]=None, a_pltf_s: Optional[RawPltf]=None, ctx: Context=ctx, st: RawStop=st, date: str=date) -> Optional[str]:
        if a_platf_s is None:
            if a_pltf_s is not None:
                return a_pltf_s.txt

            else: 
                return None


        else: 
            return a_platf_s


    d_platf_s: Optional[str] = match_platf_s(st.d_platf_s, st.d_pltf_s)
    d_platf_r: Optional[str] = match_platf_s(st.d_platf_r, st.d_pltf_r)
    dep_pl: Platform = Profile__get_parsePlatform(ctx.profile)(ctx)(d_platf_s)(d_platf_r)(st.d_cncl)
    a_platf_s_1: Optional[str] = match_platf_s(st.a_platf_s, st.a_pltf_s)
    a_platf_r: Optional[str] = match_platf_s(st.a_platf_r, st.a_pltf_r)
    arr_pl: Platform = Profile__get_parsePlatform(ctx.profile)(ctx)(a_platf_s_1)(a_platf_r)(st.a_cncl)
    pass_by: Optional[bool]
    matchValue: Optional[bool] = st.d_in_s
    matchValue_1: Optional[bool] = st.a_out_s
    (pattern_matching_result,) = (None,)
    if matchValue is not None:
        if matchValue:
            pattern_matching_result = 1

        elif matchValue_1 is not None:
            if matchValue_1:
                pattern_matching_result = 1

            else: 
                pattern_matching_result = 0


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        pass_by = True

    elif pattern_matching_result == 1:
        pass_by = None

    cancelled: Optional[bool] = default_arg(st.a_cncl, st.d_cncl)
    remarks: Optional[Array[Any]] = msg_lto_remarks(ctx, st.msg_l)
    arrival_prognosis_type: Optional[str] = Profile__get_parsePrognosisType(ctx.profile)(ctx)(st.a_prog_type)
    return StopOver(stop, dep.when, dep.delay, default_stopover.prognosed_departure, dep.planned_when, dep_pl.platform, dep_pl.prognosed_platform, dep_pl.planned_platform, arr.when, arr.delay, default_stopover.prognosed_arrival, arr.planned_when, arr_pl.platform, arr_pl.prognosed_platform, arr_pl.planned_platform, remarks, pass_by, cancelled, Profile__get_parsePrognosisType(ctx.profile)(ctx)(st.d_prog_type), arrival_prognosis_type)


def parse_stopovers(ctx: Context, stop_l: Optional[Array[RawStop]], date: str) -> Optional[Array[StopOver]]:
    if stop_l is None:
        return None

    else: 
        def mapping(s_1: RawStop, ctx: Context=ctx, stop_l: Optional[Array[RawStop]]=stop_l, date: str=date) -> StopOver:
            return Profile__get_parseStopover(ctx.profile)(ctx)(s_1)(date)

        def predicate(s: RawStop, ctx: Context=ctx, stop_l: Optional[Array[RawStop]]=stop_l, date: str=date) -> bool:
            return get_element_at(s.loc_x, ctx.common.locations) is not None

        return map(mapping, filter(predicate, stop_l), None)



__all__ = ["default_stopover", "parse_stopover", "parse_stopovers"]

