from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Mapping, Protocol, Tuple, TypeVar, Union

from atoti_core import BaseHierarchies, BaseHierarchyBound, keyword_only_dataclass

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._hierarchy_arguments import HierarchyArguments
from ._java_api import JavaApi
from .column import Column
from .level import Level

LevelOrColumn = Union[Level, Column]

_BaseHierarchy = TypeVar("_BaseHierarchy", bound=BaseHierarchyBound, covariant=True)


class _CreateHierarchyFromArguments(Protocol[_BaseHierarchy]):
    def __call__(self, arguments: HierarchyArguments) -> _BaseHierarchy:
        ...


@keyword_only_dataclass
@dataclass(frozen=True)
class LocalHierarchies(  # type: ignore[misc]
    DelegateMutableMapping[
        Tuple[str, str],
        _BaseHierarchy,  # pyright: ignore[reportGeneralTypeIssues]
    ],
    BaseHierarchies[_BaseHierarchy],
):
    """Local hierarchies class."""

    _java_api: JavaApi = field(repr=False)
    _create_hierarchy_from_arguments: _CreateHierarchyFromArguments[_BaseHierarchy]

    @abstractmethod
    def _get_underlying(self) -> Dict[Tuple[str, str], _BaseHierarchy]:
        """Fetch the hierarchies from the JVM each time they are needed."""

    def _update(self, other: Mapping[Tuple[str, str], _BaseHierarchy], /) -> None:
        raise AttributeError(f"{self._get_name()} cube hierarchies cannot be changed.")

    def _get_name(self) -> str:
        return self.__class__.__name__.replace("Hierarchies", "")
