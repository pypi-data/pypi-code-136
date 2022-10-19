from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import numpy as np

from sonusai.mixture.dataclasses_sonusai import DataClassSonusAIMixin
from sonusai.mixture.segment import Segment


@dataclass(frozen=True)
class TruthSetting(DataClassSonusAIMixin):
    index: Optional[List[int]] = None
    function: Optional[str] = None
    config: Optional[dict] = None


TruthSettings = List[TruthSetting]

OptionalNumberStr = Optional[Union[float, int, str]]
OptionalListNumberStr = Optional[List[Union[float, int, str]]]


@dataclass
class Augmentation(DataClassSonusAIMixin):
    normalize: OptionalNumberStr = None
    pitch: OptionalNumberStr = None
    tempo: OptionalNumberStr = None
    gain: OptionalNumberStr = None
    eq1: OptionalListNumberStr = None
    eq2: OptionalListNumberStr = None
    eq3: OptionalListNumberStr = None
    lpf: OptionalNumberStr = None
    count: Optional[int] = None
    mixup: Optional[int] = 1


Augmentations = List[Augmentation]


@dataclass(frozen=True)
class TargetFile(DataClassSonusAIMixin):
    name: str
    duration: float
    truth_settings: TruthSettings
    augmentations: Optional[Augmentations] = None
    class_balancing_augmentation: Optional[Augmentation] = None


TargetFiles = List[TargetFile]


@dataclass
class AugmentedTarget(DataClassSonusAIMixin):
    target_file_index: int
    target_augmentation_index: int


AugmentedTargets = List[AugmentedTarget]


@dataclass(frozen=True)
class NoiseFile(DataClassSonusAIMixin):
    name: str
    duration: float
    augmentations: Optional[Augmentations] = None


NoiseFiles = List[NoiseFile]

ClassCount = List[int]


@dataclass
class MRecord(DataClassSonusAIMixin):
    target_file_index: List[int] = None
    noise_file_index: int = None
    noise_offset: int = None
    target_augmentation_index: List[int] = None
    noise_augmentation_index: int = None
    snr: float = None
    random_snr: Optional[bool] = None
    samples: int = None
    target_gain: List[int] = None
    class_count: ClassCount = None
    target_snr_gain: float = None
    noise_snr_gain: float = None
    o_frame_offset: Optional[int] = None


MRecords = List[MRecord]

MixtureIDs = Union[str, int, List[int], range]


@dataclass
class MixtureDatabase(DataClassSonusAIMixin):
    class_balancing: Optional[bool] = False
    class_balancing_augmentation: Optional[Augmentation] = None
    class_count: ClassCount = None
    class_labels: List[str] = None
    class_weights_threshold: List[float] = None
    exhaustive_noise: Optional[bool] = True
    feature: str = None
    feature_samples: int = None
    feature_step_samples: int = None
    first_cba_index: Optional[int] = None
    frame_size: int = None
    mixid_padding: Optional[int] = None
    mixtures: MRecords = None
    noise_augmentations: Augmentations = None
    noises: NoiseFiles = None
    num_classes: int = None
    random_snrs: Optional[List[str]] = None
    seed: Optional[int] = 0
    snrs: List[float] = None
    target_augmentations: Augmentations = None
    targets: TargetFiles = None
    truth_mutex: bool = None
    truth_reduction_function: str = None
    truth_settings: TruthSettings = None


def convert_json_to_mixdb(data: str) -> MixtureDatabase:
    import json

    return MixtureDatabase.from_dict(json.loads(data))


def load_mixdb(name: str) -> MixtureDatabase:
    from os.path import exists
    from os.path import splitext

    import h5py

    from sonusai import SonusAIError

    if not exists(name):
        raise SonusAIError(f'{name} does not exist')

    ext = splitext(name)[1]

    if ext == '.json':
        with open(file=name, mode='r', encoding='utf-8') as f:
            json_mixdb = f.read()
    elif ext == '.h5':
        with h5py.File(name, 'r') as f:
            json_mixdb = f.attrs['mixdb']
    else:
        raise SonusAIError(f'Do not know how to load mixdb from {name}')

    return convert_json_to_mixdb(json_mixdb)


