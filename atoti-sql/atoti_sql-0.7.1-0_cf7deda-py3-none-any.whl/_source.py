from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Optional

from atoti_core import EMPTY_MAPPING, doc, keyword_only_dataclass

import atoti as tt
from atoti._docs_utils import TABLE_CREATION_KWARGS
from atoti._jdbc_utils import normalize_jdbc_url
from atoti._sources import DataSource, InferTypes

from ._infer_driver import infer_driver

SQL_KWARGS = {
    "url": """url: The JDBC connection string of the database.
            The ``jdbc:`` prefix is optional but the database specific part (such as ``h2:`` or ``mysql:``) is mandatory.
            For instance:

                * ``h2:file:/home/user/database/file/path;USER=username;PASSWORD=passwd``
                * ``mysql://localhost:7777/example?user=username&password=passwd``
                * ``postgresql://postgresql.db.server:5430/example?user=username&password=passwd``

            More examples can be found `here <https://www.baeldung.com/java-jdbc-url-format>`__.""",
    "sql": """sql: The result of this SQL query will be loaded into the table.""",
    "driver": """driver: The JDBC driver used to load the data.
            If ``None``, the driver is inferred from the URL.
            Drivers can be found in the :mod:`atoti_sql.drivers` module.""",
}


def _create_source_params(
    *,
    driver: str,
    sql: str,
    url: str,
) -> Dict[str, Any]:
    return {
        "driverClass": driver,
        "query": sql,
        "url": url,
    }


@keyword_only_dataclass
@dataclass(frozen=True)
class SqlDataSource(DataSource):

    _infer_types: InferTypes

    @property
    def key(self) -> str:
        return "JDBC"

    def load_sql_into_table(
        self,
        sql: str,
        *,
        driver: str,
        scenario_name: str,
        table: tt.Table,
        url: str,
    ) -> None:
        source_params = _create_source_params(
            driver=driver,
            sql=sql,
            url=url,
        )
        self.load_data_into_table(
            table.name,
            scenario_name=scenario_name,
            source_params=source_params,
        )

    def infer_sql_types(
        self,
        sql: str,
        *,
        keys: Iterable[str],
        default_values: Mapping[str, Any],
        url: str,
        driver: str,
    ) -> Dict[str, tt.DataType]:
        source_params = _create_source_params(
            driver=driver,
            sql=sql,
            url=url,
        )
        return self._infer_types(
            source_key=self.key,
            keys=keys,
            default_values=default_values,
            source_params=source_params,
        )


@doc(**{**TABLE_CREATION_KWARGS, **SQL_KWARGS})
def read_sql(
    self: tt.Session,
    sql: str,
    /,
    *,
    url: str,
    table_name: str,
    driver: Optional[str] = None,
    keys: Iterable[str] = (),
    partitioning: Optional[str] = None,
    types: Mapping[str, tt.DataType] = EMPTY_MAPPING,
    default_values: Mapping[str, Any] = EMPTY_MAPPING,
) -> tt.Table:
    """Create a table from the result of the passed SQL query.

    Note:
        This method requires the :mod:`atoti-sql <atoti_sql>` plugin.

    Args:
        {sql}
        {url}
        {driver}
        {table_name}
        {keys}
        {partitioning}
        types: Types for some or all columns of the table.
            Types for non specified columns will be inferred from the SQL types.
        {default_values}

    Example:
        .. doctest:: read_sql

            >>> table = session.read_sql(
            ...     "SELECT * FROM MYTABLE;",
            ...     url=f"h2:file:{{RESOURCES}}/h2-database;USER=root;PASSWORD=pass",
            ...     table_name="Cities",
            ...     keys=["ID"],
            ... )
            >>> len(table)
            5

        .. doctest:: read_sql
            :hide:

            Remove the edited H2 database from Git's working tree.
            >>> session.close()
            >>> import os
            >>> os.system(f"git checkout -- {{RESOURCES}}/h2-database.mv.db")
            0

    """
    url = normalize_jdbc_url(url)
    inferred_types = SqlDataSource(
        _load_data_into_table=self._java_api.load_data_into_table,
        _infer_types=self._java_api.infer_table_types_from_source,
    ).infer_sql_types(
        sql,
        keys=keys,
        default_values=default_values,
        url=url,
        driver=driver or infer_driver(url),
    )
    types = {**inferred_types, **types} if types is not None else inferred_types
    table = self.create_table(
        table_name,
        types=types,
        keys=keys,
        partitioning=partitioning,
        default_values=default_values,
    )
    load_sql(table, sql, url=url, driver=driver)
    return table


@doc(
    **{
        **SQL_KWARGS,
        # Declare the types here because blackdoc and doctest conflict when inlining it in the docstring.
        "types": """{"ID": tt.INT, "CITY": tt.STRING, "MY_VALUE": tt.DOUBLE}""",
    }
)
def load_sql(
    self: tt.Table,
    sql: str,
    *,
    url: str,
    driver: Optional[str] = None,
) -> None:
    """Load the result of the passed SQL query into the table.

    Note:
        This method requires the :mod:`atoti-sql <atoti_sql>` plugin.

    Args:
        {sql}
        {url}
        {driver}

    Example:
        .. doctest:: load_sql

            >>> table = session.create_table("Cities", types={types}, keys=["ID"])
            >>> table.load_sql(
            ...     "SELECT * FROM MYTABLE;",
            ...     url=f"h2:file:{{RESOURCES}}/h2-database;USER=root;PASSWORD=pass",
            ... )
            >>> len(table)
            5

        .. doctest:: read_sql
            :hide:

            Remove the edited H2 database from Git's working tree.
            >>> session.close()
            >>> import os
            >>> os.system(f"git checkout -- {{RESOURCES}}/h2-database.mv.db")
            0
    """
    url = normalize_jdbc_url(url)
    SqlDataSource(
        _load_data_into_table=self._java_api.load_data_into_table,
        _infer_types=self._java_api.infer_table_types_from_source,
    ).load_sql_into_table(
        sql,
        driver=driver or infer_driver(url),
        scenario_name=self.scenario,
        table=self,
        url=url,
    )
