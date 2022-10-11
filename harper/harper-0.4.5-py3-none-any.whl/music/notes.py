"""Canonical note-frequency classes."""
import abc
import sys
import inspect

from harper.media import Audio, Visual
from harper.synthesis import (
    generate_sine_sample,
    generate_sawtooth_sample,
    generate_square_sample,
)
from harper.audio.signal import Signal


class Note(Audio, Visual, metaclass=abc.ABCMeta):
    """Abstract base class for musical notes."""

    frequency = ValueError("Overwrite me.")

    def __init__(
        self, seconds=1, sampling_rate=44100, amplitude=16000, waveform="sine"
    ):
        """Create a musical note of the given duration.

        Parameters
        ----------
        seconds: float
            Duration for which to generate samples. Optional, defaults to 1.
        sampling_rate: int
            Number of samples to generate per second. Optional,
            defaults to 44100.
        amplitude: int
            Magnitude by which generated trignometric values will
            be multiplied. Represents the largest absolute value
            which the timeseries will have. Optional, defaults
            to 16,000 (fits into 2 bytes).

        Returns
        -------
        harper.music.notes.Note

        """
        self.seconds = seconds
        self.sampling_rate = sampling_rate
        self._waveform = waveform
        self.amplitude = amplitude
        self.signal = Signal.from_timeseries(self._create_timeseries())

    @property
    def _n_samples(self):
        return int(round(self.seconds * self.sampling_rate))

    def _create_timeseries(self):
        if self._waveform == "sine":
            f = generate_sine_sample
        elif self._waveform == "sawtooth":
            f = generate_sawtooth_sample
        elif self._waveform == "square":
            f = generate_square_sample
        return [
            int(
                f(
                    x,
                    self.frequency,
                    amplitude=self.amplitude,
                    sampling_rate=self.sampling_rate,
                )
            )
            for x in range(self._n_samples)
        ]

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

    @classmethod
    def __gt__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency > other.frequency

    @classmethod
    def __ge__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency >= other.frequency

    @classmethod
    def __hash__(cls):
        """Hash based on frequency."""
        return hash(cls.frequency)

    @classmethod
    def __lt__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency < other.frequency

    @classmethod
    def __le__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency <= other.frequency

    @classmethod
    def __eq__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency == other.frequency

    @classmethod
    def __ne__(cls, other):
        """Compare frequencies to create rich comparisons."""
        return cls.frequency != other.frequency


class C0(Note):
    """A C0 note."""

    frequency = 16.35


class CSHARP0(Note):
    """A CSHARP0 note."""

    frequency = 17.32


class DFLAT0(Note):
    """A DFLAT0 note."""

    frequency = 17.32


class D0(Note):
    """A D0 note."""

    frequency = 18.35


class DSHARP0(Note):
    """A DSHARP0 note."""

    frequency = 19.45


class EFLAT0(Note):
    """A EFLAT0 note."""

    frequency = 19.45


class E0(Note):
    """A E0 note."""

    frequency = 20.60


class F0(Note):
    """A F0 note."""

    frequency = 21.83


class FSHARP0(Note):
    """A FSHARP0 note."""

    frequency = 23.12


class GFLAT0(Note):
    """A GFLAT0 note."""

    frequency = 23.12


class G0(Note):
    """A G0 note."""

    frequency = 24.50


class GSHARP0(Note):
    """A GSHARP0 note."""

    frequency = 25.96


class AFLAT0(Note):
    """A AFLAT0 note."""

    frequency = 25.96


class A0(Note):
    """A A0 note."""

    frequency = 27.50


class ASHARP0(Note):
    """A ASHARP0 note."""

    frequency = 29.14


class BFLAT0(Note):
    """A BFLAT0 note."""

    frequency = 29.14


class B0(Note):
    """A B0 note."""

    frequency = 30.87


class C1(Note):
    """A C1 note."""

    frequency = 32.70


class CSHARP1(Note):
    """A CSHARP1 note."""

    frequency = 34.65


class DFLAT1(Note):
    """A DFLAT1 note."""

    frequency = 34.65


class D1(Note):
    """A D1 note."""

    frequency = 36.71


