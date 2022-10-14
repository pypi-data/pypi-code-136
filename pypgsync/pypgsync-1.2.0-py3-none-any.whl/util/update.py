"""
Functions to update records in the database.
"""
from typing import Any
import psycopg


def point_update(con: psycopg.Connection, table_name: str, set_column: str, set_value: Any,
                 where_column: str, where_value: Any):
    """
    Standard point update of a record in a table (set where).
    Note: multiple records may be updated if the where column is not unique.
    """
    sql = f"UPDATE {table_name} SET {set_column}=%s WHERE {where_column}=%s;"
    cur = con.cursor()
    cur.execute(sql, (set_value, where_value))
    con.commit()
