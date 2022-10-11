"""Window functions for snipping things."""

import numpy as np

from harper.audio.signal import Signal


def blackman(signal, window_size):
    """Run a blackman window over a Signal.

    Chunks the signal into fragments of equal size and
    tapers them via the blackman window.

    Parameters
    ----------
    signal: harper.Signal
        Signal to be transformed
    window_size: int
        The number of samples to chunk the signal into.

    Returns
    -------
    harper.Signal
        A chunked and transformed window.

    """
    np_array = np.array(signal.timeseries)
    series_list = list(np_array)
    chunks = sliding(series_list, window_size, window_size)

    b_window = np.blackman(window_size)

    _b_chunks = list()
    for chunk in chunks:
        windowed_chunk = np.multiply(chunk, b_window)
        _b_chunks.append(Signal.from_complex_timeseries(windowed_chunk))

    return _b_chunks


def sliding(
    iterable: iter, size: int, stride: int = 2, unequal: str = "pad", padval=0
) -> list:
    """Pass through an iterable and return certain windowed segments.

    It's basically a moving window of a certain size and stride
    that extracts subsets of an iterable.

    Parameters
    ----------
    iterable : iter
        The thing to move through
    size: int
        The size of the window to pan with. This is how many
        elements will be considered as part of a subset.
    stride: int
        After getting a subset, how many steps should the window
        move before selecting the next chunk?
    unequal : str
        Can be 'pad' or 'drop'. It's very possible that the
        end of a list wont contain the expected number of items,
        eg.
        [1,2,3]
        with a size of 4 would only find 3 elements. What should happen?
        If 'pad' we add a value to that subset. Specify the value with the
        padval keyword argument. If 'drop' we simply let the subset be
        3 items.


    Examples
    --------
    orig = [1,2,3,4,5,6,7,8]
    window(orig, size=2, stride=3)

      -> [(1,2),3,4,5,6,7,8]
      -> [1,2,3,(4,5),6,7,8]
      -> [1,2,3,4,5,6,(7,8)]

    would return [[1,2], [4,5], [7,8]]

    """
    finished = list()

    start = 0
    end = start + size
    final = len(iterable)

    # when to break:
    # if end is exactly final, thats the last time we should run
    # if end is greater than final, thats the last time we should run

    while start <= final:
        current = iterable[start:end]
        if len(current) == 0:
            break
        if len(current) < size:
            if unequal == "pad":
                while len(current) < size:
                    if isinstance(current, bytes):
                        current = current + b"\x00"
                    else:
                        current.append(padval)
            if unequal == "drop":
                pass
        finished.append(current)
        if end >= final:
            break
        start += stride
        end += stride
    return finished


def tukey():
    # TODO: define tukey window
    pass
