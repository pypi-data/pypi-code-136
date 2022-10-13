# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Core classes and functions for the quicksong library """
from typing import Sequence, Optional, Iterator, Tuple, Iterable, Union, Callable
import logging
import numpy as np

from .streaming import StreamingTransform

log = logging.getLogger("quicksong")
numeric = Union[int, float, np.number]
SpectrogramFeature = Callable[[np.ndarray], float]


def make_training_dataset(features, intervals, dt):
    """For each interval in intervals, extract the corresponding frames from features

    features - (t,k) array of features
    labels   - structured numpy array with fields "id", "start", and "stop"
    dt       - frame duration in the features array (same units as labels)

    Returns X (features array), y (labels)
    """
    out_feats = []
    out_labels = []
    for interval in intervals:
        id = interval["id"]
        frames = slice(int(interval["start"] / dt), int(interval["stop"] / dt))
        feats = features[frames, :]
        labels = np.ones(feats.shape[0], dtype="i") * id
        out_feats.append(feats)
        out_labels.append(labels)
    return np.row_stack(out_feats), np.concatenate(out_labels)


class FeatureExtractor:
    """Extracts features from acoustic signals.

    This class is basically glue for the streaming transformers that convert the
    input signal into a spectrogram and convolve the spectrogram features.
    Unlike these transformers, it is able to handle arbitrary-sized inputs.

    """

    def __init__(
        self,
        signal_transformer: StreamingTransform,
        features: Sequence[SpectrogramFeature],
        convolver: StreamingTransform,
    ):
        from copy import copy

        self.signal_t = signal_transformer
        self.frame_size = signal_transformer.block_size
        self.feature_t = features
        self.block_size = convolver.block_size
        self.convolvers = tuple(copy(convolver) for f in features)
        self.reset()

    def _calculate_features(self, frame: np.ndarray):
        stft = self.signal_t.process(frame)
        features = tuple(feat(stft) for feat in self.feature_t)
        self.feat_buf.append(features)
        self.feat_count += 1

    def reset(self):
        """Reset the signal and feature buffers"""
        from collections import deque

        self.signal_buf = np.zeros(self.signal_t.block_size)
        self.signal_buf_ptr = 0
        self.feat_buf = deque()
        self.feat_count = 0
        self.feat_prefilled = False

    def process(self, signal: np.ndarray):
        # calculate the spectrogram frames first and then store features.
        signal_ptr = 0
        if self.signal_buf_ptr > 0:
            needed = self.frame_size - self.signal_buf_ptr
            log.debug("filling incomplete frame with %ds samples", needed)
            self.signal_buf[self.signal_buf_ptr :] = signal[:needed]
            signal_ptr += needed
            self._calculate_features(self.signal_buf)
            self.signal_buf_ptr = 0
        for f, i in enumerate(range(signal_ptr, signal.size, self.frame_size)):
            s = signal[i : i + self.frame_size]
            log.debug("frame %d: sample %d, %d samples", f, i, s.size)
            if s.size == self.frame_size:
                self._calculate_features(s)
            else:
                # partial fill
                self.signal_buf[: s.size] = s
                self.signal_buf[s.size :] = 0
                self.signal_buf_ptr = s.size
        # process the feature buffer
        log.debug("processing feature buffer in blocks of %d frames", self.block_size)
        while self.feat_count > self.block_size:
            log.debug("buffer contains %d frames", self.feat_count)
            features = zip(*(self.feat_buf.popleft() for i in range(self.block_size)))
            self.feat_count -= self.block_size
            if not self.feat_prefilled:
                log.debug(" - prefilling the convolver")
                for feature, conv in zip(features, self.convolvers):
                    conv.prefill(np.asarray(feature))
                self.feat_prefilled = True
            else:
                log.debug(" - convolving")
                results = []
                for feature, conv in zip(features, self.convolvers):
                    results.append(conv.process(np.asarray(feature)))
                yield np.column_stack(results)

    def close(self) -> np.ndarray:
        """Process any remaining samples and return result"""
        if self.signal_buf_ptr > 0:
            log.debug("processing last frame with %d samples", self.signal_buf_ptr)
            self._calculate_features(self.signal_buf[: self.signal_buf_ptr])
        log.debug("feature buffer contains %d frames", self.feat_count)
        if self.feat_count > self.block_size:
            log.error(
                "warning: closing feature extractor with more than one block left, some samples may be lost"
            )
        nframes = min(self.block_size, self.feat_count)
        features = zip(*(self.feat_buf.popleft() for i in range(nframes)))
        results = []
        for feature, conv in zip(features, self.convolvers):
            results.append(
                np.row_stack((conv.process(np.asarray(feature)), conv.close()))
            )
        self.reset()
        return np.column_stack(results)

    def process_all(self, signal: np.ndarray) -> np.ndarray:
        """Process an entire signal and then close the extractor"""
        out = []
        for block in self.process(signal):
            out.append(block)
        out.append(self.close())
        return np.row_stack(out)


class IntervalFinder:
    """Finds runs in a binary vector meeting duration criteria"""

    frame: int
    interval_start: Optional[int]
    interval_end: Optional[int]

    def __init__(self, max_gap: float, min_duration: float, dt: float):
        self.max_gap = int(max_gap / dt)
        self.min_duration = int(min_duration / dt)
        self.reset()

    def reset(self) -> None:
        self.frame = 0
        self.interval_start = None
        self.interval_end = None

    def process(self, frames: np.ndarray) -> Iterator[Tuple[int, int]]:
        """Find intervals of zeros in a binary vector, yielded as (start, stop) tuples"""
        for p in frames:
            if not p:
                if self.interval_start is None:
                    logging.debug("ON: %d", self.frame)
                    self.interval_start = self.frame
                self.interval_end = self.frame
            elif self.interval_end is None:
                pass
            elif self.frame - self.interval_end < self.max_gap:
                logging.debug("GAP: %d-%d", self.interval_end, self.frame)
                pass
            else:
                logging.debug(
                    "OFF: %d (duration=%d)",
                    self.interval_end,
                    self.interval_end - self.interval_start,
                )
                if self.interval_end - self.interval_start > self.min_duration:
                    yield (self.interval_start, self.interval_end)
                self.interval_end = self.interval_start = None
            self.frame += 1


def make_hanning_kernels(widths: Sequence[float]) -> np.ndarray:
    """Create an array of hanning kernels of specified widths. All the kernels
    are aligned such that tau=0 is in the center"""
    nk = len(widths)
    nt = max(widths)
    ht = nt // 2
    kernels = np.zeros((nt, nk))
    for i, ws in enumerate(widths):
        offset = ht - ws // 2
        w = np.hanning(ws)
        kernels[offset : offset + ws, i] = w / np.sum(w**2)
    return kernels


def pad_intervals(
    intervals: Iterable[Tuple[numeric, numeric]],
    pad_before: numeric,
    pad_after: numeric,
) -> Iterator[Tuple[numeric, numeric]]:
    it = ((s - pad_before, e + pad_after) for s, e in intervals)
    start, end = next(it)
    for s, e in it:
        if s <= end:
            end = e
        else:
            yield (start, end)
            start, end = s, e
    yield (start, end)
