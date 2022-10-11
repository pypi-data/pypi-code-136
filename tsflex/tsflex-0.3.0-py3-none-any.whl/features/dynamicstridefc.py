# wrapper voor rond FC
# wrapt de calculate...
# maar moet enkel voor de train split werken..
# dus custom cross validatieloop schrijven?

import numpy as np
import pandas as pd

from .feature_collection import FeatureCollection
from .function_wrapper import FuncWrapper
from .segmenter.strided_rolling import StridedRolling
from ..utils.data import flatten

from sklearn.base import TransformerMixin
from typing import Union, List, Tuple, Any

class DynamicStrideFC_v0(FeatureCollection, TransformerMixin):

    def _get_stroll(self, kwargs):
        assert kwargs["segment_start_idxs"] is None
        assert kwargs["strides"] is not None
        min_stride = min(kwargs["strides"])
        window = kwargs["window"]
        # TODO: this should not be implemented here...
        # TODO: this should not focus on only the first series in the series list
        segment_start_idxs = []
        max_label_pct = max(self._label_dist.values())
        for label, label_pct in self._label_dist.items():
            oversampling_ratio = (max_label_pct / label_pct)
            label_stride = min_stride / oversampling_ratio
            sub_df = self._label_df[self._label_df["label"] == label]
            nb_points = ((sub_df.index + sub_df.duration) - window - sub_df.index) // (label_stride)
            for idx, nb in zip(sub_df.index, nb_points):
                segment_start_idxs += [idx + label_stride*np.arange(nb)]
        segment_start_idxs = np.unique(np.concatenate(segment_start_idxs))
        kwargs["segment_start_idxs"] = segment_start_idxs
        kwargs["approve_sparsity"] = True  # TODO
        return super()._get_stroll(kwargs)

    # def _get_stroll(self, kwargs):
    #     assert kwargs["setpoints"] is None
    #     assert kwargs["strides"] is not None
    #     min_stride = min(kwargs["strides"])
    #     window = kwargs["window"]
    #     # TODO: this should not be implemented here...
    #     # TODO: this should not focus on only the first series in the series list
    #     # start, end = kwargs["data"][0].index[,-1])
    #     # print(start, end)
    #     setpoints = []
    #     max_label_pct = max(self._label_dist.values())
    #     for label, label_pct in self._label_dist.items():
    #         label_stride = min_stride / (max_label_pct / label_pct)
    #         # print(label, label_stride)
    #         sub_df = self._label_df[self._label_df["label"] == label]
    #         # nb_points = ((sub_df.index + sub_df.duration) - window - sub_df.index) // (label_stride)
    #         nb_points = ((sub_df.index + sub_df.duration) - sub_df.index) // (label_stride)
    #         for idx, nb in zip(sub_df.index, nb_points):
    #             setpoints += [idx + label_stride*np.arange(nb)]
    #     setpoints = np.unique(np.concatenate(setpoints))
    #     kwargs["setpoints"] = setpoints
    #     kwargs["approve_sparsity"] = True # TODO
    #     return super()._get_stroll(kwargs)

    @staticmethod
    def _get_index_freq(index):
        if isinstance(index, pd.DatetimeIndex):
            return pd.infer_freq(index)
        index_freqs = np.unique(np.diff(index))
        if len(index_freqs) == 1:
            return index_freqs[0]
        return None

    def fit(
        self,
        X: pd.DataFrame,
        y: Union[str, list, np.ndarray, pd.Series],
        *args,
        **kwargs,
    ):
        assert all(fd.stride is not None for fd in flatten(self._feature_desc_dict.values()))
        if isinstance(y, str):
            y = X[y]
        if isinstance(y, pd.Series):
            y = y.values
        assert len(y) == len(X)

        diff_label = np.insert(y[1:] != y[:-1], 0, True)

        self._label_df = pd.DataFrame(
            index=X.index[diff_label],
            data={
                "label": y[diff_label]
            },
        )
        self._label_df.index.name = "start_time"

        freq = self._get_index_freq(X.index)
        duration = list(self._label_df.index[1:] - self._label_df.index[:-1])
        duration += [X.index[-1] - self._label_df.index[-1]]  # might be off by 1 for the last index
        if freq is not None:  # fixes the off by 1 if we can induce the frequency
            duration[-1] += freq
        self._label_df["duration"] = duration

        ## uniform setpoint creation
        # labels, counts = np.unique(y, return_counts=True)
        # label_dist = {
        #     l: c/len(X) for l, c in zip(labels, counts)
        # }
        # majority_pct = np.max(counts) / len(X)
        # print(label_dist)
        # print(majority_pct)
        self._label_dist = {}
        total_duration = np.sum(self._label_df["duration"])
        for label in self._label_df["label"].unique():
            sub_df = self._label_df[self._label_df["label"] == label]
            self._label_dist[label] = np.sum(sub_df.duration) / total_duration
        # print(self._label_dist)

        # setpoints = []
        # stride = 3
        # for label in labels:
        #     print(label, label_dist[label], stride * label_dist[label] / majority_pct)
        #     sub_df = self._label_df[self._label_df["label"] == label]
        #     # print(sub_df)


        return super().calculate(X, *args, **kwargs)
        

    def transform(
        self,
        X,
        *args,
        **kwargs,
    ):
        # wrapper voor vanila feature extractie
        return self.calculate(X, *args, **kwargs)  # super of self?





