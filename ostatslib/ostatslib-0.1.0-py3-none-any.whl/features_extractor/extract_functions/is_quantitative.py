"""Set of functions to compose FeatureExtractor class"""

import numpy as np
from numpy.typing import NDArray


def is_quantitative(column_array: NDArray) -> bool:
    """Function to indicate if a variable is quantitative.
    It's based in numpy's scalar dtypes hierarchy:
    https://numpy.org/doc/stable/reference/arrays.scalars.html

    Args:
        column_array (NDArray): 1-dimension array with a variable (column) data

    Returns:
        bool: true if the variable is quantitative
    """
    _dtype: np.dtype = column_array.dtype

    is_numeric: bool = np.issubdtype(_dtype, np.number)
    if not is_numeric:
        return False

    unique_values: NDArray = np.unique(column_array)
    unique_values_count: int = len(unique_values)
    rows_count: int = len(column_array)

    is_integer: bool = np.issubdtype(_dtype, np.integer)
    if is_integer:
        return __handle_is_quantitative_integers_case(
            unique_values, unique_values_count, rows_count)

    return __handle_is_quantitative_inexact_case(
        unique_values, unique_values_count, rows_count)


TINY_ROW_COUNT: int = 10
LOW_ROW_COUNT: int = 100
MEDIUM_ROW_COUNT: int = 500
LOW_UNIQUE_VALUES_COUNT: int = 5


def __handle_is_quantitative_integers_case(
        unique_values: int,
        unique_values_count: int,
        rows_count: int) -> bool:

    if unique_values_count == 2:
        return False

    if (unique_values_count <= LOW_UNIQUE_VALUES_COUNT and
        rows_count >= LOW_ROW_COUNT and
            __is_array_equally_spaced(unique_values)):
        return False

    return True


def __handle_is_quantitative_inexact_case(
        unique_values: int,
        unique_values_count: int,
        rows_count: int) -> bool:

    if unique_values_count == 2 and rows_count > TINY_ROW_COUNT:
        return False

    if (unique_values_count <= LOW_UNIQUE_VALUES_COUNT and
        rows_count > MEDIUM_ROW_COUNT and
            __is_array_equally_spaced(unique_values)):
        return False

    return True


def __is_array_equally_spaced(values: NDArray):
    intervals = np.diff(values)
    return np.all(intervals == intervals[0])
