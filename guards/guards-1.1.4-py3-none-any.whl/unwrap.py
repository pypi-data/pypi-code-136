import dataclasses

import typing_inspect
from typing import Type, Union
from .null import NullType


@dataclasses.dataclass
class UnwrapResults:
    unwrapped_type: Type
    """ The type(s) with Null/None types filtered out. If there is only one type left after
        filtering Null/None types out then this will be that type. Otherwise it will be a
        Union type with the remaining types in (and the Null/None types filtered out).

        If the type was not a Union, then we simply set that type into `unwrapped_type`
        and leave is_nullable/is_optional as False.
    """
    is_nullable: bool = False
    is_optional: bool = False


def unwrap_union(type_to_unwrap: Type, /) -> UnwrapResults:
    """
    Returns the first non-Null or non-None type inside the optional/Union type as
    the `unwrapped_type` result.

    If the type passed in is not an optional/nullable/union type, then set returned
    `unwrapped_type` to the type unaltered.

    Args:
        type_to_unwrap: Type to inspect and unwrap the optionality/nullability/union from.
    Returns:
        UnwrapResults: With the unwrapped_type, and if type is Nullable and/or Optional.
            If the Union has more than one none-Null/None type in it, then we will return
            a Union with the None and Null types filtered out.
    """
    if not typing_inspect.is_union_type(type_to_unwrap):
        return UnwrapResults(type_to_unwrap)

    NoneType = type(None)
    saw_null = False
    saw_none = False
    types = []

    hint_union_sub_types = typing_inspect.get_args(type_to_unwrap)
    for sub_type in hint_union_sub_types:
        if sub_type is NullType:
            saw_null = True
            continue

        if sub_type is NoneType:
            saw_none = True
            continue

        types.append(sub_type)

    if len(types) == 1:
        # No other non-Null/None types, use the type directly.
        unwrapped_type = types[0]
    else:
        # Construct final Union type with the None/Null filtered out.
        unwrapped_type = Union[tuple(types)]

    return UnwrapResults(unwrapped_type, is_nullable=saw_null, is_optional=saw_none)
