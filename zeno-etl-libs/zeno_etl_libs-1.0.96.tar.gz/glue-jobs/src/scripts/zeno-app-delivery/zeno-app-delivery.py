"""
purpose -- Gets zeno app delivery data from MongoDB
Author -- abhinav.srivastava@zeno.health
"""

import os
import sys
import argparse

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

sys.path.append('../../../../../../../..')

from zeno_etl_libs.db.db import DB, MongoDB
from zeno_etl_libs.helper.aws.s3 import S3
from zeno_etl_libs.helper import helper

parser = argparse.ArgumentParser(description="This is ETL custom script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False)

args, unknown = parser.parse_known_args()
env = args.env

os.environ['env'] = env

s3 = S3()

rs_db = DB(read_only=False)
rs_db.open_connection()

mg_db = MongoDB()
mg_client = mg_db.open_connection("generico-crm")
db = mg_client['generico-crm']

schema = 'prod2-generico'
table_name = 'zeno-app-delivery'

try:
    collection = db['deliveryTaskGroupLog'].find({})
    data_raw = pd.DataFrame(list(collection))
    data_raw['tasks'] = data_raw['tasks'].apply(pd.Series)
    app_data = json_normalize(data_raw['tasks'])
    print(app_data.columns)
    app_data.columns = [c.replace('_', '-') for c in app_data.columns]
    app_data.rename(columns={"createdAt": "created-at", "updated-time": "updated-at"}, inplace=True)
    print(app_data.head(20).to_string())
    table_info = helper.get_table_info(db=rs_db, table_name=table_name, schema=schema)
    print(table_info)
    truncate_query = f''' DELETE FROM "{schema}"."{table_name}" '''
    rs_db.execute(truncate_query)
    print(truncate_query)
    s3.write_df_to_db(df=app_data[table_info['column_name']], table_name=table_name, db=rs_db,
                      schema=schema)

    # inter_df = app_data.sort_values(['order_id', 'agent_id', 'status'], ascending=[True, True, True])
    # inter_df['row_number'] = inter_df.groupby(['order_id', 'agent_id']).cumcount()
    # print(inter_df.head(20).to_string())
    # df_restructured = inter_df.loc[inter_df["row_number"] == 0, ("order_id", "store_id", "store_name", "agent_id")]
    # df_restructured_1 = inter_df[inter_df["status"].eq(inter_df.groupby(["order_id", "agent_id"])["status"].transform("max"))]
    # print(df_restructured.shape)
    # print(df_restructured_1.to_string())
except Exception as error:
    raise Exception(error)
finally:
    rs_db.close_connection()
    mg_db.close_connection()