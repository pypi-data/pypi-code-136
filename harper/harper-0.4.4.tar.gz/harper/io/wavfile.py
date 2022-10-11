"""Handy wavfile handiness. Additional handling handled as well."""
import io

from harper.audio.windows import sliding
from harper.bops import IO, BIG_ENDIAN, LITTLE_ENDIAN
from harper.exceptions import InvalidWaveFileError
from harper.audio.signal import Signal
from harper.media import Audio, Visual


def _get_endian(wav_byte_array):
    """Check the first four bytes of the wav file to discover endianess."""
    if wav_byte_array[0:4] == b"RIFX":
        return BIG_ENDIAN
    elif wav_byte_array[0:4] == b"RIFF":
        return LITTLE_ENDIAN
    else:
        raise InvalidWaveFileError("First four bytes of file invalid.")


class WavFile(Audio, Visual):
    """Wavfile file loading and structuring."""

    _header_length = 44

    def __init__(self, path):
        """Create a WavFile object from a path on disk.

        Parameters
        ----------
        path: str
            The path to the wavfile

        Returns
        -------
        harper.WavFile
            WavFile object

        """
        self.path = path
        with open(self.path, "rb") as f:
            self._bytes = f.read()

        self._endian = _get_endian(self._bytes)
        self._io = IO(self._endian)

        self._header = _WavHeader(
            self._bytes[0 : self._header_length],  # noqa: E203
            self._endian,
            self,
        )
        self.filesize = self._header.filesize
        self.numChannels = self._header.numChannels
        self.sampleRate = self._header.sampleRate

        self.numSamples = self._header.numberSamples
        self.frameRate = self._header.frameRate
        self.dataRate = self._header.dataRate
        self.bytesPerFrame = self._header.bytesPerFrame
        self.sizeOfData = self._header.sizeOfData

        self._data = _WavData(
            self._bytes[self._header_length :],  # noqa: E203
            self.bytesPerSample,
            self.numChannels,
            self,
        )

        self.interleaved = self._data.interleaved
        self.channels = self._data.channels
        self.signals = [Signal.from_timeseries(c) for c in self.channels]

        self._io_bytes = io.BytesIO(self.interleaved)

    @property
    def size(self):
        """Size in bytes of WavFile data component."""
        return self.sizeOfData

    @property
    def bytesPerSample(self):
        """Minimum bytes required to encode any sample from data."""
        return self._header.bytesPerSample

    def read_bytes(self, n_bytes):
        """Return bytes in file-like fashion from the sample data.

        Parameters
        ----------
        n_bytes: int
            The numbe of bytes to return

        Returns
        -------
        bytes
            The number of bytes requested.

        """
        return self._io_bytes.read(n_bytes)

    def seek(self, offset_from_start=0):
        """Change position of current file read.

        Parameters
        ----------
        offset_from_start: int
            The position of the file read pointer, starting from
            the start of the file, to move to.

        Returns
        -------
        None

        """
        return self._io_bytes.seek(offset_from_start)

    @property
    def tell(self):
        """Return the current position of the file read pointer."""
        return self._io_bytes.tell()

    def read(self, n_bytes=None, n_frames=None, n_samples=None):
        """Read a given number of bytes from the data bytes.

        Accepts a broader array of parameters than just WavFile.read_bytes,
        as one can specify a number of samples or frames to read.

        Parameters
        ----------
        n_bytes: int
            Number of bytes to read. Optional, defaults to None
        n_frames: int
            Number of frames to read. Optional, defaults to None
        n_samples: int
            Number of samples to read. Optional, defaults to None

        Returns
        -------
        bytes
            The specified number of bytes.
        """
        to_read = n_bytes
        to_read = (
            n_frames * self.bytesPerFrame if n_frames is not None else to_read
        )
        to_read = (
            n_samples * self.bytesPerSample
            if n_samples is not None
            else to_read
        )

        return self.read_bytes(to_read)

    @property
    def y_plot(self):
        """Plottable range information on the time dimension."""
        # TODO: make a timeseries esque thing for wavfile
        return self._bytes

    @property
    def x_plot(self):
        """Plottable domain information on the time dimension."""
        return range(0, len(self.y_plot))