class DSHARP1(Note):
    """A DSHARP1 note."""

    frequency = 38.89


class EFLAT1(Note):
    """A EFLAT1 note."""

    frequency = 38.89


class E1(Note):
    """A E1 note."""

    frequency = 41.20


class F1(Note):
    """A F1 note."""

    frequency = 43.65


class FSHARP1(Note):
    """A FSHARP1 note."""

    frequency = 46.25


class GFLAT1(Note):
    """A GFLAT1 note."""

    frequency = 46.25


class G1(Note):
    """A G1 note."""

    frequency = 49.00


class GSHARP1(Note):
    """A GSHARP1 note."""

    frequency = 51.91


class AFLAT1(Note):
    """A AFLAT1 note."""

    frequency = 51.91


class A1(Note):
    """A A1 note."""

    frequency = 55.00


class ASHARP1(Note):
    """A ASHARP1 note."""

    frequency = 58.27


class BFLAT1(Note):
    """A BFLAT1 note."""

    frequency = 58.27


class B1(Note):
    """A B1 note."""

    frequency = 61.74


class C2(Note):
    """A C2 note."""

    frequency = 65.41


class CSHARP2(Note):
    """A CSHARP2 note."""

    frequency = 69.30


class DFLAT2(Note):
    """A DFLAT2 note."""

    frequency = 69.30


class D2(Note):
    """A D2 note."""

    frequency = 73.42


class DSHARP2(Note):
    """A DSHARP2 note."""

    frequency = 77.78


class EFLAT2(Note):
    """A EFLAT2 note."""

    frequency = 77.78


class E2(Note):
    """A E2 note."""

    frequency = 82.41


class F2(Note):
    """A F2 note."""

    frequency = 87.31


class FSHARP2(Note):
    """A FSHARP2 note."""

    frequency = 92.50


class GFLAT2(Note):
    """A GFLAT2 note."""

    frequency = 92.50


class G2(Note):
    """A G2 note."""

    frequency = 98.00


class GSHARP2(Note):
    """A GSHARP2 note."""

    frequency = 103.83


class AFLAT2(Note):
    """A AFLAT2 note."""

    frequency = 103.83


class A2(Note):
    """A A2 note."""

    frequency = 110.00


class ASHARP2(Note):
    """A ASHARP2 note."""

    frequency = 116.54


class BFLAT2(Note):
    """A BFLAT2 note."""

    frequency = 116.54


class B2(Note):
    """A B2 note."""

    frequency = 123.47


class C3(Note):
    """A C3 note."""

    frequency = 130.81


class CSHARP3(Note):
    """A CSHARP3 note."""

    frequency = 138.59


class DFLAT3(Note):
    """A DFLAT3 note."""

    frequency = 138.59


class D3(Note):
    """A D3 note."""

    frequency = 146.83


class DSHARP3(Note):
    """A DSHARP3 note."""

    frequency = 155.56


class EFLAT3(Note):
    """A EFLAT3 note."""

    frequency = 155.56


class E3(Note):
    """A E3 note."""

    frequency = 164.81


class F3(Note):
    """A F3 note."""

    frequency = 174.61


class FSHARP3(Note):
    """A FSHARP3 note."""

    frequency = 185.00


class GFLAT3(Note):
    """A GFLAT3 note."""

    frequency = 185.00


class G3(Note):
    """A G3 note."""

    frequency = 196.00


class GSHARP3(Note):
    """A GSHARP3 note."""

    frequency = 207.65


class AFLAT3(Note):
    """A AFLAT3 note."""

    frequency = 207.65


class A3(Note):
    """A A3 note."""

    frequency = 220.00


class ASHARP3(Note):
    """A ASHARP3 note."""

    frequency = 233.08


class BFLAT3(Note):
    """A BFLAT3 note."""

    frequency = 233.08


class B3(Note):
    """A B3 note."""

    frequency = 246.94


class C4(Note):
    """A C4 note."""

    frequency = 261.63


class CSHARP4(Note):
    """A CSHARP4 note."""

    frequency = 277.18


class DFLAT4(Note):
    """A DFLAT4 note."""

    frequency = 277.18


