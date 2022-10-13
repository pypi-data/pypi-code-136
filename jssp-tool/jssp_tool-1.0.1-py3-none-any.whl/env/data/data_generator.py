import numpy as np


def gen_instance_uniformly(n_j, n_m, low, high):
    # 每个task的处理时长
    durations = np.random.randint(low=low, high=high, size=(n_j, n_m))
    # 机器编号，从0开始
    machines = np.expand_dims(np.arange(0, n_m), axis=0).repeat(repeats=n_j, axis=0)
    machines = _permute_rows(machines)
    return durations, machines


def _permute_rows(x: np.ndarray):
    """
    打乱每个job的machine处理顺序
    Args:
        x (np.ndarray): shape (n_j,n_m)
    """
    ix_i = np.tile(np.arange(x.shape[0]), (x.shape[1], 1)).T
    ix_j = np.random.sample(x.shape).argsort(axis=1)
    return x[ix_i, ix_j]
