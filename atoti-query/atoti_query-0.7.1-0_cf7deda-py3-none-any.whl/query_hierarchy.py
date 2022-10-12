from dataclasses import dataclass
from typing import Mapping

from atoti_core import BaseHierarchy, keyword_only_dataclass

from .query_level import QueryLevel


@keyword_only_dataclass
@dataclass(eq=False)
class QueryHierarchy(BaseHierarchy[QueryLevel]):
    """Hierarchy of a query cube."""

    _name: str
    _dimension: str
    _levels: Mapping[str, QueryLevel]
    _slicing: bool

    @property
    def levels(self) -> Mapping[str, QueryLevel]:
        """Levels of the hierarchy."""
        return self._levels

    @property
    def dimension(self) -> str:
        """Dimension of the hierarchy."""
        return self._dimension

    @property
    def slicing(self) -> bool:
        """Whether the hierarchy is slicing or not."""
        return self._slicing

    @property
    def name(self) -> str:
        """Name of the hierarchy."""
        return self._name

    def __getitem__(self, key: str, /) -> QueryLevel:
        return self.levels[key]
