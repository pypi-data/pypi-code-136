"""
purpose -- Gets zeno app delivery data from MongoDB
Author -- abhinav.srivastava@zeno.health
"""

import os
import sys
import argparse

import pandas as pd
from pandas.io.json import json_normalize

sys.path.append('../../../../../../../..')

from zeno_etl_libs.db.db import DB, MongoDB
from zeno_etl_libs.helper.aws.s3 import S3
from zeno_etl_libs.helper import helper
from zeno_etl_libs.logger import get_logger

parser = argparse.ArgumentParser(description="This is ETL custom script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False)

args, unknown = parser.parse_known_args()
env = args.env

os.environ['env'] = env
logger = get_logger()

s3 = S3()

rs_db = DB(read_only=False)
rs_db.open_connection()

mg_db = MongoDB()
mg_client = mg_db.open_connection("generico-crm")
db = mg_client['generico-crm']

schema = 'prod2-generico'
table_name = 'zeno-app-delivery'


def max_last_date():
    """
    This function helps in getting the maximum updated-at date from the
    Redshift table for incremental load
    """
    query = f""" select max("updated-at") as max_date from "{schema}"."{table_name}" """
    df = pd.read_sql_query(query, rs_db.connection)
    if df[b'max_date'][0] is None:
        return "2020-01-01 00:00:00.000000"
    return str(df[b'max_date'][0])


try:
    table_info = helper.get_table_info(db=rs_db, table_name=table_name, schema=schema)
    logger.info(table_info)

    collection = db['deliveryTaskGroupLog'].find({})
    data_raw = pd.DataFrame(list(collection))

    data_raw['tasks'] = data_raw['tasks'].apply(pd.Series)
    app_data = json_normalize(data_raw['tasks'])

    logger.info(app_data.columns)

    collection = db['deliveryAgent'].find({})
    del_agent_data_raw = pd.DataFrame(list(collection))

    del_agent_data_raw.rename(columns={"id": "agent_id", "name": "agent_name"}, inplace=True)
    del_agent_data = del_agent_data_raw[['agent_id', 'agent_name', 'username']]
    del_agent_data.drop_duplicates(inplace=True)

    # merging agent data
    app_data = app_data.merge(del_agent_data, how='left', on=['agent_id'])
    app_data.columns = [c.replace('_', '-') for c in app_data.columns]
    app_data.rename(columns={"createdAt": "created-at", "updated-time": "updated-at"}, inplace=True)
    app_data['agent-id'] = app_data['agent-id'].astype('Int64')

    max_update_date = max_last_date()
    logger.info(f"max update-at date: {max_update_date}")

    app_data = app_data.loc[app_data['updated-at'] >= max_update_date]

    s3.write_df_to_db(df=app_data[table_info['column_name']], table_name=table_name, db=rs_db,
                      schema=schema)

except Exception as error:
    raise Exception(error)
finally:
    rs_db.close_connection()
    mg_db.close_connection()
