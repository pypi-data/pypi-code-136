from __future__ import annotations

import logging as _logging
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from types import TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Final,
    Iterable,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
    cast,
)
from warnings import warn

import pandas as pd
import pyarrow as pa
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    MissingPluginError,
    PathLike,
    doc,
    keyword_only_dataclass,
)
from atoti_query import QuerySession
from numpy.typing import NDArray

from ._arrow_utils import get_data_types_from_arrow
from ._delegate_mutable_mapping import DelegateMutableMapping
from ._docs_utils import (
    CLIENT_SIDE_ENCRYPTION_DOC,
    CSV_KWARGS,
    EXTERNAL_TABLE_KWARGS,
    PARQUET_KWARGS,
    TABLE_CREATION_KWARGS,
)
from ._file_utils import split_path_and_pattern
from ._local_session import LocalSession
from ._pandas_utils import pandas_to_arrow
from ._path_utils import stem_path
from ._runtime_type_checking_utils import typecheck
from ._sources.csv import CsvDataSource
from ._sources.parquet import ParquetDataSource
from ._spark_utils import write_spark_to_parquet
from ._transaction import Transaction
from .client_side_encryption_config import ClientSideEncryptionConfig
from .config import (
    BasicAuthenticationConfig,
    BrandingConfig,
    ClientCertificateConfig,
    HttpsConfig,
    I18nConfig,
    JwtConfig,
    KerberosConfig,
    LdapConfig,
    LoggingConfig,
    OidcConfig,
    UserContentStorageConfig,
)
from .config._session_config import SessionConfig, create_authentication_config
from .config.user_content_storage_config import (
    _create_user_content_storage_config_from_path_or_url,
)
from .cube import Cube
from .cubes import Cubes
from .directquery import MultiColumnArrayConversion
from .directquery._clustering_columns_parameter import CLUSTERING_COLUMNS_PARAMETER
from .directquery._external_database_connection import ExternalDatabaseConnectionT
from .directquery._external_database_connection_info import (
    ExternalDatabaseConnectionInfo,
)
from .directquery._external_table import ExternalTableT
from .directquery._external_table_options import ExternalTableOptions
from .experimental._distributed.session import DistributedSession
from .table import Table
from .tables import Tables
from .type import DataType

if TYPE_CHECKING:
    # PySpark is only imported for type checking as we don't want it as a dependency
    from pyspark.sql import (  # pylint: disable=undeclared-dependency, nested-import
        DataFrame as SparkDataFrame,
    )

_CubeCreationMode = Literal[  # pylint: disable=invalid-name
    "auto", "manual", "no_measures"
]


def _infer_table_name(
    *, path: PathLike, pattern: Optional[str], table_name: Optional[str]
) -> str:
    """Infer the name of a table given the path and table_name parameters."""
    if pattern is not None and table_name is None:
        raise ValueError(
            "The table_name parameter is required when the path argument is a glob pattern."
        )
    return table_name or stem_path(path).capitalize()


@keyword_only_dataclass
@dataclass(frozen=True)
class _SessionPrivateParameters:
    config: Optional[SessionConfig] = None


@keyword_only_dataclass
@dataclass(frozen=True)
class _CreateTablePrivateParameters:
    is_parameter_table: bool = False


