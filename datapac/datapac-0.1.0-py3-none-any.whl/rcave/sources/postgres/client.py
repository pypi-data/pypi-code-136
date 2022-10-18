from contextlib import contextmanager
from typing import TYPE_CHECKING

import psycopg2.extensions as ext
from psycopg2 import connect  # noqa
from psycopg2 import sql
from psycopg2.extras import DictCursor

ext.string_types.pop(ext.JSON.values[0], None)
ext.string_types.pop(ext.JSONARRAY.values[0], None)
ext.string_types.pop(ext.JSONB.values[0], None)
ext.string_types.pop(ext.JSONBARRAY.values[0], None)

if TYPE_CHECKING:
    from psycopg2 import connection


@contextmanager
def disabled_contraints(conn: "connection"):
    with conn.cursor() as cursor:
        cursor.execute("set session_replication_role = 'origin'")

        yield

        cursor.execute("set session_replication_role = 'replica'")


def insert(conn: "connection", table: str, row: dict):
    with conn.cursor() as cursor:
        cursor.execute(
            sql.SQL("insert into {} ({}) values ({})").format(
                sql.Identifier(table),
                sql.SQL(",").join([sql.Identifier(key) for key in row.keys()]),
                sql.SQL(", ").join(sql.Placeholder() * len(row.keys())),
            ),
            list(row.values()),
        )


def select(conn: "connection", table: str, where: dict | None = None) -> list[dict]:
    where_clause, where_values = _compile_where(where)

    with conn.cursor(cursor_factory=DictCursor) as cursor:
        statement = sql.SQL("select * from {} {}").format(
            sql.Identifier(table),
            where_clause,
        )

        cursor.execute(statement, where_values)

        return [dict(row) for row in cursor.fetchall()]


def _compile_where(conditions: dict | None):
    if conditions is None:
        return sql.SQL(""), []

    return (
        sql.SQL("where {}").format(
            sql.SQL(" and ").join(
                sql.SQL("{} = %s").format(sql.Identifier(key), sql.Placeholder())
                for key in conditions.keys()
            )
        ),
        list(conditions.values()),
    )
