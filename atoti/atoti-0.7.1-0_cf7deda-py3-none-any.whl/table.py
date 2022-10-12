from __future__ import annotations

import pathlib
import tempfile
from dataclasses import dataclass, field
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import pandas as pd
import pyarrow as pa
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    IPythonKeyCompletions,
    MissingPluginError,
    ReprJson,
    ReprJsonable,
    deprecated,
    doc,
    get_ipython_key_completions_for_mapping,
    keyword_only_dataclass,
)
from numpy.typing import NDArray

from ._arrow_utils import write_arrow_to_file
from ._base_column_condition import BaseColumnCondition, ColumnConditionCoordinates
from ._docs_utils import (
    CLIENT_SIDE_ENCRYPTION_DOC,
    CSV_KWARGS,
    PARQUET_KWARGS,
    TABLE_APPEND_DOC,
    TABLE_IADD_DOC,
)
from ._file_utils import split_path_and_pattern
from ._java_api import JavaApi
from ._pandas_utils import pandas_to_arrow
from ._report import TableReport
from ._runtime_type_checking_utils import typecheck
from ._sources.arrow import ArrowDataSource
from ._sources.csv import CsvDataSource
from ._sources.parquet import ParquetDataSource
from ._spark_utils import write_spark_to_parquet
from .client_side_encryption_config import ClientSideEncryptionConfig
from .column import Column
from .type import DataType

if TYPE_CHECKING:
    from pyspark.sql import (  # pylint: disable=undeclared-dependency, nested-import
        DataFrame as SparkDataFrame,
    )

_Row = Union[Tuple[Any, ...], Mapping[str, Any]]

_DOC_KWARGS = {"what": "table"}