class D4(Note):
    """A D4 note."""

    frequency = 293.66


class DSHARP4(Note):
    """A DSHARP4 note."""

    frequency = 311.13


class EFLAT4(Note):
    """A EFLAT4 note."""

    frequency = 311.13


class E4(Note):
    """A E4 note."""

    frequency = 329.63


class F4(Note):
    """A F4 note."""

    frequency = 349.23


class FSHARP4(Note):
    """A FSHARP4 note."""

    frequency = 369.99


class GFLAT4(Note):
    """A GFLAT4 note."""

    frequency = 369.99


class G4(Note):
    """A G4 note."""

    frequency = 392.00


class GSHARP4(Note):
    """A GSHARP4 note."""

    frequency = 415.30


class AFLAT4(Note):
    """A AFLAT4 note."""

    frequency = 415.30


class A4(Note):
    """A A4 note."""

    frequency = 440.00


class ASHARP4(Note):
    """A ASHARP4 note."""

    frequency = 466.16


class BFLAT4(Note):
    """A BFLAT4 note."""

    frequency = 466.16


class B4(Note):
    """A B4 note."""

    frequency = 493.88


class C5(Note):
    """A C5 note."""

    frequency = 523.25


class CSHARP5(Note):
    """A CSHARP5 note."""

    frequency = 554.37


class DFLAT5(Note):
    """A DFLAT5 note."""

    frequency = 554.37


class D5(Note):
    """A D5 note."""

    frequency = 587.33


class DSHARP5(Note):
    """A DSHARP5 note."""

    frequency = 622.25


class EFLAT5(Note):
    """A EFLAT5 note."""

    frequency = 622.25


class E5(Note):
    """A E5 note."""

    frequency = 659.25


class F5(Note):
    """A F5 note."""

    frequency = 698.46


class FSHARP5(Note):
    """A FSHARP5 note."""

    frequency = 739.99


class GFLAT5(Note):
    """A GFLAT5 note."""

    frequency = 739.99


class G5(Note):
    """A G5 note."""

    frequency = 783.99


class GSHARP5(Note):
    """A GSHARP5 note."""

    frequency = 830.61


class AFLAT5(Note):
    """A AFLAT5 note."""

    frequency = 830.61


class A5(Note):
    """A A5 note."""

    frequency = 880.00


class ASHARP5(Note):
    """A ASHARP5 note."""

    frequency = 932.33


class BFLAT5(Note):
    """A BFLAT5 note."""

    frequency = 932.33


class B5(Note):
    """A B5 note."""

    frequency = 987.77


class C6(Note):
    """A C6 note."""

    frequency = 1046.50


class CSHARP6(Note):
    """A CSHARP6 note."""

    frequency = 1108.73


class DFLAT6(Note):
    """A DFLAT6 note."""

    frequency = 1108.73


class D6(Note):
    """A D6 note."""

    frequency = 1174.66


class DSHARP6(Note):
    """A DSHARP6 note."""

    frequency = 1244.51


class EFLAT6(Note):
    """A EFLAT6 note."""

    frequency = 1244.51


class E6(Note):
    """A E6 note."""

    frequency = 1318.51


class F6(Note):
    """A F6 note."""

    frequency = 1396.91


class FSHARP6(Note):
    """A FSHARP6 note."""

    frequency = 1479.98


class GFLAT6(Note):
    """A GFLAT6 note."""

    frequency = 1479.98


class G6(Note):
    """A G6 note."""

    frequency = 1567.98


class GSHARP6(Note):
    """A GSHARP6 note."""

    frequency = 1661.22


class AFLAT6(Note):
    """A AFLAT6 note."""

    frequency = 1661.22


class A6(Note):
    """A A6 note."""

    frequency = 1760.00


class ASHARP6(Note):
    """A ASHARP6 note."""

    frequency = 1864.66


class BFLAT6(Note):
    """A BFLAT6 note."""

    frequency = 1864.66


class B6(Note):
    """A B6 note."""

    frequency = 1975.53


class C7(Note):
    """A C7 note."""

    frequency = 2093.00


class CSHARP7(Note):
    """A CSHARP7 note."""

    frequency = 2217.46