class Session(LocalSession[Cubes]):
    """Holds a connection to the Java gateway."""

    def __init__(
        self,
        *,
        name: Optional[str] = "Unnamed",
        app_extensions: Mapping[str, Union[str, Path]] = EMPTY_MAPPING,
        authentication: Optional[
            Union[BasicAuthenticationConfig, KerberosConfig, LdapConfig, OidcConfig]
        ] = None,
        branding: Optional[BrandingConfig] = None,
        client_certificate: Optional[ClientCertificateConfig] = None,
        extra_jars: Iterable[Union[str, Path]] = (),
        https: Optional[HttpsConfig] = None,
        i18n: Optional[I18nConfig] = None,
        java_options: Iterable[str] = (),
        jwt: Optional[JwtConfig] = None,
        logging: Optional[LoggingConfig] = None,  # pylint: disable=W0621
        port: int = 0,
        same_site: Optional[Literal["none", "strict"]] = None,
        user_content_storage: Optional[
            Union[
                Path,
                str,
                UserContentStorageConfig,
            ]
        ] = None,
        **kwargs: Any,
    ):
        """Create a session.

        Args:

            name: The name of the session.

                For a better prototyping experience in notebooks, creating a session with the same name as an already running session will close the latter one.
                Pass ``None`` to opt out of this behavior.
            app_extensions: Mapping from the name of an extension (i.e. :guilabel:`name` property in their :guilabel:`package.json`) to the path of its :guilabel:`dist` directory.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                Extensions can `enhance the app <../../how_tos/customization/customize_the_app.html>`__ in many ways such as:

                * Adding new type of widgets.
                * Attaching custom menu items or titlebar buttons to a set of widgets.
                * Providing other React contexts to the components rendered by the app.

                The :download:`app extension template <../../app-extension-template/extension.zip>` can be used as a starting point.

                See also:
                    Existing extensions in :mod:`atoti_plus.app_extension`.

            authentication: The configuration to enable authentication on the session.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                Users and roles are configured using :attr:`atoti.Session.security`.
            branding: The config to customize some elements of the UI to change its appearance.
            client_certificate: The config to enable client certificate based authentication on the session.
            extra_jars: The paths to the JARs to add to the classpath of the Java process when starting the session.
            https: The config providing certificates to enable HTTPS on the session.
            i18n: The config to internationalize the session.
            java_options: The additional options to pass when starting the Java process (e.g. for optimization or debugging purposes).

                In particular, the ``-Xmx`` option can be set to increase the amount of RAM that the session can use.

                If this option is not specified, the JVM default memory setting is used which is 25% of the machine memory.
            jwt: The config to set the key pair used to validate JWTs when authenticating with the session.
            logging: The config describing how to handle session logs.
            port: The port on which the session will be exposed.

                Defaults to a random available port.
            same_site: The value to use for the *SameSite* attribute of the HTTP cookie sent by the session when *authentication* is configured.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                See https://web.dev/samesite-cookies-explained for more information.

                Setting it to ``none`` requires the session to be served through HTTPS.

                Defaults to ``lax``.
            user_content_storage: The location of the database where the user content will be stored.
                The user content is what is not part of the data sources, such as the dashboards, widgets, and filters saved in the application.
                If a path to a directory is given, it will be created if needed.
                When ``None``, the user content is kept in memory and is thus lost when the session is closed.
        """
        private_parameters = _SessionPrivateParameters(**kwargs)

        config = private_parameters.config or SessionConfig(
            app_extensions=app_extensions,
            authentication=create_authentication_config(authentication)
            if authentication
            else None,
            branding=branding,
            client_certificate=client_certificate,
            extra_jars=extra_jars,
            https=https,
            i18n=i18n,
            java_options=java_options,
            jwt=jwt,
            logging=logging,  # pylint: disable=W0621
            port=port,
            same_site=same_site,
            user_content_storage=_create_user_content_storage_config_from_path_or_url(
                user_content_storage
            )
            if isinstance(user_content_storage, (Path, str))
            else user_content_storage,
        )

        if name is not None:
            _sessions._clear_duplicate_sessions(name)

        super().__init__(name=name, config=config, distributed=False)

        self._warn_if_license_about_to_expire()
        self._cubes = Cubes(
            _delete_cube=self._java_api.delete_cube,
            _get_cube=self._get_cube,
            _get_cubes=self._get_cubes,
        )
        self._tables = Tables(java_api=self._java_api)

        if name is not None:
            _sessions._sessions[name] = self

    def __enter__(self) -> Session:
        return self

    @property
    def cubes(self) -> Cubes:
        """Cubes of the session."""
        return self._cubes

    @property
    def tables(self) -> Tables:
        """Tables of the session."""
        return self._tables

    @doc(
        **TABLE_CREATION_KWARGS,
        # Declare the types here because blackdoc and doctest conflict when inlining it in the docstring.
        data_types="""{"Date": tt.LOCAL_DATE, "Product": tt.STRING, "Quantity": tt.DOUBLE}""",
    )
    def create_table(
        self,
        name: str,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> Table:
        """Create a table from a schema.

        Args:
            name: The name of the table to create.
            types: Types for all columns of the table.
                This defines the columns which will be expected in any future data loaded into the table.

                See also:
                    :mod:`atoti.type` for data type constants.

            {keys}
            {partitioning}
            {default_values}

        Example:

            >>> from datetime import date
            >>> table = session.create_table(
            ...     "Product",
            ...     types={data_types},
            ...     keys=["Date", "Product"],
            ... )
            >>> table.head()
            Empty DataFrame
            Columns: [Quantity]
            Index: []
            >>> table.append(
            ...     (date(2021, 5, 19), "TV", 15.0),
            ...     (date(2022, 8, 17), "Car", 2.0),
            ... )
            >>> table.head()
                                Quantity
            Date       Product
            2021-05-19 TV           15.0
            2022-08-17 Car           2.0

            Inserting a row with the same key values as an existing row replaces the latter:

            >>> table += (date(2021, 5, 19), "TV", 8.0)
            >>> table.head()
                                Quantity
            Date       Product
            2021-05-19 TV            8.0
            2022-08-17 Car           2.0

        """
        private_parameters = _CreateTablePrivateParameters(**kwargs)
        self._java_api.create_table(
            name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            default_values=default_values,
            is_parameter_table=private_parameters.is_parameter_table,
        )
        return Table(_name=name, _java_api=self._java_api)

    def connect_to_external_database(
        self,
        connection_info: ExternalDatabaseConnectionInfo[
            ExternalDatabaseConnectionT, ExternalTableT
        ],
        /,
    ) -> ExternalDatabaseConnectionT:
        """Connect to an external database using DirectQuery.

        Args:
            connection_info: Information needed to connect to the external database.
                Each `DirectQuery plugin <../../reference.html#directquery>`__ has its own ``*ConnectionInfo`` class.
        """
        self._java_api.connect_to_database(
            connection_info._database_key,
            url=connection_info._url,
            password=connection_info._password,
            options=connection_info._options,
        )
        return connection_info._get_database_connection(self._java_api)

    @doc(**EXTERNAL_TABLE_KWARGS)
    def add_external_table(
        self,
        external_table: ExternalTableT,  # type: ignore
        /,
        table_name: Optional[str] = None,
        *,
        columns: Mapping[str, str] = EMPTY_MAPPING,
        options: Optional[ExternalTableOptions[ExternalTableT]] = None,
    ) -> Table:
        """Add a table from an external database to the session.

        Args:
            external_table: The external database table from which to build the session table.
                Instances of such tables are obtained through an :class:`~atoti.ExternalDatabaseConnection`.
            table_name: The name to give to the table in the session.
                If ``None``, the name of the external table is used.
            {columns}
            options: The database specific options to read the table.
                Each `DirectQuery plugin <../../reference.html#directquery>`__ has its own ``*TableOptions`` class.
        """
        if table_name is None:
            table_name = external_table._coordinates.table_name

        array_conversion = None
        clustering_columns = None
        keys = None
        if options is not None:
            array_conversion = options._array_conversion
            clustering_columns = cast(
                Optional[Sequence[str]],
                options._options.get(CLUSTERING_COLUMNS_PARAMETER),
            )
            keys = options._keys

        if array_conversion is not None:
            if isinstance(array_conversion, MultiColumnArrayConversion):
                self._java_api.add_external_multi_column_array_table(
                    external_table._database_key,
                    array_prefixes=array_conversion.column_prefixes,
                    clustering_columns=clustering_columns,
                    columns=columns,
                    coordinates=external_table._coordinates,
                    keys=keys,
                    local_table_name=table_name,
                )
            else:
                self._java_api.add_external_table_with_multi_row_arrays(
                    external_table._database_key,
                    array_columns=array_conversion.array_columns,
                    clustering_columns=clustering_columns,
                    coordinates=external_table._coordinates,
                    index_column=array_conversion.index_column,
                    local_table_name=table_name,
                    columns=columns,
                )
        else:
            # Table without conversion
            self._java_api.add_external_table(
                external_table._database_key,
                clustering_columns=clustering_columns,
                columns=columns,
                coordinates=external_table._coordinates,
                keys=keys,
                local_table_name=table_name,
            )
        self._java_api.refresh()
        return Table(_name=table_name, _java_api=self._java_api)

    def _synchronize_with_external_database(self) -> None:
        self._java_api.synchronize_with_external_database()

    @doc(**TABLE_CREATION_KWARGS)
    def read_pandas(
        self,
        dataframe: pd.DataFrame,
        /,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> Table:
        """Read a pandas DataFrame into a table.

        All the named indices of the DataFrame are included into the table.
        Multilevel columns are flattened into a single string name.

        Args:
            dataframe: The DataFrame to load.
            {table_name}
            {keys}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from pandas dtypes.
            {default_values}

        Example:
            >>> dataframe = pd.DataFrame(
            ...     columns=["Product", "Price"],
            ...     data=[
            ...         ("phone", 600.0),
            ...         ("headset", 80.0),
            ...         ("watch", 250.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(
            ...     dataframe, keys=["Product"], table_name="Pandas"
            ... )
            >>> table.head().sort_index()
                     Price
            Product
            headset   80.0
            phone    600.0
            watch    250.0

        """
        arrow_table = pandas_to_arrow(dataframe, types=types)
        return self.read_arrow(
            arrow_table,
            table_name=table_name,
            keys=keys,
            partitioning=partitioning,
            types=types,
            default_values=default_values,
            **kwargs,
        )

    @doc(**TABLE_CREATION_KWARGS)
    def read_arrow(
        self,
        table: pa.Table,  # pyright: ignore[reportUnknownParameterType]
        /,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> Table:
        """Read an Arrow Table into a table.

        Args:
            table: The Arrow Table to load.
            {table_name}
            {keys}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from arrow DataTypes.
            {default_values}

        Example:
            >>> import pyarrow as pa
            >>> arrow_table = pa.Table.from_arrays(
            ...     [
            ...         pa.array(["phone", "headset", "watch"]),
            ...         pa.array([600.0, 80.0, 250.0]),
            ...     ],
            ...     names=["Product", "Price"],
            ... )
            >>> arrow_table
            pyarrow.Table
            Product: string
            Price: double
            ----
            Product: [["phone","headset","watch"]]
            Price: [[600,80,250]]
            >>> table = session.read_arrow(
            ...     arrow_table, keys=["Product"], table_name="Arrow"
            ... )
            >>> table.head().sort_index()
                     Price
            Product
            headset   80.0
            phone    600.0
            watch    250.0

        """
        types_from_arrow = get_data_types_from_arrow(table)
        types = {**types_from_arrow, **types} if types is not None else types_from_arrow
        created_table = self.create_table(
            table_name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            default_values=default_values,
            **kwargs,
        )
        created_table.load_arrow(table)
        return created_table

    @doc(**TABLE_CREATION_KWARGS)
    @typecheck(ignored_params=["dataframe"])
    def read_spark(
        self,
        dataframe: SparkDataFrame,
        /,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
    ) -> Table:
        """Read a Spark DataFrame into a table.

        Args:
            dataframe: The DataFrame to load.
            {table_name}
            {keys}
            {partitioning}
            {default_values}

        """
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "spark"
            write_spark_to_parquet(dataframe, directory=path)
            return self.read_parquet(
                path,
                keys=keys,
                table_name=table_name,
                partitioning=partitioning,
                default_values=default_values,
            )

    @doc(**{**TABLE_CREATION_KWARGS, **CSV_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def read_csv(
        self,
        path: PathLike,
        /,
        *,
        keys: Iterable[str] = (),
        table_name: Optional[str] = None,
        separator: Optional[str] = ",",
        encoding: str = "utf-8",
        process_quotes: Optional[bool] = True,
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        columns: Mapping[str, str] = EMPTY_MAPPING,
        array_separator: Optional[str] = None,
        date_patterns: Mapping[str, str] = EMPTY_MAPPING,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> Table:
        """Read a CSV file into a table.

        Args:
            {path}
            {keys}
            table_name: The name of the table to create.
                Required when *path* is a glob pattern.
                Otherwise, defaults to the final component of the *path* argument.
            {separator}
            {encoding}
            {process_quotes}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from the first 1,000 lines.
            {columns}
            {array_separator}
            {date_patterns}
            {default_values}
            {client_side_encryption}

        """
        full_path = path
        path, pattern = split_path_and_pattern(path, ".csv")

        table_name = _infer_table_name(
            path=path, pattern=pattern, table_name=table_name
        )

        csv_file_format = CsvDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _discover_csv_file_format=self._java_api.discover_csv_file_format,
        ).discover_file_format(
            path=path,
            keys=keys,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            default_values=default_values,
            client_side_encryption=client_side_encryption,
            columns=columns,
        )
        types = (
            {**csv_file_format.types, **types}
            if types is not None
            else csv_file_format.types
        )
        process_quotes = (
            process_quotes
            if process_quotes is not None
            else csv_file_format.process_quotes
        )
        separator = separator if separator is not None else csv_file_format.separator

        table = self.create_table(
            table_name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            default_values=default_values,
        )
        table.load_csv(
            full_path,
            columns=columns,
            separator=csv_file_format.separator,
            encoding=encoding,
            process_quotes=csv_file_format.process_quotes,
            array_separator=array_separator,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        return table

    @doc(**{**TABLE_CREATION_KWARGS, **PARQUET_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def read_parquet(
        self,
        path: PathLike,
        /,
        *,
        keys: Iterable[str] = (),
        columns: Mapping[str, str] = EMPTY_MAPPING,
        table_name: Optional[str] = None,
        partitioning: Optional[str] = None,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> Table:
        """Read a Parquet file into a table.

        Args:
            {path}
            {keys}
            {columns}
            table_name: The name of the table to create.
                Required when *path* is a glob pattern.
                Otherwise, defaults to the final component of the *path* argument.
            {partitioning}
            {default_values}
            {client_side_encryption}

        """
        full_path = path
        path, pattern = split_path_and_pattern(path, ".parquet")
        table_name = _infer_table_name(
            path=path, pattern=pattern, table_name=table_name
        )

        inferred_types = ParquetDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _infer_types=self._java_api.infer_table_types_from_source,
        ).infer_parquet_types(
            path=path,
            keys=keys,
            pattern=pattern,
            client_side_encryption=client_side_encryption,
            columns=columns,
            default_values=default_values,
        )

        table = self.create_table(
            table_name,
            types=inferred_types,
            keys=keys,
            partitioning=partitioning,
            default_values=default_values,
        )
        table.load_parquet(
            full_path, client_side_encryption=client_side_encryption, columns=columns
        )
        return table

    @doc(**TABLE_CREATION_KWARGS)
    def read_numpy(
        self,
        array: NDArray[Any],
        /,
        *,
        columns: Sequence[str],
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
    ) -> Table:
        """Read a NumPy 2D array into a new table.

        Args:
            array: The NumPy 2D ndarray to read the data from.
            columns: The names to use for the table's columns.
                They must be in the same order as the values in the NumPy array.
            {table_name}
            {keys}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from numpy data types.
            {default_values}

        """
        dataframe = pd.DataFrame(array, columns=columns)
        return self.read_pandas(
            dataframe,
            table_name=table_name,
            keys=keys,
            partitioning=partitioning,
            types=types,
            default_values=default_values,
        )

    def read_sql(  # pylint: disable=no-self-use
        self,
        sql: str,
        /,
        *,
        url: str,
        table_name: str,
        driver: Optional[str] = None,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        default_values: Mapping[str, Any] = EMPTY_MAPPING,
    ) -> Table:
        raise MissingPluginError("sql")

    def start_transaction(self, scenario_name: str = BASE_SCENARIO_NAME) -> Transaction:
        """Start a transaction to batch several table operations.

        * It is more efficient than doing each table operation one after the other.
        * It avoids possibly incorrect intermediate states (e.g. if loading some new data requires dropping existing rows first).

        .. note::
            Some operations are not allowed during a transaction:

            * Long-running operations such as :meth:`atoti.Table.load_kafka`.
            * Operations changing the structure of the session's tables such as :meth:`atoti.Table.join` or :meth:`atoti.Session.read_parquet`.
            * Operations not related to data loading or dropping such as defining a new measure.
            * Operations on parameter tables created from :meth:`atoti.Cube.create_parameter_hierarchy_from_members` and :meth:`atoti.Cube.create_parameter_simulation`.
            * Operations on other source scenarios than the one the transaction is started on.

        Args:
            scenario_name: The name of the source scenario impacted by all the table operations inside the transaction.

        Example:
            >>> df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("Berlin", 150.0),
            ...         ("London", 240.0),
            ...         ("New York", 270.0),
            ...         ("Paris", 200.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(
            ...     df, keys=["City"], table_name="start_transaction example"
            ... )
            >>> cube = session.create_cube(table)
            >>> extra_df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("Singapore", 250.0),
            ...     ],
            ... )
            >>> with session.start_transaction():
            ...     table += ("New York", 100.0)
            ...     table.drop(table["City"] == "Paris")
            ...     table.load_pandas(extra_df)
            ...
            >>> table.head().sort_index()
                       Price
            City
            Berlin     150.0
            London     240.0
            New York   100.0
            Singapore  250.0

        """
        return Transaction(
            scenario_name,
            start=self._java_api.start_transaction,
            end=self._java_api.end_transaction,
        )

    def create_cube(
        self,
        base_table: Table,
        name: Optional[str] = None,
        *,
        mode: _CubeCreationMode = "auto",
    ) -> Cube:
        """Create a cube based on the passed table.

        Args:
            base_table: The base table of the cube.
            name: The name of the created cube.
                Defaults to the name of the base table.
            mode: The cube creation mode:

                * ``auto``: Creates hierarchies for every key column or non-numeric column of the table, and measures for every numeric column.
                * ``manual``: Does not create any hierarchy or measure (except from the count).
                * ``no_measures``: Creates the hierarchies like ``auto`` but does not create any measures.

        Example:
            >>> table = session.create_table(
            ...     "Table",
            ...     types={"id": tt.STRING, "value": tt.DOUBLE},
            ... )
            >>> cube_auto = session.create_cube(table)
            >>> sorted(cube_auto.measures)
            ['contributors.COUNT', 'update.TIMESTAMP', 'value.MEAN', 'value.SUM']
            >>> list(cube_auto.hierarchies)
            [('Table', 'id')]
            >>> cube_no_measures = session.create_cube(table, mode="no_measures")
            >>> sorted(cube_no_measures.measures)
            ['contributors.COUNT', 'update.TIMESTAMP']
            >>> list(cube_no_measures.hierarchies)
            [('Table', 'id')]
            >>> cube_manual = session.create_cube(table, mode="manual")
            >>> sorted(cube_manual.measures)
            ['contributors.COUNT', 'update.TIMESTAMP']
            >>> list(cube_manual.hierarchies)
            []

        """
        if name is None:
            name = base_table.name

        self._java_api.create_cube_from_table(
            table_name=base_table.name, cube_name=name, creation_mode=mode.upper()
        )
        self._java_api.refresh()
        Cube(
            java_api=self._java_api,
            name=name,
            base_table=base_table,
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
            read_pandas=self.read_pandas,
        )

        return self.cubes[name]

    def create_scenario(self, name: str, *, origin: str = BASE_SCENARIO_NAME) -> None:
        """Create a new source scenario.

        Args:
            name: The name of the scenario.
            origin: The scenario to fork.
        """
        self._java_api.create_scenario(name, origin)

    def delete_scenario(self, name: str) -> None:
        """Delete the source scenario with the provided name if it exists."""
        if name == BASE_SCENARIO_NAME:
            raise ValueError("Cannot delete the base scenario")
        self._java_api.delete_scenario(name)

    @property
    def scenarios(self) -> Sequence[str]:
        """Collection of source scenarios of the session."""
        return self._java_api.get_scenarios()

    def export_translations_template(self, path: PathLike) -> None:
        """Export a template containing all translatable values in the session's cubes.

        Args:
            path: The path at which to write the template.
        """
        self._java_api.export_i18n_template(path)

    def _get_cube(self, cube_name: str) -> Cube:
        java_cube = self._java_api.get_cube(cube_name)
        return Cube(
            java_api=self._java_api,
            name=java_cube.name(),
            base_table=self.tables[java_cube.storeName()],
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
            read_pandas=self.read_pandas,
        )

    def _get_cubes(self) -> Dict[str, Cube]:
        return {
            java_cube.name(): Cube(
                java_api=self._java_api,
                name=java_cube.name(),
                base_table=self.tables[java_cube.storeName()],
                session_name=self.name,
                query_mdx=self.query_mdx,
                execute_gaq=self._create_query_session()._execute_gaq,
                read_pandas=self.read_pandas,
            )
            for java_cube in self._java_api.get_cubes()
        }

    def _warn_if_license_about_to_expire(
        self, *, minimum_remaining_time: timedelta = timedelta(days=7)
    ) -> None:
        remaining_time = self._java_api.license_end_date - datetime.now()
        if remaining_time < minimum_remaining_time:
            required_action = (
                "update to atoti's latest version or upgrade to Atoti+"
                if self._java_api.is_community_license
                else "contact ActiveViam to get a new license"
            )
            warn(
                f"The license is about to expire, {required_action} in the coming {remaining_time.days} days.",
                category=FutureWarning,
            )


_Session = Union[Session, DistributedSession, QuerySession]


@keyword_only_dataclass
@dataclass(frozen=True)
class _Sessions(DelegateMutableMapping[str, _Session]):

    _sessions: Dict[str, _Session] = field(default_factory=dict, init=False)

    def _get_underlying(self) -> Dict[str, _Session]:
        """Get the underlying mapping."""
        self._remove_closed_sessions()
        return self._sessions

    def _clear_duplicate_sessions(self, name: str, /) -> None:
        self._remove_closed_sessions()
        if name in self._sessions:
            _logging.getLogger("atoti.session").warning(
                """Deleting existing "%s" session to create the new one.""", name
            )
            del self[name]

    def __enter__(self) -> _Sessions:
        return self

    def __exit__(  # pylint: disable=too-many-positional-parameters
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.close()

    def close(self) -> None:
        """Close all the opened sessions."""
        for session in self._sessions.values():
            if isinstance(session, Session):
                session.close()

    def _remove_closed_sessions(self) -> None:
        sessions_to_remove = [
            session
            for session in self._sessions.values()
            if isinstance(session, Session) and session.closed
        ]
        for session in sessions_to_remove:
            session_name = session.name

            if session_name is None:
                raise ValueError(
                    "Sessions in this mutable mapping are expected to have a name."
                )

            del self._sessions[session_name]

    def _update(self, other: Mapping[str, _Session], /) -> None:
        self._remove_closed_sessions()
        for session_name, session in other.items():
            if session_name in self._sessions:
                del self[session_name]
            self._sessions[session_name] = session

    def __getitem__(self, key: str, /) -> _Session:
        """Get a session."""
        self._remove_closed_sessions()
        return self._sessions[key]

    def _delete_keys(self, keys: Optional[Iterable[str]] = None, /) -> None:
        self._remove_closed_sessions()
        keys = self._default_to_all_keys(keys)
        for key in keys:
            if key in self._sessions:
                session = self._sessions[key]
                if isinstance(session, Session):
                    session.close()
                del self._sessions[key]


# pylint: disable=invalid-name
_sessions: Final = _Sessions()