class DynamicStrideFC():

    def __init__(self, feature_collection: FeatureCollection):
        self.feature_collection = feature_collection

    @staticmethod
    def _get_index_freq(index):
        if isinstance(index, pd.DatetimeIndex):
            return pd.infer_freq(index)
        index_freqs = np.unique(np.diff(index))
        if len(index_freqs) == 1:
            return index_freqs[0]
        return None

    # def _get_stroll(self, kwargs):
    #     assert kwargs["segment_start_idxs"] is None
    #     assert kwargs["strides"] is not None
    #     min_stride = min(kwargs["strides"])
    #     window = kwargs["window"]
    #     # TODO: this should not be implemented here...
    #     # TODO: this should not focus on only the first series in the series list
    #     segment_start_idxs = []
    #     max_label_pct = max(self._label_dist.values())
    #     for label, label_pct in self._label_dist.items():
    #         oversampling_ratio = (max_label_pct / label_pct)
    #         label_stride = min_stride / oversampling_ratio
    #         sub_df = self._label_df[self._label_df["label"] == label]
    #         nb_points = ((sub_df.index + sub_df.duration) - window - sub_df.index) // (label_stride)
    #         for idx, nb in zip(sub_df.index, nb_points):
    #             segment_start_idxs += [idx + label_stride*np.arange(nb)]
    #     segment_start_idxs = np.unique(np.concatenate(segment_start_idxs))
    #     kwargs["segment_start_idxs"] = segment_start_idxs
    #     kwargs["approve_sparsity"] = True  # TODO
    #     return super()._get_stroll(kwargs)

    def calculate_dynamic_stride(
        self,
        X: pd.DataFrame,
        y: Union[str, list, np.ndarray, pd.Series],
        **kwargs,
    ):
        assert all(fd.stride is not None for fd in flatten(self.feature_collection._feature_desc_dict.values()))
        assert all(fd.window is not None for fd in flatten(self.feature_collection._feature_desc_dict.values()))
        if isinstance(y, str):
            y = X[y]
        if isinstance(y, pd.Series):
            y = y.values
        assert len(y) == len(X)
        assert not "segment_start_idxs" in kwargs.keys()
        assert not "segment_end_idxs" in kwargs.keys()

        diff_label = np.insert(y[1:] != y[:-1], 0, True)

        self._label_df = pd.DataFrame(
            index=X.index[diff_label],
            data={
                "label": y[diff_label]
            },
        )
        self._label_df.index.name = "start_time"

        freq = self._get_index_freq(X.index)
        duration = list(self._label_df.index[1:] - self._label_df.index[:-1])
        duration += [X.index[-1] - self._label_df.index[-1]]  # might be off by 1 for the last index
        if freq is not None:  # fixes the off by 1 if we can induce the frequency
            duration[-1] += freq
        self._label_df["duration"] = duration

        self._label_dist = {}
        total_duration = np.sum(self._label_df["duration"])
        for label in self._label_df["label"].unique():
            sub_df = self._label_df[self._label_df["label"] == label]
            self._label_dist[label] = np.sum(sub_df.duration) / total_duration

        segment_start_idxs = []
        min_stride = min(flatten(fd.stride for fd in flatten(self.feature_collection._feature_desc_dict.values())))
        max_window = max(fd.window for fd in flatten(self.feature_collection._feature_desc_dict.values()))
        max_label_pct = max(self._label_dist.values())
        for label, label_pct in self._label_dist.items():
            oversampling_ratio = (max_label_pct / label_pct)
            label_stride = min_stride / oversampling_ratio
            sub_df = self._label_df[self._label_df["label"] == label]
            nb_points = ((sub_df.index + sub_df.duration) - max_window - sub_df.index) // (label_stride)
            # nb_points = ((sub_df.index + sub_df.duration) - sub_df.index) // (label_stride)
            for idx, nb in zip(sub_df.index, nb_points):
                segment_start_idxs += [idx + label_stride*np.arange(nb)]
        segment_start_idxs = np.unique(np.concatenate(segment_start_idxs))
        kwargs["segment_start_idxs"] = segment_start_idxs
        kwargs["approve_sparsity"] = True  # TODO

        return self.feature_collection.calculate(X, **kwargs)
