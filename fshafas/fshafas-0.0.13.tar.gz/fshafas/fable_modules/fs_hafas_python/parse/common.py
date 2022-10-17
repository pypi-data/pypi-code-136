from __future__ import annotations
from typing import (Literal, Any, Optional, TypeVar, Callable)
from ...fable_library.array import (map, choose, append)
from ...fable_library.option import (default_arg, some)
from ...fable_library.types import Array
from ..context import (Context, CommonData, Profile__get_parseOperator, Profile__get_parseLine, Profile__get_parseHint, Profile__get_parseIcon, Profile__get_parseLocations, Profile__get_parsePolyline)
from ..extra_types import Icon
from ..types_hafas_client import (Operator, Line, FeatureCollection)
from ..types_raw_hafas_client import (RawCommon, RawOp, RawProd, RawRem, RawIco, RawPoly, RawMsg)

_A = TypeVar("_A")

_B = TypeVar("_B")

def update_operators(ctx: Context, ops: Array[Operator]) -> Context:
    def _arrow364(__unit: Literal[None]=None, ctx: Context=ctx, ops: Array[Operator]=ops) -> CommonData:
        input_record: CommonData = ctx.common
        return CommonData(ops, input_record.locations, input_record.lines, input_record.hints, input_record.icons, input_record.polylines)

    return Context(ctx.profile, ctx.opt, _arrow364(), ctx.res)


def update_lines(ctx: Context, lines: Array[Line]) -> Context:
    def _arrow365(__unit: Literal[None]=None, ctx: Context=ctx, lines: Array[Line]=lines) -> CommonData:
        input_record: CommonData = ctx.common
        return CommonData(input_record.operators, input_record.locations, lines, input_record.hints, input_record.icons, input_record.polylines)

    return Context(ctx.profile, ctx.opt, _arrow365(), ctx.res)


def parse_common(ctx: Context, c: RawCommon) -> CommonData:
    def mapping(op: RawOp, ctx: Context=ctx, c: RawCommon=c) -> Operator:
        return Profile__get_parseOperator(ctx.profile)(ctx)(op)

    ctx1: Context = update_operators(ctx, map(mapping, default_arg(c.op_l, []), None))
    def mapping_1(p: RawProd, ctx: Context=ctx, c: RawCommon=c) -> Line:
        return Profile__get_parseLine(ctx1.profile)(ctx1)(p)

    ctx2: Context = update_lines(ctx, map(mapping_1, default_arg(c.prod_l, []), None))
    def mapping_2(p_1: RawRem, ctx: Context=ctx, c: RawCommon=c) -> Optional[Any]:
        return Profile__get_parseHint(ctx2.profile)(ctx2)(p_1)

    hints: Array[Optional[Any]] = map(mapping_2, default_arg(c.rem_l, []), None)
    def chooser(x: Optional[Icon]=None, ctx: Context=ctx, c: RawCommon=c) -> Optional[Icon]:
        return x

    def mapping_3(i: RawIco, ctx: Context=ctx, c: RawCommon=c) -> Optional[Icon]:
        return Profile__get_parseIcon(ctx2.profile)(ctx2)(i)

    icons: Array[Icon] = choose(chooser, map(mapping_3, default_arg(c.ico_l, []), None), None)
    locations: Array[Any] = Profile__get_parseLocations(ctx2.profile)(ctx2)(default_arg(c.loc_l, []))
    def _arrow366(__unit: Literal[None]=None, ctx: Context=ctx, c: RawCommon=c) -> CommonData:
        input_record: CommonData = ctx2.common
        return CommonData(input_record.operators, locations, input_record.lines, input_record.hints, input_record.icons, input_record.polylines)

    ctx3: Context = Context(ctx2.profile, ctx2.opt, _arrow366(), ctx2.res)
    def mapping_4(p_2: RawPoly, ctx: Context=ctx, c: RawCommon=c) -> FeatureCollection:
        return Profile__get_parsePolyline(ctx2.profile)(ctx3)(p_2)

    return CommonData(ctx2.common.operators, locations, ctx2.common.lines, hints, icons, map(mapping_4, default_arg(c.poly_l, []), None))


