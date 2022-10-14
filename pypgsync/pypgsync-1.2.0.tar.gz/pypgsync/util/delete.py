"""
Functions to delete records from the database.
"""
from typing import Any
import psycopg


def delete_record_by_primary_key_value(con: psycopg.Connection, table_name: str, primary_key: str,
                                       primary_key_value: Any):
    """
    Delete a record from a table by primary key.
    """
    sql = f"DELETE FROM {table_name} WHERE {primary_key}=%s;"
    cur = con.cursor()
    cur.execute(sql, (primary_key_value,))
    con.commit()
