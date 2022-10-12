from __future__ import annotations

from dataclasses import dataclass
from typing import List, Mapping, TypeVar

from atoti_core import ReprJson, ReprJsonable, keyword_only_dataclass

from .._external_table_coordinates import ExternalTableCoordinates
from ..type import DataType


@keyword_only_dataclass
@dataclass(frozen=True)
class ExternalTable(ReprJsonable):
    _coordinates: ExternalTableCoordinates

    _database_key: str

    types: Mapping[str, DataType]
    """Mapping from the name of each column to their type."""

    def _repr_json_(self) -> ReprJson:
        data = {name: str(datatype) for name, datatype in self.types.items()}
        return data, {"expanded": True, "root": self._coordinates.table_name}

    @property
    def name(self) -> str:
        """Name of the table."""
        return self._coordinates.table_name

    @property
    def columns(self) -> List[str]:
        """Columns of the table."""
        return list(self.types.keys())


ExternalTableT = TypeVar("ExternalTableT", bound=ExternalTable, covariant=True)