def get_samples_in_mixid(mixdb: MixtureDatabase, mixid: int) -> int:
    return mixdb.mixtures[mixid].samples


def get_transform_frames_in_mrecord(mixdb: MixtureDatabase, mrecord: MRecord) -> int:
    return mrecord.samples // mixdb.frame_size


def get_feature_frames_in_mrecord(mixdb: MixtureDatabase, mrecord: MRecord) -> int:
    return mrecord.samples // mixdb.feature_step_samples


def get_class_weights_threshold(mixdb: Union[MixtureDatabase, Dict]) -> List[float]:
    """Get the class_weights_threshold from a mixture database or a config."""

    from sonusai import SonusAIError

    if isinstance(mixdb, dict):
        class_weights_threshold = mixdb['class_weights_threshold']
        num_classes = mixdb['num_classes']
    else:
        class_weights_threshold = mixdb.class_weights_threshold
        num_classes = mixdb.num_classes

    if not isinstance(class_weights_threshold, list):
        class_weights_threshold = [class_weights_threshold] * num_classes

    if len(class_weights_threshold) != num_classes:
        raise SonusAIError(f'invalid class_weights_threshold length: {len(class_weights_threshold)}')

    return class_weights_threshold


def get_file_frame_segments(mixdb: MixtureDatabase, mixids: MixtureIDs = None) -> Dict[int, Segment]:
    """
    Get Segment data from a mixture database
    Return a dictionary where:
        - keys are the mixids
        - values are file frame Segment objects
    """
    _mixid = convert_mixids_to_list(mixdb, mixids)

    # remove duplicates
    _mixid = sorted(list(set(_mixid)))

    file_frame_segments = {}
    for m in _mixid:
        file_frame_segments[m] = Segment(mixdb.mixtures[m].o_frame_offset,
                                         get_feature_frames_in_mrecord(mixdb, mixdb.mixtures[m]))

    return file_frame_segments


def new_mixdb_from_mixids(mixdb: MixtureDatabase, mixids: MixtureIDs) -> MixtureDatabase:
    from copy import deepcopy

    from sonusai import SonusAIError

    mixdb_out = deepcopy(mixdb)
    mixdb_out.mixtures = get_mrecords_from_mixids(mixdb_out, mixids)

    if not mixdb_out.mixtures:
        raise SonusAIError(f'Error processing mixid: {mixids}; resulted in empty list of mixtures')

    return mixdb_out


def convert_mixids_to_list(mixdb: MixtureDatabase, mixids: MixtureIDs = None) -> List[int]:
    from sonusai import SonusAIError

    result = mixids
    all_mixids = list(range(len(mixdb.mixtures)))

    if result is None:
        result = all_mixids

    if isinstance(result, str):
        if result == '*':
            result = all_mixids
        else:
            try:
                result = eval(f'{all_mixids}[{result}]')
            except NameError:
                result = []

    if isinstance(result, range):
        result = list(result)

    if isinstance(result, int):
        result = [result]

    if not all(isinstance(x, int) and 0 <= x < len(mixdb.mixtures) for x in result):
        raise SonusAIError(f'Invalid entries in mixids of {mixids}')

    if not result:
        raise SonusAIError(f'Empty mixids {mixids}')

    return result


def get_mrecords_from_mixids(mixdb: MixtureDatabase, mixids: MixtureIDs = None) -> MRecords:
    from copy import deepcopy

    return [deepcopy(mixdb.mixtures[i]) for i in convert_mixids_to_list(mixdb, mixids)]


