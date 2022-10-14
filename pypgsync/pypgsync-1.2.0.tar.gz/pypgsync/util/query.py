"""
Postgres query functions which are not specific to any pypgsync mode and therefore can potentially
be re-used
"""
from typing import List, Dict
import psycopg

from pypgsync.util.conversion import convert_return_value_to_python_type


def get_primary_keys(cur: psycopg.Cursor, table_names: List[str]) -> List[str]:
    """
    Get the primary keys for a list of tables
    """
    if table_names is None or len(table_names) == 0:
        return []

    condition_str = ",".join([f"'{table_name}'::regclass" for table_name in table_names])
    sql = f"""
        SELECT
            i.indrelid::regclass AS table_name,
            a.attname
        FROM pg_index i
        JOIN pg_attribute a
            ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        WHERE TRUE
            AND i.indrelid::regclass IN ({condition_str})
            AND i.indisprimary;"""
    cur.execute(sql)
    primary_keys = {row[0]: row[1] for row in cur.fetchall()}
    return primary_keys


def get_column_values(cur: psycopg.Cursor, table_name: str, column_name) -> List:
    """
    Get the column values for a column in a table
    """
    sql = f"SELECT {column_name} FROM {table_name};"
    cur.execute(sql)
    column_values = [row[0] for row in cur.fetchall()]
    return column_values


def get_table_column_names(cur: psycopg.Cursor, table_name: str) -> List[str]:
    """For a given table, return all column names in the database"""
    sql = f"""SELECT * FROM {table_name} LIMIT 1;"""
    cur.execute(sql)
    column_names = [desc[0] for desc in cur.description]
    return column_names


def get_column_records(cur: psycopg.Cursor, table_name: str, column_name: str) -> List[str]:
    """
    Get the records for a single column in a table
    """
    sql = f"SELECT {column_name} FROM {table_name}"
    cur.execute(sql)
    records = [row[0] for row in cur.fetchall()]
    return records


def get_column_set_diff(cur_db_1: psycopg.Cursor, cur_db_2: psycopg.Cursor, table_name: str,
                        column_name: str) -> Dict:
    values_db_1 = get_column_records(cur_db_1, table_name, column_name)
    values_db_2 = get_column_records(cur_db_2, table_name, column_name)

    result = {
        "intersection": set(values_db_1).intersection(set(values_db_2)),
        "not_in_db_1": set(values_db_2).difference(set(values_db_1)),
        "not_in_db_2": set(values_db_1).difference(set(values_db_2)),
    }
    return result


def get_column_records_for_primary_key_subset(cur: psycopg.Cursor, table_name: str,
                                              column_names: List[str], primary_key_column: str,
                                              pk_values: List) -> List[Dict]:
    """
    Get records for column and primary key for a subset of primary keys. Sorted by primary key.
    """
    if pk_values is None or len(pk_values) == 0:
        return []

    if column_names is None or len(column_names) == 0:
        return []

    if type(pk_values[0]) == str:
        in_condition = ",".join([f"'{pk_value}'" for pk_value in pk_values])
    elif type(pk_values[0]) == int:
        in_condition = ",".join([f"{pk_value}" for pk_value in pk_values])
    else:
        raise ValueError("Primary key values must be either strings or integers")

    column_names_str = ",".join(column_names)
    sql = f"""
        SELECT
            {primary_key_column},
            {column_names_str}
        FROM {table_name}
        WHERE {primary_key_column} IN ({in_condition})
        ORDER BY {primary_key_column}"""
    cur.execute(sql)
    records = []
    for row in cur.fetchall():
        record = {column_name: convert_return_value_to_python_type(row[i + 1])
                  for i, column_name in enumerate(column_names)}
        record[primary_key_column] = row[0]
        records.append(record)
    return records
