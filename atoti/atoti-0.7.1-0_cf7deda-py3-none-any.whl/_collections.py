from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Iterable, Iterator, MutableSet, Set, TypeVar

_Item = TypeVar("_Item")


# This class is a collection wrapper, it's fine to pass the wrapped collection positionally.


@dataclass(frozen=True)
class ReactiveMutableSet(MutableSet[_Item]):  # pylint: disable=keyword-only-dataclass

    """A set which calls a method each time its elements are changed."""

    _data: set[_Item] = field(repr=False)

    @abstractmethod
    def _on_change(self) -> None:
        """Hook called each time the data in the set changes."""

    def __contains__(self, value: object) -> bool:
        return value in self._data

    def add(self, value: _Item) -> None:
        self._data.add(value)
        self._on_change()

    def clear(self) -> None:
        self._data.clear()
        self._on_change()

    def discard(self, value: _Item) -> None:
        self._data.discard(value)
        self._on_change()

    def update(self, *s: Iterable[_Item]) -> None:
        self._data.update(*s)
        self._on_change()

    def __iter__(self) -> Iterator[_Item]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return repr(self._data)


class DelegateMutableSet(MutableSet[_Item]):
    """Mutable set backed by an underlying set."""

    @abstractmethod
    def _get_underlying(self) -> Set[_Item]:
        """Get the underlying set."""

    @abstractmethod
    def _set_underlying(self, new_set: Set[_Item]) -> None:
        """Set the underlying set."""

    def __contains__(self, value: object) -> bool:
        return value in self._get_underlying()

    def __iter__(self) -> Iterator[_Item]:
        return iter(self._get_underlying())

    def __len__(self) -> int:
        return len(self._get_underlying())

    def __repr__(self) -> str:
        return repr(self._get_underlying())

    def add(self, value: _Item) -> None:
        new_set = set(self._get_underlying())
        new_set.add(value)
        self._set_underlying(new_set)

    def clear(self) -> None:
        new_set: Set[_Item] = set()
        self._set_underlying(new_set)

    def discard(self, value: _Item) -> None:
        new_set = set(self._get_underlying())
        new_set.discard(value)
        self._set_underlying(new_set)

    def update(self, *s: Iterable[_Item]) -> None:
        new_set = set(self._get_underlying())
        new_set.update(*s)
        self._set_underlying(new_set)
