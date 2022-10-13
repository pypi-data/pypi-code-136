from typing import List
from typing import Tuple
from typing import Union

import numpy as np

from sonusai.mixture.mixdb import MRecord
from sonusai.mixture.mixdb import MixtureDatabase

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = {}


def get_augmented_noise_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[List[np.ndarray]]:
    """Get a list of lists of augmented noise audio data."""
    from tqdm import tqdm

    from sonusai.mixture import apply_augmentation

    augmented_noise_audios = []
    for file_index in tqdm(range(len(mixdb.noises)), desc='Read noise audio', disable=not show_progress):
        audio_in = read_audio(mixdb.noises[file_index].name)
        augmented_noise_audios.append(list())
        for augmentation_index, augmentation in enumerate(mixdb.noise_augmentations):
            augmented_noise_audios[-1].append(apply_augmentation(audio_in=audio_in, augmentation=augmentation))

    return augmented_noise_audios


def get_raw_target_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[np.ndarray]:
    """Get a list of raw target audio data."""
    from tqdm import tqdm

    from sonusai.utils import p_tqdm_map

    MP_DICT['mixdb'] = mixdb

    names = [mixdb.targets[i].name for i in range(len(mixdb.targets))]
    progress = tqdm(total=len(names), desc='Read target audio', disable=not show_progress)
    raw_target_audios = p_tqdm_map(read_audio, names, progress=progress)

    return raw_target_audios


