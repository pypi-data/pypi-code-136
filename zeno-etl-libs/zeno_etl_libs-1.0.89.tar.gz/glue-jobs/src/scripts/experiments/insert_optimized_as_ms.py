import argparse
import sys
import pandas as pd
import os
sys.path.append('../../../..')

from zeno_etl_libs.logger import get_logger
from zeno_etl_libs.db.db import DB
from zeno_etl_libs.queries.as_ms import as_ms


def main(db, table_suffix):
    table_name = f"as-ms"
    if table_suffix:
        table_name = f"as-ms-{table_suffix}"
    db.execute(query="begin ;")

    query = as_ms.max_short_book_id.format(table_name)
    db.execute(query, params=None)

    as_ms_intermediate: pd.DataFrame = rs_db.cursor.fetch_dataframe()
    max_short_book_id = as_ms_intermediate.values[0][0]

    if max_short_book_id is None:
        max_short_book_id = 0
    # Insert
    query = as_ms.insert_as_ms_query.format(table_name, max_short_book_id)
    db.execute(query=query)

    # Update
    query = as_ms.update_as_ms_query.format(table_name, table_name)
    db.execute(query=query)

    """ committing the transaction """
    db.execute(query=" end; ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is ETL script.")
    parser.add_argument('-e', '--env', default="dev", type=str, required=False,
                        help="This is env(dev, stag, prod)")
    parser.add_argument('-ts', '--table_suffix', default="", type=str, required=False,
                        help="Table suffix for testing.")
    args, unknown = parser.parse_known_args()
    env = args.env
    table_suffix = args.table_suffix
    os.environ['env'] = env
    logger = get_logger()
    logger.info(f"env: {env}")
    logger.info(f"New automation testing, env: {env}")

    rs_db = DB()
    rs_db.open_connection()

    """ For single transaction  """
    rs_db.connection.autocommit = False

    """ calling the main function """
    main(db=rs_db, table_suffix=table_suffix)

    # Closing the DB Connection
    rs_db.close_connection()
