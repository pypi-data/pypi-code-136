from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, Iterable, Mapping, Optional

from atoti_core import PathLike, keyword_only_dataclass

from .._path_utils import to_absolute_path
from ..client_side_encryption_config import ClientSideEncryptionConfig
from ..type import DataType
from . import DataSource, InferTypes


def create_parquet_params(
    *,
    path: PathLike,
    pattern: Optional[str],
    columns: Mapping[str, str],
    client_side_encryption: Optional[ClientSideEncryptionConfig],
) -> Dict[str, Any]:
    """Create the Parquet specific parameters."""
    return {
        "absolutePath": to_absolute_path(path),
        "globPattern": pattern,
        "columns": columns,
        "clientSideEncryptionConfig": asdict(client_side_encryption)
        if client_side_encryption is not None
        else None,
    }


@keyword_only_dataclass
@dataclass(frozen=True)
class ParquetDataSource(DataSource):

    _infer_types: InferTypes

    @property
    def key(self) -> str:
        return "PARQUET"

    def infer_parquet_types(
        self,
        *,
        path: PathLike,
        keys: Iterable[str],
        pattern: Optional[str],
        client_side_encryption: Optional[ClientSideEncryptionConfig],
        columns: Mapping[str, str],
        default_values: Mapping[str, Any],
    ) -> Dict[str, DataType]:
        return self._infer_types(
            source_key=self.key,
            keys=keys,
            default_values=default_values,
            source_params=create_parquet_params(
                path=path,
                pattern=pattern,
                columns=columns,
                client_side_encryption=client_side_encryption,
            ),
        )

    def load_parquet_into_table(
        self,
        *,
        path: PathLike,
        table_name: str,
        columns: Mapping[str, str],
        scenario_name: str,
        pattern: Optional[str] = None,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> None:
        self.load_data_into_table(
            table_name,
            scenario_name=scenario_name,
            source_params=create_parquet_params(
                path=path,
                pattern=pattern,
                columns=columns,
                client_side_encryption=client_side_encryption,
            ),
        )
