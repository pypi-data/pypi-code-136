"""sonusai genft

usage: genft [-hvs] (-d MIXDB) [-i MIXID] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    -i MIXID, --mixid MIXID         Mixture ID(s) to generate. [default: *].
    -o OUTPUT, --output OUTPUT      Output directory.
    -s, --segsnr                    Save segsnr. [default: False].

Generate SonusAI feature/truth data from a SonusAI mixture database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file.
    MIXID       A glob of mixture ID(s) to generate.

Outputs:
    OUTPUT/     A directory containing:
                    <id>.h5:
                        dataset:    feature
                        dataset:    truth_f
                        dataset:    segsnr (optional)
                    <id>.txt
                    genft.log

"""
from typing import List

import numpy as np

from sonusai import logger
from sonusai.mixture import MixtureDatabase
from sonusai.mixture import MixtureIDs

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = {}


def genft(mixdb: MixtureDatabase,
          mixids: MixtureIDs,
          raw_target_audios: List[np.ndarray] = None,
          augmented_noise_audios: List[List[np.ndarray]] = None,
          mixture: np.ndarray = None,
          truth_t: np.ndarray = None,
          segsnr_t: np.ndarray = None,
          compute_truth: bool = True,
          compute_segsnr: bool = False) -> (np.ndarray,
                                            np.ndarray,
                                            np.ndarray):
    import multiprocessing as mp

    from sonusai.mixture import convert_mixids_to_list
    from sonusai.mixture import extract_results
    from sonusai.mixture import get_feature_and_truth_f
    from sonusai.utils import p_map

    mixids = convert_mixids_to_list(mixdb, mixids)
    results = []
    if mp.current_process().daemon:
        for mixid in mixids:
            results.append(get_feature_and_truth_f(mixdb=mixdb,
                                                   mrecord=mixdb.mixtures[mixid],
                                                   mixture=mixture,
                                                   truth_t=truth_t,
                                                   segsnr_t=segsnr_t,
                                                   raw_target_audios=raw_target_audios,
                                                   augmented_noise_audios=augmented_noise_audios,
                                                   compute_truth=compute_truth,
                                                   compute_segsnr=compute_segsnr))
    else:
        MP_DICT['mixdb'] = mixdb
        MP_DICT['mixture'] = mixture
        MP_DICT['truth_t'] = truth_t
        MP_DICT['segsnr_t'] = segsnr_t
        MP_DICT['raw_target_audios'] = raw_target_audios
        MP_DICT['augmented_noise_audios'] = augmented_noise_audios
        MP_DICT['compute_truth'] = compute_truth
        MP_DICT['compute_segsnr'] = compute_segsnr

        results = p_map(_genft_kernel, mixids)

    return extract_results(results)


def _genft_kernel(mixid: int) -> None:
    from sonusai.mixture import get_feature_and_truth_f

    return get_feature_and_truth_f(mixdb=MP_DICT['mixdb'],
                                   mrecord=MP_DICT['mixdb'].mixtures[mixid],
                                   raw_target_audios=MP_DICT['raw_target_audios'],
                                   augmented_noise_audios=MP_DICT['augmented_noise_audios'],
                                   mixture=MP_DICT['mixture'],
                                   truth_t=MP_DICT['truth_t'],
                                   segsnr_t=MP_DICT['segsnr_t'],
                                   compute_truth=MP_DICT['compute_truth'],
                                   compute_segsnr=MP_DICT['compute_segsnr'])


def _process_mixture(mixid: int) -> None:
    from os.path import join

    import h5py

    from sonusai.mixture import get_mixid_padded_name
    from sonusai.mixture import get_mixture_metadata

    mixdb = MP_DICT['mixdb']
    compute_segsnr = MP_DICT['compute_segsnr']
    mixid_padded_name = get_mixid_padded_name(mixdb, mixid)
    output_base = join(MP_DICT['output_dir'], mixid_padded_name)

    with h5py.File(output_base + '.h5', 'a') as f:
        mixture_t = None
        if 'mixture' in f:
            mixture_t = np.array(f['mixture'])

        truth_t = None
        if 'truth_t' in f:
            truth_t = np.array(f['truth_t'])

        segsnr_t = None
        if compute_segsnr and 'segsnr_t' in f:
            segsnr_t = np.array(f['segsnr_t'])

        feature, truth_f, segsnr = genft(mixdb=mixdb,
                                         mixids=mixid,
                                         raw_target_audios=MP_DICT['raw_target_audios'],
                                         augmented_noise_audios=MP_DICT['augmented_noise_audios'],
                                         mixture=mixture_t,
                                         truth_t=truth_t,
                                         segsnr_t=segsnr_t,
                                         compute_segsnr=compute_segsnr)

        datasets = ['feature', 'truth_f', 'segsnr']
        for dataset in datasets:
            if dataset in f:
                del f[dataset]

        f.create_dataset(name='feature', data=feature, dtype=np.single)
        f.create_dataset(name='truth_f', data=truth_f, dtype=np.single)
        if compute_segsnr:
            f.create_dataset(name='segsnr', data=segsnr, dtype=np.single)

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
    from pyaaware import FeatureGenerator
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

    if not output_dir:
        output_dir = splitext(mixdb_name)[0]

    if exists(output_dir) and not isdir(output_dir):
        remove(output_dir)

    makedirs(output_dir, exist_ok=True)

    start_time = time.monotonic()

    create_file_handler(join(output_dir, 'genft.log'))
    update_console_handler(verbose)
    initial_log_messages('genft')

    logger.info(f'\nLoad mixture database from {mixdb_name}')
    mixdb = load_mixdb(name=mixdb_name)
    mixid = convert_mixids_to_list(mixdb, mixid)

    total_samples = sum([sub.samples for sub in [mixdb.mixtures[m] for m in mixid]])
    duration = total_samples / sonusai.mixture.SAMPLE_RATE
    total_transform_frames = total_samples // mixdb.frame_size
    total_feature_frames = total_samples // mixdb.feature_step_samples

    logger.info('')
    logger.info(f'Found {len(mixid):,} mixtures to process')
    logger.info(f'{total_samples:,} samples, '
                f'{total_transform_frames:,} transform frames, '
                f'{total_feature_frames:,} feature frames')

    check_audio_files_exist(mixdb)

    fg = FeatureGenerator(frame_size=mixdb.frame_size,
                          feature_mode=mixdb.feature,
                          num_classes=mixdb.num_classes,
                          truth_mutex=mixdb.truth_mutex)

    MP_DICT['mixdb'] = mixdb
    MP_DICT['output_dir'] = output_dir
    MP_DICT['raw_target_audios'] = get_raw_target_audios(mixdb)
    MP_DICT['augmented_noise_audios'] = get_augmented_noise_audios(mixdb)
    MP_DICT['compute_segsnr'] = compute_segsnr

    progress = tqdm(total=len(mixid), desc='genft')
    p_tqdm_map(_process_mixture, mixid, progress=progress)
    progress.close()

    logger.info(f'Wrote {len(mixid)} mixtures to {output_dir}')
    logger.info('')
    logger.info(f'Duration: {seconds_to_hms(seconds=duration)}')
    logger.info(f'feature:  {human_readable_size(total_feature_frames * fg.stride * fg.num_bands * 4, 1)}')
    logger.info(f'truth_f:  {human_readable_size(total_feature_frames * mixdb.num_classes * 4, 1)}')
    if compute_segsnr:
        logger.info(f'segsnr:   {human_readable_size(total_transform_frames * 4, 1)}')

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
