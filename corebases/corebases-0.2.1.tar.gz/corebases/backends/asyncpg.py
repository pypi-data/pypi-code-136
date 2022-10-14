import contextlib
from functools import lru_cache
from typing import Any, AsyncIterator, List, Optional, Tuple

from asyncpg import Connection, Pool, create_pool
from sqlalchemy.dialects.postgresql import pypostgresql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.sql import ClauseElement
from sqlalchemy.sql.ddl import DDLElement

from corebases import interface as i


@lru_cache(None)
def _get_dialect() -> Dialect:
    dialect = pypostgresql.dialect(paramstyle="pyformat")

    dialect.implicit_returning = True
    dialect.supports_native_enum = True
    dialect.supports_smallserial = True  # 9.2+
    dialect._backslash_escapes = False
    dialect.supports_sane_multi_rowcount = True  # psycopg 2.0.9+
    dialect._has_native_hstore = True
    dialect.supports_native_decimal = True

    return dialect


def _compile(query: ClauseElement, values: dict = None) -> Tuple[str, list, tuple]:
    if values:
        query = query.values(**values)
    compiled = query.compile(
        dialect=_get_dialect(), compile_kwargs={"render_postcompile": True}
    )

    if not isinstance(query, DDLElement):
        compiled_params = sorted(compiled.params.items())

        mapping = {
            key: "$" + str(i) for i, (key, _) in enumerate(compiled_params, start=1)
        }
        compiled_query = compiled.string % mapping

        processors = compiled._bind_processors
        args = [
            processors[key](val) if key in processors else val
            for key, val in compiled_params
        ]

        result_map = compiled._result_columns
    else:
        compiled_query = compiled.string
        args = []
        result_map = None

    return compiled_query, args, result_map


class AsyncPGConnection(i.Connection):
    def __init__(self, connect: Connection):
        self._connect = connect

    async def fetch_all(
        self, query: ClauseElement, values: dict = None
    ) -> List[i.Record]:
        query, args, _ = _compile(query, values)
        result: List[i.Record] = await self._connect.fetch(query, *args)
        return result

    async def fetch_one(
        self, query: ClauseElement, values: dict = None
    ) -> Optional[i.Record]:
        query, args, _ = _compile(query, values)
        result: Optional[i.Record] = await self._connect.fetchrow(query, *args)
        return result

    async def execute(self, query: ClauseElement, values: dict = None) -> Any:
        query, args, _ = _compile(query, values)
        return await self._connect.fetchval(query, *args)

    @contextlib.asynccontextmanager
    async def transaction(self) -> AsyncIterator[i.Connection]:
        yield self


class AsyncPGDatabase(i.Database):
    def __init__(self, *args, **kwargs):
        self._pool_args = args
        self._pool_kwargs = kwargs

    async def connect(self) -> None:
        self._pool: Pool = create_pool(*self._pool_args, **self._pool_kwargs)
        await self._pool

    async def disconnect(self) -> None:
        await self._pool.close()

    async def fetch_all(
        self, query: ClauseElement, values: dict = None
    ) -> List[i.Record]:
        query, args, _ = _compile(query, values)
        result: List[i.Record] = await self._pool.fetch(query, *args)
        return result

    async def fetch_one(
        self, query: ClauseElement, values: dict = None
    ) -> Optional[i.Record]:
        query, args, _ = _compile(query, values)
        result: Optional[i.Record] = await self._pool.fetchrow(query, *args)
        return result

    async def execute(self, query: ClauseElement, values: dict = None) -> Any:
        query, args, _ = _compile(query, values)
        return await self._pool.fetchval(query, *args)

    @contextlib.asynccontextmanager
    async def transaction(self) -> AsyncIterator[i.Connection]:
        async with self._pool.acquire() as connection:
            async with connection.transaction():
                yield AsyncPGConnection(connection)
