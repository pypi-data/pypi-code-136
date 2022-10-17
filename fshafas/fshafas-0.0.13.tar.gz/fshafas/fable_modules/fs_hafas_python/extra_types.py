from __future__ import annotations
from dataclasses import dataclass
from typing import (Literal, Optional, Any, TypeVar, Generic)
from ..fable_library.reflection import (TypeInfo, class_type, string_type, option_type, record_type)
from ..fable_library.string import (to_console, printf)
from ..fable_library.types import (Exception, Record, Array)
from ..fable_library.util import equals

_B = TypeVar("_B")

_S = TypeVar("_S")

def _expr74() -> TypeInfo:
    return class_type("FsHafas.Client.Log", None, Log)


class Log:
    def __init__(self, __unit: Literal[None]=None) -> None:
        pass


Log_reflection = _expr74

def Log__ctor(__unit: Literal[None]=None) -> Log:
    return Log(__unit)


def _expr75() -> TypeInfo:
    return class_type("FsHafas.Client.HafasError", None, HafasError, class_type("System.Exception"))


class HafasError(Exception):
    def __init__(self, code: str, msg: str) -> None:
        super().__init__(msg)
        self.code_004027: str = code


HafasError_reflection = _expr75

def HafasError__ctor_Z384F8060(code: str, msg: str) -> HafasError:
    return HafasError(code, msg)


def _expr76() -> TypeInfo:
    return record_type("FsHafas.Client.Icon", [], Icon, lambda: [("type", string_type), ("title", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Icon(Record):
    type: str
    title: Optional[str]

Icon_reflection = _expr76

def Log__cctor(__unit: Literal[None]=None) -> None:
    Log.debug = False


Log__cctor()

def Log_get_Debug(__unit: Literal[None]=None) -> bool:
    return Log.debug


def Log_set_Debug_Z1FBCCD16(v: bool) -> None:
    Log.debug = v


def Log_Print(msg: str, o: Any=None) -> None:
    if Log.debug:
        to_console(printf("%s %A"))(msg)(o)



def HafasError__get_code(e: HafasError) -> str:
    return e.code_004027


def HafasError__get_isHafasError(e: HafasError) -> bool:
    return True


def _expr77(gen0: TypeInfo, gen1: TypeInfo) -> TypeInfo:
    return class_type("FsHafas.Client.IndexMap`2", [gen0, gen1], IndexMap_2)


class IndexMap_2(Generic[_B, _S]):
    def __init__(self, default_value: Optional[Any]=None) -> None:
        self.default_value: _B = default_value
        self.dict: Any = dict()


IndexMap_2_reflection = _expr77

def IndexMap_2__ctor_2B594(default_value: Optional[Any]=None) -> IndexMap_2[_B]:
    return IndexMap_2(default_value)


def IndexMap_2__get_Item_2B595(__: IndexMap_2[_S, _B], s: _S) -> _B:
    v: _B = __.dict.get(s)
    if not equals(v, None):
        return v

    else: 
        return __.default_value



def IndexMap_2__set_Item_541DA560(__: IndexMap_2[Any, Any], s: Any=None, b: Any=None) -> None:
    __.dict[s]=b


def IndexMap_2__get_Keys(__: IndexMap_2[_S, Any]) -> Array[_S]:
    return list(__.dict)


__all__ = ["Log_reflection", "HafasError_reflection", "Icon_reflection", "Log_get_Debug", "Log_set_Debug_Z1FBCCD16", "Log_Print", "HafasError__get_code", "HafasError__get_isHafasError", "IndexMap_2_reflection", "IndexMap_2__get_Item_2B595", "IndexMap_2__set_Item_541DA560", "IndexMap_2__get_Keys"]

