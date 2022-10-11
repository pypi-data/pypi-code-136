"""Build Chords from notes."""
import functools

from harper.media import Audio, Visual
from harper.music.notes import Note


class Chord(Audio, Visual):
    """Combination of notes."""

    def __init__(self, canon, seconds=1, sampling_rate=44100, amplitude=16000):
        self._canon = canon
        self.seconds = seconds
        self.sampling_rate = sampling_rate
        self.amplitude = amplitude

        self.notes = sorted(
            [
                n(
                    seconds=self.seconds,
                    sampling_rate=self.sampling_rate,
                    amplitude=self.amplitude,
                )
                for n in self._canon
            ]
        )

        self.signal = functools.reduce(
            lambda x, y: x + y, [n.signal for n in self.notes]
        )

    def __add__(self, other):
        """Add a note or a chord to a chord."""
        if not isinstance(other, (Note, Chord)):
            raise TypeError("Can only add Notes or Chords to Chords.")

        if other.seconds != self.seconds:
            raise ValueError("Can only add Notes or Chords of equal duration.")

        if isinstance(other, Note):
            _notes = self._canon
            _notes.append(type(other))
            return Chord(_notes, self.seconds)

        if isinstance(other, Chord):
            _notes = self._canon
            _notes.extend(other._canon)
            return Chord(_notes, self.seconds)

    @property
    def timeseries(self):
        """Chord timeseries."""
        return self.signal.timeseries

    @property
    def spectrum(self):
        """Chord signal spectrum."""
        return self.signal.spectrum

    @property
    def _complex_spectrum(self):
        return self.signal._complex_spectrum

    @property
    def _complex_timeseries(self):
        return self.signal._complex_timeseries

    @property
    def bytesPerSample(self):
        """Minimum bytes to encode any sample in the timeseries."""
        return self.signal.bytesPerSample

    def read_bytes(self, n):
        """Read bytes in in file-like operation.

        Parameters
        ----------
        n: int
            Number of bytes to read.

        Returns
        -------
        bytes
            Number of desired bytes.

        """
        return self.signal.read_bytes(n)

    def seek(self, offset_from_start=0):
        """Reposition file cursor relative to file start.

        Parameters
        ----------
        offset_from_start: int
            Where to position the cursor, relative to the beginning
            of the file. Optional, defaults to 0 (file start).

        Returns
        -------
        None

        """
        return self.signal.seek(offset_from_start=offset_from_start)

    @property
    def y_plot(self):
        """Y dimension for plotting time domain representation."""
        return self.signal.y_plot

    @property
    def x_plot(self):
        """X dimension for plotting time domain representation."""
        return self.signal.x_plot

    @property
    def x_plot_spectrum(self):
        """X dimension for plotting frequency domain representation."""
        return self.signal.x_plot_spectrum

    @property
    def y_plot_spectrum(self):
        """Y dimension for plotting frequency domain representation."""
        return self.signal.y_plot_spectrum

    def __len__(self):
        """Length of time domain representation of Signal."""
        return len(self.canon)

    def __getitem__(self, key):
        """Get item from notes."""
        return self.notes[0]
