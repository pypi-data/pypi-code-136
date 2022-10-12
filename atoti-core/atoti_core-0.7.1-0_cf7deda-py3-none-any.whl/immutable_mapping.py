from dataclasses import dataclass
from typing import Iterator, Mapping, TypeVar

from .ipython_key_completions import (
    IPythonKeyCompletions,
    get_ipython_key_completions_for_mapping,
)

_Key = TypeVar("_Key")
_Value = TypeVar("_Value")


# This class is a collection wrapper, it's fine to pass the wrapped collection positionally.
@dataclass(frozen=True)
class ImmutableMapping(Mapping[_Key, _Value]):  # pylint: disable=keyword-only-dataclass
    """Immutable mapping."""

    __data: Mapping[_Key, _Value]

    def __getitem__(self, key: _Key) -> _Value:
        """Get the value with the given key."""
        return self.__data[key]

    def __iter__(self) -> Iterator[_Key]:
        """Return the iterator on elements."""
        return iter(self.__data)

    def __len__(self) -> int:
        """Return the number of elements."""
        return len(self.__data)

    def __repr__(self) -> str:
        return repr(self.__data)

    def _ipython_key_completions_(self) -> IPythonKeyCompletions:
        return get_ipython_key_completions_for_mapping(self)  # type: ignore
