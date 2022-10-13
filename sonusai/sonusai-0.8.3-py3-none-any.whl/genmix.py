"""sonusai genmix

usage: genmix [-hvts] (-d MIXDB) [-i MIXID] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    -i MIXID, --mixid MIXID         Mixture ID(s) to generate. [default: *].
    -o OUTPUT, --output OUTPUT      Output directory.
    -t, --truth                     Save truth_t. [default: False].
    -s, --segsnr                    Save segsnr_t. [default: False].

Generate SonusAI mixture data from a SonusAI mixture database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file.
    MIXID       A glob of mixture ID(s) to generate.

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5:
                        dataset:    mixture
                        dataset:    target
                        dataset:    noise
                        dataset:    truth_t
                        dataset:    segsnr_t
                    <id>.txt
                    genmix.log
"""
from typing import List

import numpy as np

from sonusai import logger
from sonusai.mixture import MixtureDatabase
from sonusai.mixture import MixtureIDs
from sonusai.mixture import extract_results

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = {}


def genmix(mixdb: MixtureDatabase,
           mixids: MixtureIDs = None,
           raw_target_audios: List[np.ndarray] = None,
           augmented_noise_audios: List[List[np.ndarray]] = None,
           compute_truth: bool = False,
           compute_segsnr: bool = False) -> (np.ndarray,
                                             np.ndarray,
                                             np.ndarray,
                                             np.ndarray,
                                             np.ndarray):
    import multiprocessing as mp

    from sonusai.mixture import convert_mixids_to_list
    from sonusai.mixture import get_audio_and_truth_t
    from sonusai.utils import p_map

    mixids = convert_mixids_to_list(mixdb, mixids)
    results = []
    if mp.current_process().daemon:
        for mixid in mixids:
            results.append(get_audio_and_truth_t(mixdb=mixdb,
                                                 mrecord=mixdb.mixtures[mixid],
                                                 raw_target_audios=raw_target_audios,
                                                 augmented_noise_audios=augmented_noise_audios,
                                                 compute_truth=compute_truth,
                                                 compute_segsnr=compute_segsnr))
    else:
        MP_DICT['mixdb'] = mixdb
        MP_DICT['raw_target_audios'] = raw_target_audios
        MP_DICT['augmented_noise_audios'] = augmented_noise_audios
        MP_DICT['compute_truth'] = compute_truth
        MP_DICT['compute_segsnr'] = compute_segsnr

        results = p_map(_genmix_kernel, mixids)

    return extract_results(results)


def _genmix_kernel(mixid: int) -> None:
    from sonusai.mixture import get_audio_and_truth_t

    return get_audio_and_truth_t(mixdb=MP_DICT['mixdb'],
                                 mrecord=MP_DICT['mixdb'].mixtures[mixid],
                                 raw_target_audios=MP_DICT['raw_target_audios'],
                                 augmented_noise_audios=MP_DICT['augmented_noise_audios'],
                                 compute_truth=MP_DICT['compute_truth'],
                                 compute_segsnr=MP_DICT['compute_segsnr'])


