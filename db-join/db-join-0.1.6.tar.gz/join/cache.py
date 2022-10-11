"""
"""
import collections.abc


class LRUCache(collections.abc.MutableMapping):
    """
    Least-recently used cache algorithm
    >>> cache = LRUCache(2)
    >>> cache[1] = 'hello'
    >>> cache[2] = 'bye'
    >>> list(cache.items())
    [(1, 'hello'), (2, 'bye')]
    >>> cache[1]
    'hello'
    >>> list(cache.items())
    [(2, 'bye'), (1, 'hello')]
    >>> cache[2] = 'there'
    >>> list(cache.items())
    [(1, 'hello'), (2, 'there')]
    >>> cache[3] = 'intercepted'
    >>> list(cache.items())
    [(2, 'there'), (3, 'intercepted')]
    """
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def keys(self):
        return self.cache.keys()

    def values(self):
        return self.cache.values()

    def items(self):
        return self.cache.items()

    def __iter__(self):
        return iter(self.keys())

    def __getitem__(self, key):
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def __delitem__(self, key):
        self.cache.pop(key)

    def _truncate(self):
        count = len(self.cache) - self.maxsize
        for _ in range(count):
            k = next(iter(self.cache.keys()))
            self.cache.pop(k, None)

    def __setitem__(self, key, val):
        self.cache.pop(key, None)
        self.cache[key] = val
        self._truncate()