class DFLAT7(Note):
    """A DFLAT7 note."""

    frequency = 2217.46


class D7(Note):
    """A D7 note."""

    frequency = 2349.32


class DSHARP7(Note):
    """A DSHARP7 note."""

    frequency = 2489.02


class EFLAT7(Note):
    """A EFLAT7 note."""

    frequency = 2489.02


class E7(Note):
    """A E7 note."""

    frequency = 2637.02


class F7(Note):
    """A F7 note."""

    frequency = 2793.83


class FSHARP7(Note):
    """A FSHARP7 note."""

    frequency = 2959.96


class GFLAT7(Note):
    """A GFLAT7 note."""

    frequency = 2959.96


class G7(Note):
    """A G7 note."""

    frequency = 3135.96


class GSHARP7(Note):
    """A GSHARP7 note."""

    frequency = 3322.44


class AFLAT7(Note):
    """A AFLAT7 note."""

    frequency = 3322.44


class A7(Note):
    """A A7 note."""

    frequency = 3520.00


class ASHARP7(Note):
    """A ASHARP7 note."""

    frequency = 3729.31


class BFLAT7(Note):
    """A BFLAT7 note."""

    frequency = 3729.31


class B7(Note):
    """A B7 note."""

    frequency = 3951.07


class C8(Note):
    """A C8 note."""

    frequency = 4186.01


class CSHARP8(Note):
    """A CSHARP8 note."""

    frequency = 4434.92


class DFLAT8(Note):
    """A DFLAT8 note."""

    frequency = 4434.92


class D8(Note):
    """A D8 note."""

    frequency = 4698.63


class DSHARP8(Note):
    """A DSHARP8 note."""

    frequency = 4978.03


class EFLAT8(Note):
    """A EFLAT8 note."""

    frequency = 4978.03


class E8(Note):
    """A E8 note."""

    frequency = 5274.04


class F8(Note):
    """A F8 note."""

    frequency = 5587.65


class FSHARP8(Note):
    """A FSHARP8 note."""

    frequency = 5919.91


class GFLAT8(Note):
    """A GFLAT8 note."""

    frequency = 5919.91


class G8(Note):
    """A G8 note."""

    frequency = 6271.93


class GSHARP8(Note):
    """A GSHARP8 note."""

    frequency = 6644.88


class AFLAT8(Note):
    """A AFLAT8 note."""

    frequency = 6644.88


class A8(Note):
    """A A8 note."""

    frequency = 7040.00


class ASHARP8(Note):
    """A ASHARP8 note."""

    frequency = 7458.62


class BFLAT8(Note):
    """A BFLAT8 note."""

    frequency = 7458.62


class B8(Note):
    """A B8 note."""

    frequency = 7902.13


class _Notes:
    """Private container class to implement intervals, mostly."""

    _notes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    _notes = [x[1] for x in _notes]
    _notes.remove(Note)
    _notes.remove(Audio)
    _notes.remove(Visual)
    _notes.remove(Signal)
    _notes = [n(seconds=0.01) for n in _notes]
    _notes = list(set(_notes))
    _notes = sorted(_notes, key=lambda x: x.frequency)
    _notes = list(type(n) for n in _notes)

    @classmethod
    def index(cls, item):
        """Return index from notes collection for a given note."""
        return cls._notes.index(item)

    @classmethod
    def __len__(cls):
        """Length of time domain representation of Signal."""
        return len(cls._notes)

    @classmethod
    def __getitem__(cls, key):
        """Enable indexing against the Signal."""
        return cls._notes[key]


def add_interval(note, steps):
    """Add an interval to a note.

    Parameters
    ----------
    note: harper.music.note.Note
        Note to add an interval to
    steps: int
        Steps to add. Denoted in half-steps, so 1 is a half-step and 2
        is a whole step.

    Returns
    -------
    harper.music.note.Note
        Resulting note

    """
    n = _Notes()

    current_idx = n.index(type(note))
    result_idx = current_idx + steps
    resulting_note = n[result_idx]
    return resulting_note(
        seconds=note.seconds,
        sampling_rate=note.sampling_rate,
        amplitude=note.amplitude,
        waveform=note._waveform,
    )