def _process_mixture(mixid: int) -> None:
    from os.path import join

    import h5py

    from sonusai import SonusAIError
    from sonusai.mixture import get_mixid_padded_name
    from sonusai.mixture import get_mixture_metadata

    mixdb = MP_DICT['mixdb']
    output_dir = MP_DICT['output_dir']
    compute_truth = MP_DICT['compute_truth']
    compute_segsnr = MP_DICT['compute_segsnr']
    mixid_padded_name = get_mixid_padded_name(mixdb, mixid)
    output_base = join(output_dir, mixid_padded_name)

    mixture, truth_t, target, noise, segsnr_t = genmix(mixdb=mixdb,
                                                       mixids=mixid,
                                                       raw_target_audios=MP_DICT['raw_target_audios'],
                                                       augmented_noise_audios=MP_DICT['augmented_noise_audios'],
                                                       compute_segsnr=compute_segsnr,
                                                       compute_truth=compute_truth)

    samples = mixture.shape[0]
    if compute_truth:
        if samples != truth_t.shape[0]:
            raise SonusAIError(
                f'truth_t samples does not match mixture samples: {truth_t.shape[0]} != {samples}')
        if mixdb.num_classes != truth_t.shape[1]:
            raise SonusAIError(
                f'truth_t num_classes is incorrect: {truth_t.shape[1]} != {mixdb.num_classes}')
    if samples != target.shape[0]:
        raise SonusAIError(f'target samples does not match mixture samples: {target.shape[0]} != {samples}')
    if samples != noise.shape[0]:
        raise SonusAIError(f'noise samples does not match mixture samples: {noise.shape[0]} != {samples}')
    if compute_segsnr and samples != segsnr_t.shape[0]:
        raise SonusAIError(f'segsnr_t samples does not match mixture samples: {segsnr_t.shape[0]} != {samples}')

    with h5py.File(output_base + '.h5', 'a') as f:
        datasets = ['mixture', 'truth_t', 'target', 'noise', 'segsnr_t']
        for dataset in datasets:
            if dataset in f:
                del f[dataset]

        f.create_dataset(name='mixture', data=mixture, dtype=np.int16)
        if compute_truth:
            f.create_dataset(name='truth_t', data=truth_t, dtype=np.single)
        f.create_dataset(name='target', data=target, dtype=np.int16)
        f.create_dataset(name='noise', data=noise, dtype=np.int16)
        if compute_segsnr:
            f.create_dataset(name='segsnr_t', data=segsnr_t, dtype=np.single)

    with open(file=output_base + '.txt', mode='w') as f:
        f.write(get_mixture_metadata(mixdb, mixdb.mixtures[mixid]))


def main():
    import time
    from os import makedirs
    from os import remove
    from os.path import exists
    from os.path import isdir
    from os.path import join
    from os.path import splitext

    from docopt import docopt
    from tqdm import tqdm

    import sonusai
    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.mixture import get_augmented_noise_audios
    from sonusai.mixture import get_raw_target_audios
    from sonusai.mixture import check_audio_files_exist
    from sonusai.mixture import convert_mixids_to_list
    from sonusai.mixture import load_mixdb
    from sonusai.utils import p_tqdm_map
    from sonusai.utils import human_readable_size
    from sonusai.utils import seconds_to_hms
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    mixdb_name = args['--mixdb']
    mixid = args['--mixid']
    output_dir = args['--output']
    compute_segsnr = args['--segsnr']
    compute_truth = args['--truth']

    if not output_dir:
        output_dir = splitext(mixdb_name)[0]

    if exists(output_dir) and not isdir(output_dir):
        remove(output_dir)

    makedirs(output_dir, exist_ok=True)

    start_time = time.monotonic()

    create_file_handler(join(output_dir, 'genmix.log'))
    update_console_handler(verbose)
    initial_log_messages('genmix')

    logger.info(f'\nLoad mixture database from {mixdb_name}')
    mixdb = load_mixdb(name=mixdb_name)
    mixid = convert_mixids_to_list(mixdb, mixid)

    total_samples = sum([sub.samples for sub in [mixdb.mixtures[m] for m in mixid]])
    duration = total_samples / sonusai.mixture.SAMPLE_RATE

    logger.info('')
    logger.info(f'Found {len(mixid):,} mixtures to process')
    logger.info(f'{total_samples:,} samples')

    check_audio_files_exist(mixdb)

    MP_DICT['mixdb'] = mixdb
    MP_DICT['output_dir'] = output_dir
    MP_DICT['raw_target_audios'] = get_raw_target_audios(mixdb)
    MP_DICT['augmented_noise_audios'] = get_augmented_noise_audios(mixdb)
    MP_DICT['compute_truth'] = compute_truth
    MP_DICT['compute_segsnr'] = compute_segsnr

    progress = tqdm(total=len(mixid), desc='genmix')
    p_tqdm_map(_process_mixture, mixid, progress=progress)
    progress.close()

    logger.info(f'Wrote {len(mixid)} mixtures to {output_dir}')
    logger.info('')
    logger.info(f'Duration: {seconds_to_hms(seconds=duration)}')
    logger.info(f'mixture:  {human_readable_size(total_samples * 2, 1)}')
    if compute_truth:
        logger.info(f'truth_t:  {human_readable_size(total_samples * mixdb.num_classes * 4, 1)}')
    logger.info(f'target:   {human_readable_size(total_samples * 2, 1)}')
    logger.info(f'noise:    {human_readable_size(total_samples * 2, 1)}')
    if compute_segsnr:
        logger.info(f'segsnr:   {human_readable_size(total_samples * 4, 1)}')

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
