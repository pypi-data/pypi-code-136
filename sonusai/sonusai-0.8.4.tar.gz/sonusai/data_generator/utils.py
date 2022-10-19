from sonusai.mixture import MRecords
from sonusai.mixture import MixtureDatabase


def get_frames_per_batch_from_mixdb(mixdb: MixtureDatabase,
                                    mixtures: MRecords,
                                    batch_size: int,
                                    timesteps: int) -> (int, int):
    from sonusai import SonusAIError

    frames = sum([sub.samples for sub in mixtures]) // mixdb.feature_step_samples
    frames_per_batch = get_frames_per_batch(batch_size, timesteps)
    total_batches = frames // frames_per_batch
    if total_batches == 0:
        raise SonusAIError(
            f'Error: dataset only contains {frames} frames which is not enough to fill a batch size of '
            f'{frames_per_batch}. Either provide more data or decrease the batch size')

    return frames_per_batch, total_batches


def get_frames_per_batch(batch_size: int, timesteps: int) -> int:
    return batch_size if timesteps == 0 else batch_size * timesteps
