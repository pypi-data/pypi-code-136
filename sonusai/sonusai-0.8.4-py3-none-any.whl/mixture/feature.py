from dataclasses import dataclass
from os import PathLike
from typing import List
from typing import Union

import numpy as np

from sonusai.mixture import DEFAULT_FRAME_SIZE
from sonusai.mixture.mixdb import MRecord
from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureIDs

MP_DICT = {}


def _get_ft_from_dir_kernel(mixid: int) -> (np.ndarray, np.ndarray):
    """Get feature/truth for a given mixid from a directory containing genft data"""
    from os.path import join

    import h5py

    from sonusai.mixture import get_mixid_padded_name

    mixid_padded_name = get_mixid_padded_name(MP_DICT['mixdb'], mixid)

    with h5py.File(join(MP_DICT['location'], mixid_padded_name + '.h5'), 'r') as f:
        feature = np.array(f['feature'])
        truth_f = np.array(f['truth_f'])

    return feature, truth_f


def get_ft_from_dir(mixdb: MixtureDatabase,
                    location: Union[str, bytes, PathLike],
                    mixids: MixtureIDs = None) -> (np.ndarray, np.ndarray):
    """Get feature/truth for given mixids from a directory containing genft data"""
    from sonusai.mixture import convert_mixids_to_list
    from sonusai.utils import p_map

    MP_DICT['mixdb'] = mixdb
    MP_DICT['location'] = location
    mixids = convert_mixids_to_list(mixdb, mixids)
    result = p_map(_get_ft_from_dir_kernel, mixids)

    feature = np.vstack([result[i][0] for i in range(len(result))])
    truth_f = np.vstack([result[i][1] for i in range(len(result))])

    return feature, truth_f


def get_feature_from_audio(audio: np.ndarray, feature: str) -> np.ndarray:
    from sonusai.mixture import get_pad_length
    from sonusai.mixture import MRecord

    fs = get_feature_stats(feature=feature, num_classes=1)
    audio = np.pad(array=audio,
                   pad_width=(0, get_pad_length(len(audio), fs.feature_step_samples)),
                   mode='constant',
                   constant_values=0)
    mixdb = MixtureDatabase(feature=feature,
                            mixtures=[MRecord(samples=len(audio))],
                            feature_samples=fs.feature_samples,
                            feature_step_samples=fs.feature_step_samples,
                            frame_size=DEFAULT_FRAME_SIZE,
                            num_classes=1,
                            truth_mutex=False,
                            truth_reduction_function='max')
    feature, _, _ = get_feature_and_truth_f(mixdb=mixdb,
                                            mrecord=mixdb.mixtures[0],
                                            mixture=audio,
                                            compute_truth=False)
    return feature


def read_feature_data(filename: str) -> (MixtureDatabase, np.ndarray, np.ndarray, np.ndarray):
    """Read mixdb, feature, truth_f, and segsnr data from given HDF5 file and return them as a tuple."""
    import h5py

    from sonusai.mixture import convert_json_to_mixdb

    with h5py.File(filename, 'r') as f:
        return (convert_json_to_mixdb(f.attrs['mixdb']),
                np.array(f['/feature']),
                np.array(f['/truth_f']),
                np.array(f['/segsnr']))


def get_feature_and_truth_f(mixdb: MixtureDatabase,
                            mrecord: MRecord,
                            mixture: np.ndarray = None,
                            truth_t: np.ndarray = None,
                            segsnr_t: np.ndarray = None,
                            raw_target_audios: List[np.ndarray] = None,
                            augmented_noise_audios: List[List[np.ndarray]] = None,
                            compute_truth: bool = True,
                            compute_segsnr: bool = False) -> (np.ndarray, np.ndarray, np.ndarray):
    from pyaaware import FeatureGenerator
    from pyaaware import ForwardTransform

    from sonusai import SonusAIError
    from sonusai.mixture import get_audio_and_truth_t
    from sonusai.mixture import get_feature_frames_in_mrecord
    from sonusai.mixture import get_transform_frames_in_mrecord
    from sonusai.mixture import truth_reduction
    from sonusai.utils import int16_to_float

    segsnr = None
    if mixture is None or (compute_truth and truth_t is None) or (compute_segsnr and segsnr_t is None):
        (mixture,
         truth_t,
         _,
         _,
         segsnr) = get_audio_and_truth_t(mixdb=mixdb,
                                         mrecord=mrecord,
                                         raw_target_audios=raw_target_audios,
                                         augmented_noise_audios=augmented_noise_audios,
                                         compute_truth=compute_truth,
                                         compute_segsnr=compute_segsnr,
                                         frame_based_segsnr=True)

    if len(mixture) != mrecord.samples:
        raise SonusAIError(f'Wrong number of samples in mixture')

    fft = ForwardTransform(N=mixdb.frame_size * 4,
                           R=mixdb.frame_size)

    fg = FeatureGenerator(frame_size=mixdb.frame_size,
                          feature_mode=mixdb.feature,
                          num_classes=mixdb.num_classes,
                          truth_mutex=mixdb.truth_mutex)

    transform_frames = get_transform_frames_in_mrecord(mixdb, mrecord)
    feature_frames = get_feature_frames_in_mrecord(mixdb, mrecord)

    if truth_t is None:
        truth_t = np.zeros((mrecord.samples, mixdb.num_classes), dtype=np.single)

    feature = np.empty((feature_frames, fg.stride, fg.num_bands), dtype=np.single)
    truth_f = np.empty((feature_frames, mixdb.num_classes), dtype=np.single)

    feature_frame = 0
    for transform_frame in range(transform_frames):
        indices = slice(transform_frame * mixdb.frame_size,
                        (transform_frame + 1) * mixdb.frame_size)
        fd = fft.execute(int16_to_float(mixture[indices]))

        fg.execute(fd, truth_reduction(truth_t[indices], mixdb.truth_reduction_function))

        if fg.eof():
            feature[feature_frame] = fg.feature()
            truth_f[feature_frame] = fg.truth()
            feature_frame += 1

    return feature, truth_f, segsnr


@dataclass(frozen=True)
class FeatureStats:
    feature_ms: float
    feature_samples: int
    feature_step_ms: float
    feature_step_samples: int
    num_bands: int
    stride: int
    step: int
    decimation: int


def get_feature_stats(feature: str,
                      num_classes: int,
                      frame_size: int = DEFAULT_FRAME_SIZE) -> FeatureStats:
    import h5py
    from pyaaware import FeatureGenerator

    import sonusai

    fg = FeatureGenerator(feature_mode=feature,
                          frame_size=frame_size,
                          num_classes=num_classes)

    transform_frame_ms = float(frame_size) / float(sonusai.mixture.SAMPLE_RATE / 1000)

    return FeatureStats(feature_ms=transform_frame_ms * fg.decimation * fg.stride,
                        feature_samples=frame_size * fg.decimation * fg.stride,
                        feature_step_ms=transform_frame_ms * fg.decimation * fg.step,
                        feature_step_samples=frame_size * fg.decimation * fg.step,
                        num_bands=fg.num_bands,
                        stride=fg.stride,
                        step=fg.step,
                        decimation=fg.decimation)
