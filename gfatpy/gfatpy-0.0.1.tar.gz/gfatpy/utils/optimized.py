import numpy as np
from numpy.polynomial.polynomial import polyfit


import numba


def best_slope_fit(mat1: np.ndarray, mat2: np.ndarray, window: int) -> np.ndarray:

    assert mat1.shape == mat2.shape, "Matrices shape must match"
    assert isinstance(window, int), "Window argument must be an integer"

    x = np.arange(window)
    res = np.array([])

    # Iter in first dimension, equivalent to time in lidar case
    for idx in range(mat1.shape[0]):
        windowed1 = _rolling(mat1[idx], window)
        windowed2 = _rolling(mat2[idx], window)

        slopes1 = polyfit(x, windowed1.T, 1)[0]
        slopes2 = polyfit(x, windowed2.T, 1)[0]
        chosen_group = np.argmin(np.abs(slopes1 - slopes2) / slopes1)
        res = np.hstack([res, chosen_group + np.floor(window / 2)])  # Append chosen bin

    return res.astype(int)


@numba.njit(parallel=True)
def windowed_corrcoefs(arr1: np.ndarray, arr2: np.ndarray, w_size: int):
    range_shape = arr1.shape[1] - (w_size - 1)
    _corrcoefs = np.empty((arr1.shape[0], range_shape))
    for t_idx in numba.prange(arr1.shape[0]):
        w1 = _rolling(arr1[t_idx], w_size)
        w2 = _rolling(arr2[t_idx], w_size)
        for idx in numba.prange(range_shape):
            _w1 = w1[idx]
            _w2 = w2[idx]
            coeff = np.corrcoef(_w1, _w2)[1, 0]
            _corrcoefs[t_idx][idx] = coeff
    return _corrcoefs


@numba.njit()
def _rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
