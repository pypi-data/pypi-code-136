"""Function to indicate if a variable is dichotomous"""

import numpy as np
from numpy.typing import NDArray


def is_dichotomous(column_array: NDArray) -> bool:
    """Function to indicate if a variable is dichotomous.
    It's based in numpy's scalar dtypes hierarchy:
    https://numpy.org/doc/stable/reference/arrays.scalars.html

    Args:
        column_array (NDArray): 1-dimension array with a variable (column) data

    Returns:
        bool: true if the variable is dichotomous
    """
    _dtype: np.dtype = column_array.dtype

    if np.issubdtype(_dtype, np.bool_) or len(np.unique(column_array)) == 2:
        return True

    return False
