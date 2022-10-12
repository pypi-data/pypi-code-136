# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import (Dict, Generic, Iterable, Iterator, List, Mapping, Set,
                    TypeVar)

from plenary.iterate import nested_flatten

__all__ = [
    'PriorityChainMap'
]


_K = TypeVar('_K')
_V = TypeVar('_V')


class PriorityChainMap(Mapping[_K, _V], Generic[_K, _V]):
    def __init__(self, *initial: Mapping[_K, _V]):
        self._maps: Mapping[int, List[Mapping[_K, _V]]] = defaultdict(list)

        for m in initial:
            self.insert(m)

    def _key_set(self) -> Set[_K]:
        key_set: Set[_K] = set()

        for m in self._map_iterable():
            key_set.update(m.keys())

        return key_set

    def _map_iterable(self, reverse_order: bool = False, reverse_list: bool = False) -> Iterable[Mapping[_K, _V]]:
        list_index = -1 if reverse_list else 1

        return nested_flatten(
            v[::list_index] for k, v in sorted(self._maps.items(), key=lambda p: p[0], reverse=reverse_order)
        )

    def insert(self, m: Mapping[_K, _V], order: int = 0, append: bool = False) -> None:
        """ Insert a mapping into the chain at a specified position in the mapping order. If other mappings exist at
        the supplied order index then the new mapping is appended or inserted into the order according to the append
        argument.

        :param m: mapping to add to the chain
        :param order: order/priority, lower order mappings are returned over others when duplicate keys exist
        :param append: if True append the mapping to the end of the mapping list for a given order, otherwise insert
        """
        if append:
            self._maps[order].append(m)
        else:
            self._maps[order].insert(0, m)

    def __getitem__(self, __k: _K) -> _V:
        for m in self._map_iterable():
            try:
                return m[__k]
            except KeyError:
                continue

        raise KeyError(f"Key {__k!r} not found in any map")

    def __len__(self) -> int:
        return len(self._key_set())

    def __iter__(self) -> Iterator[_K]:
        return iter(self._key_set())

    def to_dict(self) -> Dict[_K, _V]:
        return dict(self.items())
