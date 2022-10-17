from __future__ import annotations
from typing import (Any, Optional, Tuple, Literal, TypeVar, Callable)
from ..fable_library.array import (map, for_all)
from ..fable_library.mutable_map import Dictionary
from ..fable_library.reflection import (full_name, is_record, name, get_record_elements, get_generics, is_union, get_union_case_fields, get_union_cases, is_function, get_function_elements, is_array, get_element_type, is_tuple, get_tuple_elements, is_enum, get_enum_underlying_type, equals)
from ..fable_library.seq import (to_array, delay, append, singleton, collect)
from ..fable_library.string import trim_start
from ..fable_library.types import Array
from ..fable_library.util import (IEnumerable_1, Lazy, structural_hash)
from .type_info import (TypeInfo, RecordField, UnionCase)

__A = TypeVar("__A")

def _007CPrimitiveType_007C__007C(prim_type: Any) -> Optional[TypeInfo]:
    match_value: str = full_name(prim_type)
    (pattern_matching_result,) = (None,)
    if match_value == "System.String":
        pattern_matching_result = 0

    elif match_value == "System.Char":
        pattern_matching_result = 1

    elif match_value == "System.Int16":
        pattern_matching_result = 2

    elif match_value == "System.Int32":
        pattern_matching_result = 3

    elif match_value == "Microsoft.FSharp.Core.int64`1":
        pattern_matching_result = 4

    elif match_value == "System.Int64":
        pattern_matching_result = 4

    elif match_value == "System.UInt16":
        pattern_matching_result = 5

    elif match_value == "System.UInt32":
        pattern_matching_result = 6

    elif match_value == "System.UInt64":
        pattern_matching_result = 7

    elif match_value == "System.DateTime":
        pattern_matching_result = 8

    elif match_value == "System.TimeSpan":
        pattern_matching_result = 9

    elif match_value == "System.DateTimeOffset":
        pattern_matching_result = 10

    elif match_value == "System.Boolean":
        pattern_matching_result = 11

    elif match_value == "System.Single":
        pattern_matching_result = 12

    elif match_value == "System.Double":
        pattern_matching_result = 13

    elif match_value == "Microsoft.FSharp.Core.decimal`1":
        pattern_matching_result = 14

    elif match_value == "System.Decimal":
        pattern_matching_result = 14

    elif match_value == "System.Numerics.BigInteger":
        pattern_matching_result = 15

    elif match_value == "Microsoft.FSharp.Core.Unit":
        pattern_matching_result = 16

    elif match_value == "System.Guid":
        pattern_matching_result = 17

    elif match_value == "System.Byte":
        pattern_matching_result = 18

    elif match_value == "System.SByte":
        pattern_matching_result = 19

    elif match_value == "System.Object":
        pattern_matching_result = 20

    elif match_value == "System.Uri":
        pattern_matching_result = 21

    else: 
        pattern_matching_result = 22

    if pattern_matching_result == 0:
        return TypeInfo(2)

    elif pattern_matching_result == 1:
        return TypeInfo(1)

    elif pattern_matching_result == 2:
        return TypeInfo(11)

    elif pattern_matching_result == 3:
        return TypeInfo(6)

    elif pattern_matching_result == 4:
        return TypeInfo(12)

    elif pattern_matching_result == 5:
        return TypeInfo(3)

    elif pattern_matching_result == 6:
        return TypeInfo(4)

    elif pattern_matching_result == 7:
        return TypeInfo(5)

    elif pattern_matching_result == 8:
        return TypeInfo(15)

    elif pattern_matching_result == 9:
        return TypeInfo(18)

    elif pattern_matching_result == 10:
        return TypeInfo(16)

    elif pattern_matching_result == 11:
        return TypeInfo(7)

    elif pattern_matching_result == 12:
        return TypeInfo(8)

    elif pattern_matching_result == 13:
        return TypeInfo(9)

    elif pattern_matching_result == 14:
        return TypeInfo(10)

    elif pattern_matching_result == 15:
        return TypeInfo(17)

    elif pattern_matching_result == 16:
        return TypeInfo(0)

    elif pattern_matching_result == 17:
        return TypeInfo(19)

    elif pattern_matching_result == 18:
        return TypeInfo(13)

    elif pattern_matching_result == 19:
        return TypeInfo(14)

    elif pattern_matching_result == 20:
        return TypeInfo(20)

    elif pattern_matching_result == 21:
        return TypeInfo(21)

    elif pattern_matching_result == 22:
        return None



