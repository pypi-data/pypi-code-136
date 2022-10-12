from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping, Optional, Protocol

from atoti_core import PathLike, keyword_only_dataclass

from .._path_utils import to_absolute_path
from ..client_side_encryption_config import ClientSideEncryptionConfig
from ..type import DataType
from . import DataSource


def create_csv_params(
    *,
    path: PathLike,
    columns: Mapping[str, str],
    separator: Optional[str],
    encoding: str,
    process_quotes: Optional[bool],
    array_separator: Optional[str],
    pattern: Optional[str],
    date_patterns: Mapping[str, str],
    client_side_encryption: Optional[ClientSideEncryptionConfig],
) -> Mapping[str, Any]:
    """Create the CSV specific parameters."""
    return {
        "absolutePath": to_absolute_path(path),
        "columns": columns,
        "separator": separator,
        "encoding": encoding,
        "processQuotes": process_quotes,
        "arraySeparator": array_separator,
        "globPattern": pattern,
        "datePatterns": date_patterns,
        "clientSideEncryptionConfig": asdict(client_side_encryption)
        if client_side_encryption is not None
        else None,
    }


@keyword_only_dataclass
@dataclass(frozen=True)
class CsvFileFormat:
    process_quotes: bool
    separator: str
    types: Mapping[str, DataType]


class _DiscoverCsvFileFormat(Protocol):
    def __call__(
        self,
        *,
        keys: Iterable[str],
        default_values: Mapping[str, Any],
        source_params: Mapping[str, Any],
    ) -> CsvFileFormat:
        ...


@keyword_only_dataclass
@dataclass(frozen=True)
class CsvDataSource(DataSource):

    _discover_csv_file_format: _DiscoverCsvFileFormat

    @property
    def key(self) -> str:
        return "CSV"

    def discover_file_format(
        self,
        path: PathLike,
        *,
        keys: Iterable[str],
        separator: Optional[str],
        encoding: str,
        process_quotes: Optional[bool],
        array_separator: Optional[str],
        pattern: Optional[str],
        date_patterns: Mapping[str, str],
        default_values: Mapping[str, Any],
        client_side_encryption: Optional[ClientSideEncryptionConfig],
        columns: Mapping[str, str],
    ) -> CsvFileFormat:
        """Infer Table types from a CSV file or directory."""
        source_params = create_csv_params(
            path=path,
            columns=columns,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        return self._discover_csv_file_format(
            keys=keys,
            default_values=default_values,
            source_params=source_params,
        )

    def load_csv_into_table(
        self,
        *,
        path: PathLike,
        table_name: str,
        columns: Mapping[str, str],
        scenario_name: str,
        separator: Optional[str],
        encoding: str,
        process_quotes: Optional[bool],
        array_separator: Optional[str],
        pattern: Optional[str],
        date_patterns: Mapping[str, str],
        client_side_encryption: Optional[ClientSideEncryptionConfig],
    ) -> None:
        source_params = create_csv_params(
            path=path,
            columns=columns,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        self.load_data_into_table(
            table_name,
            scenario_name=scenario_name,
            source_params=source_params,
        )
