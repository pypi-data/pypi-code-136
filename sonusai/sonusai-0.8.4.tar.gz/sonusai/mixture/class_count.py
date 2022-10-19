from typing import List

import numpy as np

from sonusai.mixture.mixdb import ClassCount
from sonusai.mixture.mixdb import MRecord
from sonusai.mixture.mixdb import MRecords
from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureIDs


def get_class_count_from_mrecord(mixdb: MixtureDatabase,
                                 mrecord: MRecord,
                                 target_audios: List[np.ndarray],
                                 noise_audio: np.ndarray) -> (ClassCount, np.ndarray):
    """Computes the number of samples for which each truth index is active for a given sample-based truth input."""
    from sonusai.mixture import get_class_weights_threshold
    from sonusai.mixture import generate_truth

    truth_t = generate_truth(mixdb=mixdb,
                             mrecord=mrecord,
                             target_audios=target_audios,
                             noise_audio=noise_audio)

    class_weights_threshold = get_class_weights_threshold(mixdb)

    class_count = [0] * mixdb.num_classes
    num_classes = mixdb.num_classes
    if mixdb.truth_mutex:
        num_classes -= 1
    for cl in range(num_classes):
        class_count[cl] = int(np.sum(truth_t[:, cl] >= class_weights_threshold[cl]))

    return class_count, truth_t


def get_class_count_from_mixids(mixdb: MixtureDatabase, mixids: MixtureIDs = None) -> ClassCount:
    """Sums the class counts for given mixids."""
    from sonusai.mixture import get_mrecords_from_mixids

    mixtures = get_mrecords_from_mixids(mixdb, mixids)
    return get_class_count_from_mixtures(mixdb, mixtures)


def get_class_count_from_mixtures(mixdb: MixtureDatabase, mrecords: MRecords) -> ClassCount:
    """Sums the class counts for given mixtures."""
    from sonusai import SonusAIError

    total_class_count = [0] * mixdb.num_classes
    for mrecord in mrecords:
        for cl in range(mixdb.num_classes):
            total_class_count[cl] += mrecord.class_count[cl]

    if mixdb.truth_mutex:
        # Compute the class count for the 'other' class
        if total_class_count[-1] != 0:
            raise SonusAIError('Error: truth_mutex was set, but the class count for the last count was non-zero.')
        total_class_count[-1] = sum([sub.samples for sub in mrecords]) - sum(total_class_count)

    return total_class_count
