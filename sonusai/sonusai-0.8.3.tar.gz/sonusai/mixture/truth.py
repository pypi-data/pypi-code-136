from typing import List

import numpy as np

from sonusai.mixture.mixdb import MRecord
from sonusai.mixture.mixdb import MixtureDatabase


def _strictly_decreasing(list_to_check: list) -> bool:
    return all(x > y for x, y in zip(list_to_check, list_to_check[1:]))


def generate_truth(mixdb: MixtureDatabase,
                   mrecord: MRecord,
                   target_audios: List[np.ndarray],
                   noise_audio: np.ndarray,
                   compute: bool = True) -> np.ndarray:
    from sonusai import SonusAIError

    if not compute:
        return np.empty(0, dtype=np.single)

    if len(target_audios) != len(mrecord.target_file_index):
        raise SonusAIError('Number of target audio entries does not match number of target file indices')

    if not all(len(target_audio) == len(noise_audio) for target_audio in target_audios):
        raise SonusAIError('Lengths of target audio do not match length of noise audio')

    truth = np.zeros((mrecord.samples, mixdb.num_classes), dtype=np.single)
    for idx in range(len(target_audios)):
        for truth_setting in mixdb.targets[mrecord.target_file_index[idx]].truth_settings:
            config = {
                'index':       truth_setting.index,
                'function':    truth_setting.function,
                'config':      truth_setting.config,
                'frame_size':  mixdb.frame_size,
                'num_classes': mixdb.num_classes,
                'mutex':       mixdb.truth_mutex,
                'target_gain': mrecord.target_gain[idx] * mrecord.target_snr_gain
            }
            truth += truth_function(target_audio=target_audios[idx], noise_audio=noise_audio, config=config)

    return truth


