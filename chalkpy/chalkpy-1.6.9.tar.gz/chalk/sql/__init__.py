from os import PathLike
from typing import Optional, Union, overload

from chalk.sql.base.protocols import BaseSQLSourceProtocol, IncrementalSettings, TableIngestProtocol
from chalk.sql.base.sql_source import BaseSQLSource
from chalk.sql.integrations import *
from chalk.sql.integrations.bigquery import BigQuerySourceImpl
from chalk.sql.integrations.chalk_query import ChalkQuery, StringChalkQuery
from chalk.sql.integrations.cloudsql import CloudSQLSourceImpl
from chalk.sql.integrations.mysql import MySQLSourceImpl
from chalk.sql.integrations.postgres import PostgreSQLSourceImpl
from chalk.sql.integrations.redshift import RedshiftSourceImpl
from chalk.sql.integrations.snowflake import SnowflakeSourceImpl
from chalk.sql.integrations.sqlite import SQLiteFileSourceImpl, SQLiteInMemorySourceImpl


@overload
def SnowflakeSource(*, name: str) -> BaseSQLSourceProtocol:
    ...


@overload
def SnowflakeSource(
    *,
    account_identifier: str,
    warehouse: str,
    user: str,
    password: str,
    db: str,
    schema: str,
    role: str,
) -> BaseSQLSourceProtocol:
    ...


def SnowflakeSource(
    *,
    name: Optional[str] = None,
    account_identifier: Optional[str] = None,
    warehouse: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    db: Optional[str] = None,
    schema: Optional[str] = None,
    role: Optional[str] = None,
) -> BaseSQLSourceProtocol:
    return SnowflakeSourceImpl(
        name=name,
        account_identifier=account_identifier,
        warehouse=warehouse,
        user=user,
        password=password,
        db=db,
        schema=schema,
        role=role,
    )


@overload
def PostgreSQLSource(
    *,
    host: str,
    port: str,
    db: str,
    user: str,
    password: str,
) -> TableIngestProtocol:
    ...


@overload
def PostgreSQLSource(*, name: str) -> TableIngestProtocol:
    ...


@overload
def PostgreSQLSource() -> TableIngestProtocol:
    ...


def PostgreSQLSource(
    *,
    host: Optional[str] = None,
    port: Optional[str] = None,
    db: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    name: Optional[str] = None,
) -> TableIngestProtocol:
    return PostgreSQLSourceImpl(host, port, db, user, password, name)


@overload
def MySQLSource(
    *,
    host: str,
    port: str,
    db: str,
    user: str,
    password: str,
) -> BaseSQLSourceProtocol:
    ...


@overload
def MySQLSource(*, name: str) -> BaseSQLSourceProtocol:
    ...


@overload
def MySQLSource() -> BaseSQLSourceProtocol:
    ...


def MySQLSource(
    *,
    host: Optional[str] = None,
    port: Optional[str] = None,
    db: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    name: Optional[str] = None,
) -> TableIngestProtocol:
    return MySQLSourceImpl(host, port, db, user, password, name)


def SQLiteInMemorySource() -> TableIngestProtocol:
    return SQLiteInMemorySourceImpl()


def SQLiteFileSource(filename: Union[str, PathLike]) -> TableIngestProtocol:
    return SQLiteFileSourceImpl(filename)


@overload
def RedshiftSource(
    *,
    host: str,
    db: str,
    user: str,
    password: str,
) -> BaseSQLSourceProtocol:
    ...


@overload
def RedshiftSource(*, name: str) -> BaseSQLSourceProtocol:
    ...


@overload
def RedshiftSource() -> BaseSQLSourceProtocol:
    ...


def RedshiftSource(
    *,
    host: Optional[str] = None,
    db: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    name: Optional[str] = None,
) -> BaseSQLSourceProtocol:
    return RedshiftSourceImpl(host, db, user, password, name)


@overload
def BigQuerySource() -> BaseSQLSourceProtocol:
    ...


@overload
def BigQuerySource(*, name: str) -> BaseSQLSourceProtocol:
    ...


def BigQuerySource(
    *,
    name: Optional[str] = None,
    project: Optional[str] = None,
    dataset: Optional[str] = None,
    location: Optional[str] = None,
    credentials_base64: Optional[str] = None,
    credentials_path: Optional[str] = None,
) -> BaseSQLSourceProtocol:
    return BigQuerySourceImpl(
        name=name,
        project=project,
        dataset=dataset,
        location=location,
        credentials_base64=credentials_base64,
        credentials_path=credentials_path,
    )


@overload
def CloudSQLSource() -> BaseSQLSourceProtocol:
    ...


@overload
def CloudSQLSource(*, name: str) -> BaseSQLSourceProtocol:
    ...


def CloudSQLSource(
    *,
    name: Optional[str] = None,
    instance_name: Optional[str] = None,
    db: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
) -> BaseSQLSourceProtocol:
    return CloudSQLSourceImpl(
        name=name,
        instance_name=instance_name,
        db=db,
        user=user,
        password=password,
    )


__all__ = [
    "ChalkQuery",
    "BaseSQLSourceProtocol",
    "BigQuerySource",
    "CloudSQLSource",
    "IncrementalSettings",
    "MySQLSource",
    "PostgreSQLSource",
    "RedshiftSource",
    "SQLiteFileSource",
    "SQLiteInMemorySource",
    "SnowflakeSource",
]
