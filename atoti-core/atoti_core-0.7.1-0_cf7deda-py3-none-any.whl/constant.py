from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date, datetime, time

# Here `get_args()` is used on `Union`, not on `Literal`.
from typing import (  # pylint: disable=preferred-function
    Sequence,
    Tuple,
    Union,
    get_args,
)

from .data_type import DataType

_ConstantArrayElement = Union[float, int]

ConstantValue = Union[
    bool,
    date,
    datetime,
    float,
    int,
    Sequence[_ConstantArrayElement],
    str,
    time,
]

_CONSTANT_ARRAY_ELEMENT_TYPES = get_args(_ConstantArrayElement)


def _get_checked_value_and_data_type(  # pylint: disable=too-many-branches,too-many-return-statements
    value: ConstantValue, /
) -> Tuple[ConstantValue, DataType]:
    # Use the widest types to avoid compilation problems.
    # For better performance, types are checked from the most probable to the least.

    if isinstance(value, bool):
        return value, "boolean"
    if isinstance(value, float):
        if math.isnan(value):
            raise ValueError(
                f"`{value}` is not a valid constant value. To compare against NaN, use `isnan()` instead."
            )

        return value, "double"
    if isinstance(value, int):
        return value, "long"
    if isinstance(value, str):
        return value, "String"
    if isinstance(value, datetime):
        return value, "LocalDateTime" if value.tzinfo is None else "ZonedDateTime"
    if isinstance(value, date):
        return value, "LocalDate"
    if isinstance(value, time):
        return value, "LocalTime"
    if isinstance(value, tuple):
        # `tuple` is intentionally not supported so that branches of `Union[ConstantValue, Tuple[ConstantValue, ...]]` can be distinguised with an `isinstance(value, tuple)` check.
        raise TypeError(
            "Tuples are not valid constant values. Use lists for constant arrays instead."
        )
    if isinstance(value, list):
        if len(value) == 0:
            raise ValueError(
                "Empty arrays are not supported as their data type cannot be inferred."
            )

        invalid_array_element_type = next(
            (
                type(element)
                for element in value
                if not isinstance(element, _CONSTANT_ARRAY_ELEMENT_TYPES)
            ),
            None,
        )

        if invalid_array_element_type:
            raise TypeError(
                f"Expected all the elements of the constant array to have a type of `{[valid_type.__name__ for valid_type in _CONSTANT_ARRAY_ELEMENT_TYPES]}` but got `{invalid_array_element_type.__name__}`."
            )

        if any(isinstance(element, float) for element in value):
            return [float(element) for element in value], "double[]"

        return [int(element) for element in value], "long[]"

    raise TypeError(f"Unexpected constant value type: `{type(value).__name__}`.")


@dataclass(frozen=True)
class Constant:  # pylint: disable=keyword-only-dataclass
    data_type: DataType = field(init=False)
    value: ConstantValue

    def __post_init__(self) -> None:
        value, data_type = _get_checked_value_and_data_type(self.value)
        self.__dict__["value"] = value
        self.__dict__["data_type"] = data_type
