from dataclasses import dataclass
from os import PathLike
from typing import List
from typing import Union

import numpy as np
from tensorflow.keras.utils import Sequence

from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureIDs


class KerasFromH5(Sequence):
    """Generates data for Keras from a directory containing genft data"""

    @dataclass(frozen=True)
    class BatchParams:
        mixid: List[int]
        offset: int
        extra: int

    def __init__(self,
                 mixdb: MixtureDatabase,
                 mixids: MixtureIDs,
                 location: Union[str, bytes, PathLike],
                 batch_size: int,
                 timesteps: int,
                 flatten: bool,
                 add1ch: bool,
                 shuffle: bool = False):
        """Initialization"""
        from os.path import exists
        from os.path import isdir
        from os.path import join

        import h5py

        from sonusai import SonusAIError
        from sonusai.mixture import convert_mixids_to_list
        from sonusai.mixture import get_feature_stats
        from sonusai.mixture import get_mixid_padded_name

        self.mixdb = mixdb
        self.mixids = convert_mixids_to_list(self.mixdb, mixids)
        self.location = location
        self.batch_size = batch_size
        self.timesteps = timesteps
        self.flatten = flatten
        self.add1ch = add1ch
        self.shuffle = shuffle

        if not isdir(self.location):
            raise SonusAIError(f'Specified location, {self.location}, is not a directory')

        for m in self.mixids:
            mixid_padded_name = get_mixid_padded_name(self.mixdb, m)
            filename = join(self.location, mixid_padded_name + '.h5')
            if not exists(filename):
                raise SonusAIError(f'Could not find {filename}')
            with h5py.File(filename, 'r') as f:
                datasets = ['feature', 'truth_f']
                for dataset in datasets:
                    if dataset not in f:
                        raise SonusAIError(f'Could not find "{dataset}" in {filename}')

        fs = get_feature_stats(feature=self.mixdb.feature,
                               num_classes=self.mixdb.num_classes,
                               frame_size=self.mixdb.frame_size)

        self.stride = fs.stride
        self.num_bands = fs.num_bands
        self.num_classes = self.mixdb.num_classes
        self.mixtures = None
        self.mixture_frame_segments = None
        self.batch_frame_segments = None
        self.total_batches = None

        self._initialize_mixtures()

    def __len__(self) -> int:
        """Denotes the number of batches per epoch"""
        return self.total_batches

    def __getitem__(self, batch_index: int) -> (np.ndarray, np.ndarray):
        """Get one batch of data"""
        from sonusai.utils import reshape_inputs

        batch_params = self.batch_params[batch_index]

        result = []
        for mixid in batch_params.mixid:
            result.append(self._get_ft(mixid))

        feature = np.vstack([result[i][0] for i in range(len(result))])
        truth = np.vstack([result[i][1] for i in range(len(result))])

        if batch_params.extra > 0:
            feature = feature[batch_params.offset:-batch_params.extra]
            truth = truth[batch_params.offset:-batch_params.extra]
        else:
            feature = feature[batch_params.offset:]
            truth = truth[batch_params.offset:]

        feature, truth, _, _, _, _ = reshape_inputs(feature=feature,
                                                    truth=truth,
                                                    batch_size=self.batch_size,
                                                    timesteps=self.timesteps,
                                                    flatten=self.flatten,
                                                    add1ch=self.add1ch)

        return feature, truth

    def on_epoch_end(self) -> None:
        """Modification of dataset between epochs"""
        import random

        if self.shuffle:
            random.shuffle(self.mixids)
            self._initialize_mixtures()

    def _get_ft(self, mixid: int) -> (np.ndarray, np.ndarray):
        from os.path import join

        import h5py

        from sonusai.mixture import get_mixid_padded_name

        mixid_padded_name = get_mixid_padded_name(self.mixdb, mixid)

        with h5py.File(join(self.location, mixid_padded_name + '.h5'), 'r') as f:
            feature = np.array(f['feature'])
            truth_f = np.array(f['truth_f'])

        return feature, truth_f

    def _initialize_mixtures(self) -> None:
        from sonusai.data_generator.utils import get_frames_per_batch_from_mixdb
        from sonusai.mixture import get_mrecords_from_mixids

        self.mixtures = get_mrecords_from_mixids(mixdb=self.mixdb, mixids=self.mixids)
        frames_per_batch, self.total_batches = get_frames_per_batch_from_mixdb(mixdb=self.mixdb,
                                                                               mixtures=self.mixtures,
                                                                               batch_size=self.batch_size,
                                                                               timesteps=self.timesteps)

        # Compute mixid, offset, and extra for dataset
        # offsets and extras are needed because mixtures are not guaranteed to fall on batch boundaries.
        # When fetching a new index that starts in the middle of a sequence of mixtures, the
        # previous feature frame offset must be maintained in order to preserve the correct
        # data sequence. And the extra must be maintained in order to preserve the correct data length.
        cumulative_frames = 0
        start_mixture_index = 0
        offset = 0
        self.batch_params = []
        for m in range(len(self.mixids)):
            current_frames = self.mixtures[m].samples // self.mixdb.feature_step_samples
            cumulative_frames += current_frames
            while cumulative_frames >= frames_per_batch:
                extra = cumulative_frames - frames_per_batch
                mixid = self.mixids[start_mixture_index:m + 1]
                self.batch_params.append(self.BatchParams(mixid=mixid, offset=offset, extra=extra))
                if extra == 0:
                    start_mixture_index = m + 1
                    offset = 0
                else:
                    start_mixture_index = m
                    offset = current_frames - extra
                cumulative_frames = extra
