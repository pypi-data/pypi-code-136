from __future__ import annotations
import json as json_1
from typing import (Any, Tuple, Optional, Literal, Callable, TypeVar)
from ..fable_library.array import map as map_2
from ..fable_library.list import (map as map_1, of_array, FSharpList, concat, singleton, empty, is_empty, tail, head)
from ..fable_library.map import (to_list, of_list, try_find)
from ..fable_library.option import value as value_5
from ..fable_library.seq import (to_list as to_list_1, delay, map as map_3)
from ..fable_library.string import (to_text, printf, join)
from ..fable_library.types import (to_string, Array)
from ..fable_library.util import (IEnumerable_1, compare_primitives, get_enumerator, partial_apply)
from .json_type import Json
from .type_check import (_007CNativeString_007C__007C, _007CNativeBool_007C__007C, _007CNativeNumber_007C__007C, _007CNull_007C__007C, _007CNativeArray_007C__007C, _007CNativeObject_007C__007C)

_A = TypeVar("_A")

def InteropUtil_isDateOffset(value: Any=None) -> bool:
    if isinstance(value, Date):
        return True

    else: 
        return False



def SimpleJson_toString(_arg: Json) -> str:
    if _arg.tag == 2:
        if _arg.fields[0]:
            return "true"

        else: 
            return "false"


    elif _arg.tag == 0:
        return to_string(_arg.fields[0])

    elif _arg.tag == 1:
        return to_text(printf("\"%s\""))(_arg.fields[0])

    elif _arg.tag == 4:
        def mapping(_arg_1: Json, _arg: Json=_arg) -> str:
            return SimpleJson_toString(_arg_1)

        arg_1: str = join(",", map_1(mapping, _arg.fields[0]))
        return to_text(printf("[%s]"))(arg_1)

    elif _arg.tag == 5:
        def mapping_1(tupled_arg: Tuple[str, Json], _arg: Json=_arg) -> str:
            arg_3: str = SimpleJson_toString(tupled_arg[1])
            return to_text(printf("\"%s\":%s"))(tupled_arg[0])(arg_3)

        arg_4: str = join(",", map_1(mapping_1, to_list(_arg.fields[0])))
        return to_text(printf("{%s}"))(arg_4)

    else: 
        return "null"



def SimpleJson_parseNative_0027(x: Any=None) -> Json:
    active_pattern_result: Optional[str] = _007CNativeString_007C__007C(x)
    if active_pattern_result is not None:
        str_1: str = active_pattern_result
        return Json(1, str_1)

    else: 
        active_pattern_result_1: Optional[bool] = _007CNativeBool_007C__007C(x)
        if active_pattern_result_1 is not None:
            value: bool = active_pattern_result_1
            return Json(2, value)

        else: 
            active_pattern_result_2: Optional[float] = _007CNativeNumber_007C__007C(x)
            if active_pattern_result_2 is not None:
                number: float = active_pattern_result_2
                return Json(0, number)

            elif _007CNull_007C__007C(x) is not None:
                return Json(3)

            else: 
                active_pattern_result_4: Optional[Array[Any]] = _007CNativeArray_007C__007C(x)
                if active_pattern_result_4 is not None:
                    arr: Array[Any] = active_pattern_result_4
                    def _arrow4(x_1: Any=None, x: Any=x) -> Json:
                        return SimpleJson_parseNative_0027(x_1)

                    return Json(4, of_array(map_2(_arrow4, arr, None)))

                else: 
                    active_pattern_result_5: Optional[Any] = _007CNativeObject_007C__007C(x)
                    if active_pattern_result_5 is not None:
                        object: Any = value_5(active_pattern_result_5)
                        def _arrow8(__unit: Literal[None]=None, x: Any=x) -> IEnumerable_1[Tuple[str, Json]]:
                            def _arrow7(key: str) -> Tuple[str, Json]:
                                return (key, SimpleJson_parseNative_0027(object[key]))

                            return map_3(_arrow7, object.keys())

                        class ObjectExpr17:
                            @property
                            def Compare(self) -> Callable[[str, str], int]:
                                def _arrow12(x_2: str, y: str) -> int:
                                    return compare_primitives(x_2, y)

                                return _arrow12

                        return Json(5, of_list(to_list_1(delay(_arrow8)), ObjectExpr17()))

                    else: 
                        return Json(3)







def SimpleJson_parseNative(input: str) -> Json:
    return SimpleJson_parseNative_0027(json_1.loads(input))


def SimpleJson_tryParseNative(input: str) -> Optional[Json]:
    try: 
        return SimpleJson_parseNative(input)

    except Exception as ex:
        return None



def SimpleJson_fromObjectLiteral(x: Optional[Any]=None) -> Optional[Json]:
    try: 
        return SimpleJson_parseNative_0027(x)

    except Exception as match_value:
        return None



def SimpleJson_mapKeys(f: Callable[[str], str], _arg: Json) -> Json:
    if _arg.tag == 5:
        def mapping(tupled_arg: Tuple[str, Json], f: Callable[[str], str]=f, _arg: Json=_arg) -> Tuple[str, Json]:
            return (f(tupled_arg[0]), SimpleJson_mapKeys(f, tupled_arg[1]))

        class ObjectExpr51:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                def _arrow50(x: str, y: str) -> int:
                    return compare_primitives(x, y)

                return _arrow50

        return Json(5, of_list(map_1(mapping, to_list(_arg.fields[0])), ObjectExpr51()))

    elif _arg.tag == 4:
        def mapping_1(_arg_1: Json, f: Callable[[str], str]=f, _arg: Json=_arg) -> Json:
            return SimpleJson_mapKeys(f, _arg_1)

        return Json(4, map_1(mapping_1, _arg.fields[0]))

    else: 
        return _arg