def get_mixids_data(mixdb: MixtureDatabase,
                    mixids: MixtureIDs,
                    truth_f: np.ndarray,
                    predict: np.ndarray) -> (np.ndarray, np.ndarray):
    """Collect per-feature data of specified mixids from mixdb where inputs are:
       truth_f:   truth data matching mixdb (size feature_frames x num_classes)
       predict:   prediction or segsnr data (size feature_frames x ndim, where ndim > 1)

    Returns:
        truth_f_out:    np.ndarray combined truth from mixids
        predict_out:    np.ndarray combined data from mixids
    """
    from sonusai import SonusAIError
    from sonusai.mixture import get_slices

    in_frames = truth_f.shape[0]

    if in_frames != predict.shape[0]:
        raise SonusAIError('truth_f and predict have different number of frames')

    num_classes = truth_f.shape[1]
    # same as num_class for prediction data, but use for segsnr too
    num_data = predict.shape[1]

    _mixid = convert_mixids_to_list(mixdb, mixids)
    # TODO: Eliminate file_frame_segments
    file_frame_segments = get_file_frame_segments(mixdb, _mixid)
    out_frames = sum([file_frame_segments[m].length for m in _mixid])
    truth_f_out = np.empty((out_frames, num_classes), dtype=np.single)
    predict_out = np.empty((out_frames, num_data), dtype=np.single)

    # Handle the special case when input data is smaller, i.e., prediction when total mixture
    # length is a non-multiple of the batch size. In this case just pad both with zeros; should
    # have negligible effect on metrics
    max_in_index = max([file_frame_segments[m].get_slice().stop for m in _mixid])
    frame_diff = max_in_index - in_frames
    if frame_diff > 0:
        truth_f = np.concatenate((truth_f, np.zeros((frame_diff, num_classes))))
        predict = np.concatenate((predict, np.zeros((frame_diff, num_classes))))

    start = 0
    for m in _mixid:
        in_slice, out_slice = get_slices(file_frame_segments[m], start)

        if len(truth_f[in_slice]) != len(truth_f_out[out_slice]):
            raise SonusAIError(f'in_slice and out_slice are different lengths')

        truth_f_out[out_slice] = truth_f[in_slice]
        predict_out[out_slice] = predict[in_slice]
        start += file_frame_segments[m].length

    return truth_f_out, predict_out


def evaluate_random_rule(rule: str) -> Union[str, float]:
    """Evaluate 'rand' directive."""
    import re
    from random import uniform

    from sonusai.mixture import RAND_PATTERN

    def rand_repl(m):
        return f'{uniform(float(m.group(1)), float(m.group(4))):.2f}'

    return eval(re.sub(RAND_PATTERN, rand_repl, rule))


def get_mixid_padded_name(mixdb: MixtureDatabase, mixid: int) -> str:
    return f'{mixid:0{mixdb.mixid_padding}}'


def get_mixture_metadata(mixdb: MixtureDatabase, mrecord: MRecord) -> str:
    metadata = ''
    for ti in range(len(mrecord.target_file_index)):
        metadata += f'target {ti} name: {mixdb.targets[ti].name}\n'
        metadata += f'target {ti} augmentation: {mixdb.target_augmentations[ti].to_dict()}\n'
        metadata += f'target {ti} target_gain: {mrecord.target_gain[ti]}\n'
        ts = mixdb.targets[ti].truth_settings
        for tsi in range(len(ts)):
            metadata += f'target {ti} truth index {tsi}: {ts[tsi].index}\n'
    metadata += f'noise name: {mixdb.noises[mrecord.noise_file_index].name}\n'
    metadata += f'noise augmentation: {mixdb.noise_augmentations[mrecord.noise_augmentation_index].to_dict()}\n'
    metadata += f'snr: {mrecord.snr}\n'
    metadata += f'random_snr: {mrecord.random_snr}\n'
    metadata += f'samples: {mrecord.samples}\n'
    metadata += f'target_snr_gain: {mrecord.target_snr_gain}\n'
    metadata += f'noise_snr_gain: {mrecord.noise_snr_gain}\n'
    metadata += f'class_count: {mrecord.class_count}\n'

    return metadata
