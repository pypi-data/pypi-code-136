from __future__ import annotations

from dataclasses import dataclass

from atoti_core import keyword_only_dataclass

from .._path_utils import to_absolute_path
from . import DataSource


@keyword_only_dataclass
@dataclass(frozen=True)
class ArrowDataSource(DataSource):
    @property
    def key(self) -> str:
        return "ARROW"

    def load_arrow_into_table(
        self,
        *,
        path: str,
        table_name: str,
        scenario_name: str,
    ) -> None:
        self.load_data_into_table(
            table_name,
            scenario_name=scenario_name,
            source_params={
                "absolutePath": to_absolute_path(path),
            },
        )
