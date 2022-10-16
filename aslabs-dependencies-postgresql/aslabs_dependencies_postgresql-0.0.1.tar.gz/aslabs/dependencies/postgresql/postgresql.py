from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
import psycopg2
from dataclasses import dataclass
from contextlib import contextmanager


TClient = TypeVar("TClient")
TFactory = TypeVar("TFactory")


@dataclass
class PostgresqlConfig:
    host: str
    database: str
    user: str
    password: str


class PostgresqlConnectionFactory:
    def __init__(self, config: PostgresqlConfig):
        self._config = config

    def get_connection(self) -> psycopg2.extensions.connection:
        return psycopg2.connect(
            host=self._config.host,
            database=self._config.database,
            user=self._config.user,
            password=self._config.password)

    @contextmanager
    def cursor(self):
        conn = self.get_connection()
        cur = conn.cursor()
        yield cur
        cur.close()
        conn.close()


class PostgresqlSingletonClientResolver(ResolverABC):
    def __init__(self):
        self._connection = None

    def __call__(self, deps: DependenciesABC) -> TClient:
        config = deps.get(PostgresqlConfig)
        if self._connection is not None:
            return self._connection
        self._connection = PostgresqlConnectionFactory(config).get_connection()
        return self._connection

    @property
    def resolved_type(self) -> Type[TClient]:
        return psycopg2.extensions.connection


class PostgresqlConnectionFactoryResolver(ResolverABC):
    def __init__(self):
        self._factory = None

    def __call__(self, deps: DependenciesABC) -> TFactory:
        config = deps.get(PostgresqlConfig)
        if self._factory is not None:
            return self._factory
        self._factory = PostgresqlConnectionFactory(config)
        return self._factory

    @property
    def resolved_type(self) -> Type[TFactory]:
        return PostgresqlConnectionFactory
