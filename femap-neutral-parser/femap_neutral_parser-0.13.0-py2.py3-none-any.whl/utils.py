"""Misc utilities
"""
from collections.abc import Mapping, MutableMapping

try:
    from Levenshtein import distance

    HAS_LEVENSHTEIN = True
except ImportError:
    import difflib

    HAS_LEVENSHTEIN = False


def get_close_matches(txt, allowed, n=6):
    if not HAS_LEVENSHTEIN:
        return difflib.get_close_matches(txt, allowed, n=n, cutoff=0.1)
    distances = [(k, distance(txt, k)) for k in allowed]
    distances = sorted(distances, key=lambda x: x[1])[:n]
    return [k[0] for k in distances]


class CaseInsensitiveDict(MutableMapping):
    """
    credit:
    https://github.com/kennethreitz/requests/blob/v1.2.3/requests/structures.py#L37
    ---
    A case-insensitive ``dict``-like object.
    Implements all methods and operations of
    ``collections.MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.
    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive:
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.
    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.


    >>> regular_dict = {'a': 5, 'B': 6}
    >>> mydict = CaseInsensitiveDict(regular_dict)
    >>> mydict["A"]
    5
    >>> regular_dict == mydict
    True
    """

    def __init__(self, data=None, **kwargs):
        self._store = dict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        try:
            return self._store[key.lower()][1]
        except KeyError:
            key = key.lower()
            allowed = self._store.keys()
            closest_matches = get_close_matches(key, allowed)
            msg = f"key `{key}` not found. closest found are: {closest_matches}"
            raise KeyError(msg)

    def __contains__(self, key):
        # skip __getitem__
        return key.lower() in self._store

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return ((lowerkey, keyval[1]) for (lowerkey, keyval) in self._store.items())

    def __eq__(self, other):
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    # def __repr__(self):
    #     return '%s(%r)' % (self.__class__.__name__, dict(self.items()))


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
