from dataclasses import dataclass

from atoti_core import BaseLevel, ReprJson, keyword_only_dataclass


@keyword_only_dataclass
@dataclass(eq=False)
class QueryLevel(BaseLevel):
    """Level of a query cube."""

    _dimension: str
    _hierarchy: str

    @property
    def dimension(self) -> str:
        """Dimension of the level."""
        return self._dimension

    @property
    def hierarchy(self) -> str:
        """Hierarchy of the level."""
        return self._hierarchy

    def _repr_json_(self) -> ReprJson:
        data = {
            "dimension": self.dimension,
            "hierarchy": self.hierarchy,
        }
        return (
            data,
            {"expanded": True, "root": self.name},
        )
