from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Mapping, TypeVar

from atoti_core import keyword_only_dataclass

from .._external_table_coordinates import ExternalTableCoordinates
from .._java_api import JavaApi
from ..directquery import ExternalTables
from ..type import DataType
from ._external_table import ExternalTable, ExternalTableT


@keyword_only_dataclass
@dataclass(frozen=True)
class ExternalDatabaseConnection(Generic[ExternalTableT], ABC):
    _java_api: JavaApi
    _database_key: str

    @property
    def tables(self) -> ExternalTables[ExternalTableT]:
        """Tables of the external database."""
        table_descriptions = self._java_api.get_external_tables(self._database_key)
        return ExternalTables(
            _tables=table_descriptions,
            _database_key=self._database_key,
            _create_table=lambda coordinates: self._discover_and_create_table(
                coordinates
            ),
        )

    @abstractmethod
    def _create_table(
        self,
        coordinates: ExternalTableCoordinates,
        /,
        *,
        types: Mapping[str, DataType],
    ) -> ExternalTableT:
        ...

    def _discover_and_create_table(
        self,
        coordinates: ExternalTableCoordinates,
    ) -> ExternalTableT:
        columns = self._java_api.get_external_table_schema(
            self._database_key, coordinates=coordinates
        )
        return self._create_table(coordinates, types=columns)


ExternalDatabaseConnectionT = TypeVar(
    "ExternalDatabaseConnectionT",
    bound=ExternalDatabaseConnection[ExternalTable],
)