def get_element_at(index: int, arr: Array[_A]) -> Optional[_A]:
    if index < len(arr):
        return some(arr[index])

    else: 
        return None



def get_element_at_some(index: Optional[int], arr: Array[_A]) -> Optional[_A]:
    (pattern_matching_result, index_2) = (None, None)
    if index is not None:
        if index < len(arr):
            pattern_matching_result = 0
            index_2 = index

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return some(arr[index_2])

    elif pattern_matching_result == 1:
        return None



def get_array(common: Optional[RawCommon], getter: Callable[[RawCommon], Optional[Array[_A]]]) -> Array[_A]:
    if common is None:
        return [0] * 0

    else: 
        match_value: Optional[Array[_A]] = getter(common)
        if match_value is None:
            return [0] * 0

        else: 
            return match_value




def map_index_array(common: Optional[RawCommon], get_target_array: Callable[[RawCommon], Optional[Array[_A]]], index_arr: Optional[Array[int]]=None) -> Array[_A]:
    elements: Array[_A] = get_array(common, get_target_array)
    if index_arr is None:
        return [0] * 0

    else: 
        def chooser(x: Optional[_A]=None, common: Optional[RawCommon]=common, get_target_array: Callable[[RawCommon], Optional[Array[_A]]]=get_target_array, index_arr: Optional[Array[int]]=index_arr) -> Optional[_A]:
            return x

        def mapping(i: int, common: Optional[RawCommon]=common, get_target_array: Callable[[RawCommon], Optional[Array[_A]]]=get_target_array, index_arr: Optional[Array[int]]=index_arr) -> Optional[_A]:
            return get_element_at(i, elements)

        return choose(chooser, map(mapping, index_arr, None), None)



def append_some_array(arr1: Optional[Array[_A]]=None, arr2: Optional[Array[_A]]=None) -> Optional[Array[_A]]:
    if arr1 is None:
        if arr2 is not None:
            arr2_2: Array[_A] = arr2
            return arr2_2

        else: 
            return None


    elif arr2 is None:
        arr1_2: Array[_A] = arr1
        return arr1_2

    else: 
        arr1_1: Array[_A] = arr1
        arr2_1: Array[_A] = arr2
        return append(arr1_1, arr2_1, None)



def map_array(target_array: Array[_B], get_index: Callable[[_A], Optional[int]], source_array: Optional[Array[_A]]=None) -> Array[_B]:
    if source_array is None:
        return [0] * 0

    else: 
        def chooser(x: Optional[_B]=None, target_array: Array[_B]=target_array, get_index: Callable[[_A], Optional[int]]=get_index, source_array: Optional[Array[_A]]=source_array) -> Optional[_B]:
            return x

        def mapping(elt: Optional[_A]=None, target_array: Array[_B]=target_array, get_index: Callable[[_A], Optional[int]]=get_index, source_array: Optional[Array[_A]]=source_array) -> Optional[_B]:
            return get_element_at_some(get_index(elt), target_array)

        return choose(chooser, map(mapping, source_array, None), None)



def to_option(arr: Array[_A]) -> Optional[Array[_A]]:
    if len(arr) > 0:
        return arr

    else: 
        return None



def msg_lto_remarks(ctx: Context, msg_l: Optional[Array[RawMsg]]=None) -> Optional[Array[Any]]:
    def chooser(x_1: Optional[Any]=None, ctx: Context=ctx, msg_l: Optional[Array[RawMsg]]=msg_l) -> Optional[Any]:
        return x_1

    def get_index(x: RawMsg, ctx: Context=ctx, msg_l: Optional[Array[RawMsg]]=msg_l) -> Optional[int]:
        return x.rem_x

    return to_option(choose(chooser, map_array(ctx.common.hints, get_index, msg_l), None))


__all__ = ["update_operators", "update_lines", "parse_common", "get_element_at", "get_element_at_some", "get_array", "map_index_array", "append_some_array", "map_array", "to_option", "msg_lto_remarks"]

