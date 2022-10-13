import numbers

import pandas as pd

try:
    from Levenshtein import distance, ratio

    HAS_LEVENSHTEIN = True
except ImportError:
    import difflib

    HAS_LEVENSHTEIN = False


def get_close_matches(txt, allowed, n=4):
    """
    >>> get_close_matches("ratatouille",
    ...                   ["rastaquere", "moule à gaufres", "broucouille"],
    ...                   n=2)
    ['broucouille', 'rastaquere']
    """
    if not HAS_LEVENSHTEIN:
        return difflib.get_close_matches(txt, allowed, n=n, cutoff=0.1)
    distances = [(k, ratio(txt, k)) for k in allowed]
    sorted_distances = sorted(distances, key=lambda x: x[1])
    sorted_distances = sorted_distances[::-1][:n]
    return [k[0] for k in sorted_distances]
