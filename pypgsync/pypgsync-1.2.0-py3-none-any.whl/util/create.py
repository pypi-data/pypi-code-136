"""
Functions to insert and create new records in the database.
"""
from typing import List, Dict
import psycopg


def insert_records(con: psycopg.Connection, table_name: str, records: List[Dict]):
    """
    Standard insert into table.

    Records are expected to be of format
        {
            "column_name_1": value_1,
            "column_name_2": value_2,
            ...
        }
    Function assumes that table exists and that the columns are of the correct type.
    """

    columns_names = set()
    for record in records:
        for column_name in record.keys():
            columns_names.add(column_name)
    columns_names = list(columns_names)

    columns_names_str = ",".join(columns_names)
    values_str = ",".join(["%s" for _ in range(len(columns_names))])
    sql = f"INSERT INTO {table_name} ({columns_names_str}) VALUES ({values_str});"

    values = []
    for record in records:
        value_row = []
        for column_name in columns_names:
            value_row.append(record.get(column_name))
        values.append(tuple(value_row))
    values = tuple(values)

    cur = con.cursor()
    cur.executemany(sql, values)
    con.commit()
