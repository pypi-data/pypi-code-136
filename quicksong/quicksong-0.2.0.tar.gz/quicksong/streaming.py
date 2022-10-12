# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Module for doing streaming conversions """
from typing import Sequence
from abc import ABC, abstractmethod
import logging
import numpy as np

log = logging.getLogger("quicksong")


class StreamingTransform(ABC):
    """Abstract base class for streaming transforms"""

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def prefill(self, samples: np.ndarray) -> None:
        raise NotImplementedError

    @abstractmethod
    def process(self, block: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class OverlapSaveConvolver(StreamingTransform):
    """Computes running convolution using the overlap-save method.

    This class is initialized with one or more convolution kernels. The signal
    to be convolved is then passed to the intialized object in blocks through
    the conv() method.

    This class assumes that the kernels are acausal, with tau=0 at the center.
    The block size is set to half the size of the largest kernel. In order for
    the convolution to be aligned with the time base of the input, the first
    block needs to be discarded and a block of zeros needs to be processed at
    the end. The prefill() and close() methods are provided for convenience.

    kernel:     the convolution kernel(s). For a single kernel, this is a 1-D array. For
                multiple kernels, this should be a (ntau, nkernel) 2-D array

    """

    block_size: int
    ntau: int
    nkernels: int
    nfft: int
    kernels: np.ndarray
    buffer: np.ndarray

    def __init__(self, kernel: np.ndarray):
        from math import ceil, log

        if kernel.ndim == 1:
            self.ntau = kernel.size
            self.nkernels = 1
        elif kernel.ndim == 2:
            self.ntau, self.nkernels = kernel.shape
        else:
            raise ValueError("Kernel input must be 1d or 2d")
        self.block_size = self.ntau // 2
        self.nfft = 2 ** ceil(log(self.block_size + self.ntau, 2))
        self.kernels = np.fft.rfft(kernel, n=self.nfft, axis=0)
        self.reset()

    def __copy__(self):
        """Clones the convolver with the same kernels and an empty buffer"""
        cls = self.__class__
        result = cls.__new__(cls)
        for attr in ("ntau", "nkernels", "block_size", "nfft"):
            result.__dict__[attr] = self.__dict__[attr]
        result.kernels = self.kernels
        result.reset()
        return result

    def reset(self) -> None:
        self.buffer = np.zeros(self.nfft)

    def prefill(self, signal: np.ndarray) -> None:
        """Prefill the buffer"""
        self.buffer[-signal.size:] = signal

    def process(self, block: np.ndarray) -> np.ndarray:
        """Process a block of samples. Check block_size property. Incomplete
        blocks are padded with zeros."""
        if block.ndim != 1:
            raise IncompatibleBlockSize("Input signal must be 1-D")
        elif block.size > self.block_size:
            raise IncompatibleBlockSize(
                f"Block size is too large (max {self.block_size}"
            )
        # shift the buffer and add the block to the end
        # self.buffer = np.roll(self.buffer, -self.block_size)
        self.buffer[: -block.size] = self.buffer[block.size:]
        self.buffer[-block.size:] = block
        S = np.fft.rfft(self.buffer, n=self.nfft)
        C = self.kernels * S[:, np.newaxis]
        c = np.fft.irfft(C, n=self.nfft, axis=0)
        return c[-block.size:]

    def close(self):
        """End the convolution by processing a block of zeros """
        return self.process(np.zeros(self.block_size))


class STFT(StreamingTransform):
    """Compute a running short-time fourier transform."""

    nfft: int
    window: np.ndarray
    block_size: int
    buffer: np.ndarray

    def __init__(
        self,
        sampling_rate: float,
        window: float,
        shift: float,
        frequency_range: Sequence[float],
    ):
        import libtfr
        from math import ceil, log

        window_samples = int(window * sampling_rate)
        self.nfft = 2 ** ceil(log(window_samples, 2))
        self.block_size = int(shift * sampling_rate)
        self.mfft = libtfr.mfft_precalc(self.nfft, np.hanning(window_samples))
        df = sampling_rate / self.nfft
        f = np.arange(0, sampling_rate, df)
        f1, f2 = frequency_range
        self.findx = ((f >= f1) & (f < f2)).nonzero()[0]
        self.reset()

    @property
    def prefill_size(self) -> int:
        """Recommended prefill size"""
        return self.nfft - self.block_size

    def reset(self) -> None:
        self.buffer = np.zeros(self.nfft)

    def prefill(self, signal: np.ndarray) -> None:
        """Prefill the buffer"""
        self.buffer[-signal.size :] = signal

    def process(self, block: np.ndarray) -> np.ndarray:
        if block.ndim != 1:
            raise IncompatibleBlockSize("Input signal must be 1-D")
        elif block.size < self.block_size:
            block = np.pad(block, (0, self.block_size - block.size), "constant", constant_values=0)
        elif block.size > self.block_size:
            raise IncompatibleBlockSize(
                f"Block size does not match spectrogram shift ({self.block_size})"
            )
        # shift the buffer and add the next frame to the end
        self.buffer[: -self.block_size] = self.buffer[self.block_size :]
        self.buffer[-self.block_size :] = block
        return self.mfft.mtfft(self.buffer)[self.findx, 0]


class IncompatibleBlockSize(ValueError):
    """Raised when data provided to convolver is not the right size or shape"""

    pass
