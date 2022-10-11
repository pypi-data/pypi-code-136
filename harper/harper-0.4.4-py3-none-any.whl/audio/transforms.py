"""Various signal transform functions."""
import math
import random
import typing

from harper.audio.windows import sliding
from .signal import Signal
from .spectogram import Spectogram


def haar(signal):
    """Compute a level 1 haar transform on a signal.

    Parameters
    ----------
    signal : harper.Signal
        Signal to perform a haar transform on.

    Returns
    -------
    tuple
        A tuple of (trend, fluctuations) from the haar transform.

    """
    ts = signal.timeseries

    windowed_ts = sliding(ts, 2, 2, unequal="pad", padval=0)

    avgs = [(x[0] + x[1]) / math.sqrt(2) for x in windowed_ts]
    diffs = [(x[0] - x[1]) / math.sqrt(2) for x in windowed_ts]

    rounded_avgs = [round(x) for x in avgs]
    rounded_diffs = [round(x) for x in diffs]

    return rounded_avgs, rounded_diffs


def time_shift(signal, shift_limit: typing.float):
    """Permute a signal by shifting timeseries data by a random amount.

    Parameters
    ----------
    signal: harper.Signal
        Signal to timeshift.
    shift_limit: float
        The maximum amount we will timeshift, as a a percentage of the total
        number of samples.

    Returns
    -------
    harper.Signal
        A timeshifted signal
    """
    shift_amt = int(random.random() * shift_limit * len(signal))
    return Signal.from_timeseries(signal.timeseries.roll(shift_amt))


def create_spectogram(signal):
    """Generate a spectogram from a signal.

    Parameters
    ----------
    signal: harper.Signal

    Returns
    -------
    harper.Spectogram

    """
    pass
