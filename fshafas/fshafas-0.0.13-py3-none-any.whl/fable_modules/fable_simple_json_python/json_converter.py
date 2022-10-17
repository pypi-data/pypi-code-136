from __future__ import annotations
import base64
import json as json_1
from math import (floor, isnan)
from typing import (Any, List, Literal, Tuple, Optional, Callable)
from ..fable_library.array import (try_find as try_find_1, map as map_2, zip, equals_with, map_indexed, concat, find as find_1)
from ..fable_library.big_int import (parse as parse_3, from_int32)
from ..fable_library.bit_converter import (to_int64, get_bytes_int32)
from ..fable_library.choice import FSharpResult_2
from ..fable_library.date import (parse as parse_4, to_string as to_string_2)
from ..fable_library.date_offset import (parse as parse_5, datetime)
from ..fable_library.decimal import (Decimal, to_string as to_string_1)
from ..fable_library.double import parse
from ..fable_library.guid import parse as parse_6
from ..fable_library.int32 import (parse as parse_1, try_parse)
from ..fable_library.list import (singleton, empty, FSharpList, is_empty, head, tail as tail_1, length, to_array, try_find as try_find_2, of_array, choose, map as map_3)
from ..fable_library.long import (from_number, parse as parse_2, try_parse as try_parse_1, to_number, from_integer)
from ..fable_library.map import (remove, try_find, to_list as to_list_1, contains_key, count, find, of_list as of_list_1, is_empty as is_empty_1, to_array as to_array_2)
from ..fable_library.map_util import (add_to_dict, add_to_set)
from ..fable_library.mutable_map import Dictionary
from ..fable_library.mutable_set import HashSet
from ..fable_library.option import (map as map_1, some, value as value_86)
from ..fable_library.reflection import (TypeInfo, string_type, union_type as union_type_4, name as name_2, make_union, full_name, make_record, get_record_field, get_union_fields)
from ..fable_library.seq import (to_list, delay, append, singleton as singleton_1, empty as empty_1, for_all, try_find as try_find_3, collect, map as map_4, to_array as to_array_1)
from ..fable_library.set import of_list
from ..fable_library.string import (ends_with, substring, to_fail, printf, join, to_text)
from ..fable_library.types import (Array, Union, to_string, FSharpRef, int64, Uint8Array)
from ..fable_library.uri import Uri
from ..fable_library.util import (IEnumerable_1, equals, IComparable, compare, compare_primitives, IStructuralComparable, safe_hash, structural_hash, get_enumerator, ignore, int32_to_string, int64_to_string)
from .json_type import (Json_reflection, Json)
from .simple_json import (SimpleJson_toPlainObject, SimpleJson_toString, SimpleJson_parseNative)
from .type_info_converter import (is_primitive, enum_union)
from .type_info import (TypeInfo as TypeInfo_1, UnionCase, RecordField)

Convert_insideBrowser: bool = False

Convert_isUsingFable3: bool = True

Convert_insideWorker: bool = False

def _expr78() -> TypeInfo:
    return union_type_4("Fable.SimpleJson.Python.Convert.InternalMap", [], Convert_InternalMap, lambda: [[], [("Item1", string_type), ("Item2", Json_reflection())], [("Item1", string_type), ("Item2", Json_reflection()), ("Item3", Convert_InternalMap_reflection()), ("Item4", Convert_InternalMap_reflection())]])


