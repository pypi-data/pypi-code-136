import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator, Type, TypeVar, Union

import asynch
from asynch.cursors import Cursor, DictCursor
from asynch.errors import ClickHouseException

from tesseract_olap.backend import Backend
from tesseract_olap.backend.exceptions import UpstreamInternalError
from tesseract_olap.common import AnyDict
from tesseract_olap.query import DataQuery, MembersQuery
from tesseract_olap.query.exceptions import EmptyResult, InvalidQuery
from tesseract_olap.schema import Schema

from .sqlbuild import dataquery_sql, membersquery_sql

logger = logging.getLogger("tesseract_olap.backend.clickhouse")

CursorType = TypeVar("CursorType", bound=Cursor)


class ClickhouseBackend(Backend):
    """Clickhouse Backend class

    This is the main implementation for Clickhouse of the core :class:`Backend`
    class.

    Must be initialized with a connection string with the parameters for the
    Clickhouse database. Then must be connected before used to execute queries,
    and must be closed after finishing use.
    """

    connection_string: str

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string

    def __repr__(self) -> str:
        return f"ClickhouseBackend('{self.connection_string}')"

    async def connect(self, **kwargs):
        pass

    @asynccontextmanager
    async def acquire(
        self, curcls: Type[CursorType] = Cursor
    ) -> AsyncGenerator[CursorType, None]:
        conn = await asynch.connect(dsn=self.connection_string)
        try:
            async with conn.cursor(cursor=curcls) as cursor:
                yield cursor  # type: ignore
        except ClickHouseException as exc:
            raise UpstreamInternalError(str(exc)) from None
        finally:
            await conn.close()

    def close(self):
        pass

    async def wait_closed(self):
        pass

    async def execute(
        self, query: Union["DataQuery", "MembersQuery"], **kwargs
    ) -> AsyncIterator[AnyDict]:
        """
        Processes the requests in a :class:`DataQuery` or :class:`MembersQuery`
        instance, sends the query to the database, and returns an `AsyncIterator`
        to access the rows.
        Each iteration yields a tuple of the same length, where the first tuple
        defines the column names, and the subsequents are rows with the data in
        the same order as each column.
        """
        logger.debug("Execute query", extra={"query": query})

        if isinstance(query, MembersQuery):
            sql_builder, sql_params = membersquery_sql(query)
        elif isinstance(query, DataQuery):
            sql_builder, sql_params = dataquery_sql(query)
        else:
            raise InvalidQuery(
                "ClickhouseBackend only supports DataQuery and MembersQuery instances"
            )

        async with self.acquire(DictCursor) as cursor:
            # AsyncIterator must be fully consumed before returning because
            # async context closes connection prematurely
            await cursor.execute(query=sql_builder.get_sql(), args=sql_params)
            result = cursor.fetchall()
            if result is None:
                result = []
            for row in result:
                yield row

    async def ping(self) -> bool:
        """Checks if the current connection is working correctly."""
        async with self.acquire() as cursor:
            await cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return result == (1,)

    async def validate_schema(self, schema: "Schema") -> None:
        """Checks all the tables and columns referenced in the schema exist in
        the backend.
        """
        # logger.debug("Schema %s", schema)
        # TODO: implement
        for cube in schema.cube_map.values():
            pass
        return None


# class StreamingCursor(Cursor):
#     def __init__(self, connection, echo=False):
#         super().__init__(connection, echo)
#         self.set_stream_results(True, 5000)

#         self._stream_results = True
#         self._max_row_buffer = 5000

#     def _process_response(self, response, executemany=False):
#         super()._process_response(response, executemany)
#         if self._columns and self._rows:
#             self._rows = [dict(zip(self._columns, item)) for item in self._rows]

#     async def execute(self, query: str, args: Optional[AnyDict] = None):
#         self._check_cursor_closed()
#         self._begin_query()

#         async def iter_receive_result(self, with_column_types=False):
#             gen = self.packet_generator()
#             async for rows in gen:
#                 for row in rows:
#                     yield row

#         self.connection._connection.iter_receive_result = partial(
#             iter_receive_result,
#             self.connection._connection
#         )

#         response = await self.connection._connection.execute_iter(
#             query,
#             params=args,
#             with_column_types=True,
#             settings={
#                 "max_block_size": self._max_row_buffer
#             },
#             external_tables=[
#                 {"name": name, "structure": structure, "data": data}
#                 for name, (structure, data) in self._external_tables.items()
#             ] or None,
#             types_check=self._types_check,
#             query_id=self._query_id,
#         )

#         self._process_response(response)

#         self._end_query()

#         return self._rowcount

#     async def iter_all(self):
#         logging.info(self._columns)
#         logging.info(self._types)
#         logging.info(self._rows)

#         raise ValueError("ASDF")