class _WavHeader(object):
    def __init__(self, header_byte_array, endian_sym, wavfile: WavFile):

        self._io = wavfile._io

        self._endian_sym = wavfile._endian
        self.riff = self._io.c_str(header_byte_array[0:4])
        self.filesize = self._io.c_int(header_byte_array[4:8])
        self.fileType = self._io.c_str(header_byte_array[8:12])
        self.formatChunkMarker = self._io.c_str(header_byte_array[12:16])
        self.lengthOfFormatData = self._io.c_int(header_byte_array[16:20])
        self.formatType = self._io.c_short(header_byte_array[20:22])
        self.numChannels = self._io.c_short(header_byte_array[22:24])
        self.sampleRate = self._io.c_int(header_byte_array[24:28])
        self.dataRate = self._io.c_int(
            header_byte_array[28:32]
        )  # bytes of data per second. Hz.

        # TODO: i dont think these are right.
        self.bytesPerSample = self._io.c_short(header_byte_array[32:34])
        self.bitsPerSample = self._io.c_short(header_byte_array[34:36])
        self.dataMarker = self._io.c_str(header_byte_array[36:40])
        self.sizeOfData = self._io.c_int(header_byte_array[40:44])
        self.numberSamples = self.sizeOfData / self.bytesPerSample
        self.bytesPerFrame = self.bytesPerSample * self.numChannels
        self.numberFrames = self.sizeOfData / self.bytesPerFrame
        self.frameRate = int(self.sampleRate / self.numChannels)
        self.dataRate2 = self.frameRate * self.bytesPerFrame


class _WavData(object):
    def __init__(self, dataByteArray, bytesPerSample, numChannels, wavfile):

        # lets have a working assumption that if we have more than
        # one channel, they will always be of the same length.

        self.interleaved = dataByteArray
        self._bytesPerSample = bytesPerSample
        self._wavfile = wavfile
        self._numChannels = numChannels

        self._byte_channels = list()
        windows = sliding(
            self.interleaved, size=bytesPerSample, stride=bytesPerSample
        )
        self._byte_channels = [
            windows[0 + c :: 2] for c in range(self._numChannels)  # noqa: E203
        ]

        self.channels = list()
        for channel in self._byte_channels:
            procd = list()
            for chunk in channel:
                # if chunk == b"":
                #     continue
                #     # chunk = b'\x00' * self._bytesPerSample
                processed = self._byteConversion(chunk)
                procd.append(processed)
            self.channels.append(procd)

    # this is uneccessary. since the byte_channels are
    # already broken into groupings of correctly sized bytes,
    # you could just use int.from_bytes(x, byteorder) and
    # convert like that.
    @property
    def _byteConversion(self):
        if self._bytesPerSample == 2:
            return self._wavfile._io.c_short
        elif self._bytesPerSample == 4:
            return self._wavfile._io.c_int
        elif self._bytesPerSample == 8:
            return self._wavfile._io.c_long
        else:
            raise InvalidWaveFileError("wtf")


def to_wavfile(
    signal, outfile, sample_rate=44100, channels=1, endian="little"
):
    """Save a Signal to disk as a wavfile.

    Parameters
    ----------
    signal : harper.Signal
        The Signal to save to disk.
    outfile : str
        The path to save the Signal to.
    sample_rate : int
        Sample rate of wavfile. Defaults to 44100
    channels: int
        Number of channels encoded by wavfile. Defaults to 1
    endian: str
        Can be 'little' or 'big'. Defaults to 'little'.

    Returns
    -------
    None

    """
    minimum_bytes = signal.bytesPerSample
    dataSize = signal.size

    def _create_header_bytes(
        minimum_bytes, data_size, sample_rate, channels, endian="little"
    ):
        riff = b"RIFF" if endian == "little" else b"RIFX"  # 0:4
        filesize = int.to_bytes((data_size + 44), 4, endian)  # 0 :8
        fileType = b"WAVE"
        formatChunkMarker = b"fmt "

        # TODO: i made this up.
        lengthOfFormatData = int.to_bytes(16, 4, endian)
        formatType = int.to_bytes(8, 2, endian)
        numChannels = int.to_bytes(channels, 2, endian)
        sampleRate = int.to_bytes(sample_rate, 4, endian)
        dataRate = int.to_bytes(minimum_bytes * sample_rate, 4, endian)
        bytesPerSample = int.to_bytes(minimum_bytes, 2, endian)
        bitsPerSample = int.to_bytes(minimum_bytes * 8, 2, endian)
        dataMarker = b"data"
        sizeofData = int.to_bytes(data_size, 4, endian)

        return (
            b""
            + riff
            + filesize
            + fileType
            + formatChunkMarker
            + lengthOfFormatData
            + formatType
            + numChannels
            + sampleRate
            + dataRate
            + bytesPerSample
            + bitsPerSample
            + dataMarker
            + sizeofData
        )

    def _create_data_bytes(signal):
        return signal.bytes

    header_bytes = _create_header_bytes(
        minimum_bytes, dataSize, sample_rate, channels, endian
    )
    data_bytes = _create_data_bytes(signal)
    all_bytes = b"" + header_bytes + data_bytes
    with open(outfile, "wb") as f:
        f.write(all_bytes)