class Convert_InternalMap(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> List[str]:
        return ["MapEmpty", "MapOne", "MapNode"]


Convert_InternalMap_reflection = _expr78

def Convert_flattenMap(_arg: Convert_InternalMap) -> FSharpList[Tuple[str, Json]]:
    if _arg.tag == 1:
        return singleton((_arg.fields[0], _arg.fields[1]))

    elif _arg.tag == 2:
        def _arrow81(__unit: Literal[None]=None, _arg: Convert_InternalMap=_arg) -> IEnumerable_1[Tuple[str, Json]]:
            def _arrow80(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
                def _arrow79(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
                    return singleton_1((_arg.fields[0], _arg.fields[1]))

                return append(Convert_flattenMap(_arg.fields[3]), delay(_arrow79))

            return append(Convert_flattenMap(_arg.fields[2]), delay(_arrow80))

        return to_list(delay(_arrow81))

    else: 
        return empty()



def Convert__007CKeyValue_007C__007C(key: str, map: Any) -> Optional[Tuple[str, Json, Any]]:
    def mapping(value: Json, key: str=key, map: Any=map) -> Tuple[str, Json, Any]:
        return (key, value, remove(key, map))

    return map_1(mapping, try_find(key, map))


def Convert__007CNonArray_007C__007C(_arg: Json) -> Optional[Json]:
    if _arg.tag == 4:
        return None

    else: 
        return _arg



def Convert__007CMapEmpty_007C__007C(json: Json) -> Optional[Json]:
    (pattern_matching_result,) = (None,)
    if json.tag == 1:
        if json.fields[0] == "MapEmpty":
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return json

    elif pattern_matching_result == 1:
        return None



def Convert__007CMapKey_007C__007C(_arg: Json) -> Optional[str]:
    if _arg.tag == 0:
        return to_string(_arg.fields[0])

    elif _arg.tag == 1:
        return _arg.fields[0]

    else: 
        return None



def Convert__007CMapOne_007C__007C(_arg: Json) -> Optional[Tuple[str, Json]]:
    (pattern_matching_result, key, value) = (None, None, None)
    if _arg.tag == 4:
        if not is_empty(_arg.fields[0]):
            if head(_arg.fields[0]).tag == 1:
                if head(_arg.fields[0]).fields[0] == "MapOne":
                    if not is_empty(tail_1(_arg.fields[0])):
                        active_pattern_result: Optional[str] = Convert__007CMapKey_007C__007C(head(tail_1(_arg.fields[0])))
                        if active_pattern_result is not None:
                            if not is_empty(tail_1(tail_1(_arg.fields[0]))):
                                if is_empty(tail_1(tail_1(tail_1(_arg.fields[0])))):
                                    pattern_matching_result = 0
                                    key = active_pattern_result
                                    value = head(tail_1(tail_1(_arg.fields[0])))

                                else: 
                                    pattern_matching_result = 1


                            else: 
                                pattern_matching_result = 1


                        else: 
                            pattern_matching_result = 1


                    else: 
                        pattern_matching_result = 1


                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return (key, value)

    elif pattern_matching_result == 1:
        return None



def Convert__007CMapNode_007C__007C(_arg: Json) -> Optional[Tuple[str, Json, Json, Json]]:
    (pattern_matching_result, key, left, right, value) = (None, None, None, None, None)
    if _arg.tag == 4:
        if not is_empty(_arg.fields[0]):
            if head(_arg.fields[0]).tag == 1:
                if head(_arg.fields[0]).fields[0] == "MapNode":
                    if not is_empty(tail_1(_arg.fields[0])):
                        active_pattern_result: Optional[str] = Convert__007CMapKey_007C__007C(head(tail_1(_arg.fields[0])))
                        if active_pattern_result is not None:
                            if not is_empty(tail_1(tail_1(_arg.fields[0]))):
                                if not is_empty(tail_1(tail_1(tail_1(_arg.fields[0])))):
                                    if not is_empty(tail_1(tail_1(tail_1(tail_1(_arg.fields[0]))))):
                                        if not is_empty(tail_1(tail_1(tail_1(tail_1(tail_1(_arg.fields[0])))))):
                                            if head(tail_1(tail_1(tail_1(tail_1(tail_1(_arg.fields[0])))))).tag == 0:
                                                if is_empty(tail_1(tail_1(tail_1(tail_1(tail_1(tail_1(_arg.fields[0]))))))):
                                                    pattern_matching_result = 0
                                                    key = active_pattern_result
                                                    left = head(tail_1(tail_1(tail_1(_arg.fields[0]))))
                                                    right = head(tail_1(tail_1(tail_1(tail_1(_arg.fields[0])))))
                                                    value = head(tail_1(tail_1(_arg.fields[0])))

                                                else: 
                                                    pattern_matching_result = 1


                                            else: 
                                                pattern_matching_result = 1


                                        else: 
                                            pattern_matching_result = 1


                                    else: 
                                        pattern_matching_result = 1


                                else: 
                                    pattern_matching_result = 1


                            else: 
                                pattern_matching_result = 1


                        else: 
                            pattern_matching_result = 1


                    else: 
                        pattern_matching_result = 1


                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return (key, value, left, right)

    elif pattern_matching_result == 1:
        return None



def Convert_generateMap(json: Json) -> Optional[Convert_InternalMap]:
    if Convert__007CMapEmpty_007C__007C(json) is not None:
        return Convert_InternalMap(0)

    else: 
        active_pattern_result_1: Optional[Tuple[str, Json]] = Convert__007CMapOne_007C__007C(json)
        if active_pattern_result_1 is not None:
            key: str = active_pattern_result_1[0]
            value: Json = active_pattern_result_1[1]
            return Convert_InternalMap(1, key, value)

        else: 
            active_pattern_result_2: Optional[Tuple[str, Json, Json, Json]] = Convert__007CMapNode_007C__007C(json)
            if active_pattern_result_2 is not None:
                key_1: str = active_pattern_result_2[0]
                left: Json = active_pattern_result_2[2]
                right: Json = active_pattern_result_2[3]
                value_1: Json = active_pattern_result_2[1]
                matchValue: Optional[Convert_InternalMap] = Convert_generateMap(left)
                matchValue_1: Optional[Convert_InternalMap] = Convert_generateMap(right)
                (pattern_matching_result, left_map, right_map) = (None, None, None)
                if matchValue is not None:
                    if matchValue_1 is not None:
                        pattern_matching_result = 0
                        left_map = matchValue
                        right_map = matchValue_1

                    else: 
                        pattern_matching_result = 1


                else: 
                    pattern_matching_result = 1

                if pattern_matching_result == 0:
                    return Convert_InternalMap(2, key_1, value_1, left_map, right_map)

                elif pattern_matching_result == 1:
                    return None


            else: 
                return None





def Convert_flatteFable3Map(tree: Any) -> FSharpList[Tuple[str, Json]]:
    def _arrow86(__unit: Literal[None]=None, tree: Any=tree) -> IEnumerable_1[Tuple[str, Json]]:
        def _arrow82(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
            matchValue: Optional[Json] = try_find("k", tree)
            matchValue_1: Optional[Json] = try_find("v", tree)
            (pattern_matching_result, key, value) = (None, None, None)
            if matchValue is not None:
                if matchValue.tag == 1:
                    if matchValue_1 is not None:
                        pattern_matching_result = 0
                        key = matchValue.fields[0]
                        value = matchValue_1

                    else: 
                        pattern_matching_result = 1


                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                return singleton_1((key, value))

            elif pattern_matching_result == 1:
                return empty_1()


        def _arrow85(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
            def _arrow83(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
                match_value_1: Optional[Json] = try_find("left", tree)
                (pattern_matching_result_1, left) = (None, None)
                if match_value_1 is not None:
                    if match_value_1.tag == 5:
                        pattern_matching_result_1 = 0
                        left = match_value_1.fields[0]

                    else: 
                        pattern_matching_result_1 = 1


                else: 
                    pattern_matching_result_1 = 1

                if pattern_matching_result_1 == 0:
                    return Convert_flatteFable3Map(left)

                elif pattern_matching_result_1 == 1:
                    return empty_1()


            def _arrow84(__unit: Literal[None]=None) -> IEnumerable_1[Tuple[str, Json]]:
                match_value_2: Optional[Json] = try_find("right", tree)
                (pattern_matching_result_2, right) = (None, None)
                if match_value_2 is not None:
                    if match_value_2.tag == 5:
                        pattern_matching_result_2 = 0
                        right = match_value_2.fields[0]

                    else: 
                        pattern_matching_result_2 = 1


                else: 
                    pattern_matching_result_2 = 1

                if pattern_matching_result_2 == 0:
                    return Convert_flatteFable3Map(right)

                elif pattern_matching_result_2 == 1:
                    return empty_1()


            return append(_arrow83(), delay(_arrow84))

        return append(_arrow82(), delay(_arrow85))

    return to_list(delay(_arrow86))


def Convert_flattenFable3Lists(linked_list: Any) -> FSharpList[Json]:
    def _arrow89(__unit: Literal[None]=None, linked_list: Any=linked_list) -> IEnumerable_1[Json]:
        def _arrow87(__unit: Literal[None]=None) -> IEnumerable_1[Json]:
            match_value: Optional[Json] = try_find("head", linked_list)
            if match_value is None:
                return empty_1()

            else: 
                return singleton_1(match_value)


        def _arrow88(__unit: Literal[None]=None) -> IEnumerable_1[Json]:
            match_value_1: Optional[Json] = try_find("tail", linked_list)
            (pattern_matching_result, tail) = (None, None)
            if match_value_1 is not None:
                if match_value_1.tag == 5:
                    pattern_matching_result = 0
                    tail = match_value_1.fields[0]

                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                return Convert_flattenFable3Lists(tail)

            elif pattern_matching_result == 1:
                return empty_1()


        return append(_arrow87(), delay(_arrow88))

    return to_list(delay(_arrow89))


def Convert_arrayLike(_arg: TypeInfo_1) -> bool:
    if _arg.tag == 28:
        return True

    elif _arg.tag == 26:
        return True

    elif _arg.tag == 29:
        return True

    elif _arg.tag == 30:
        return True

    elif _arg.tag == 27:
        return True

    elif _arg.tag == 33:
        return True

    elif _arg.tag == 34:
        return True

    else: 
        return False



def Convert_isRecord(_arg: TypeInfo_1) -> bool:
    if _arg.tag == 37:
        return True

    else: 
        return False



def Convert_unionOfRecords(_arg: TypeInfo_1) -> bool:
    if _arg.tag == 38:
        def predicate(case: UnionCase, _arg: TypeInfo_1=_arg) -> bool:
            if len(case.CaseTypes) == 1:
                return Convert_isRecord(case.CaseTypes[0])

            else: 
                return False


        return for_all(predicate, _arg.fields[0]()[0])

    else: 
        return False



def Convert_optional(_arg: TypeInfo_1) -> bool:
    if _arg.tag == 25:
        return True

    else: 
        return False



def Convert_isQuoted(input: str) -> bool:
    if input.find("\"") == 0:
        return ends_with(input, "\"")

    else: 
        return False



def Convert_betweenQuotes(input: str) -> str:
    return ("\"" + input) + "\""


def Convert_removeQuotes(input: str) -> str:
    return substring(input, 1, len(input) - 2)


def Convert_fromJsonAs(input_mut: Json, type_info_mut: TypeInfo_1) -> Any:
    while True:
        (input, type_info) = (input_mut, type_info_mut)
        (pattern_matching_result, value_2, value_4, value_5, value_7, value_8, value_9, value_10, value_11, value_12, value_13, value_14, value_15, value_16, value_17, value_18, value_19, value_20, value_21, value_22, value_23, value_24, value_25, getl_elem_type, value_26, get_elem_type, value_27, get_elem_type_1, value_28, generic_json, value_29, value_30, value_31, value_32, value_33, value_34, value_35, value_36, value_37, value_38, get_types_1, values, json_value_5, optional_type_delayed_5, value_45, value_46, dict_1, case_name_4, get_types_2, case_name_5, get_types_3, get_fields, serialized_record, case_value, get_types_4, element_type_delayed, values_4, element_type_delayed_1, values_5, element_type_delayed_2, linked_list, element_type_delayed_3, values_6, element_type_delayed_4, values_7, array_12, tuple_types_delayed, dict_2, get_types_5, get_types_6, tuples, get_types_7, tuples_1, dict_3, get_types_8, get_type, items, get_types_9, map, get_type_1) = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        if input.tag == 1:
            if type_info.tag == 9:
                if input.fields[0].lower() == "nan":
                    pattern_matching_result = 1

                else: 
                    pattern_matching_result = 2
                    value_4 = input.fields[0]


            elif type_info.tag == 8:
                if input.fields[0].lower() == "nan":
                    pattern_matching_result = 4

                else: 
                    pattern_matching_result = 5
                    value_7 = input.fields[0]


            elif type_info.tag == 6:
                pattern_matching_result = 8
                value_10 = input.fields[0]

            elif type_info.tag == 1:
                pattern_matching_result = 9
                value_11 = input.fields[0]

            elif type_info.tag == 2:
                pattern_matching_result = 11
                value_13 = input.fields[0]

            elif type_info.tag == 10:
                pattern_matching_result = 13
                value_15 = input.fields[0]

            elif type_info.tag == 21:
                pattern_matching_result = 15
                value_17 = input.fields[0]

            elif type_info.tag == 11:
                pattern_matching_result = 16
                value_18 = input.fields[0]

            elif type_info.tag == 3:
                pattern_matching_result = 19
                value_21 = input.fields[0]

            elif type_info.tag == 4:
                pattern_matching_result = 20
                value_22 = input.fields[0]

            elif type_info.tag == 5:
                pattern_matching_result = 22
                value_24 = input.fields[0]

            elif type_info.tag == 36:
                pattern_matching_result = 24
                getl_elem_type = type_info.fields[0]
                value_26 = input.fields[0]

            elif type_info.tag == 28:
                pattern_matching_result = 26
                get_elem_type_1 = type_info.fields[0]
                value_28 = input.fields[0]

            elif type_info.tag == 20:
                pattern_matching_result = 29
                generic_json = input

            elif type_info.tag == 12:
                pattern_matching_result = 30
                value_29 = input.fields[0]

            elif type_info.tag == 13:
                pattern_matching_result = 31
                value_30 = input.fields[0]

            elif type_info.tag == 14:
                pattern_matching_result = 34
                value_33 = input.fields[0]

            elif type_info.tag == 17:
                pattern_matching_result = 35
                value_34 = input.fields[0]

            elif type_info.tag == 15:
                pattern_matching_result = 37
                value_36 = input.fields[0]

            elif type_info.tag == 16:
                pattern_matching_result = 38
                value_37 = input.fields[0]

            elif type_info.tag == 25:
                if not equals(input, Json(3)):
                    pattern_matching_result = 42
                    json_value_5 = input
                    optional_type_delayed_5 = type_info.fields[0]

                else: 
                    pattern_matching_result = 63


            elif type_info.tag == 19:
                pattern_matching_result = 43
                value_45 = input.fields[0]

            elif type_info.tag == 38:
                if Convert_isQuoted(input.fields[0]):
                    pattern_matching_result = 46
                    case_name_4 = input.fields[0]
                    get_types_2 = type_info.fields[0]

                else: 
                    pattern_matching_result = 47
                    case_name_5 = input.fields[0]
                    get_types_3 = type_info.fields[0]


            elif type_info.tag == 37:
                pattern_matching_result = 48
                get_fields = type_info.fields[0]
                serialized_record = input.fields[0]

            elif type_info.tag == 22:
                pattern_matching_result = 62
                get_type_1 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif input.tag == 2:
            if type_info.tag == 7:
                pattern_matching_result = 7
                value_9 = input.fields[0]

            elif type_info.tag == 20:
                pattern_matching_result = 29
                generic_json = input

            elif type_info.tag == 25:
                if not equals(input, Json(3)):
                    pattern_matching_result = 42
                    json_value_5 = input
                    optional_type_delayed_5 = type_info.fields[0]

                else: 
                    pattern_matching_result = 63


            elif type_info.tag == 22:
                pattern_matching_result = 62
                get_type_1 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif input.tag == 3:
            if type_info.tag == 2:
                pattern_matching_result = 27

            elif type_info.tag == 0:
                pattern_matching_result = 28

            elif type_info.tag == 20:
                pattern_matching_result = 29
                generic_json = input

            elif type_info.tag == 25:
                pattern_matching_result = 41

            elif type_info.tag == 22:
                pattern_matching_result = 62
                get_type_1 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif input.tag == 5:
            if type_info.tag == 20:
                pattern_matching_result = 29
                generic_json = input

            elif type_info.tag == 38:
                pattern_matching_result = 40
                get_types_1 = type_info.fields[0]
                values = input.fields[0]

            elif type_info.tag == 25:
                if not equals(input, Json(3)):
                    pattern_matching_result = 42
                    json_value_5 = input
                    optional_type_delayed_5 = type_info.fields[0]

                else: 
                    pattern_matching_result = 63


            elif type_info.tag == 12:
                pattern_matching_result = 45
                dict_1 = input.fields[0]

            elif type_info.tag == 26:
                pattern_matching_result = 52
                element_type_delayed_2 = type_info.fields[0]
                linked_list = input.fields[0]

            elif type_info.tag == 37:
                pattern_matching_result = 56
                dict_2 = input.fields[0]
                get_types_5 = type_info.fields[0]

            elif type_info.tag == 32:
                pattern_matching_result = 59
                dict_3 = input.fields[0]
                get_types_8 = type_info.fields[0]

            elif type_info.tag == 31:
                pattern_matching_result = 61
                get_types_9 = type_info.fields[0]
                map = input.fields[0]

            elif type_info.tag == 22:
                pattern_matching_result = 62
                get_type_1 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif input.tag == 4:
            if type_info.tag == 20:
                pattern_matching_result = 29
                generic_json = input

            elif type_info.tag == 25:
                if not equals(input, Json(3)):
                    pattern_matching_result = 42
                    json_value_5 = input
                    optional_type_delayed_5 = type_info.fields[0]

                else: 
                    pattern_matching_result = 63


            elif type_info.tag == 38:
                pattern_matching_result = 49
                case_value = input.fields[0]
                get_types_4 = type_info.fields[0]

            elif type_info.tag == 28:
                pattern_matching_result = 50
                element_type_delayed = type_info.fields[0]
                values_4 = input.fields[0]

            elif type_info.tag == 26:
                pattern_matching_result = 51
                element_type_delayed_1 = type_info.fields[0]
                values_5 = input.fields[0]

            elif type_info.tag == 27:
                pattern_matching_result = 53
                element_type_delayed_3 = type_info.fields[0]
                values_6 = input.fields[0]

            elif type_info.tag == 29:
                pattern_matching_result = 54
                element_type_delayed_4 = type_info.fields[0]
                values_7 = input.fields[0]

            elif type_info.tag == 30:
                pattern_matching_result = 55
                array_12 = input.fields[0]
                tuple_types_delayed = type_info.fields[0]

            elif type_info.tag == 31:
                pattern_matching_result = 57
                get_types_6 = type_info.fields[0]
                tuples = input.fields[0]

            elif type_info.tag == 32:
                pattern_matching_result = 58
                get_types_7 = type_info.fields[0]
                tuples_1 = input.fields[0]

            elif type_info.tag == 34:
                pattern_matching_result = 60
                get_type = type_info.fields[0]
                items = input.fields[0]

            elif type_info.tag == 22:
                pattern_matching_result = 62
                get_type_1 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif type_info.tag == 9:
            pattern_matching_result = 0
            value_2 = input.fields[0]

        elif type_info.tag == 8:
            pattern_matching_result = 3
            value_5 = input.fields[0]

        elif type_info.tag == 6:
            pattern_matching_result = 6
            value_8 = input.fields[0]

        elif type_info.tag == 1:
            pattern_matching_result = 10
            value_12 = input.fields[0]

        elif type_info.tag == 2:
            pattern_matching_result = 12
            value_14 = input.fields[0]

        elif type_info.tag == 10:
            pattern_matching_result = 14
            value_16 = input.fields[0]

        elif type_info.tag == 11:
            pattern_matching_result = 17
            value_19 = input.fields[0]

        elif type_info.tag == 3:
            pattern_matching_result = 18
            value_20 = input.fields[0]

        elif type_info.tag == 5:
            pattern_matching_result = 21
            value_23 = input.fields[0]

        elif type_info.tag == 18:
            pattern_matching_result = 23
            value_25 = input.fields[0]

        elif type_info.tag == 36:
            pattern_matching_result = 25
            get_elem_type = type_info.fields[0]
            value_27 = input.fields[0]

        elif type_info.tag == 20:
            pattern_matching_result = 29
            generic_json = input

        elif type_info.tag == 13:
            pattern_matching_result = 32
            value_31 = input.fields[0]

        elif type_info.tag == 14:
            pattern_matching_result = 33
            value_32 = input.fields[0]

        elif type_info.tag == 17:
            pattern_matching_result = 36
            value_35 = input.fields[0]

        elif type_info.tag == 16:
            pattern_matching_result = 39
            value_38 = input.fields[0]

        elif type_info.tag == 25:
            if not equals(input, Json(3)):
                pattern_matching_result = 42
                json_value_5 = input
                optional_type_delayed_5 = type_info.fields[0]

            else: 
                pattern_matching_result = 63


        elif type_info.tag == 12:
            pattern_matching_result = 44
            value_46 = input.fields[0]

        elif type_info.tag == 22:
            pattern_matching_result = 62
            get_type_1 = type_info.fields[0]

        else: 
            pattern_matching_result = 63

        if pattern_matching_result == 0:
            return value_2

        elif pattern_matching_result == 1:
            return float('nan')

        elif pattern_matching_result == 2:
            return parse(value_4)

        elif pattern_matching_result == 3:
            return value_5

        elif pattern_matching_result == 4:
            return float('nan')

        elif pattern_matching_result == 5:
            return parse(value_7)

        elif pattern_matching_result == 6:
            return floor(value_8)

        elif pattern_matching_result == 7:
            return value_9

        elif pattern_matching_result == 8:
            return parse_1(value_10, 511, False, 32)

        elif pattern_matching_result == 9:
            return value_11

        elif pattern_matching_result == 10:
            return chr(value_12)

        elif pattern_matching_result == 11:
            return value_13

        elif pattern_matching_result == 12:
            return to_string(value_14)

        elif pattern_matching_result == 13:
            return Decimal(value_15)

        elif pattern_matching_result == 14:
            return Decimal(value_16)

        elif pattern_matching_result == 15:
            return Uri(value_17)

        elif pattern_matching_result == 16:
            return parse_1(value_18, 511, False, 16)

        elif pattern_matching_result == 17:
            return (int(value_19) + 0x8000 & 0xFFFF) - 0x8000

        elif pattern_matching_result == 18:
            return int(value_20+0x10000 if value_20 < 0 else value_20) & 0xFFFF

        elif pattern_matching_result == 19:
            return parse_1(value_21, 511, True, 16)

        elif pattern_matching_result == 20:
            return parse_1(value_22, 511, True, 32)

        elif pattern_matching_result == 21:
            return from_number(value_23, True)

        elif pattern_matching_result == 22:
            return parse_2(value_24, 511, True, 64)

        elif pattern_matching_result == 23:
            return floor(value_25)

        elif pattern_matching_result == 24:
            pattern_input: Tuple[TypeInfo_1, Any] = getl_elem_type()
            underlying_type: TypeInfo_1 = pattern_input[0]
            original_type: Any = pattern_input[1]
            if underlying_type.tag == 6:
                match_value_1: Tuple[bool, int]
                out_arg: int = 0
                def _arrow90(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> int:
                    return out_arg

                def _arrow91(v: int, input: Json=input, type_info: TypeInfo_1=type_info) -> None:
                    nonlocal out_arg
                    out_arg = v or 0

                match_value_1 = (try_parse(value_26, 511, False, 32, FSharpRef(_arrow90, _arrow91)), out_arg)
                if match_value_1[0]:
                    return match_value_1[1]

                else: 
                    arg_1: str = name_2(original_type)
                    return to_fail(printf("The value \'%s\' is not valid for enum of type \'%s\'"))(value_26)(arg_1)


            elif underlying_type.tag == 12:
                match_value_2: Tuple[bool, int64]
                out_arg_1: int64 = int64(0)
                def _arrow92(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> int64:
                    return out_arg_1

                def _arrow93(v_1: int64, input: Json=input, type_info: TypeInfo_1=type_info) -> None:
                    nonlocal out_arg_1
                    out_arg_1 = v_1

                match_value_2 = (try_parse_1(value_26, 511, False, 64, FSharpRef(_arrow92, _arrow93)), out_arg_1)
                if match_value_2[0]:
                    return match_value_2[1]

                else: 
                    arg_3: str = name_2(original_type)
                    return to_fail(printf("The value \'%s\' is not valid for enum of type \'%s\'"))(value_26)(arg_3)


            else: 
                arg_5: str = name_2(original_type)
                return to_fail(printf("The value \'%s\' cannot be converted to enum of type \'%s\'"))(value_26)(arg_5)


        elif pattern_matching_result == 25:
            pattern_input_1: Tuple[TypeInfo_1, Any] = get_elem_type()
            return value_27

        elif pattern_matching_result == 26:
            elem_type: TypeInfo_1 = get_elem_type_1()
            if elem_type.tag == 13:
                return base64.b64decode(value_28)

            else: 
                return to_fail(printf("Cannot convert arbitrary string \'%s\' to %A"))(value_28)(elem_type)


        elif pattern_matching_result == 27:
            return None

        elif pattern_matching_result == 28:
            return None

        elif pattern_matching_result == 29:
            return SimpleJson_toPlainObject(generic_json)

        elif pattern_matching_result == 30:
            return parse_2(value_29, 511, False, 64)

        elif pattern_matching_result == 31:
            return parse_1(value_30, 511, True, 8)

        elif pattern_matching_result == 32:
            return int(value_31+0x100 if value_31 < 0 else value_31) & 0xFF

        elif pattern_matching_result == 33:
            return (int(value_32) + 0x80 & 0xFF) - 0x80

        elif pattern_matching_result == 34:
            return parse_1(value_33, 511, False, 8)

        elif pattern_matching_result == 35:
            return parse_3(value_34)

        elif pattern_matching_result == 36:
            return from_int32(floor(value_35))

        elif pattern_matching_result == 37:
            return parse_4(value_36)

        elif pattern_matching_result == 38:
            return parse_5(value_37)

        elif pattern_matching_result == 39:
            return datetime.fromtimestamp(to_number(from_number(floor(value_38), False)) * 1000, 0)

        elif pattern_matching_result == 40:
            pattern_input_2: Tuple[Array[UnionCase], Any] = get_types_1()
            union_type: Any = pattern_input_2[1]
            cases: Array[UnionCase] = pattern_input_2[0]
            match_value_3: FSharpList[Tuple[str, Json]] = to_list_1(values)
            (pattern_matching_result_1, case_name_1, values_1, case_name_2, json) = (None, None, None, None, None)
            if not is_empty(match_value_3):
                if head(match_value_3)[1].tag == 4:
                    if is_empty(tail_1(match_value_3)):
                        pattern_matching_result_1 = 0
                        case_name_1 = head(match_value_3)[0]
                        values_1 = head(match_value_3)[1].fields[0]

                    else: 
                        pattern_matching_result_1 = 2


                else: 
                    active_pattern_result: Optional[Json] = Convert__007CNonArray_007C__007C(head(match_value_3)[1])
                    if active_pattern_result is not None:
                        if is_empty(tail_1(match_value_3)):
                            pattern_matching_result_1 = 1
                            case_name_2 = head(match_value_3)[0]
                            json = active_pattern_result

                        else: 
                            pattern_matching_result_1 = 2


                    else: 
                        pattern_matching_result_1 = 2



            else: 
                pattern_matching_result_1 = 2

            if pattern_matching_result_1 == 0:
                def predicate(case: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                    return case.CaseName == case_name_1

                _arg: Optional[UnionCase] = try_find_1(predicate, cases)
                if _arg is not None:
                    def _arrow94(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                        found_case: UnionCase = _arg
                        return Convert_arrayLike(found_case.CaseTypes[0]) if (len(found_case.CaseTypes) == 1) else False

                    if _arrow94():
                        found_case_2: UnionCase = _arg
                        return make_union(found_case_2.Info, [Convert_fromJsonAs(Json(4, values_1), found_case_2.CaseTypes[0])])

                    else: 
                        def _arrow95(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                            found_case_1: UnionCase = _arg
                            return Convert_optional(found_case_1.CaseTypes[0]) if (len(found_case_1.CaseTypes) == 1) else False

                        if _arrow95():
                            found_case_3: UnionCase = _arg
                            return make_union(found_case_3.Info, [Convert_fromJsonAs(Json(4, values_1), found_case_3.CaseTypes[0])])

                        else: 
                            found_case_4: UnionCase = _arg
                            if (len(found_case_4.CaseTypes) != length(values_1)) if ((not Convert_arrayLike(found_case_4.CaseTypes[0])) if (len(found_case_4.CaseTypes) == 1) else False) else False:
                                arg_14: int = length(values_1) or 0
                                arg_13: int = len(found_case_4.CaseTypes) or 0
                                to_fail(printf("Expected case \'%s\' to have %d argument types but the JSON data only contained %d values"))(found_case_4.CaseName)(arg_13)(arg_14)

                            def mapping(tupled_arg: Tuple[TypeInfo_1, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                                return Convert_fromJsonAs(tupled_arg[1], tupled_arg[0])

                            return make_union(found_case_4.Info, map_2(mapping, zip(found_case_4.CaseTypes, to_array(values_1)), None))



                else: 
                    def _arrow96(case_1: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                        return to_text(printf(" \'%s\' "))(case_1.CaseName)

                    expected_cases: str = join(", ", map_2(_arrow96, cases, None))
                    arg_10: str = name_2(union_type)
                    return to_fail(printf("Case %s was not valid for type \'%s\', expected one of the cases [%s]"))(case_name_1)(arg_10)(expected_cases)


            elif pattern_matching_result_1 == 1:
                def predicate_1(case_2: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                    return case_2.CaseName == case_name_2

                _arg_1: Optional[UnionCase] = try_find_1(predicate_1, cases)
                (pattern_matching_result_2, case_info, case_name_3, case_type) = (None, None, None, None)
                if _arg_1 is not None:
                    def _arrow99(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                        test_expr: Array[TypeInfo_1] = _arg_1.CaseTypes
                        def _arrow98(x: TypeInfo_1, y: TypeInfo_1) -> bool:
                            return equals(x, y)

                        return (len(test_expr) == 1) if (not equals_with(_arrow98, test_expr, None)) else False

                    if _arrow99():
                        pattern_matching_result_2 = 0
                        case_info = _arg_1.Info
                        case_name_3 = _arg_1.CaseName
                        case_type = _arg_1.CaseTypes[0]

                    else: 
                        pattern_matching_result_2 = 1


                else: 
                    pattern_matching_result_2 = 1

                if pattern_matching_result_2 == 0:
                    return make_union(case_info, [Convert_fromJsonAs(json, case_type)])

                elif pattern_matching_result_2 == 1:
                    def _arrow97(case_3: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                        return to_text(printf(" \'%s\' "))(case_3.CaseName)

                    expected_cases_1: str = join(", ", map_2(_arrow97, cases, None))
                    arg_17: str = name_2(union_type)
                    return to_fail(printf("Case %s was not valid for type \'%s\', expected one of the cases [%s]"))(case_name_2)(arg_17)(expected_cases_1)


            elif pattern_matching_result_1 == 2:
                if (count(values) == 2) if (contains_key("fields", values) if contains_key("tag", values) else False) else False:
                    matchValue: Optional[Json] = try_find("tag", values)
                    matchValue_1: Optional[Json] = try_find("fields", values)
                    (pattern_matching_result_3, case_index, field_values) = (None, None, None)
                    if matchValue is not None:
                        if matchValue.tag == 0:
                            if matchValue_1 is not None:
                                if matchValue_1.tag == 4:
                                    pattern_matching_result_3 = 0
                                    case_index = matchValue.fields[0]
                                    field_values = matchValue_1.fields[0]

                                else: 
                                    pattern_matching_result_3 = 1


                            else: 
                                pattern_matching_result_3 = 1


                        else: 
                            pattern_matching_result_3 = 1


                    else: 
                        pattern_matching_result_3 = 1

                    if pattern_matching_result_3 == 0:
                        found_case_5: UnionCase = cases[int(case_index)]
                        def mapping_1(index: int, value_44: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                            return Convert_fromJsonAs(value_44, found_case_5.CaseTypes[index])

                        return make_union(found_case_5.Info, map_indexed(mapping_1, to_array(field_values), None))

                    elif pattern_matching_result_3 == 1:
                        arg_20: str = full_name(union_type)
                        arg_19: str = SimpleJson_toString(Json(5, values))
                        return to_fail(printf("Could not deserialize JSON(%s) into type %s"))(arg_19)(arg_20)


                elif Convert_unionOfRecords(type_info):
                    def predicate_2(keyword: str, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                        return contains_key(keyword, values)

                    found_discriminator_key: Optional[str] = try_find_2(predicate_2, of_array(["__typename", "$typename", "$type"]))
                    if found_discriminator_key is not None:
                        discriminator_value_json: Json = find(found_discriminator_key, values)
                        if discriminator_value_json.tag == 1:
                            discriminator_value: str = discriminator_value_json.fields[0]
                            def predicate_3(case_4: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                                return case_4.CaseName.upper() == discriminator_value.upper()

                            found_union_case: Optional[UnionCase] = try_find_3(predicate_3, cases)
                            if found_union_case is not None:
                                case_5: UnionCase = found_union_case
                                return make_union(case_5.Info, [Convert_fromJsonAs(Json(5, values), case_5.CaseTypes[0])])

                            else: 
                                arg_22: str = name_2(union_type)
                                return to_fail(printf("Union of records of type \'%s\' does not have a matching case \'%s\'"))(arg_22)(discriminator_value)


                        else: 
                            arg_24: str = name_2(union_type)
                            return to_fail(printf("Union of records of type \'%s\' cannot be deserialized with the value of the discriminator key is not a string to match against a specific union case"))(arg_24)


                    else: 
                        arg_21: str = name_2(union_type)
                        return to_fail(printf("Could not serialize the JSON object into the union of records of type %s because the JSON did not contain a known discriminator. Expected \'__typename\', \'$typeName\' or \'$type\'"))(arg_21)


                else: 
                    unexpected_json: str = json_1.dumps(match_value_3)
                    expected_type: str = json_1.dumps(cases)
                    return to_fail(printf("Expected JSON:\n%s\nto match the type\n%s"))(unexpected_json)(expected_type)



        elif pattern_matching_result == 41:
            return None

        elif pattern_matching_result == 42:
            return some(Convert_fromJsonAs(json_value_5, optional_type_delayed_5()))

        elif pattern_matching_result == 43:
            return parse_6(value_45)

        elif pattern_matching_result == 44:
            return from_integer(int(value_46), False, 2)

        elif pattern_matching_result == 45:
            def get(key: str, input: Json=input, type_info: TypeInfo_1=type_info) -> Optional[Json]:
                return try_find(key, dict_1)

            get: Callable[[str], Optional[Json]] = get
            def chooser(x_1: Optional[Json]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> Optional[Json]:
                return x_1

            _arg_2: FSharpList[Json] = choose(chooser, of_array([get("low"), get("high"), get("unsigned")]))
            (pattern_matching_result_4, high, low) = (None, None, None)
            if not is_empty(_arg_2):
                if head(_arg_2).tag == 0:
                    if not is_empty(tail_1(_arg_2)):
                        if head(tail_1(_arg_2)).tag == 0:
                            if not is_empty(tail_1(tail_1(_arg_2))):
                                if head(tail_1(tail_1(_arg_2))).tag == 2:
                                    if is_empty(tail_1(tail_1(tail_1(_arg_2)))):
                                        pattern_matching_result_4 = 0
                                        high = head(tail_1(_arg_2)).fields[0]
                                        low = head(_arg_2).fields[0]

                                    else: 
                                        pattern_matching_result_4 = 1


                                else: 
                                    pattern_matching_result_4 = 1


                            else: 
                                pattern_matching_result_4 = 1


                        else: 
                            pattern_matching_result_4 = 1


                    else: 
                        pattern_matching_result_4 = 1


                else: 
                    pattern_matching_result_4 = 1


            else: 
                pattern_matching_result_4 = 1

            if pattern_matching_result_4 == 0:
                return to_int64(concat([get_bytes_int32(int(low)), get_bytes_int32(int(high))], Uint8Array), 0)

            elif pattern_matching_result_4 == 1:
                return to_fail(printf("Unable to construct int64 from object literal { low: int, high: int, unsigned: bool }"))


        elif pattern_matching_result == 46:
            pattern_input_3: Tuple[Array[UnionCase], Any] = get_types_2()
            case_types: Array[UnionCase] = pattern_input_3[0]
            def predicate_4(case_6: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                return case_6.CaseName == Convert_removeQuotes(case_name_4)

            _arg_3: Optional[UnionCase] = try_find_1(predicate_4, case_types)
            if _arg_3 is None:
                def _arrow100(case_7: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                    return to_text(printf(" \'%s\' "))(case_7.CaseName)

                expected_cases_2: str = join(", ", map_2(_arrow100, case_types, None))
                arg_29: str = name_2(pattern_input_3[1])
                return to_fail(printf("Case %s was not valid for type \'%s\', expected one of the cases [%s]"))(case_name_4)(arg_29)(expected_cases_2)

            else: 
                return make_union(_arg_3.Info, [])


        elif pattern_matching_result == 47:
            pattern_input_4: Tuple[Array[UnionCase], Any] = get_types_3()
            case_types_1: Array[UnionCase] = pattern_input_4[0]
            def predicate_5(case_8: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                return case_8.CaseName == case_name_5

            _arg_4: Optional[UnionCase] = try_find_1(predicate_5, case_types_1)
            if _arg_4 is None:
                def _arrow101(case_9: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                    return to_text(printf(" \'%s\' "))(case_9.CaseName)

                expected_cases_3: str = join(", ", map_2(_arrow101, case_types_1, None))
                arg_33: str = name_2(pattern_input_4[1])
                return to_fail(printf("Case %s was not valid for type \'%s\', expected one of the cases [%s]"))(case_name_5)(arg_33)(expected_cases_3)

            else: 
                return make_union(_arg_4.Info, [])


        elif pattern_matching_result == 48:
            input_mut = SimpleJson_parseNative(serialized_record)
            type_info_mut = type_info
            continue

        elif pattern_matching_result == 49:
            pattern_input_5: Tuple[Array[UnionCase], Any] = get_types_4()
            cases_1: Array[UnionCase] = pattern_input_5[0]
            (pattern_matching_result_5, case_name_6, case_name_8, values_3, otherwise_6) = (None, None, None, None, None)
            if not is_empty(case_value):
                if head(case_value).tag == 1:
                    if is_empty(tail_1(case_value)):
                        pattern_matching_result_5 = 0
                        case_name_6 = head(case_value).fields[0]

                    else: 
                        pattern_matching_result_5 = 1
                        case_name_8 = head(case_value).fields[0]
                        values_3 = tail_1(case_value)


                else: 
                    pattern_matching_result_5 = 2
                    otherwise_6 = case_value


            else: 
                pattern_matching_result_5 = 2
                otherwise_6 = case_value

            if pattern_matching_result_5 == 0:
                def predicate_6(case_10: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                    return case_10.CaseName == case_name_6

                _arg_5: Optional[UnionCase] = try_find_1(predicate_6, cases_1)
                if _arg_5 is None:
                    def _arrow102(case_11: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                        return to_text(printf(" \'%s\' "))(case_11.CaseName)

                    expected_cases_4: str = join(", ", map_2(_arrow102, cases_1, None))
                    arg_37: str = name_2(pattern_input_5[1])
                    return to_fail(printf("Case \'%s\' was not valid for type \'%s\', expected one of the cases [%s]"))(case_name_6)(arg_37)(expected_cases_4)

                else: 
                    case_name_7: str = _arg_5.CaseName
                    case_info_types: Array[TypeInfo_1] = _arg_5.CaseTypes
                    return make_union(_arg_5.Info, [])


            elif pattern_matching_result_5 == 1:
                def predicate_7(case_12: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                    return case_12.CaseName == case_name_8

                _arg_6: Optional[UnionCase] = try_find_1(predicate_7, cases_1)
                if _arg_6 is not None:
                    types: Array[TypeInfo_1] = _arg_6.CaseTypes
                    found_case_name: str = _arg_6.CaseName
                    case_info_4: Any = _arg_6.Info
                    if len(types) != length(values_3):
                        to_fail(printf("The number of union case parameters for \'%s\' is different"))(found_case_name)

                    def mapping_2(tupled_arg_1: Tuple[TypeInfo_1, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                        return Convert_fromJsonAs(tupled_arg_1[1], tupled_arg_1[0])

                    return make_union(case_info_4, map_2(mapping_2, zip(types, to_array(values_3)), None))

                else: 
                    def _arrow103(_arg_7: UnionCase, input: Json=input, type_info: TypeInfo_1=type_info) -> str:
                        return _arg_7.CaseName

                    expected_cases_5: str = join(", ", map_2(_arrow103, cases_1, None))
                    return to_fail(printf("Case %s was not valid, expected one of [%s]"))(case_name_8)(expected_cases_5)


            elif pattern_matching_result_5 == 2:
                unexpected_json_1: str = json_1.dumps(otherwise_6)
                expected_type_1: str = json_1.dumps(cases_1)
                return to_fail(printf("Expected JSON:\n%s\nto match the type\n%s"))(unexpected_json_1)(expected_type_1)


        elif pattern_matching_result == 50:
            element_type: TypeInfo_1 = element_type_delayed()
            def mapping_3(value_50: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                return Convert_fromJsonAs(value_50, element_type)

            return to_array(map_3(mapping_3, values_4))

        elif pattern_matching_result == 51:
            element_type_1: TypeInfo_1 = element_type_delayed_1()
            def mapping_4(value_52: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                return Convert_fromJsonAs(value_52, element_type_1)

            return map_3(mapping_4, values_5)

        elif pattern_matching_result == 52:
            element_type_2: TypeInfo_1 = element_type_delayed_2()
            def mapping_5(value_54: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                return Convert_fromJsonAs(value_54, element_type_2)

            return map_3(mapping_5, Convert_flattenFable3Lists(linked_list))

        elif pattern_matching_result == 53:
            element_type_3: TypeInfo_1 = element_type_delayed_3()
            def mapping_6(value_56: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> IComparable:
                return Convert_fromJsonAs(value_56, element_type_3)

            class ObjectExpr105:
                @property
                def Compare(self) -> Callable[[IComparable, IComparable], int]:
                    def _arrow104(x_2: IComparable, y_1: IComparable) -> int:
                        return compare(x_2, y_1)

                    return _arrow104

            return of_list(map_3(mapping_6, values_6), ObjectExpr105())

        elif pattern_matching_result == 54:
            element_type_4: TypeInfo_1 = element_type_delayed_4()
            def _arrow106(value_58: Json, input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                return Convert_fromJsonAs(value_58, element_type_4)

            return map_3(_arrow106, values_7)

        elif pattern_matching_result == 55:
            def mapping_7(tupled_arg_2: Tuple[TypeInfo_1, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Any:
                return Convert_fromJsonAs(tupled_arg_2[1], tupled_arg_2[0])

            return map_2(mapping_7, zip(tuple_types_delayed(), to_array(array_12)), None)

        elif pattern_matching_result == 56:
            pattern_input_6: Tuple[Array[RecordField], Any] = get_types_5()
            record_type: Any = pattern_input_6[1]
            fields: Array[RecordField] = pattern_input_6[0]
            def _arrow111(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> Array[Any]:
                values_8: FSharpList[Tuple[str, Json]] = to_list_1(dict_2)
                def mapping_10(_arg_8: RecordField) -> Any:
                    field_type: TypeInfo_1 = _arg_8.FieldType
                    field_name: str = _arg_8.FieldName
                    def predicate_8(tupled_arg_3: Tuple[str, Json], _arg_8: RecordField=_arg_8) -> bool:
                        return field_name == tupled_arg_3[0]

                    _arg_9: Optional[Tuple[str, Json]] = try_find_2(predicate_8, values_8)
                    if _arg_9 is None:
                        if field_type.tag == 25:
                            return None

                        else: 
                            dict_keys: str
                            def _arrow110(__unit: Literal[None]=None, _arg_8: RecordField=_arg_8) -> FSharpList[str]:
                                list_11: FSharpList[Tuple[str, Json]] = to_list_1(dict_2)
                                def _arrow109(__unit: Literal[None]=None) -> Callable[[Tuple[str, Json]], str]:
                                    f2: Tuple[str, Json]
                                    clo_44: Callable[[str], str] = to_text(printf("\'%s\'"))
                                    def _arrow107(arg_44: str) -> str:
                                        return clo_44(arg_44)

                                    f2 = _arrow107
                                    def _arrow108(arg_45: Tuple[str, Json]) -> str:
                                        return f2(arg_45[0])

                                    return _arrow108

                                return map_3(_arrow109(), list_11)

                            arg_46: str = join(", ", _arrow110())
                            dict_keys = to_text(printf("[ %s ]"))(arg_46)
                            record_fields: str
                            def mapping_9(_arg_10: RecordField, _arg_8: RecordField=_arg_8) -> str:
                                name_1: str = _arg_10.FieldName
                                if _arg_10.FieldType.tag == 25:
                                    return to_text(printf("optional(\'%s\')"))(name_1)

                                else: 
                                    return to_text(printf("required(\'%s\')"))(name_1)


                            arg_49: str = join(", ", map_2(mapping_9, fields, None))
                            record_fields = to_text(printf("[ %s ]"))(arg_49)
                            arg_52: str = name_2(record_type)
                            return to_fail(printf("Could not find the required key \'%s\' in the JSON object literal with keys %s to match with record type \'%s\' that has fields %s"))(field_name)(dict_keys)(arg_52)(record_fields)


                    else: 
                        key_2: str = _arg_9[0]
                        return Convert_fromJsonAs(_arg_9[1], field_type)


                return map_2(mapping_10, fields, None)

            return make_record(record_type, _arrow111())

        elif pattern_matching_result == 57:
            pattern_input_7: Tuple[TypeInfo_1, TypeInfo_1] = get_types_6()
            key_type: TypeInfo_1 = pattern_input_7[0]
            def _arrow115(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> IEnumerable_1[Any]:
                def _arrow114(key_value_pair: Json) -> IEnumerable_1[Any]:
                    def _arrow113(__unit: Literal[None]=None) -> Callable[[], Array[TypeInfo_1]]:
                        a: Array[TypeInfo_1] = [key_type, pattern_input_7[1]]
                        def _arrow112(__unit: Literal[None]=None) -> Array[TypeInfo_1]:
                            return a

                        return _arrow112

                    return singleton_1(Convert_fromJsonAs(key_value_pair, TypeInfo_1(30, _arrow113())))

                return collect(_arrow114, tuples)

            pairs: FSharpList[Any] = to_list(delay(_arrow115))
            if ((key_type.tag == 6) or (key_type.tag == 2)) or (key_type.tag == 7):
                class ObjectExpr117:
                    @property
                    def Compare(self) -> Callable[[str, str], int]:
                        def _arrow116(x_3: str, y_2: str) -> int:
                            return compare_primitives(x_3, y_2)

                        return _arrow116

                return of_list_1(pairs, ObjectExpr117())

            else: 
                class ObjectExpr119:
                    @property
                    def Compare(self) -> Callable[[IStructuralComparable, IStructuralComparable], int]:
                        def _arrow118(x_4: IStructuralComparable, y_3: IStructuralComparable) -> int:
                            return compare(x_4, y_3)

                        return _arrow118

                return of_list_1(pairs, ObjectExpr119())


        elif pattern_matching_result == 58:
            pattern_input_8: Tuple[TypeInfo_1, TypeInfo_1, Any] = get_types_7()
            key_type_1: TypeInfo_1 = pattern_input_8[0]
            def _arrow122(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> IEnumerable_1[Any]:
                def _arrow121(key_value_pair_1: Json) -> IEnumerable_1[Any]:
                    def _arrow120(__unit: Literal[None]=None) -> Array[TypeInfo_1]:
                        return [key_type_1, pattern_input_8[1]]

                    return singleton_1(Convert_fromJsonAs(key_value_pair_1, TypeInfo_1(30, _arrow120)))

                return collect(_arrow121, tuples_1)

            pairs_1: FSharpList[Any] = to_list(delay(_arrow122))
            class ObjectExpr125:
                @property
                def Equals(self) -> Callable[[FSharpResult_2[Any, Any], FSharpResult_2[Any, Any]], bool]:
                    def _arrow123(x_5: FSharpResult_2[Any, Any], y_4: FSharpResult_2[Any, Any]) -> bool:
                        return equals(x_5, y_4)

                    return _arrow123

                @property
                def GetHashCode(self) -> Callable[[FSharpResult_2[Any, Any]], int]:
                    def _arrow124(x_5: FSharpResult_2[Any, Any]) -> int:
                        return safe_hash(x_5)

                    return _arrow124

            class ObjectExpr128:
                @property
                def Equals(self) -> Callable[[dict[str, Any], dict[str, Any]], bool]:
                    def _arrow126(x_6: dict[str, Any], y_5: dict[str, Any]) -> bool:
                        return equals(x_6, y_5)

                    return _arrow126

                @property
                def GetHashCode(self) -> Callable[[dict[str, Any]], int]:
                    def _arrow127(x_6: dict[str, Any]) -> int:
                        return structural_hash(x_6)

                    return _arrow127

            class ObjectExpr131:
                @property
                def Equals(self) -> Callable[[IStructuralComparable, IStructuralComparable], bool]:
                    def _arrow129(x_7: IStructuralComparable, y_6: IStructuralComparable) -> bool:
                        return equals(x_7, y_6)

                    return _arrow129

                @property
                def GetHashCode(self) -> Callable[[IStructuralComparable], int]:
                    def _arrow130(x_7: IStructuralComparable) -> int:
                        return structural_hash(x_7)

                    return _arrow130

            output: Any = Dictionary([], ObjectExpr125()) if (key_type_1.tag == 38) else (Dictionary([], ObjectExpr128()) if (key_type_1.tag == 37) else Dictionary([], ObjectExpr131()))
            with get_enumerator(pairs_1) as enumerator:
                while enumerator.System_Collections_IEnumerator_MoveNext():
                    for_loop_var: Tuple[IStructuralComparable, Any] = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                    add_to_dict(output, for_loop_var[0], for_loop_var[1])
            return output

        elif pattern_matching_result == 59:
            pattern_input_9: Tuple[TypeInfo_1, TypeInfo_1, Any] = get_types_8()
            key_type_2: TypeInfo_1 = pattern_input_9[0]
            def mapping_11(tupled_arg_4: Tuple[str, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Tuple[Any, Any]:
                return (Convert_fromJsonAs(Json(1, tupled_arg_4[0]), key_type_2), Convert_fromJsonAs(tupled_arg_4[1], pattern_input_9[1]))

            pairs_2: FSharpList[Tuple[Any, Any]] = map_3(mapping_11, to_list_1(dict_3))
            class ObjectExpr134:
                @property
                def Equals(self) -> Callable[[FSharpResult_2[Any, Any], FSharpResult_2[Any, Any]], bool]:
                    def _arrow132(x_8: FSharpResult_2[Any, Any], y_7: FSharpResult_2[Any, Any]) -> bool:
                        return equals(x_8, y_7)

                    return _arrow132

                @property
                def GetHashCode(self) -> Callable[[FSharpResult_2[Any, Any]], int]:
                    def _arrow133(x_8: FSharpResult_2[Any, Any]) -> int:
                        return safe_hash(x_8)

                    return _arrow133

            class ObjectExpr137:
                @property
                def Equals(self) -> Callable[[dict[str, Any], dict[str, Any]], bool]:
                    def _arrow135(x_9: dict[str, Any], y_8: dict[str, Any]) -> bool:
                        return equals(x_9, y_8)

                    return _arrow135

                @property
                def GetHashCode(self) -> Callable[[dict[str, Any]], int]:
                    def _arrow136(x_9: dict[str, Any]) -> int:
                        return structural_hash(x_9)

                    return _arrow136

            class ObjectExpr140:
                @property
                def Equals(self) -> Callable[[IStructuralComparable, IStructuralComparable], bool]:
                    def _arrow138(x_10: IStructuralComparable, y_9: IStructuralComparable) -> bool:
                        return equals(x_10, y_9)

                    return _arrow138

                @property
                def GetHashCode(self) -> Callable[[IStructuralComparable], int]:
                    def _arrow139(x_10: IStructuralComparable) -> int:
                        return structural_hash(x_10)

                    return _arrow139

            output_1: Any = Dictionary([], ObjectExpr134()) if (key_type_2.tag == 38) else (Dictionary([], ObjectExpr137()) if (key_type_2.tag == 37) else Dictionary([], ObjectExpr140()))
            with get_enumerator(pairs_2) as enumerator_1:
                while enumerator_1.System_Collections_IEnumerator_MoveNext():
                    for_loop_var_1: Tuple[Any, Any] = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                    add_to_dict(output_1, for_loop_var_1[0], for_loop_var_1[1])
            return output_1

        elif pattern_matching_result == 60:
            elem_type_1: TypeInfo_1 = get_type()
            class ObjectExpr143:
                @property
                def Equals(self) -> Callable[[FSharpResult_2[Any, Any], FSharpResult_2[Any, Any]], bool]:
                    def _arrow141(x_11: FSharpResult_2[Any, Any], y_10: FSharpResult_2[Any, Any]) -> bool:
                        return equals(x_11, y_10)

                    return _arrow141

                @property
                def GetHashCode(self) -> Callable[[FSharpResult_2[Any, Any]], int]:
                    def _arrow142(x_11: FSharpResult_2[Any, Any]) -> int:
                        return safe_hash(x_11)

                    return _arrow142

            class ObjectExpr146:
                @property
                def Equals(self) -> Callable[[dict[str, Any], dict[str, Any]], bool]:
                    def _arrow144(x_12: dict[str, Any], y_11: dict[str, Any]) -> bool:
                        return equals(x_12, y_11)

                    return _arrow144

                @property
                def GetHashCode(self) -> Callable[[dict[str, Any]], int]:
                    def _arrow145(x_12: dict[str, Any]) -> int:
                        return structural_hash(x_12)

                    return _arrow145

            class ObjectExpr149:
                @property
                def Equals(self) -> Callable[[IStructuralComparable, IStructuralComparable], bool]:
                    def _arrow147(x_13: IStructuralComparable, y_12: IStructuralComparable) -> bool:
                        return equals(x_13, y_12)

                    return _arrow147

                @property
                def GetHashCode(self) -> Callable[[IStructuralComparable], int]:
                    def _arrow148(x_13: IStructuralComparable) -> int:
                        return structural_hash(x_13)

                    return _arrow148

            hashset: Any = HashSet([], ObjectExpr143()) if (elem_type_1.tag == 38) else (HashSet([], ObjectExpr146()) if (elem_type_1.tag == 37) else HashSet([], ObjectExpr149()))
            with get_enumerator(items) as enumerator_2:
                while enumerator_2.System_Collections_IEnumerator_MoveNext():
                    ignore(add_to_set(Convert_fromJsonAs(enumerator_2.System_Collections_Generic_IEnumerator_1_get_Current(), elem_type_1), hashset))
            return hashset

        elif pattern_matching_result == 61:
            pattern_input_10: Tuple[TypeInfo_1, TypeInfo_1] = get_types_9()
            value_type_5: TypeInfo_1 = pattern_input_10[1]
            key_type_3: TypeInfo_1 = pattern_input_10[0]
            matchValue_2: Optional[Json] = try_find("comparer", map)
            matchValue_3: Optional[Json] = try_find("tree", map)
            (pattern_matching_result_6, comparer_2, tree_2, comparer_3, tree_3) = (None, None, None, None, None)
            if matchValue_2 is not None:
                if matchValue_2.tag == 5:
                    if matchValue_3 is not None:
                        if matchValue_3.tag == 4:
                            def _arrow160(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                                tree: FSharpList[Json] = matchValue_3.fields[0]
                                return is_empty_1(matchValue_2.fields[0])

                            if _arrow160():
                                pattern_matching_result_6 = 0
                                comparer_2 = matchValue_2.fields[0]
                                tree_2 = matchValue_3.fields[0]

                            else: 
                                pattern_matching_result_6 = 2


                        elif matchValue_3.tag == 5:
                            def _arrow161(__unit: Literal[None]=None, input: Json=input, type_info: TypeInfo_1=type_info) -> bool:
                                tree_1: Any = matchValue_3.fields[0]
                                return is_empty_1(matchValue_2.fields[0])

                            if _arrow161():
                                pattern_matching_result_6 = 1
                                comparer_3 = matchValue_2.fields[0]
                                tree_3 = matchValue_3.fields[0]

                            else: 
                                pattern_matching_result_6 = 2


                        else: 
                            pattern_matching_result_6 = 2


                    else: 
                        pattern_matching_result_6 = 2


                else: 
                    pattern_matching_result_6 = 2


            else: 
                pattern_matching_result_6 = 2

            if pattern_matching_result_6 == 0:
                match_value_6: Optional[Convert_InternalMap] = Convert_generateMap(Json(4, tree_2))
                if match_value_6 is None:
                    input_json: str = SimpleJson_toString(Json(4, tree_2))
                    return to_fail(printf("Could not generate map from JSON\n %s"))(input_json)

                else: 
                    def mapping_12(tupled_arg_5: Tuple[str, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Tuple[Any, Any]:
                        key_6: str = tupled_arg_5[0]
                        return (Convert_fromJsonAs(Json(1, key_6), key_type_3) if (not Convert_isQuoted(key_6)) else Convert_fromJsonAs(SimpleJson_parseNative(key_6), key_type_3), Convert_fromJsonAs(tupled_arg_5[1], value_type_5))

                    pairs_3: FSharpList[Tuple[Any, Any]] = map_3(mapping_12, Convert_flattenMap(match_value_6))
                    if ((key_type_3.tag == 6) or (key_type_3.tag == 2)) or (key_type_3.tag == 7):
                        class ObjectExpr151:
                            @property
                            def Compare(self) -> Callable[[str, str], int]:
                                def _arrow150(x_14: str, y_13: str) -> int:
                                    return compare_primitives(x_14, y_13)

                                return _arrow150

                        return of_list_1(pairs_3, ObjectExpr151())

                    else: 
                        class ObjectExpr153:
                            @property
                            def Compare(self) -> Callable[[IStructuralComparable, IStructuralComparable], int]:
                                def _arrow152(x_15: IStructuralComparable, y_14: IStructuralComparable) -> int:
                                    return compare(x_15, y_14)

                                return _arrow152

                        return of_list_1(pairs_3, ObjectExpr153())



            elif pattern_matching_result_6 == 1:
                class ObjectExpr155:
                    @property
                    def Compare(self) -> Callable[[str, str], int]:
                        def _arrow154(x_16: str, y_15: str) -> int:
                            return compare_primitives(x_16, y_15)

                        return _arrow154

                input_mut = Json(5, of_list_1(Convert_flatteFable3Map(tree_3), ObjectExpr155()))
                type_info_mut = type_info
                continue

            elif pattern_matching_result_6 == 2:
                def mapping_13(tupled_arg_6: Tuple[str, Json], input: Json=input, type_info: TypeInfo_1=type_info) -> Tuple[str, Any]:
                    key_7: str = tupled_arg_6[0]
                    return ((Convert_fromJsonAs(Json(1, key_7), key_type_3) if (True if is_primitive(key_type_3) else enum_union(key_type_3)) else Convert_fromJsonAs(SimpleJson_parseNative(key_7), key_type_3)) if (not Convert_isQuoted(key_7)) else Convert_fromJsonAs(SimpleJson_parseNative(key_7), key_type_3), Convert_fromJsonAs(tupled_arg_6[1], value_type_5))

                pairs_4: FSharpList[Tuple[str, Any]] = map_3(mapping_13, to_list_1(map))
                if ((key_type_3.tag == 6) or (key_type_3.tag == 2)) or (key_type_3.tag == 7):
                    class ObjectExpr157:
                        @property
                        def Compare(self) -> Callable[[str, str], int]:
                            def _arrow156(x_17: str, y_16: str) -> int:
                                return compare_primitives(x_17, y_16)

                            return _arrow156

                    return of_list_1(pairs_4, ObjectExpr157())

                else: 
                    class ObjectExpr159:
                        @property
                        def Compare(self) -> Callable[[IStructuralComparable, IStructuralComparable], int]:
                            def _arrow158(x_18: IStructuralComparable, y_17: IStructuralComparable) -> int:
                                return compare(x_18, y_17)

                            return _arrow158

                    return of_list_1(pairs_4, ObjectExpr159())



        elif pattern_matching_result == 62:
            arg_56: str = full_name(get_type_1())
            arg_55: str = SimpleJson_toString(input)
            return to_fail(printf("Cannot convert %s to %s"))(arg_55)(arg_56)

        elif pattern_matching_result == 63:
            arg_58: str = to_string(type_info)
            arg_57: str = SimpleJson_toString(input)
            return to_fail(printf("Cannot convert %s to %s"))(arg_57)(arg_58)

        break


def Convert_fromJson(json: Json, type_info: TypeInfo_1) -> Any:
    return Convert_fromJsonAs(json, type_info)


def Convert_quoteText(input_text: str) -> str:
    return Convert_betweenQuotes(input_text)


def Convert_serialize(value_mut: Any, type_info_mut: TypeInfo_1) -> str:
    while True:
        (value, type_info) = (value_mut, type_info_mut)
        if type_info.tag == 2:
            content: str = value
            if content is None:
                return "null"

            else: 
                return Convert_quoteText(content)


        elif type_info.tag == 0:
            return "null"

        elif (type_info.tag == 9) or (type_info.tag == 8):
            if isnan(value):
                return Convert_quoteText("NaN")

            else: 
                return to_string(value)


        elif type_info.tag == 1:
            return Convert_quoteText(value)

        elif (((((((type_info.tag == 13) or (type_info.tag == 14)) or (type_info.tag == 3)) or (type_info.tag == 4)) or (type_info.tag == 11)) or (type_info.tag == 36)) or (type_info.tag == 18)) or (type_info.tag == 6):
            return int32_to_string(value)

        elif (type_info.tag == 5) or (type_info.tag == 12):
            return Convert_betweenQuotes(int64_to_string(value))

        elif type_info.tag == 17:
            return Convert_betweenQuotes(int64_to_string(value))

        elif type_info.tag == 10:
            return Convert_betweenQuotes(to_string_1(value))

        elif type_info.tag == 7:
            if value:
                return "true"

            else: 
                return "false"


        elif type_info.tag == 19:
            def _arrow162(__unit: Literal[None]=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                copy_of_struct: str = value
                return str(copy_of_struct)

            return Convert_betweenQuotes(_arrow162())

        elif type_info.tag == 21:
            return Convert_betweenQuotes(to_string(value))

        elif type_info.tag == 15:
            def _arrow163(__unit: Literal[None]=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                copy_of_struct_1: Any = value
                return to_string_2(copy_of_struct_1, "O")

            return Convert_betweenQuotes(_arrow163())

        elif type_info.tag == 16:
            def _arrow164(__unit: Literal[None]=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                copy_of_struct_2: Any = value
                return to_string_2(copy_of_struct_2, "O")

            return Convert_betweenQuotes(_arrow164())

        elif type_info.tag == 37:
            def mapping(field: RecordField, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                arg_1: str = Convert_serialize(get_record_field(value, field.PropertyInfo), field.FieldType)
                return to_text(printf("\"%s\": %s"))(field.FieldName)(arg_1)

            return ("{" + join(", ", map_2(mapping, type_info.fields[0]()[0], None))) + "}"

        elif type_info.tag == 33:
            element_type: TypeInfo_1 = type_info.fields[0]()
            def mapping_1(element: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element, element_type)

            return ("[" + join(", ", map_4(mapping_1, value))) + "]"

        elif type_info.tag == 34:
            element_type_1: TypeInfo_1 = type_info.fields[0]()
            def mapping_2(element_1: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element_1, element_type_1)

            return ("[" + join(", ", map_4(mapping_2, value))) + "]"

        elif type_info.tag == 27:
            element_type_2: TypeInfo_1 = type_info.fields[0]()
            def mapping_3(element_2: IComparable, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element_2, element_type_2)

            return ("[" + join(", ", map_4(mapping_3, value))) + "]"

        elif type_info.tag == 28:
            element_type_3: TypeInfo_1 = type_info.fields[0]()
            def mapping_4(element_3: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element_3, element_type_3)

            return ("[" + join(", ", map_2(mapping_4, value, None))) + "]"

        elif type_info.tag == 26:
            element_type_4: TypeInfo_1 = type_info.fields[0]()
            def mapping_5(element_4: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element_4, element_type_4)

            return ("[" + join(", ", map_3(mapping_5, value))) + "]"

        elif type_info.tag == 29:
            element_type_5: TypeInfo_1 = type_info.fields[0]()
            def mapping_6(element_5: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                return Convert_serialize(element_5, element_type_5)

            return ("[" + join(", ", map_2(mapping_6, to_array_1(value), None))) + "]"

        elif type_info.tag == 25:
            match_value: Optional[Any] = value
            if match_value is not None:
                value_mut = value_86(match_value)
                type_info_mut = type_info.fields[0]()
                continue

            else: 
                return "null"


        elif type_info.tag == 38:
            pattern_input_1: Tuple[Array[UnionCase], Any] = type_info.fields[0]()
            pattern_input_2: Tuple[Any, Array[Any]] = get_union_fields(value, pattern_input_1[1])
            used_case: Any = pattern_input_2[0]
            fields: Array[Any] = pattern_input_2[1]
            def predicate(case: UnionCase, value: Any=value, type_info: TypeInfo_1=type_info) -> bool:
                return case.CaseName == name_2(used_case)

            case_types: Array[TypeInfo_1] = find_1(predicate, pattern_input_1[0]).CaseTypes
            if True if enum_union(type_info) else (len(case_types) == 0):
                return Convert_betweenQuotes(name_2(used_case))

            elif len(case_types) == 1:
                return ((("{" + Convert_betweenQuotes(name_2(used_case))) + ": ") + Convert_serialize(fields[0], case_types[0])) + "}"

            else: 
                def mapping_7(index: int, case_type: TypeInfo_1, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                    return Convert_serialize(fields[index], case_type)

                serialized_fields_1: str = join(", ", map_indexed(mapping_7, case_types, None))
                return (((("{" + Convert_betweenQuotes(name_2(used_case))) + ": ") + "[") + serialized_fields_1) + "] }"


        elif type_info.tag == 31:
            pattern_input_3: Tuple[TypeInfo_1, TypeInfo_1] = type_info.fields[0]()
            key_type: TypeInfo_1 = pattern_input_3[0]
            def mapping_8(tupled_arg: Tuple[IComparable, Any], value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                serialized_key: str = Convert_serialize(tupled_arg[0], key_type)
                serialized_value: str = Convert_serialize(tupled_arg[1], pattern_input_3[1])
                if True if is_primitive(key_type) else enum_union(key_type):
                    if not Convert_isQuoted(serialized_key):
                        return (Convert_quoteText(serialized_key) + ": ") + serialized_value

                    else: 
                        return (serialized_key + ": ") + serialized_value


                else: 
                    return ((("[" + serialized_key) + ", ") + serialized_value) + "]"


            serialized_values: str = join(", ", map_2(mapping_8, to_array_2(value), None))
            if True if is_primitive(key_type) else enum_union(key_type):
                return ("{" + serialized_values) + "}"

            else: 
                return ("[" + serialized_values) + "]"


        elif type_info.tag == 32:
            pattern_input_4: Tuple[TypeInfo_1, TypeInfo_1, Any] = type_info.fields[0]()
            key_type_1: TypeInfo_1 = pattern_input_4[0]
            def mapping_9(pair: Any, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                pattern_input_5: Tuple[IComparable, Any] = (pair[0], pair[1])
                serialized_key_1: str = Convert_serialize(pattern_input_5[0], key_type_1)
                serialized_value_1: str = Convert_serialize(pattern_input_5[1], pattern_input_4[1])
                if True if is_primitive(key_type_1) else enum_union(key_type_1):
                    if not Convert_isQuoted(serialized_key_1):
                        return (Convert_betweenQuotes(serialized_key_1) + ": ") + serialized_value_1

                    else: 
                        return (serialized_key_1 + ": ") + serialized_value_1


                else: 
                    return ((("[" + serialized_key_1) + ", ") + serialized_value_1) + "]"


            serialized_values_1: str = join(", ", map_4(mapping_9, value))
            if True if is_primitive(key_type_1) else enum_union(key_type_1):
                return ("{" + serialized_values_1) + "}"

            else: 
                return ("[" + serialized_values_1) + "]"


        elif type_info.tag == 30:
            tuple_types: Array[TypeInfo_1] = type_info.fields[0]()
            if len(tuple_types) == 1:
                return ("[" + Convert_serialize(value, tuple_types[0])) + "]"

            else: 
                def mapping_10(index_1: int, element_6: Any=None, value: Any=value, type_info: TypeInfo_1=type_info) -> str:
                    return Convert_serialize(element_6, tuple_types[index_1])

                return ("[" + join(", ", map_indexed(mapping_10, value, None))) + "]"


        elif type_info.tag == 20:
            return json_1.dumps(value)

        elif type_info.tag == 22:
            return json_1.dumps(value)

        else: 
            return "null"

        break


__all__ = ["Convert_insideBrowser", "Convert_isUsingFable3", "Convert_insideWorker", "Convert_InternalMap_reflection", "Convert_flattenMap", "Convert__007CKeyValue_007C__007C", "Convert__007CNonArray_007C__007C", "Convert__007CMapEmpty_007C__007C", "Convert__007CMapKey_007C__007C", "Convert__007CMapOne_007C__007C", "Convert__007CMapNode_007C__007C", "Convert_generateMap", "Convert_flatteFable3Map", "Convert_flattenFable3Lists", "Convert_arrayLike", "Convert_isRecord", "Convert_unionOfRecords", "Convert_optional", "Convert_isQuoted", "Convert_betweenQuotes", "Convert_removeQuotes", "Convert_fromJsonAs", "Convert_fromJson", "Convert_quoteText", "Convert_serialize"]

