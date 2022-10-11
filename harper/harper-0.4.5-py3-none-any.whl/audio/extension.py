"""Various array padding functions."""
import numpy as np


def zero_extension(array: np.ndarray, n: int) -> np.ndarray:
    """Add zeros to both sides of an array.

    Parameters
    ----------
    array: np.ndarray
        The array to pad.
    n: int
        The number of zeros to pad on to each side.

    Example
    -------
    ::
        padded = zero_pad([1,2,3], 2)

        print(padded)
        > [0,0,1,2,3,0,0]

    Returns
    -------
    numpy.ndarray
        The padded array

    """

    padding = np.zeros((n,), dtype=array.dtype)
    return np.concatenate((padding, array, padding))


def constant_extension(array: np.ndarray, n: int) -> np.ndarray:
    """Extend the last observation in both directions by a given amount.

    Parameters
    ----------
    array: np.ndarray
        The array to extend.
    n: int
        The number of repitions to pad to each side of the array.

    Example
    -------
    ::
        padded = constant_pad([1,2,3], 2)
        print(padded)
        > [1,1,1,2,3,3,3]


    """
    last_obs = array[-1]
    first_obs = array[0]
    first_array = np.full((n,), first_obs, dtype=array.dtype)
    last_array = np.full((n,), last_obs, dtype=array.dtype)
    return np.concatenate((first_array, array, last_array))


def even_extension(array: np.ndarray, n: int) -> np.ndarray:
    """Extend the array by mirroring the boundary observations


    Example
    -------
    array = [1,2,3,4,5]
    out = mirror_pad(array, 2)
    print(out)
    > [3,2,1,2,3,4,5,4,3]

    Returns
    -------
    np.ndarray
        The padded/mirrored array.



    """
    right_array = np.flip(array[(-1 - n) : -1 : 1], axis=-1)
    left_array = array[n:0:-1]
    return np.concatenate((left_array, array, right_array))


# def odd_extension(array:np.ndarray, n:int) -> np.ndarray:
#     rety
