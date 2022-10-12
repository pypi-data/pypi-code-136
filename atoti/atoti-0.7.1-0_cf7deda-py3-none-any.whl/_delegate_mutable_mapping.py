from __future__ import annotations

from abc import abstractmethod
from typing import (
    TYPE_CHECKING,
    Dict,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
    ValuesView,
    overload,
)

from atoti_core import IPythonKeyCompletions, get_ipython_key_completions_for_mapping

if TYPE_CHECKING:
    from _typeshed import SupportsKeysAndGetItem  # pylint: disable=nested-import

_Key = TypeVar("_Key")
_Value = TypeVar("_Value")
_Default = TypeVar("_Default")


class DelegateMutableMapping(MutableMapping[_Key, _Value]):
    """Mutable mapping backed by an underlying mapping.

    Reimplement `keys()`, `items()`, and `values()` methods for performance reasons.
    See https://github.com/activeviam/atoti/pull/1162#issuecomment-592551497.
    """

    @abstractmethod
    def _get_underlying(self) -> Dict[_Key, _Value]:
        ...

    @abstractmethod
    def _update(self, other: Mapping[_Key, _Value], /) -> None:
        ...

    @abstractmethod
    def _delete_keys(self, keys: Optional[Iterable[_Key]] = None, /) -> None:
        ...

    def __delitem__(self, key: _Key, /) -> None:
        return self._delete_keys([key])

    def clear(self) -> None:
        return self._delete_keys()

    @overload
    def update(
        self, __m: SupportsKeysAndGetItem[_Key, _Value], **kwargs: _Value
    ) -> None:
        ...

    @overload
    def update(self, __m: Iterable[Tuple[_Key, _Value]], **kwargs: _Value) -> None:
        ...

    @overload
    def update(self, **kwargs: _Value) -> None:
        ...

    # Pyright fails to see that the override is correct but mypy can see it.
    def update(  # type: ignore
        self,
        __m: Optional[
            Union[Mapping[_Key, _Value], Iterable[Tuple[_Key, _Value]]]
        ] = None,
        **kwargs: _Value,
    ) -> None:
        """Update the mapping."""
        other: Dict[_Key, _Value] = {}
        if __m is not None:
            other.update(__m)
        other.update(**kwargs)
        self._update(other)

    def __setitem__(self, key: _Key, value: _Value, /) -> None:
        self.update({key: value})

    def __getitem__(self, key: _Key, /) -> _Value:
        return self._get_underlying()[key]

    def __iter__(self) -> Iterator[_Key]:
        return iter(self._get_underlying())

    def reversed(self) -> Iterator[_Key]:
        return iter(reversed(self.keys()))

    def __len__(self) -> int:
        return len(self._get_underlying())

    def __repr__(self) -> str:
        return repr(self._get_underlying())

    def keys(self) -> KeysView[_Key]:
        return self._get_underlying().keys()

    def items(self) -> ItemsView[_Key, _Value]:
        return self._get_underlying().items()

    def values(self) -> ValuesView[_Value]:
        return self._get_underlying().values()

    def _ipython_key_completions_(self) -> IPythonKeyCompletions:
        return get_ipython_key_completions_for_mapping(self)  # type: ignore

    def _default_to_all_keys(
        self, keys: Optional[Iterable[_Key]] = None, /
    ) -> Iterable[_Key]:
        return self.keys() if keys is None else keys
