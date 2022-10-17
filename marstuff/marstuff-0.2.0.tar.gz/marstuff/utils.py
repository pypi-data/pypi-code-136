import contextlib
import copy
import datetime
import inspect
import typing
from enum import Enum
from typing import Callable, Iterable, Sequence, Type, TypeVar

T = TypeVar("T")


def convert(var, type_: Type[T]) -> T:
    if isinstance(type_, type) and isinstance(var, type_):
        return var
    if isinstance(type_, datetime.date) and isinstance(var, str):
        return type_.fromisoformat(var)
    with contextlib.suppress(Exception):
        return type_(var)
    return var


class NamedException:
    def __new__(cls, name, err=None):
        def __init__(self, error):
            super(Exception, self).__init__(error)

        new_class = type(name, (Exception,), {'__init__': __init__})
        return new_class(err) if err else new_class


def TypedListConverter(type_to_convert: Type[T]) -> Callable[[Iterable], typing.List[T]]:
    def _convert(list_to_convert):
        dl = []
        for elm in list_to_convert:
            dl.append(convert(elm, type_to_convert))
        return dl

    return _convert


class List(typing.List):
    def __class_getitem__(cls, item):
        return TypedListConverter(item)


class Union:
    def __class_getitem__(cls, types):
        types = (types,) if not isinstance(types, tuple) else types

        def converter(item):
            dl = []
            original = copy.deepcopy(item)
            if isinstance(item, Sequence):
                for elm in item:
                    original = copy.deepcopy(elm)
                    for type in types:
                        elm = convert(elm, type)
                        if elm is not original:
                            break
                    dl.append(elm)
            else:
                for type in types:
                    item = convert(item, type)
                    if item is not original:
                        break
                dl = item
            return dl

        return converter


def contains(self, value):
    return value in self.__members__


Enum.__class__.__contains__ = contains


def Extras(extras):
    if extras:
        frame = inspect.currentframe().f_back.f_back
        other = frame.f_locals.get('self')
        if not other:
            print(f'Got extra kwarg(s) {extras} in unknown object -> {inspect.getframeinfo(frame)}')
        else:
            name = other.__class__.__name__
            print(f'Got extra kwarg(s) {extras} in {name}')
    return extras


def get_name(object, object_class, object_enum):
    if isinstance(object, object_class):
        object_name = object.name
    elif isinstance(object, object_enum):
        if isinstance(object.value, object_class):
            object_name = object.value.name
        else:
            object_name = object.value
    elif isinstance(object, str) and object.upper() in object_enum:
        object_name = object.upper()
    else:
        raise ValueError(f"Expected a {object_class.__name__}, got {object}")
    return object_name
