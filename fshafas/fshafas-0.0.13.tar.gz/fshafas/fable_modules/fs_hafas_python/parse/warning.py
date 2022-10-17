from __future__ import annotations
from typing import (Optional, Callable)
from ...fable_library.array import map as map_1
from ...fable_library.option import map
from ...fable_library.string import replace
from ...fable_library.types import (Array, Int32Array)
from ..context import (Context, Profile__get_parseDateTime, Profile__get_parseBitmask)
from ..extra_types import IndexMap_2
from ..lib.transformations import Default_Warning
from ..types_hafas_client import (IcoCrd, Edge, Event, Line, Warning)
from ..types_raw_hafas_client import (RawHimMsgEdge, RawHimMsgEvent, RawHim, RawHimMsgCat, RawCommon)
from .common import (get_element_at_some, map_index_array, to_option)

def parse_msg_edge(ctx: Context, e: RawHimMsgEdge) -> Edge:
    ico_crd: Optional[IcoCrd] = IcoCrd(e.ico_crd.x, e.ico_crd.y, None)
    return Edge(get_element_at_some(e.f_loc_x, ctx.common.locations), get_element_at_some(e.t_loc_x, ctx.common.locations), get_element_at_some(e.ico_x, ctx.common.icons), e.dir, ico_crd)


def parse_msg_event(ctx: Context, e: RawHimMsgEvent) -> Event:
    return Event(get_element_at_some(e.f_loc_x, ctx.common.locations), get_element_at_some(e.t_loc_x, ctx.common.locations), Profile__get_parseDateTime(ctx.profile)(ctx)(e.f_date)(e.f_time)(None), Profile__get_parseDateTime(ctx.profile)(ctx)(e.t_date)(e.t_time)(None), [0] * 0)


def parse_date_time(ctx: Context, date: Optional[str]=None, time: Optional[str]=None) -> Optional[str]:
    if date is not None:
        date_1: str = date
        return Profile__get_parseDateTime(ctx.profile)(ctx)(date_1)(time)(None)

    else: 
        return None



def parse_warning(ctx: Context, w: RawHim) -> Warning:
    def mapping(p_cls: int, ctx: Context=ctx, w: RawHim=w) -> IndexMap_2[str, bool]:
        return Profile__get_parseBitmask(ctx.profile)(ctx)(p_cls)

    products: Optional[IndexMap_2[str, bool]] = map(mapping, w.prod)
    def mapping_1(c_1: RawHimMsgCat, ctx: Context=ctx, w: RawHim=w) -> int:
        return c_1.id

    def get_target_array(c: RawCommon, ctx: Context=ctx, w: RawHim=w) -> Optional[Array[RawHimMsgCat]]:
        return c.him_msg_cat_l

    categories: Array[int] = map_1(mapping_1, map_index_array(ctx.res.common, get_target_array, w.cat_ref_l), Int32Array)
    def mapping_2(e: RawHimMsgEvent, ctx: Context=ctx, w: RawHim=w) -> Event:
        return parse_msg_event(ctx, e)

    def get_target_array_1(c_2: RawCommon, ctx: Context=ctx, w: RawHim=w) -> Optional[Array[RawHimMsgEvent]]:
        return c_2.him_msg_event_l

    events: Optional[Array[Event]] = to_option(map_1(mapping_2, map_index_array(ctx.res.common, get_target_array_1, w.event_ref_l), None))
    def mapping_3(e_1: RawHimMsgEdge, ctx: Context=ctx, w: RawHim=w) -> Edge:
        return parse_msg_edge(ctx, e_1)

    def get_target_array_2(c_3: RawCommon, ctx: Context=ctx, w: RawHim=w) -> Optional[Array[RawHimMsgEdge]]:
        return c_3.him_msg_edge_l

    edges: Optional[Array[Edge]] = to_option(map_1(mapping_3, map_index_array(ctx.res.common, get_target_array_2, w.edge_ref_l), None))
    def get_target_array_3(_arg: RawCommon, ctx: Context=ctx, w: RawHim=w) -> Optional[Array[Line]]:
        return ctx.common.lines

    affected_lines: Optional[Array[Line]] = to_option(map_index_array(ctx.res.common, get_target_array_3, w.aff_prod_ref_l))
    def br_to_newline(s: Optional[str]=None, ctx: Context=ctx, w: RawHim=w) -> Optional[str]:
        def mapping_4(s_1: str, s: Optional[str]=s) -> str:
            return replace(s_1, "<br>", "\n")

        return map(mapping_4, s)

    return Warning(Default_Warning.type, w.hid, get_element_at_some(w.ico_x, ctx.common.icons), br_to_newline(w.head), br_to_newline(w.text), Default_Warning.category, w.prio, products, edges, events, parse_date_time(ctx, w.s_date, w.s_time), parse_date_time(ctx, w.e_date, w.e_time), parse_date_time(ctx, w.l_mod_date, w.l_mod_time), w.comp, categories, affected_lines, Default_Warning.from_stops, Default_Warning.to_stops)


__all__ = ["parse_msg_edge", "parse_msg_event", "parse_date_time", "parse_warning"]

