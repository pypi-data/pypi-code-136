"""
Implementation of the primary key mode, which is used to sync the tables by selected primary keys
"""
from typing import List, Dict
import psycopg
from pypgsync.util.query import get_column_set_diff, get_column_records_for_primary_key_subset, \
    get_table_column_names, get_column_values
from pypgsync.util.create import insert_records
from pypgsync.util.update import point_update
from pypgsync.util.delete import delete_record_by_primary_key_value


def row_delta_by_primary_key(cur_source: psycopg.Cursor, cur_destination: psycopg.Cursor,
                             table_name: str, primary_key: str) -> Dict:
    """
    Get primary key ids which mismatch between the source and destination databases
    """
    diff = get_column_set_diff(cur_db_1=cur_source, cur_db_2=cur_destination, table_name=table_name,
                               column_name=primary_key)

    intersection = diff["intersection"]
    delete = diff["not_in_db_1"]
    insert_pk_values = list(diff["not_in_db_2"])

    column_names = get_table_column_names(cur=cur_source, table_name=table_name)
    records_to_insert = get_column_records_for_primary_key_subset(cur=cur_source,
                                                                  table_name=table_name,
                                                                  column_names=column_names,
                                                                  primary_key_column=primary_key,
                                                                  pk_values=insert_pk_values)

    response = {
        "table_name": table_name,
        "primary_key": primary_key,
        "intersection": intersection,
        "delete": delete,
        "insert": records_to_insert,
    }

    return response


def record_delta_by_primary_key(cur_source: psycopg.Cursor, cur_destination: psycopg.Cursor,
                                table_name: str, primary_key: str, columns: List[str],
                                pk_values: List) -> Dict:
    """
    Get the records that are different between the source and destination databases for the
    given primary keys and columns.
    """

    if primary_key in columns:
        raise ValueError("Primary key cannot be in the list of columns to sync")

    source_records = get_column_records_for_primary_key_subset(cur=cur_source,
                                                               table_name=table_name,
                                                               column_names=columns,
                                                               primary_key_column=primary_key,
                                                               pk_values=pk_values)
    destination_records = get_column_records_for_primary_key_subset(cur=cur_destination,
                                                                    table_name=table_name,
                                                                    column_names=columns,
                                                                    primary_key_column=primary_key,
                                                                    pk_values=pk_values)

    source_records_dict = {record[primary_key]: record for record in source_records}
    destination_records_dict = {record[primary_key]: record for record in destination_records}

    update = []
    for pk_value in pk_values:
        source_record = source_records_dict[pk_value]
        destination_record = destination_records_dict[pk_value]
        for column in columns:
            if source_record[column] != destination_record[column]:
                update.append({primary_key: pk_value, column: source_record[column]})

    result = {
        "table_name": table_name,
        "primary_key": primary_key,
        "update": update,
    }

    return result


def delta_by_primary_key(cur_source: psycopg.Cursor, cur_destination: psycopg.Cursor,
                         table_name: str, primary_key: str, columns: List[str],
                         pk_values: List) -> Dict:
    """
    Get the records that are different between the source and destination databases for selected
    table, columns and primary key values
    """
    row_delta = row_delta_by_primary_key(cur_source, cur_destination, table_name, primary_key)

    subset_pk_values = [pk for pk in row_delta["intersection"] if pk in pk_values]
    record_delta = record_delta_by_primary_key(cur_source, cur_destination, table_name,
                                               primary_key, columns, pk_values=subset_pk_values)
    row_delta["update"] = record_delta["update"]
    return row_delta


def apply_delta_by_primary_key(con_destination: psycopg.Connection, delta: Dict):
    """
    Apply the delta to the destination database
    """
    table_name = delta["table_name"]
    primary_key = delta["primary_key"]

    insert_records(con=con_destination, table_name=table_name, records=delta["insert"])

    for record in delta["update"]:

        where_value = record[primary_key]
        where_column = primary_key

        record_keys = list(record.keys())
        record_keys.remove(primary_key)

        if len(record_keys) > 1:
            raise ValueError(f"Update records can only have 2 keys; got {record}")

        set_column = record_keys[0]
        set_value = record[set_column]

        point_update(con=con_destination, table_name=table_name, set_column=set_column,
                     set_value=set_value, where_column=where_column, where_value=where_value)

    for pk in delta["delete"]:
        delete_record_by_primary_key_value(con=con_destination, table_name=table_name,
                                           primary_key=primary_key, primary_key_value=pk)


def sync_by_primary_key(cur_source: psycopg.Cursor, con_destination: psycopg.Connection,
                        table_name: str, primary_key: str):

    column_names = get_table_column_names(cur=cur_source, table_name=table_name)
    column_names.remove(primary_key)
    pk_values = get_column_values(cur=cur_source, table_name=table_name, column_name=primary_key)

    cur_destination = con_destination.cursor()
    delta = delta_by_primary_key(cur_source=cur_source, cur_destination=cur_destination,
                                 table_name=table_name, primary_key=primary_key,
                                 columns=column_names, pk_values=pk_values)
    apply_delta_by_primary_key(con_destination=con_destination, delta=delta)
