"""Tools to downsample, resample, etc."""
import fractions

import numpy as np

from harper.audio.signal import Signal
from harper.audio.filters import lowpass_filter


def resample(signal, ratio):
    """Convert a Signal from one sample rate to another.

    Parameters
    ----------
    signal : harper.Signal
        Signal to be converted.
    ratio : int
        ratio by which to increase or decrease sample rate

    Returns
    -------
    harper.Signal
        The resampled Signal
    """
    if ratio == 1:
        return signal

    if ratio < 1:
        return downsample(signal, ratio)

    if ratio > 1:
        return upsample(signal, ratio)


def downsample(signal, ratio):
    """Downsample a signal by a certain ratio and return resulting signal.

    Note, this returns a shorter timeseries and a shorter signal,
    so a downsamples series will sound as though it has been
    sped up.

    Parameters
    ----------
    signal : harper.Signal
        Signal to be downsampled
    ratio : float
        Ratio of samples to keep.
    """
    if ratio >= 1:
        raise ValueError(
            "Must downsample with a rate lower than current sample rate."
        )
    else:
        f = fractions.Fraction(1 - ratio).limit_denominator()
        delete = f.numerator
        every = f.denominator
        total_samples = len(signal)
        must_delete = int(round((delete / every) * total_samples))
        delete_idx = np.round(
            np.linspace(0, total_samples - 1, must_delete)
        ).astype(int)
        new_array = np.delete(signal._complex_timeseries, delete_idx)
        return Signal.from_complex_timeseries(new_array)


def upsample(signal, stuff_factor):
    """Zero-stuff the signal by an integer rate.

    Parameters
    ----------
    signal : harper.Signal
        Signal to get stuffed! Stuff it, Signal!
    stuff_factor : int
        The number of zeroes to insert in between each sample

    Returns
    -------
    harper.Signal
        The zero-stuffed signal

    """
    n = signal._complex_timeseries.shape[0]
    out = np.zeros(
        ((stuff_factor + 1) * n), dtype=signal._complex_timeseries.dtype
    )
    out[:: stuff_factor + 1] = signal._complex_timeseries
    return Signal.from_complex_timeseries(out)


def interpolate(signal, stuff_factor, frequency_threshold):
    """Upsample and then lowpass filter to remove spectral images.

    Parameters
    ----------
    signal: harper.Signal
        Signal to upsample and interpolate
    stuff_factor: int
        Number of zeroes to insert between samples.t l
    frequency_threshold: int
        lowpass_filter threshold

    Returns
    -------
    harper.Signal
        interpolated sample
    """
    upsampled = upsample(signal, stuff_factor)
    interped = lowpass_filter(upsampled, threshold=frequency_threshold)
    return interped
