"""Signal filtering and modification functions."""
import copy

from harper.audio.signal import Signal
import numpy as np


def lowpass_filter(signal, threshold):
    """Filter out high frequency values on a signal.

    Parameters
    ----------
    signal: harper.Signal
        The signal to filter
    threshold: int
        The value above which frequency components will be removed.

    Returns
    -------
    harper.Signal
        The filtered signal.

    """
    new_spectra = copy.deepcopy(signal._complex_spectrum)
    new_spectra[threshold:] = 0
    timeseries = np.fft.ifft(new_spectra)
    new_signal = Signal.from_complex_timeseries(timeseries)
    return new_signal


def highpass_filter(signal, threshold):
    """Filter out low frequency values on a signal.

    Parameters
    ----------
    signal: harper.Signal
        The signal to filter
    threshold: int
        The value below which frequency components will be removed.

    Returns
    -------
    harper.Signal
        The filtered signal.

    """
    new_spectra = copy.deepcopy(signal._complex_spectrum)
    new_spectra[0:threshold] = 0
    timeseries = np.fft.ifft(new_spectra)
    new_signal = Signal.from_complex_timeseries(timeseries)
    return new_signal


def amplify_signal(signal, scale):
    """Amplify sample components by a given magnitude.

    Parameters
    ----------
    signal: harper.Signal
        The signal to amplify
    scale: Union[int, float]
        The scaling factor to increase or decrease sample strength by.

    Returns
    -------
    harper.Signal
        A new Signal with the modified amplitude.

    """
    new_series = copy.deepcopy(signal.timeseries)
    amped = list(np.round(np.array(new_series) * scale).astype("int"))
    return Signal.from_timeseries(amped)


def normalize_signal(signal, normalized_amplitude=16000):
    """Scale amplitude to a certain scale factor. Defaults to 16000.

    Parameters
    ----------
    signal: harper.Signal
        Signal to normalize
    normalized_amplitude: int
        Amplitude value to scale maximum signal magnitude to.

    Returns
    -------
    harper.Signal
        Scaled audio signal.
    """
    largest_abs_number = np.max(np.abs(np.array(signal.timeseries)))
    scale_factor = normalized_amplitude / largest_abs_number
    return amplify_signal(signal, scale_factor)