@keyword_only_dataclass
@dataclass
class Table(ReprJsonable):
    """Represents a single table."""

    _name: str
    _java_api: JavaApi = field(repr=False)
    _scenario: str = field(default=BASE_SCENARIO_NAME)
    _columns: Dict[str, Column] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name in self._java_api.get_table_column_names(self._name):
            self._columns[name] = Column(
                _name=name,
                _table_keys=self.keys,
                _table_name=self._name,
                _get_column_data_type=self._java_api.get_column_data_type,
                _get_column_default_value=self._java_api.get_column_default_value,
                _set_column_default_value=self._java_api.set_column_default_value,
            )

    @property
    def name(self) -> str:
        """Name of the table."""
        return self._name

    @property
    def keys(self) -> List[str]:
        """Names of the key columns of the table."""
        keys = self._java_api.get_key_columns(self.name)
        sorted_keys = [
            column
            for column in self._java_api.get_table_column_names(self._name)
            if column in keys
        ]
        return sorted_keys

    @property
    def scenario(self) -> str:
        """Scenario on which the table is."""
        return self._scenario

    @property
    def columns(self) -> Sequence[str]:
        """Columns of the table."""
        return list(self._columns)

    @property
    def _types(self) -> Mapping[str, DataType]:
        """Columns and their types."""
        return {name: col.data_type for name, col in self._columns.items()}

    @property
    def _partitioning(self) -> str:
        """Table partitioning."""
        return self._java_api.get_table_partitioning(self.name)

    def join(
        self,
        other: Table,
        /,
        *,
        mapping: Optional[Mapping[str, str]] = None,
    ) -> None:
        """Define a join between this table and another.

        There are two kinds of joins:

        * full join if all the key columns of the *other* table are mapped and the joined tables share the same locality (either both :class:`~atoti.Table` or both :class:`~atoti.ExternalTable`).
        * partial join otherwise.

        Depending on the cube creation mode, the join will also generate different hierarchies and measures:

        * ``manual``: No hierarchy is automatically created.
          For partial joins, creating a hierarchy for each mapped key column is necessary before creating hierarchies for the other columns.
          Once these required hierarchies exist, hierarchies for the un-mapped key columns of the *other* table will automatically be created.
        * ``no_measures``: All the key columns and non-numeric columns of the *other* table will be converted into hierarchies.
          No measures will be created in this mode.
        * ``auto``: The same hierarchies as in the ``no_measures`` mode will be created.
          Additionally, columns of the base table containing numeric values (including arrays), except for columns which are keys, will be converted into measures.
          Columns of the *other* table with these types will not be converted into measures.

        Args:
            other: The other table to join.
            mapping: The column mapping of the join.
              If ``None``, the key columns of the target table with the same names as columns in this table will be used.
        """
        # Check mapping
        for self_column_name, other_column_name in (mapping or {}).items():
            self[self_column_name]  # pylint: disable=pointless-statement
            other[other_column_name]  # pylint: disable=pointless-statement

        self._java_api.create_join(
            self.name,
            other.name,
            mapping=mapping,
        )

    @property
    def scenarios(self) -> TableScenarios:
        """All the scenarios the table can be on."""
        if self.scenario != BASE_SCENARIO_NAME:
            raise Exception("You can only create a new scenario from the base scenario")
        return TableScenarios(_java_api=self._java_api, _table=self)

    @property
    def _loading_report(self) -> TableReport:
        return TableReport(
            _clear_reports=self._java_api.clear_loading_report,
            _get_reports=self._java_api.get_loading_report,
            _table_name=self.name,
        )

    def __getitem__(self, key: str) -> Column:
        """Return the column with the given name."""
        return self._columns[key]

    def __len__(self) -> int:
        """Return the number of rows in the table."""
        return self._java_api.get_table_size(self.name, table_scenario=self.scenario)

    def _ipython_key_completions_(self) -> IPythonKeyCompletions:
        return get_ipython_key_completions_for_mapping(self._columns)

    @doc(TABLE_APPEND_DOC, **_DOC_KWARGS)
    def append(self, *rows: _Row) -> None:
        rows_df = pd.DataFrame(rows, columns=self.columns)
        self.load_pandas(rows_df)

    @doc(TABLE_IADD_DOC, **_DOC_KWARGS)
    def __iadd__(self, row: _Row) -> Table:
        """Add a single row to the table."""
        self.append(row)
        return self

    def drop(
        self,
        *filter: Union[
            BaseColumnCondition, Mapping[str, Any]
        ],  # pylint: disable=redefined-builtin
    ) -> None:
        """Delete some of the table's rows.

        Args:
            filter: Rows where this condition evaluates to ``True`` will be deleted.
                If ``None``, all the rows will be deleted.

        Example:
            >>> df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("London", 240.0),
            ...         ("New York", 270.0),
            ...         ("Paris", 200.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(df, keys=["City"], table_name="Cities")
            >>> table.head().sort_index()
                      Price
            City
            London    240.0
            New York  270.0
            Paris     200.0
            >>> table.drop((table["City"] == "Paris") | (table["Price"] <= 250.0))
            >>> table.head().sort_index()
                      Price
            City
            New York  270.0
            >>> table.drop()
            >>> table.head()
            Empty DataFrame
            Columns: [Price]
            Index: []
        """
        column_condition_coordinates: List[List[ColumnConditionCoordinates]] = []
        if len(filter) > 1 or any(
            isinstance(condition, Mapping) for condition in filter
        ):
            deprecated(
                "Passing one or several mappings is deprecated, pass a `Condition` instead."
            )
        if filter is not None:
            for condition in filter:
                if isinstance(condition, BaseColumnCondition):
                    column_condition_coordinates += condition._to_coordinates()
                else:
                    column_condition_coordinates += [
                        [
                            cast(
                                ColumnConditionCoordinates,
                                (column_name, value, "eq", self[column_name].data_type),
                            )
                            for column_name, value in condition.items()
                        ]
                    ]
        self._java_api.delete_rows_from_table(
            table_name=self.name,
            scenario_name=self.scenario,
            coordinates=column_condition_coordinates,
        )

    def _repr_json_(self) -> ReprJson:
        return {
            name: column._repr_json_()[0] for name, column in self._columns.items()
        }, {"expanded": True, "root": self.name}

    def head(self, n: int = 5) -> pd.DataFrame:
        """Return at most *n* random rows of the table as a pandas DataFrame."""
        if n < 1:
            raise ValueError("n must be at least 1.")

        return self._java_api.get_table_dataframe(
            self.name,
            n,
            types=self._types,
            scenario_name=self.scenario,
            keys=self.keys,
        )

    @doc(**{**CSV_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def load_csv(
        self,
        path: Union[pathlib.Path, str],
        /,
        *,
        columns: Mapping[str, str] = EMPTY_MAPPING,
        separator: Optional[str] = ",",
        encoding: str = "utf-8",
        process_quotes: Optional[bool] = True,
        array_separator: Optional[str] = None,
        date_patterns: Mapping[str, str] = EMPTY_MAPPING,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> None:
        """Load a CSV into this scenario.

        Args:
            {path}
            {columns}
            {separator}
            {encoding}
            {process_quotes}
            {array_separator}
            {date_patterns}
            {client_side_encryption}
        """
        path, pattern = split_path_and_pattern(path, ".csv")

        CsvDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _discover_csv_file_format=self._java_api.discover_csv_file_format,
        ).load_csv_into_table(
            path=path,
            table_name=self.name,
            columns=columns,
            scenario_name=self.scenario,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )

    def load_pandas(
        self,
        dataframe: pd.DataFrame,
        /,
    ) -> None:
        """Load a pandas DataFrame into this scenario.

        Args:
            dataframe: The DataFrame to load.
        """

        arrow_table = pandas_to_arrow(dataframe, types=self._types)
        self.load_arrow(arrow_table)

    def load_arrow(
        self,
        table: pa.Table,  # pyright: ignore[reportUnknownParameterType]
        /,
    ) -> None:
        """Load an Arrow Table into this scenario.

        Args:
            table: The Arrow Table to load.
        """
        with tempfile.TemporaryDirectory() as directory:
            filepath = pathlib.Path(directory) / "table.arrow"
            write_arrow_to_file(table, filepath=filepath)
            ArrowDataSource(
                _load_data_into_table=self._java_api.load_data_into_table
            ).load_arrow_into_table(
                table_name=self.name, path=str(filepath), scenario_name=self.scenario
            )

    def load_numpy(
        self,
        array: NDArray[Any],
        /,
    ) -> None:
        """Load a NumPy 2D array into this scenario.

        Args:
            array: The 2D array to load.
        """
        dataframe = pd.DataFrame(array, columns=self.columns)
        self.load_pandas(dataframe)

    @doc(**{**PARQUET_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def load_parquet(
        self,
        path: Union[pathlib.Path, str],
        /,
        *,
        columns: Mapping[str, str] = EMPTY_MAPPING,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> None:
        """Load a Parquet file into this scenario.

        Args:
            {path}
            {columns}
            {client_side_encryption}
        """
        path, pattern = split_path_and_pattern(path, ".parquet")
        ParquetDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _infer_types=self._java_api.infer_table_types_from_source,
        ).load_parquet_into_table(
            path=path,
            table_name=self.name,
            columns=columns,
            scenario_name=self.scenario,
            pattern=pattern,
            client_side_encryption=client_side_encryption,
        )

    @typecheck(ignored_params=["dataframe"])
    def load_spark(
        self,
        dataframe: SparkDataFrame,
        /,
    ) -> None:
        """Load a Spark DataFrame into this scenario.

        Args:
            dataframe: The dataframe to load.
        """
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "spark"
            write_spark_to_parquet(dataframe, directory=path)
            self.load_parquet(path)

    def load_kafka(  # pylint: disable=no-self-use
        self,
        bootstrap_server: str,
        topic: str,
        *,
        group_id: str,
        batch_duration: int = 1000,
        consumer_config: Mapping[str, str],
    ) -> None:
        raise MissingPluginError("kafka")

    def load_sql(  # pylint: disable=no-self-use
        self,
        sql: str,
        /,
        *,
        url: str,
        driver: Optional[str] = None,
    ) -> None:
        raise MissingPluginError("sql")


@keyword_only_dataclass
@dataclass(frozen=True)
class TableScenarios:
    """Scenarios of a table."""

    _java_api: JavaApi = field(repr=False)
    _table: Table = field(repr=False)

    def __getitem__(self, key: str) -> Table:
        """Get the scenario or create it if it does not exist.

        Args:
            key: the name of the scenario

        """
        return Table(_name=self._table.name, _java_api=self._java_api, _scenario=key)

    def __delitem__(self, key: str) -> None:
        raise Exception(
            "You cannot delete a scenario from a table since they are shared between all tables."
            "Use the Session.delete_scenario() method instead."
        )
