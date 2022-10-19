from rapidfuzz.process import cdist
from rapidfuzz.string_metric import normalized_levenshtein
import numpy as np

def match(l1, l2, workers=1, cutoff=None):
    assert len(l1) == len(l2)
    assert len(l1) > 0
    assert len(l2) > 0
    assert isinstance(l1[0], str)
    assert isinstance(l2[0], str)
    dist = cdist(l1, l2, scorer=normalized_levenshtein, score_cutoff=cutoff)
    dim = len(l1)
    keep = np.ones(dim, dtype=np.bool)
    result = -1 * np.ones(dim, dtype=np.int)
    scores = np.zeros(dim, dtype=np.float)
    for _ in range(dim):
        dim = np.count_nonzero(keep)
        ind1, ind2 = np.unravel_index(np.argmin(dist[keep,keep], axis=None), (dim,dim))
        result[ind1] = ind2
        scores[ind1] = dist[keep,keep][ind1,ind2]
        keep[ind1] = False
        keep[ind2] = False
    return result, scores
