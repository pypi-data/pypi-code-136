"""Digital signals. The core of harper."""
from __future__ import annotations

import struct
import copy
import io

import numpy as np

from harper.media import Audio, Visual
from harper.bops import structfmt, byte_width_series
from harper.synthesis import (
    complex_to_rounded_real,
    complex_to_absolute_real_int,
)


class Signal(Audio, Visual):
    """Discrete Signal."""

    def __init__(
        self,
        timeseries,
        complex_timeseries,
        complex_spectrum,
        spectrum,
        constructor=None,
    ):
        if constructor is None:
            raise ValueError("Use a constructor")

        self._timeseries = timeseries
        self._complex_timeseries = complex_timeseries
        self._complex_spectrum = complex_spectrum
        self._spectrum = spectrum

        self._bytes = struct.pack(structfmt(self.timeseries), *self.timeseries)
        self._reversed_bytes = struct.pack(
            structfmt(self.timeseries), *self.reversed_timeseries
        )
        self._io_bytes = io.BytesIO(self.bytes)
        self._io_reversed_bytes = io.BytesIO(self.reversed_bytes)

    @classmethod
    def from_wavfile(cls, fp, channel_strategy: str = "discard"):
        pass

    @classmethod
    def from_timeseries(cls, timeseries):
        _complex_spectrum = np.fft.fft(timeseries)
        _complex_timeseries = np.fft.ifft(_complex_spectrum)
        _spectrum = list(complex_to_absolute_real_int(_complex_spectrum))
        return cls(
            timeseries=timeseries,
            spectrum=_spectrum,
            complex_timeseries=_complex_timeseries,
            complex_spectrum=_complex_spectrum,
            constructor="timeseries",
        )

    @classmethod
    def from_complex_timeseries(cls, complex_timeseries):

        _timeseries = list(complex_to_rounded_real(complex_timeseries))
        _complex_spectrum = np.fft.fft(complex_timeseries)
        _spectrum = list(complex_to_absolute_real_int(_complex_spectrum))
        return cls(
            timeseries=_timeseries,
            complex_timeseries=complex_timeseries,
            complex_spectrum=_complex_spectrum,
            spectrum=_spectrum,
            constructor="complex_timeseries",
        )

    @classmethod
    def from_complex_spectrum(cls, complex_spectrum):
        _complex_timeseries = np.fft.ifft(complex_spectrum)
        _timeseries = list(complex_to_rounded_real(_complex_timeseries))
        _spectrum = list(complex_to_absolute_real_int(complex_spectrum))
        return cls(
            timeseries=_timeseries,
            complex_timeseries=_complex_timeseries,
            spectrum=_spectrum,
            complex_spectrum=complex_spectrum,
            constructor="complex_spectrum",
        )

    @property
    def bytes(self):
        """Byte string representation of digital signal data."""
        return self._bytes

    @property
    def reversed_bytes(self):
        """Reverse order byte string representation of digial signal data."""
        return self._reversed_bytes

    @property
    def spectrum(self):
        """Frequency domain representation of a discrete signal."""
        return self._spectrum

    @property
    def timeseries(self):
        """Time domain sample observations."""
        return self._timeseries

    @property
    def dominant(self):
        """Largest frequency component of the signal."""
        return np.argmax(self.spectrum)

    def top_frequencies(self, n):
        """Return the largest n frequency components of a signal.

        Parameters
        ----------
        n : int
            The number of large frequencies to reteurn

        Returns
        -------
        numpy.ndarray
            An ordered list of the largest frequency components
            of the spectrum
        """
        array = np.array(self.spectrum)
        idx = np.argpartition(array, n)[-n:]
        return idx

    @property
    def size(self):
        """Size of the signal in bytes."""
        return len(self.bytes)

    @property
    def bytesPerSample(self):
        """Smallest number of bytes that can encode the largest sample.

        If the largest number must be encoded with 4 bytes, all samples
        are encoded with 4 bytes and this returns 4.
        """
        return byte_width_series(self.timeseries)

    @property
    def reversed_timeseries(self):
        """Reverse order time domain representation of a discrete signal."""
        _ts = copy.deepcopy(self.timeseries)
        _ts.reverse()
        return _ts

    def read_bytes(self, n_bytes=None, n_samples=None):
        """File-like operation to read bytes from the Signal."""
        if (not n_bytes) and (not n_samples):
            raise ValueError("Must specify one of n_bytes, n_samples")

        to_read = n_bytes
        to_read = (
            n_samples * self.bytesPerSample
            if n_samples is not None
            else to_read
        )

        return self._io_bytes.read(to_read)

    @property
    def tell(self):
        """Tell current location of read operation on bytes."""
        return self._io_bytes.tell()

    def seek(self, offset_from_start=0):
        """Change position of read operation on bytes, relative to start."""
        return self._io_bytes.seek(offset_from_start, 0)

    @property
    def timeseries_tell(self):
        """Return current position of read operation on time series domain."""
        current_byte_pos = self.tell
        return current_byte_pos // self.bytesPerSample

    @property
    def x_plot(self):
        """X dimension for plotting time domain representation."""
        return range(0, len(self.y_plot))

    @property
    def y_plot(self):
        """Y dimension for plotting time domain representation."""
        return self.timeseries

    @property
    def x_plot_spectrum(self):
        """X dimension for plotting frequency domain representation."""
        return range(0, len(self.spectrum))

    @property
    def y_plot_spectrum(self):
        """Y dimension for plotting frequency domain representation."""
        return np.abs(self.spectrum)

    def __add__(self, other):
        """Add another Signal object."""
        if not isinstance(other, Signal):
            raise ValueError("Other object must be an instance of Signal.")
        diff = len(self) - len(other)

        if diff < 0:
            shorter_signal = self
            longer_signal = other
        else:
            shorter_signal = other
            longer_signal = self

        # so we need to add (diff) number of 0's to the shorter signal
        shorter_series = copy.deepcopy(shorter_signal.timeseries)
        shorter_series.extend([0] * abs(diff))

        np_shorter = np.array(shorter_series)
        np_longer = np.array(longer_signal.timeseries)

        combined_ts = list(np_shorter + np_longer)
        return Signal.from_timeseries(combined_ts)

    def __eq__(self, other):
        """Compare timeseries value with another signal."""
        if not isinstance(other, Signal):
            raise ValueError("Must compare to Signal object.")
        return self.timeseries == other.timeseries

    def __len__(self):
        """Length of time domain representation of Signal."""
        return len(self.timeseries)

    def __getitem__(self, key):
        """Enable indexing against the Signal."""
        return self.timeseries[key]

    def append(self, other: Signal) -> Signal:
        """Append a Signal to this Signal."""
        full_series = self.timeseries
        full_series.extend(other.timeseries)
        return Signal.from_timeseries(full_series)
