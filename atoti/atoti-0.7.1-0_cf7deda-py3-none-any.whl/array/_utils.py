from __future__ import annotations

from typing import Union

from atoti_core import is_array_type

from .._data_type_error import DataTypeError
from .._operation import Operation
from ..column import Column
from ..measure import Measure
from ..measure_description import MeasureDescription

ArrayType = Union[Column, Operation]

QUANTILE_STD_AND_VAR_DOC_KWARGS = {
    "measure_or_operand": "measure",
    "what": "of the elements of the passed array measure",
}


def check_array_type(measure: MeasureDescription) -> None:
    if isinstance(measure, Measure) and not is_array_type(measure.data_type):
        message = (
            "Incorrect measure type."
            f" Expected measure {measure.name} to be of type array but got {measure.data_type}."
        )
        raise DataTypeError(message)


def validate_n_argument(n: Union[int, MeasureDescription]) -> None:
    if isinstance(n, int) and n <= 0:
        raise ValueError("n must be greater than 0.")
