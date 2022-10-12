# -*- coding: utf-8 -*-
from threading import Lock
from types import MappingProxyType
from typing import Callable, Generic, Iterator, Mapping, TypeVar, Union

_K = TypeVar('_K')
_V = TypeVar('_V')


class MappingProxy(Mapping[_K, _V], Generic[_K, _V]):
    """ A read-only proxy for mapping-like objects. """

    def __init__(self, m: Mapping[_K, _V]):
        self._target = MappingProxyType(m)
        self._target_lock = Lock()

    @property
    def target(self) -> Mapping[_K, _V]:
        """ Get the current target of the proxy.

        :return: current proxy target
        """
        return self._target

    @target.setter
    def target(self, m: Mapping[_K, _V]) -> None:
        """ Update the target of the proxy.

        :param m: new proxy mapping target
        """
        with self._target_lock:
            self._target = MappingProxyType(m)

    def __getitem__(self, __k: _K) -> _V:
        with self._target_lock:
            return self.target[__k]

    def __len__(self) -> int:
        with self._target_lock:
            return len(self.target)

    def __iter__(self) -> Iterator[_K]:
        with self._target_lock:
            return self.target.__iter__()


StrProxyTypes = Union[Callable[[], str], int, float, str, object]


class StrProxy:
    def __init__(self, s: StrProxyTypes):
        self._target = s
        self._target_lock = Lock()

    @property
    def target(self) -> StrProxyTypes:
        with self._target_lock:
            return self.target

    @target.setter
    def target(self, t: StrProxyTypes) -> None:
        with self._target_lock:
            self._target = t

    def __str__(self) -> str:
        with self._target_lock:
            if callable(self._target):
                return self._target()
            else:
                return str(self._target)
