"""Function to indicate ratio of missing entries in a variable data"""

import numpy as np
from numpy.typing import NDArray


def get_missing_entries_ratio(column_array: NDArray) -> float:
    """Gets ratio of missing entries in an array.
    If dtype is numeric, missing entries are Nan.
    If dtype is str, missing entries are empty strings

    Args:
        column_array (NDArray): Numpy NDArray

    Returns:
        float: Ratio of missing entries
    """
    _dtype: np.dtype = column_array.dtype
    rows_count = len(column_array)

    if np.issubdtype(_dtype, np.number):
        return np.count_nonzero(np.isnan(column_array)) / rows_count

    if np.issubdtype(_dtype, np.object_):
        return 1 - (np.count_nonzero(column_array) / rows_count)

    return 0