def SimpleJson_toPlainObject(input: Json) -> Any:
    if input.tag == 2:
        return input.fields[0]

    elif input.tag == 0:
        return input.fields[0]

    elif input.tag == 1:
        return input.fields[0]

    elif input.tag == 4:
        array: Array[Any] = []
        with get_enumerator(input.fields[0]) as enumerator:
            while enumerator.System_Collections_IEnumerator_MoveNext():
                value_3: Json = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                (array.append(SimpleJson_toPlainObject(value_3)))
        return array

    elif input.tag == 5:
        js_object: Any = {}
        with get_enumerator(to_list(input.fields[0])) as enumerator_1:
            while enumerator_1.System_Collections_IEnumerator_MoveNext():
                for_loop_var: Tuple[str, Json] = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                js_object[for_loop_var[0]] = SimpleJson_toPlainObject(for_loop_var[1])
        return js_object

    else: 
        return None



def SimpleJson_mapbyKey(f: Callable[[str, Json], Json], _arg: Json) -> Json:
    if _arg.tag == 5:
        def mapping(tupled_arg: Tuple[str, Json], f: Callable[[str, Json], Json]=f, _arg: Json=_arg) -> Tuple[str, Json]:
            key: str = tupled_arg[0]
            return (key, f(key, tupled_arg[1]))

        class ObjectExpr71:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                def _arrow70(x: str, y: str) -> int:
                    return compare_primitives(x, y)

                return _arrow70

        return Json(5, of_list(map_1(mapping, to_list(_arg.fields[0])), ObjectExpr71()))

    elif _arg.tag == 4:
        def mapping_1(_arg_1: Json, f: Callable[[str, Json], Json]=f, _arg: Json=_arg) -> Json:
            return SimpleJson_mapbyKey(f, _arg_1)

        return Json(4, map_1(mapping_1, _arg.fields[0]))

    else: 
        return _arg



def SimpleJson_mapKeysByPath(f: Callable[[FSharpList[str]], Optional[str]], json: Json) -> Json:
    def map_key(xs: FSharpList[str], _arg: Json, f: Callable[[FSharpList[str]], Optional[str]]=f, json: Json=json) -> Json:
        if _arg.tag == 5:
            def mapping(tupled_arg: Tuple[str, Json], xs: FSharpList[str]=xs, _arg: Json=_arg) -> Tuple[str, Json]:
                key: str = tupled_arg[0]
                value: Json = tupled_arg[1]
                key_path: FSharpList[str] = concat([xs, singleton(key)])
                match_value: Optional[str] = f(key_path)
                if match_value is None:
                    return (key, map_key(key_path, value))

                else: 
                    return (match_value, map_key(key_path, value))


            class ObjectExpr73:
                @property
                def Compare(self) -> Callable[[str, str], int]:
                    def _arrow72(x: str, y: str) -> int:
                        return compare_primitives(x, y)

                    return _arrow72

            return Json(5, of_list(map_1(mapping, to_list(_arg.fields[0])), ObjectExpr73()))

        elif _arg.tag == 4:
            return Json(4, map_1(partial_apply(1, map_key, [xs]), _arg.fields[0]))

        else: 
            return _arg


    return map_key(empty(), json)


def SimpleJson_readPath(keys_mut: FSharpList[str], input_mut: Json) -> Optional[Json]:
    while True:
        (keys, input) = (keys_mut, input_mut)
        (pattern_matching_result, dict_1, key, dict_2, first_key, rest) = (None, None, None, None, None, None)
        if not is_empty(keys):
            if is_empty(tail(keys)):
                if input.tag == 5:
                    pattern_matching_result = 1
                    dict_1 = input.fields[0]
                    key = head(keys)

                else: 
                    pattern_matching_result = 3


            elif input.tag == 5:
                pattern_matching_result = 2
                dict_2 = input.fields[0]
                first_key = head(keys)
                rest = tail(keys)

            else: 
                pattern_matching_result = 3


        else: 
            pattern_matching_result = 0

        if pattern_matching_result == 0:
            return None

        elif pattern_matching_result == 1:
            return try_find(key, dict_1)

        elif pattern_matching_result == 2:
            match_value_1: Optional[Json] = try_find(first_key, dict_2)
            (pattern_matching_result_1, next_dict) = (None, None)
            if match_value_1 is not None:
                if match_value_1.tag == 5:
                    pattern_matching_result_1 = 0
                    next_dict = match_value_1.fields[0]

                else: 
                    pattern_matching_result_1 = 1


            else: 
                pattern_matching_result_1 = 1

            if pattern_matching_result_1 == 0:
                keys_mut = rest
                input_mut = Json(5, next_dict)
                continue

            elif pattern_matching_result_1 == 1:
                return None


        elif pattern_matching_result == 3:
            return None

        break


__all__ = ["InteropUtil_isDateOffset", "SimpleJson_toString", "SimpleJson_parseNative_0027", "SimpleJson_parseNative", "SimpleJson_tryParseNative", "SimpleJson_fromObjectLiteral", "SimpleJson_mapKeys", "SimpleJson_toPlainObject", "SimpleJson_mapbyKey", "SimpleJson_mapKeysByPath", "SimpleJson_readPath"]

