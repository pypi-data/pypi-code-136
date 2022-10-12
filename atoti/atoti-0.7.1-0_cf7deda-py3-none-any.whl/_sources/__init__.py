from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Protocol

from atoti_core import EMPTY_MAPPING, keyword_only_dataclass

from ..type import DataType


class _LoadDataIntoTable(Protocol):
    def __call__(
        self,
        *,
        table_name: str,
        source_key: str,
        scenario_name: str,
        source_params: Mapping[str, Any],
    ) -> None:
        ...


class InferTypes(Protocol):
    def __call__(
        self,
        *,
        source_key: str,
        keys: Iterable[str],
        default_values: Mapping[str, Any],
        source_params: Mapping[str, Any],
    ) -> Dict[str, DataType]:
        ...


@keyword_only_dataclass
@dataclass(frozen=True)
class DataSource(ABC):

    _load_data_into_table: _LoadDataIntoTable

    @property
    @abstractmethod
    def key(self) -> str:
        ...

    def load_data_into_table(
        self,
        table_name: str,
        *,
        scenario_name: str,
        source_params: Mapping[str, Any] = EMPTY_MAPPING,
    ) -> None:
        """Load the data into an existing table with a given source.

        Args:
            table_name: The name of the table to feed.
            scenario_name: The name of the scenario to feed.
            source_params: The parameters specific to the source.
        """
        self._load_data_into_table(
            table_name=table_name,
            source_key=self.key,
            scenario_name=scenario_name,
            source_params=source_params,
        )
