"""Smoothing functions for digital signals."""
import copy
from harper.audio.signal import Signal


def sliding_average_smooth(signal, m=3):
    """Smooth a timeseries by using an m-sized sliding filter.

    Parameters
    ----------
    signal : harper.Signal
        Signal to be smoothed.
    m : int
        filter size. Must be an odd number. Optional, defaults to 3.

    Returns
    -------
    harper.Signal
       Smooth as silk Signal.
    """
    series = copy.deepcopy(signal.timeseries)

    smooth_points = list(range(m))
    per_side = int((m - 1) / 2)
    start_slice = per_side
    end_slice = per_side * -1

    for i, s in enumerate(series[start_slice:end_slice]):
        for n in range(m):
            smooth_points[n] = series[n + i]
        j = int(round(sum(smooth_points) / len(smooth_points)))
        series[i + start_slice] = j

    return Signal.from_timeseries(series)
