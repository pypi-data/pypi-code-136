import numpy as np

def count_adjacent_true(arr):
    assert len(arr.shape) == 1
    assert arr.dtype == np.bool
    if arr.size == 0:
        return np.empty(0, dtype=int), np.empty(0, dtype=int)
    sw = np.insert(arr[1:] ^ arr[:-1], [0, arr.shape[0]-1], values=True)
    swi = np.arange(sw.shape[0])[sw]
    offset = 0 if arr[0] else 1
    lengths = swi[offset+1::2] - swi[offset:-1:2]
    return swi[offset:-1:2], lengths
