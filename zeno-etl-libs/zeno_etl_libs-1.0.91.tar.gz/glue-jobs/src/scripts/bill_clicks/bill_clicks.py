"""
purpose -- Gets minimum bill creation date for a pso and store from MongoDB to store in RS
Author -- abhinav.srivastava@zeno.health
"""

import os
import sys
import argparse
import pandas as pd

sys.path.append('../../../../../../../..')

from zeno_etl_libs.db.db import DB, MongoDB
from zeno_etl_libs.helper.aws.s3 import S3

parser = argparse.ArgumentParser(description="This is ETL custom script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False)

args, unknown = parser.parse_known_args()
env = args.env

os.environ['env'] = env

table_name = 'bill-click'
schema = 'prod2-generico'

s3 = S3()

rs_db = DB()
rs_db.open_connection()

mg_db = MongoDB()
mg_client = mg_db.open_connection("generico-crm")
db = mg_client['generico-crm']

try:
    collection = db['psoBillClickLogs'].find()

    data_raw = pd.DataFrame(list(collection))
    processed_data = data_raw.groupby(['pso_id', 'store_id'])\
        .aggregate({'createdAt': 'min'}).reset_index()
    processed_data.columns = [c.replace('_', '-').lower() for c in processed_data.columns]
    processed_data.rename(columns={'createdat':'created-at'}, inplace=True)
    query = f"""truncate table "{schema}"."{table_name}";"""
    rs_db.execute(query)

    s3.write_df_to_db(df=processed_data, table_name=table_name, db=rs_db, schema=schema)

except Exception as error:
    raise Exception(error)

finally:
    rs_db.close_connection()
    mg_db.close_connection()