def truth_function(target_audio: np.ndarray,
                   noise_audio: np.ndarray,
                   config: dict) -> np.ndarray:
    import h5py
    from pyaaware import ForwardTransform
    from pyaaware import SED

    from sonusai import SonusAIError
    from sonusai.mixture.mapped_snr_f import calculate_mapped_snr_f
    from sonusai.utils.int16_to_float import int16_to_float

    truth = np.zeros((len(target_audio), config['num_classes']), dtype=np.single)
    zero_based_indices = [x - 1 for x in config['index']]

    if config['function'] == 'sed':
        if len(target_audio) % config['frame_size'] != 0:
            raise SonusAIError(f'Number of samples in audio is not a multiple of {config["frame_size"]}')

        if 'config' not in config:
            raise SonusAIError('Truth function SED missing config')

        parameters = ['thresholds']
        for parameter in parameters:
            if parameter not in config['config']:
                raise SonusAIError(f'Truth function SED config missing required parameter: {parameter}')

        thresholds = config['config']['thresholds']
        if not _strictly_decreasing(thresholds):
            raise SonusAIError(f'Truth function SED thresholds are not strictly decreasing: {thresholds}')

        if config['target_gain'] == 0:
            return truth

        target_fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])
        # SED wants 1-based indices
        sed = SED(thresholds=thresholds,
                  index=config['index'],
                  frame_size=config['frame_size'],
                  num_classes=config['num_classes'],
                  mutex=config['mutex'])

        target_audio = np.int16(np.round(np.single(target_audio) / config['target_gain']))
        for offset in range(0, len(target_audio), config['frame_size']):
            indices = slice(offset, offset + config['frame_size'])
            new_truth = sed.execute(target_fft.energy_t(int16_to_float(target_audio[indices])))
            truth[indices] = np.reshape(new_truth, (1, len(new_truth)))

        return truth

    elif config['function'] == 'file':
        if 'config' not in config:
            raise SonusAIError('Truth function file missing config')

        parameters = ['file']
        for parameter in parameters:
            if parameter not in config['config']:
                raise SonusAIError(f'Truth function file config missing required parameter: {parameter}')

        with h5py.File(config['config']['file'], 'r') as f:
            truth_in = np.array(f['/truth_t'])

        if truth_in.ndim != 2:
            raise SonusAIError('Truth file data is not 2 dimensions')

        if truth_in.shape[0] != len(target_audio):
            raise SonusAIError('Truth file does not contain the right amount of samples')

        if config['target_gain'] == 0:
            return truth

        if len(zero_based_indices) > 1:
            if len(zero_based_indices) != truth_in.shape[1]:
                raise SonusAIError('Truth file does not contain the right amount of classes')

            truth[:, zero_based_indices] = truth_in
        else:
            index = zero_based_indices[0]
            if index + truth_in.shape[1] > config['num_classes']:
                raise SonusAIError('Truth file contains too many classes')

            truth[:, index:index + truth_in.shape[1]] = truth_in

        return truth

    elif config['function'] == 'energy_t':
        if config['target_gain'] == 0:
            return truth

        target_fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])
        for offset in range(0, len(target_audio), config['frame_size']):
            target_energy = target_fft.energy_t(int16_to_float(target_audio[offset:offset + config['frame_size']]))
            truth[offset:offset + config['frame_size'], zero_based_indices] = np.single(target_energy)

        return truth

    elif config['function'] in ['energy_f', 'snr_f', 'mapped_snr_f']:
        if config['target_gain'] == 0:
            return truth

        target_fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])
        noise_fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])

        snr_db_mean = None
        snr_db_std = None
        if config['function'] == 'mapped_snr_f':
            if 'config' not in config:
                raise SonusAIError('Truth function mapped SNR missing config')

            parameters = ['snr_db_mean', 'snr_db_std']
            for parameter in parameters:
                if parameter not in config['config']:
                    raise SonusAIError(f'Truth function mapped SNR config missing required parameter: {parameter}')

            snr_db_mean = config['config']['snr_db_mean']
            if len(snr_db_mean) != target_fft.bins:
                raise SonusAIError(f'Truth function mapped SNR snr_db_mean does not have {target_fft.bins} elements')

            snr_db_std = config['config']['snr_db_std']
            if len(snr_db_std) != target_fft.bins:
                raise SonusAIError(f'Truth function mapped SNR snr_db_std does not have {target_fft.bins} elements')

        for index in zero_based_indices:
            if index + target_fft.bins > config['num_classes']:
                raise SonusAIError('Truth index exceeds the number of classes')

        for offset in range(0, len(target_audio), config['frame_size']):
            target_energy = np.single(
                target_fft.energy_f(int16_to_float(target_audio[offset:offset + config['frame_size']])))
            if config['function'] in ['snr_f', 'mapped_snr_f']:
                noise_energy = np.single(
                    noise_fft.energy_f(int16_to_float(noise_audio[offset:offset + config['frame_size']])))
            else:
                noise_energy = np.single(1)

            indices = slice(offset, offset + config['frame_size'])
            for index in zero_based_indices:
                old_err = np.seterr(divide='ignore', invalid='ignore')
                tmp = target_energy / noise_energy
                np.seterr(**old_err)

                tmp = np.nan_to_num(tmp, nan=-np.inf, posinf=np.inf, neginf=-np.inf)

                if config['function'] == 'mapped_snr_f':
                    tmp = calculate_mapped_snr_f(tmp, snr_db_mean, snr_db_std)

                truth[indices, index:index + target_fft.bins] = tmp

        return truth

    elif config['function'] == 'phoneme':
        # Read in .txt transcript and run a Python function to generate text grid data
        # (indicating which phonemes are active)
        # Then generate truth based on this data and put in the correct classes based on config['index']
        raise SonusAIError('Truth function phoneme is not supported yet')

    raise SonusAIError(f'Unsupported truth function: {config["function"]}')


def get_truth_indices_for_mixid(mixdb: MixtureDatabase, mixid: int) -> List[int]:
    """Get a list of truth indices for a given mixid."""

    from sonusai.mixture.targets import get_truth_indices_for_target

    indices = []
    for target_file_index in mixdb.mixtures[mixid].target_file_index:
        indices.append(*get_truth_indices_for_target(mixdb.targets[target_file_index]))

    return sorted(list(set(indices)))


def truth_reduction(x: np.ndarray, func: str) -> np.ndarray:
    from sonusai import SonusAIError

    if func == 'max':
        return np.max(x, axis=0)

    if func == 'mean':
        return np.mean(x, axis=0)

    raise SonusAIError(f'Invalid truth reduction function: {func}')
