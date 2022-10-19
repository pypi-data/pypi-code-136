# Copyright Contributors to the Datalogz project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Any
import attr
from marshmallow3_annotations.ext.attrs import AttrsSchema


class DatasourcesNames:
    POSTGRES = 'postgres'
    SNOWFLAKE = 'snowflake'
    DBT = 'dbt'
    POWERBI = 'powerbi'
    REDSHIFT = 'redshift'
    MYSQL = 'mysql'
    ORACLE = 'oracle'


@attr.s(auto_attribs=True, kw_only=True)
class Common_Dashboard_DatasourceFields:
    key: str = attr.ib(default='')


class Common_Dashboard_DatasourceFieldsSchema(AttrsSchema):
    class Meta:
        target = Common_Dashboard_DatasourceFields
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Common_ETL_DatasourceFields:
    key: str = attr.ib(default='')
    datasource_type: str = attr.ib()


class Common_ETL_DatasourceFieldsSchema(AttrsSchema):
    class Meta:
        target = Common_ETL_DatasourceFields
        register_as_scheme = True
@attr.s(auto_attribs=True, kw_only=True)
class Common_DB_DatasourceFields:
    key: str = attr.ib(default='')
    user_name: str = attr.ib()
    password: str = attr.ib()
    db_name: str = attr.ib()
    datasource_type: str = attr.ib()
    data_access_location: str = attr.ib(default='')
    schemas_config: List[Dict[str, Any]] = attr.ib(default=[{}])
    data_source_name: str = attr.ib(default="")


class Common_DB_DatasourceFieldsSchema(AttrsSchema):
    class Meta:
        target = Common_DB_DatasourceFields
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Postgres(Common_DB_DatasourceFields):
    host: str = attr.ib()
    port: str = attr.ib()
    schema: str = attr.ib(default='public')
    datasource_type: str = attr.ib(
        default=DatasourcesNames.POSTGRES, init=False)

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]


class PostgresSchema(AttrsSchema):
    class Meta:
        target = Postgres
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Snowflake(Common_DB_DatasourceFields):
    account: str = attr.ib()
    warehouse: str = attr.ib()
    role: str = attr.ib(default='')
    datasource_type: str = attr.ib(
        default=DatasourcesNames.SNOWFLAKE, init=False)


class SnowflakeSchema(AttrsSchema):
    class Meta:
        target = Snowflake
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class DBT(Common_ETL_DatasourceFields):
    catalog_file: str = attr.ib()
    db_name: str = attr.ib()
    manifest_file: str = attr.ib()
    source_url: str = attr.ib()
    datasource_type: str = attr.ib(default=DatasourcesNames.DBT, init=False)


class DBT_Schema(AttrsSchema):
    class Meta:
        target = DBT
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Redshift(Common_DB_DatasourceFields):
    host: str = attr.ib()
    port: str = attr.ib()
    datasource_type: str = attr.ib(
        default=DatasourcesNames.REDSHIFT, init=False)

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]


class RedshiftSchema(AttrsSchema):
    class Meta:
        target = Redshift
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class MySql(Common_DB_DatasourceFields):
    host: str = attr.ib()
    port: str = attr.ib()
    datasource_type: str = attr.ib(default=DatasourcesNames.MYSQL, init=False)

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]


class MySqlSchema(AttrsSchema):
    class Meta:
        target = MySql
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Oracle(Common_DB_DatasourceFields):
    host: str = attr.ib()
    port: str = attr.ib()
    datasource_type: str = attr.ib(default=DatasourcesNames.ORACLE, init=False)

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]


class OracleSchema(AttrsSchema):
    class Meta:
        target = Oracle
        register_as_scheme = True
