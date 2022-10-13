from typing import Callable
from typing import Union

from sonusai.mixture import MRecord
from sonusai.mixture import MixtureDatabase


def print_mixture_details(mixdb: MixtureDatabase,
                          mixid: int = None,
                          desc_len: int = 1,
                          print_fn: Callable = print) -> None:
    import numpy as np

    from sonusai import SonusAIError
    from sonusai.mixture import SAMPLE_RATE
    from sonusai.mixture import get_feature_frames_in_mrecord

    if mixid is not None:
        if 0 < mixid >= len(mixdb.mixtures):
            raise SonusAIError(f'Given mixid is outside valid range of 0:{len(mixdb.mixtures) - 1}.')

        print_fn(f'Mixture {mixid} details:')
        mixture = mixdb.mixtures[mixid]
        targets = [mixdb.targets[idx] for idx in mixture.target_file_index]
        target_augmentations = [mixdb.target_augmentations[idx] for idx in mixture.target_augmentation_index]
        noise = mixdb.noises[mixture.noise_file_index]
        print_fn(f'Target files:')
        for idx, target in enumerate(targets):
            print_fn(f'{"  Name":{desc_len}} {target.name}')
            print_fn(f'{"  Duration":{desc_len}} {target.duration}')
            print_fn(f'  Truth settings:')
            for truth_setting in target.truth_settings:
                print_fn(f'{"    Index":{desc_len}} {truth_setting.index}')
                print_fn(f'{"    Function":{desc_len}} {truth_setting.function}')
                print_fn(f'{"    Config":{desc_len}} {truth_setting.config}')
            print_fn(f'{"  Augmentation":{desc_len}} {target_augmentations[idx]}')
        print_fn(f'{"Samples":{desc_len}} {mixture.samples}')
        print_fn(f'{"Features":{desc_len}} {get_feature_frames_in_mrecord(mixdb, mixid)}')
        print_fn(f'{"Noise":{desc_len}} {noise.name}')
        noise_offset_percent = int(np.round(100 * mixture.noise_offset / float(noise.duration * SAMPLE_RATE)))
        print_fn(f'{"Noise offset":{desc_len}} {mixture.noise_offset} samples ({noise_offset_percent}%)')
        print_fn(f'{"SNR":{desc_len}} {mixture.snr} dB')
        print_fn(f'{"Target gain":{desc_len}} {mixture.target_gain}')
        print_fn(f'{"Target SNR gain":{desc_len}} {mixture.target_snr_gain}')
        print_fn(f'{"Noise SNR gain":{desc_len}} {mixture.noise_snr_gain}')
        print_fn('')


def print_class_count(record: Union[MixtureDatabase, MRecord],
                      length: int,
                      print_fn: Callable = print,
                      all_class_counts: bool = False) -> None:
    import numpy as np

    print_fn(f'Class count:')
    idx_len = int(np.ceil(np.log10(len(record.class_count))))
    for idx, count in enumerate(record.class_count):
        if all_class_counts or count > 0:
            desc = f'  class {idx + 1:{idx_len}}'
            print_fn(f'{desc:{length}} {count}')