def check_audio_files_exist(mixdb: MixtureDatabase) -> None:
    """Walk through all the noise and target audio files in a mixture database ensuring that they exist."""
    from os.path import exists

    from sonusai import SonusAIError
    from sonusai.mixture import tokenized_expandvars

    for file_index in range(len(mixdb.noises)):
        file_name, _ = tokenized_expandvars(mixdb.noises[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')

    for file_index in range(len(mixdb.targets)):
        file_name, _ = tokenized_expandvars(mixdb.targets[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')


def read_raw_target_audio(mixdb: MixtureDatabase, show_progress: bool = False) -> List[np.ndarray]:
    """Read in all audio data beforehand to avoid reading it multiple times in a loop."""
    from tqdm import tqdm

    from sonusai.utils import p_tqdm_map

    names = [target.name for target in mixdb.targets]
    progress = tqdm(total=len(names), desc='Read target audio', disable=not show_progress)
    raw_target_audio = p_tqdm_map(read_audio, names, progress=progress)
    progress.close()

    return raw_target_audio


def get_target_noise_audio(mixdb: MixtureDatabase,
                           mrecord: MRecord,
                           raw_target_audios: List[np.ndarray] = None,
                           augmented_noise_audios: List[List[np.ndarray]] = None) -> (List[np.ndarray], np.ndarray):
    """Apply augmentations and return augmented target and noise data."""
    from sonusai import SonusAIError
    from sonusai.mixture import apply_augmentation
    from sonusai.mixture import apply_snr_gain
    from sonusai.mixture import pad_to_samples

    if raw_target_audios is None:
        raw_target_audios = get_raw_target_audios(mixdb)
    if augmented_noise_audios is None:
        augmented_noise_audios = get_augmented_noise_audios(mixdb)

    target_file_index = mrecord.target_file_index
    target_augmentation_index = mrecord.target_augmentation_index
    if len(target_file_index) != len(target_augmentation_index):
        raise SonusAIError('target_file_index and target_augmentation_index are not the same length')

    if mrecord.samples % mixdb.frame_size != 0:
        raise SonusAIError(f'Number of samples in mixture is not a multiple of {mixdb.frame_size}')

    targets = []
    for idx in range(len(target_file_index)):
        target_augmentation = mixdb.target_augmentations[target_augmentation_index[idx]]

        target = apply_augmentation(audio_in=raw_target_audios[target_file_index[idx]],
                                    augmentation=target_augmentation,
                                    length_common_denominator=mixdb.feature_step_samples)

        target = pad_to_samples(audio_in=target, samples=mrecord.samples)
        targets.append(target)

    noise = augmented_noise_audios[mrecord.noise_file_index][mrecord.noise_augmentation_index]
    noise, _ = get_next_noise(offset_in=mrecord.noise_offset,
                              length=mrecord.samples,
                              audio_in=noise)

    return apply_snr_gain(mrecord=mrecord, targets=targets, noise=noise)


def get_audio_and_truth_t(mixdb: MixtureDatabase,
                          mrecord: MRecord,
                          raw_target_audios: List[np.ndarray] = None,
                          augmented_noise_audios: List[List[np.ndarray]] = None,
                          compute_truth: bool = True,
                          compute_segsnr: bool = False,
                          frame_based_segsnr: bool = False) -> (np.ndarray,
                                                                np.ndarray,
                                                                np.ndarray,
                                                                np.ndarray,
                                                                np.ndarray):
    from sonusai.mixture import generate_segsnr
    from sonusai.mixture import generate_truth

    targets, noise = get_target_noise_audio(mixdb=mixdb,
                                            mrecord=mrecord,
                                            raw_target_audios=raw_target_audios,
                                            augmented_noise_audios=augmented_noise_audios)

    truth_t = generate_truth(mixdb=mixdb,
                             mrecord=mrecord,
                             target_audios=targets,
                             noise_audio=noise,
                             compute=compute_truth)

    target = sum(targets)

    segsnr = generate_segsnr(mixdb=mixdb,
                             mrecord=mrecord,
                             target_audio=target,
                             noise_audio=noise,
                             compute=compute_segsnr,
                             frame_based=frame_based_segsnr)

    mixture = target + noise
    return mixture, truth_t, target, noise, segsnr


def get_next_noise(offset_in: int, length: int, audio_in: np.ndarray) -> (np.ndarray, int):
    audio_out = np.take(audio_in, range(offset_in, offset_in + length), mode='wrap')
    offset_out = (offset_in + length) % len(audio_in)
    return audio_out, offset_out


def read_audio(name: str) -> np.ndarray:
    import sox

    from sonusai import SonusAIError
    from sonusai import logger
    from sonusai.mixture import tokenized_expandvars
    from sonusai.mixture import BIT_DEPTH
    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_RATE

    expanded_name, _ = tokenized_expandvars(name)

    try:
        # Read in and convert to desired format
        inp = sox.Transformer()
        inp.set_output_format(rate=SAMPLE_RATE, bits=BIT_DEPTH, channels=CHANNEL_COUNT)
        return inp.build_array(input_filepath=expanded_name,
                               sample_rate_in=int(sox.file_info.sample_rate(expanded_name)))

    except Exception as e:
        if name != expanded_name:
            logger.error(f'Error reading {name} (expanded: {expanded_name}): {e}')
        else:
            raise SonusAIError(f'Error reading {name}: {e}')


def get_mixture_data(mixdb: MixtureDatabase,
                     mrecord: MRecord) -> (np.ndarray,
                                           List[Union[np.ndarray, None]],
                                           np.ndarray,
                                           np.ndarray,
                                           np.ndarray):
    """Get mixture data assuming nothing has been loaded into memory already."""

    from sonusai.mixture import apply_augmentation
    from sonusai.mixture import generate_truth
    from sonusai.mixture import get_feature_and_truth_f
    from sonusai.mixture import get_truth_indices_for_target
    from sonusai.mixture import pad_to_samples

    target_audios = []
    target_truth_indices = []
    for idx in range(len(mrecord.target_file_index)):
        target_name = mixdb.targets[mrecord.target_file_index[idx]].name
        target_augmentation = mixdb.target_augmentations[mrecord.target_augmentation_index[idx]]

        target_audio = apply_augmentation(audio_in=read_audio(target_name),
                                          augmentation=target_augmentation,
                                          length_common_denominator=mixdb.feature_step_samples)

        target_audio = np.int16(np.round(np.single(target_audio) * mrecord.target_snr_gain))
        target_audio = pad_to_samples(audio_in=target_audio, samples=mrecord.samples)
        target_audios.append(target_audio)
        target_truth_indices.append(get_truth_indices_for_target(mixdb.targets[mrecord.target_file_index[idx]]))

    augmented_noise_audios = get_augmented_noise_audios(mixdb=mixdb, show_progress=False)
    raw_noise_audio = augmented_noise_audios[mrecord.noise_file_index][mrecord.noise_augmentation_index]
    noise_audio, _ = get_next_noise(offset_in=mrecord.noise_offset,
                                    length=mrecord.samples,
                                    audio_in=raw_noise_audio)

    noise_audio = np.int16(np.round(np.single(noise_audio) * mrecord.noise_snr_gain))

    truth_t = generate_truth(mixdb=mixdb,
                             mrecord=mrecord,
                             target_audios=target_audios,
                             noise_audio=noise_audio,
                             compute=True)

    mixture_audio = sum(target_audios) + noise_audio

    # Transform target_audios into a list num_classes long such that each entry is the target data per class
    class_audio = []
    for n in range(mixdb.num_classes):
        class_audio.append(None)
        for idx in range(len(target_audios)):
            if n + 1 in target_truth_indices[idx]:
                if class_audio[n] is None:
                    class_audio[n] = target_audios[idx]
                else:
                    class_audio[n] += target_audios[idx]

    feature, truth_f = get_feature_and_truth_f(mixdb=mixdb,
                                               mrecord=mrecord,
                                               mixture=mixture_audio,
                                               truth_t=truth_t)

    return mixture_audio, class_audio, noise_audio, feature, truth_f


def extract_results(results: List[Tuple[np.ndarray, ...]]) -> Tuple[np.ndarray, ...]:
    result = ()
    for j in range(len(results[0])):
        if results[0][j] is None:
            result += (None,)
        else:
            result += (np.concatenate([results[i][j] for i in range(len(results))]),)

    return result