def _007CRecordType_007C__007C(t: Any) -> Optional[Array[Tuple[Any, str, Any]]]:
    if is_record(t):
        def mapping(field: Any, t: Any=t) -> Tuple[Any, str, Any]:
            return (field, name(field), field[1])

        return map(mapping, get_record_elements(t), None)

    else: 
        return None



def _007CSetType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("Microsoft.FSharp.Collections.FSharpSet`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CNullable_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("System.Nullable`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CUnionType_007C__007C(t: Any) -> Optional[Array[Tuple[str, Any, Array[Any]]]]:
    if is_union(t):
        def mapping_1(info: Any, t: Any=t) -> Tuple[str, Any, Array[Any]]:
            def mapping(prop: Any, info: Any=info) -> Any:
                return prop[1]

            return (name(info), info, map(mapping, get_union_case_fields(info), None))

        return map(mapping_1, get_union_cases(t), None)

    else: 
        return None



def _007CMapType_007C__007C(t: Any) -> Optional[Tuple[Any, Any]]:
    if trim_start(full_name(t), "$").find("Microsoft.FSharp.Collections.FSharpMap`2") == 0:
        gen_args: Array[Any] = get_generics(t)
        return (gen_args[0], gen_args[1])

    else: 
        return None



def _007CListType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("Microsoft.FSharp.Collections.FSharpList`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def flatten_func_types(type_def: Any) -> Array[Any]:
    def _arrow6(__unit: Literal[None]=None, type_def: Any=type_def) -> IEnumerable_1[Any]:
        if is_function(type_def):
            pattern_input: Tuple[Any, Any] = get_function_elements(type_def)
            def _arrow5(__unit: Literal[None]=None) -> IEnumerable_1[Any]:
                return flatten_func_types(pattern_input[1])

            return append(flatten_func_types(pattern_input[0]), delay(_arrow5))

        else: 
            return singleton(type_def)


    return to_array(delay(_arrow6))


def _007CFuncType_007C__007C(t: Any) -> Optional[Array[Any]]:
    if is_function(t):
        return flatten_func_types(t)

    else: 
        return None



def _007CArrayType_007C__007C(t: Any) -> Optional[Any]:
    if is_array(t):
        return get_element_type(t)

    else: 
        return None



def _007COptionType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("Microsoft.FSharp.Core.FSharpOption`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CTupleType_007C__007C(t: Any) -> Optional[Array[Any]]:
    if is_tuple(t):
        return get_tuple_elements(t)

    else: 
        return None



def _007CSeqType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("System.Collections.Generic.IEnumerable`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CDictionaryType_007C__007C(t: Any) -> Optional[Tuple[Any, Any]]:
    if trim_start(full_name(t), "$").find("System.Collections.Generic.Dictionary") == 0:
        gen_args: Array[Any] = get_generics(t)
        return (gen_args[0], gen_args[1])

    else: 
        return None



def _007CResizeArrayType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("System.Collections.Generic.List") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CHashSetType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("System.Collections.Generic.HashSet") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CAsyncType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("Microsoft.FSharp.Control.FSharpAsync`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def _007CPromiseType_007C__007C(t: Any) -> Optional[Any]:
    if trim_start(full_name(t), "$").find("Fable.Core.JS.Promise`1") == 0:
        return get_generics(t)[0]

    else: 
        return None



def lazy_to_delayed(l: Any, unit_var: None) -> __A:
    return l.Value


def _007CEnumType_007C__007C(t: Any) -> Optional[Any]:
    if is_enum(t):
        return get_enum_underlying_type(t)

    else: 
        return None



def _createTypeInfo(resolved_type: Any) -> TypeInfo:
    active_pattern_result: Optional[TypeInfo] = _007CPrimitiveType_007C__007C(resolved_type)
    if active_pattern_result is not None:
        type_info: TypeInfo = active_pattern_result
        return type_info

    else: 
        active_pattern_result_1: Optional[Array[Any]] = _007CFuncType_007C__007C(resolved_type)
        if active_pattern_result_1 is not None:
            types: Array[Any] = active_pattern_result_1
            def _arrow13(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Array[TypeInfo]]:
                def _arrow10(__unit: Literal[None]=None) -> Array[TypeInfo]:
                    def _arrow9(resolved_type_1: Any) -> TypeInfo:
                        return create_type_info(resolved_type_1)

                    return map(_arrow9, types, None)

                l: Any = Lazy(_arrow10)
                def _arrow11(__unit: Literal[None]=None) -> Array[TypeInfo]:
                    return lazy_to_delayed(l, None)

                return _arrow11

            return TypeInfo(35, _arrow13())

        else: 
            active_pattern_result_2: Optional[Array[Tuple[Any, str, Any]]] = _007CRecordType_007C__007C(resolved_type)
            if active_pattern_result_2 is not None:
                fields: Array[Tuple[Any, str, Any]] = active_pattern_result_2
                def _arrow16(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Tuple[Array[RecordField], Any]:
                    def _arrow15(__unit: Literal[None]=None) -> IEnumerable_1[RecordField]:
                        def _arrow14(match_value: Tuple[Any, str, Any]) -> IEnumerable_1[RecordField]:
                            return singleton(RecordField(match_value[1], create_type_info(match_value[2]), match_value[0]))

                        return collect(_arrow14, fields)

                    return (to_array(delay(_arrow15)), resolved_type)

                return TypeInfo(37, _arrow16)

            else: 
                active_pattern_result_3: Optional[Array[Tuple[str, Any, Array[Any]]]] = _007CUnionType_007C__007C(resolved_type)
                if active_pattern_result_3 is not None:
                    cases: Array[Tuple[str, Any, Array[Any]]] = active_pattern_result_3
                    def _arrow21(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Tuple[Array[UnionCase], Any]:
                        def _arrow20(__unit: Literal[None]=None) -> IEnumerable_1[UnionCase]:
                            def _arrow19(match_value_1: Tuple[str, Any, Array[Any]]) -> IEnumerable_1[UnionCase]:
                                def _arrow18(resolved_type_2: Any) -> TypeInfo:
                                    return create_type_info(resolved_type_2)

                                return singleton(UnionCase(match_value_1[0], map(_arrow18, match_value_1[2], None), match_value_1[1]))

                            return collect(_arrow19, cases)

                        return (to_array(delay(_arrow20)), resolved_type)

                    l_1: Any = Lazy(_arrow21)
                    def _arrow22(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Tuple[Array[UnionCase], Any]:
                        return lazy_to_delayed(l_1, None)

                    return TypeInfo(38, _arrow22)

                else: 
                    active_pattern_result_4: Optional[Any] = _007CEnumType_007C__007C(resolved_type)
                    if active_pattern_result_4 is not None:
                        elem_type: Any = active_pattern_result_4
                        def _arrow25(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Tuple[TypeInfo, Any]]:
                            def _arrow23(__unit: Literal[None]=None) -> Tuple[TypeInfo, Any]:
                                return (create_type_info(elem_type), resolved_type)

                            l_2: Any = Lazy(_arrow23)
                            def _arrow24(__unit: Literal[None]=None) -> Tuple[TypeInfo, Any]:
                                return lazy_to_delayed(l_2, None)

                            return _arrow24

                        return TypeInfo(36, _arrow25())

                    else: 
                        active_pattern_result_5: Optional[Any] = _007CListType_007C__007C(resolved_type)
                        if active_pattern_result_5 is not None:
                            elem_type_1: Any = active_pattern_result_5
                            def _arrow26(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> TypeInfo:
                                return create_type_info(elem_type_1)

                            return TypeInfo(26, _arrow26)

                        else: 
                            active_pattern_result_6: Optional[Any] = _007CResizeArrayType_007C__007C(resolved_type)
                            if active_pattern_result_6 is not None:
                                elem_type_2: Any = active_pattern_result_6
                                def _arrow29(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                    def _arrow27(__unit: Literal[None]=None) -> TypeInfo:
                                        return create_type_info(elem_type_2)

                                    l_3: Any = Lazy(_arrow27)
                                    def _arrow28(__unit: Literal[None]=None) -> TypeInfo:
                                        return lazy_to_delayed(l_3, None)

                                    return _arrow28

                                return TypeInfo(33, _arrow29())

                            else: 
                                active_pattern_result_7: Optional[Any] = _007CHashSetType_007C__007C(resolved_type)
                                if active_pattern_result_7 is not None:
                                    elem_type_3: Any = active_pattern_result_7
                                    def _arrow32(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                        def _arrow30(__unit: Literal[None]=None) -> TypeInfo:
                                            return create_type_info(elem_type_3)

                                        l_4: Any = Lazy(_arrow30)
                                        def _arrow31(__unit: Literal[None]=None) -> TypeInfo:
                                            return lazy_to_delayed(l_4, None)

                                        return _arrow31

                                    return TypeInfo(34, _arrow32())

                                else: 
                                    active_pattern_result_8: Optional[Any] = _007CArrayType_007C__007C(resolved_type)
                                    if active_pattern_result_8 is not None:
                                        elem_type_4: Any = active_pattern_result_8
                                        def _arrow35(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                            def _arrow33(__unit: Literal[None]=None) -> TypeInfo:
                                                return create_type_info(elem_type_4)

                                            l_5: Any = Lazy(_arrow33)
                                            def _arrow34(__unit: Literal[None]=None) -> TypeInfo:
                                                return lazy_to_delayed(l_5, None)

                                            return _arrow34

                                        return TypeInfo(28, _arrow35())

                                    else: 
                                        active_pattern_result_9: Optional[Array[Any]] = _007CTupleType_007C__007C(resolved_type)
                                        if active_pattern_result_9 is not None:
                                            types_1: Array[Any] = active_pattern_result_9
                                            def _arrow39(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Array[TypeInfo]]:
                                                def _arrow37(__unit: Literal[None]=None) -> Array[TypeInfo]:
                                                    def _arrow36(resolved_type_3: Any) -> TypeInfo:
                                                        return create_type_info(resolved_type_3)

                                                    return map(_arrow36, types_1, None)

                                                l_6: Any = Lazy(_arrow37)
                                                def _arrow38(__unit: Literal[None]=None) -> Array[TypeInfo]:
                                                    return lazy_to_delayed(l_6, None)

                                                return _arrow38

                                            return TypeInfo(30, _arrow39())

                                        else: 
                                            active_pattern_result_10: Optional[Any] = _007COptionType_007C__007C(resolved_type)
                                            if active_pattern_result_10 is not None:
                                                elem_type_5: Any = active_pattern_result_10
                                                def _arrow40(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> TypeInfo:
                                                    return create_type_info(elem_type_5)

                                                return TypeInfo(25, _arrow40)

                                            else: 
                                                active_pattern_result_11: Optional[Any] = _007CNullable_007C__007C(resolved_type)
                                                if active_pattern_result_11 is not None:
                                                    elem_type_6: Any = active_pattern_result_11
                                                    def _arrow43(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                                        def _arrow41(__unit: Literal[None]=None) -> TypeInfo:
                                                            return create_type_info(elem_type_6)

                                                        l_7: Any = Lazy(_arrow41)
                                                        def _arrow42(__unit: Literal[None]=None) -> TypeInfo:
                                                            return lazy_to_delayed(l_7, None)

                                                        return _arrow42

                                                    return TypeInfo(25, _arrow43())

                                                else: 
                                                    active_pattern_result_12: Optional[Any] = _007CSetType_007C__007C(resolved_type)
                                                    if active_pattern_result_12 is not None:
                                                        elem_type_7: Any = active_pattern_result_12
                                                        def _arrow46(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                                            def _arrow44(__unit: Literal[None]=None) -> TypeInfo:
                                                                return create_type_info(elem_type_7)

                                                            l_8: Any = Lazy(_arrow44)
                                                            def _arrow45(__unit: Literal[None]=None) -> TypeInfo:
                                                                return lazy_to_delayed(l_8, None)

                                                            return _arrow45

                                                        return TypeInfo(27, _arrow46())

                                                    else: 
                                                        active_pattern_result_13: Optional[Tuple[Any, Any]] = _007CMapType_007C__007C(resolved_type)
                                                        if active_pattern_result_13 is not None:
                                                            key_type: Any = active_pattern_result_13[0]
                                                            value_type: Any = active_pattern_result_13[1]
                                                            def _arrow49(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Tuple[TypeInfo, TypeInfo]]:
                                                                def _arrow47(__unit: Literal[None]=None) -> Tuple[TypeInfo, TypeInfo]:
                                                                    return (create_type_info(key_type), create_type_info(value_type))

                                                                l_9: Any = Lazy(_arrow47)
                                                                def _arrow48(__unit: Literal[None]=None) -> Tuple[TypeInfo, TypeInfo]:
                                                                    return lazy_to_delayed(l_9, None)

                                                                return _arrow48

                                                            return TypeInfo(31, _arrow49())

                                                        else: 
                                                            active_pattern_result_14: Optional[Tuple[Any, Any]] = _007CDictionaryType_007C__007C(resolved_type)
                                                            if active_pattern_result_14 is not None:
                                                                key_type_1: Any = active_pattern_result_14[0]
                                                                value_type_1: Any = active_pattern_result_14[1]
                                                                def _arrow54(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Tuple[TypeInfo, TypeInfo, Any]]:
                                                                    def _arrow52(__unit: Literal[None]=None) -> Tuple[TypeInfo, TypeInfo, Any]:
                                                                        return (create_type_info(key_type_1), create_type_info(value_type_1), value_type_1)

                                                                    l_10: Any = Lazy(_arrow52)
                                                                    def _arrow53(__unit: Literal[None]=None) -> Tuple[TypeInfo, TypeInfo, Any]:
                                                                        return lazy_to_delayed(l_10, None)

                                                                    return _arrow53

                                                                return TypeInfo(32, _arrow54())

                                                            else: 
                                                                active_pattern_result_15: Optional[Any] = _007CSeqType_007C__007C(resolved_type)
                                                                if active_pattern_result_15 is not None:
                                                                    elem_type_8: Any = active_pattern_result_15
                                                                    def _arrow57(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                                                        def _arrow55(__unit: Literal[None]=None) -> TypeInfo:
                                                                            return create_type_info(elem_type_8)

                                                                        l_11: Any = Lazy(_arrow55)
                                                                        def _arrow56(__unit: Literal[None]=None) -> TypeInfo:
                                                                            return lazy_to_delayed(l_11, None)

                                                                        return _arrow56

                                                                    return TypeInfo(29, _arrow57())

                                                                else: 
                                                                    active_pattern_result_16: Optional[Any] = _007CAsyncType_007C__007C(resolved_type)
                                                                    if active_pattern_result_16 is not None:
                                                                        elem_type_9: Any = active_pattern_result_16
                                                                        def _arrow60(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                                                            def _arrow58(__unit: Literal[None]=None) -> TypeInfo:
                                                                                return create_type_info(elem_type_9)

                                                                            l_12: Any = Lazy(_arrow58)
                                                                            def _arrow59(__unit: Literal[None]=None) -> TypeInfo:
                                                                                return lazy_to_delayed(l_12, None)

                                                                            return _arrow59

                                                                        return TypeInfo(23, _arrow60())

                                                                    else: 
                                                                        active_pattern_result_17: Optional[Any] = _007CPromiseType_007C__007C(resolved_type)
                                                                        if active_pattern_result_17 is not None:
                                                                            elem_type_10: Any = active_pattern_result_17
                                                                            def _arrow63(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], TypeInfo]:
                                                                                def _arrow61(__unit: Literal[None]=None) -> TypeInfo:
                                                                                    return create_type_info(elem_type_10)

                                                                                l_13: Any = Lazy(_arrow61)
                                                                                def _arrow62(__unit: Literal[None]=None) -> TypeInfo:
                                                                                    return lazy_to_delayed(l_13, None)

                                                                                return _arrow62

                                                                            return TypeInfo(24, _arrow63())

                                                                        else: 
                                                                            def _arrow66(__unit: Literal[None]=None, resolved_type: Any=resolved_type) -> Callable[[], Any]:
                                                                                def _arrow64(__unit: Literal[None]=None) -> Any:
                                                                                    return resolved_type

                                                                                l_14: Any = Lazy(_arrow64)
                                                                                def _arrow65(__unit: Literal[None]=None) -> Any:
                                                                                    return lazy_to_delayed(l_14, None)

                                                                                return _arrow65

                                                                            return TypeInfo(22, _arrow66())




















class ObjectExpr69:
    @property
    def Equals(self) -> Callable[[Any, Any], bool]:
        def _arrow67(x: Any, y: Any) -> bool:
            return equals(x, y)

        return _arrow67

    @property
    def GetHashCode(self) -> Callable[[Any], int]:
        def _arrow68(x: Any) -> int:
            return structural_hash(x)

        return _arrow68


type_info_cache: Any = Dictionary([], ObjectExpr69())

def create_type_info(resolved_type: Any) -> TypeInfo:
    return _createTypeInfo(resolved_type)


def is_primitive(_arg: TypeInfo) -> bool:
    if (((((((((((((((((_arg.tag == 0) or (_arg.tag == 2)) or (_arg.tag == 3)) or (_arg.tag == 4)) or (_arg.tag == 5)) or (_arg.tag == 6)) or (_arg.tag == 7)) or (_arg.tag == 8)) or (_arg.tag == 9)) or (_arg.tag == 10)) or (_arg.tag == 11)) or (_arg.tag == 12)) or (_arg.tag == 13)) or (_arg.tag == 15)) or (_arg.tag == 16)) or (_arg.tag == 17)) or (_arg.tag == 19)) or (_arg.tag == 25):
        return True

    else: 
        return False



def enum_union(_arg: TypeInfo) -> bool:
    if _arg.tag == 38:
        def predicate(case: UnionCase, _arg: TypeInfo=_arg) -> bool:
            return len(case.CaseTypes) == 0

        return for_all(predicate, _arg.fields[0]()[0])

    else: 
        return False



__all__ = ["_007CPrimitiveType_007C__007C", "_007CRecordType_007C__007C", "_007CSetType_007C__007C", "_007CNullable_007C__007C", "_007CUnionType_007C__007C", "_007CMapType_007C__007C", "_007CListType_007C__007C", "flatten_func_types", "_007CFuncType_007C__007C", "_007CArrayType_007C__007C", "_007COptionType_007C__007C", "_007CTupleType_007C__007C", "_007CSeqType_007C__007C", "_007CDictionaryType_007C__007C", "_007CResizeArrayType_007C__007C", "_007CHashSetType_007C__007C", "_007CAsyncType_007C__007C", "_007CPromiseType_007C__007C", "lazy_to_delayed", "_007CEnumType_007C__007C", "_createTypeInfo", "type_info_cache", "create_type_info", "is_primitive", "enum_union"]

