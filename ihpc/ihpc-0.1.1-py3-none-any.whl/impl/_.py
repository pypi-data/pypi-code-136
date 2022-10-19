'''Generic implementation
'''


__all__ = ['CacheClear', 'Generic', 'New']


import functools as f
import typing as t

if t.TYPE_CHECKING:
    from typing_extensions import Self


class CacheClear:
    '''`functools._lru_cache_wrapper.cache_clear`
    '''

    def cache_clear(self) -> 'Self':
        self._cache_clear()
        return self

    @classmethod
    def _cache_clear(cls) -> None:
        for attr in dir(cls):
            obj = getattr(cls, attr)
            if isinstance(obj, f._lru_cache_wrapper):
                obj.cache_clear()


class New:
    '''Object constructor
    '''

    @classmethod
    def new(cls, *args, **kwargs) -> 'Self':
        return cls(*args, **kwargs)


class Generic(CacheClear, New):
    pass
