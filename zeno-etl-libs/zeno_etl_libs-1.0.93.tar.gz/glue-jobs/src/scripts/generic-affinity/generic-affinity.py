import argparse
import os
import sys

sys.path.append('../../../../..')

from zeno_etl_libs.logger import get_logger
from zeno_etl_libs.db.db import DB, PostGreWrite
from zeno_etl_libs.helper.aws.s3 import S3
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import datetime

parser = argparse.ArgumentParser(description="This is ETL script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False,
                    help="This is env(dev, stag, prod)")

args, unknown = parser.parse_known_args()

env = args.env
os.environ['env'] = env
logger = get_logger()

rs_db = DB()
rs_db.open_connection()

# PostGre
pg = PostGreWrite()
pg.open_connection()

s3 = S3()

schema = 'prod2-generico'
table_name = 'generic-affinity'
logger.info(f"Starting job in env: {env}")

# =============================================================================
# patient level bill count
# =============================================================================
gb = f"""
    select
    	"patient-id" ,
    	count(distinct case when "type" = 'generic' and "bill-flag" = 'gross' then "bill-id" end ) as "generic_bill_count",
    	count(distinct case when "bill-flag" = 'gross' then "bill-id" end) as gross_bill_count
    from
    	"{schema}".sales
    where
    	date("created-at")< CURRENT_DATE
    group by
    	"patient-id"
    """
p_bills=rs_db.get_df(gb)

logger.info("Data: patient level bill count fetched successfully")

p_bills.columns = [c.replace('-', '_') for c in p_bills.columns]
p_bills[['generic_bill_count', 'gross_bill_count']].fillna(0, inplace=True)

p_bills['generic_bill_pct'] = (p_bills['generic_bill_count'] / (p_bills['gross_bill_count'])) * 100

# =============================================================================
# patient level substitution
# =============================================================================

subs = f"""
    select
    	"patient-id" ,
    	"substitution-status" ,
    	sum(quantity) as quantity
    from
    	"{schema}".sales
    where
    	"bill-flag" = 'gross'
    	and "type" = 'generic'
    	and date("created-at")<CURRENT_DATE 
    group by
    	"patient-id", "substitution-status" 
    """
p_subs=rs_db.get_df(subs)

p_subs.columns = [c.replace('-', '_') for c in p_subs.columns]

p_subs['quantity'].fillna(0, inplace=True)
p_subs1 = pd.pivot_table(p_subs,
                         values='quantity',
                         index=['patient_id'],
                         columns=['substitution_status']).reset_index()
p_subs1.columns = [c.replace('-', '_') for c in p_subs1.columns]

p_subs1.fillna(0, inplace=True)
p_subs1['subs_pct'] = (p_subs1['substituted'] / (p_subs1['substituted'] + p_subs1['not_substituted'])) * 100

metadata = pd.merge(right=p_subs1, left=p_bills, on=['patient_id'], how='left')

# =============================================================================
# patient level return %
# =============================================================================


ret = f"""
    select
    	"patient-id" ,
    	count(distinct case when "type" = 'generic' and "bill-flag" = 'return' then "bill-id" end ) as "generic_return_bill_count",
    	count(distinct case when "bill-flag" = 'return' then "bill-id" end) as "gross_return_bill"
    from
    	"{schema}".sales
    where
    	date("created-at")< CURRENT_DATE
    group by
    	"patient-id"
    """
p_return=rs_db.get_df(ret)

p_return.columns = [c.replace('-', '_') for c in p_return.columns]

p_return[['generic_return_bill_count', 'gross_return_bill']].fillna(0, inplace=True)
p_return['return_pct'] = ((p_return['generic_return_bill_count']) / (p_return['gross_return_bill'])) * 100

p_return['not_return_pct'] = 100 - p_return['return_pct']

metadata = pd.merge(left=metadata, right=p_return, on=['patient_id'], how='left')

metadata['not_return_pct'].fillna(100, inplace=True)

# =============================================================================
# patient level recency
# =============================================================================

rec = f"""
    select
    	"patient-id" ,
    	max("created-at") as "last_visit"
    from
    	"{schema}".sales
    where
    	"bill-flag" = 'gross'
    	and date("created-at")<CURRENT_DATE
    group by
    	"patient-id"

    """
p_recency=rs_db.get_df(rec)

p_recency.columns = [c.replace('-', '_') for c in p_recency.columns]

prev_date = (datetime.datetime.today() + relativedelta(days=-1))
p_recency['last_visit'] = pd.to_datetime(p_recency['last_visit'], format="%y-%m-%d")
p_recency['prev_date'] = prev_date
p_recency['prev_date'] = pd.to_datetime(p_recency['prev_date'], format="%y-%m-%d")

p_recency['num_months'] = (p_recency['prev_date'] - p_recency['last_visit']) / np.timedelta64(1, 'M')

conditions = [
    (

        (p_recency['num_months'] <= 3)
    ),

    (
            (p_recency['num_months'] > 3) &
            (p_recency['num_months'] <= 6)
    ),

    (
            (p_recency['num_months'] > 6) &
            (p_recency['num_months'] <= 12)
    ),

    (

        (p_recency['num_months'] > 12)
    )
]
choices = [100, 75, 50, 25]
p_recency['recency_pct'] = np.select(conditions, choices, default=0)
p_recency['recency_pct'].fillna(0, inplace=True)

metadata = pd.merge(left=metadata, right=p_recency, on=['patient_id'], how='left')

# =============================================================================
# patient level generic recency
# =============================================================================

gen_rec = f"""
    select
    	"patient-id" ,
    	max("created-at") as "last_generic_visit"
    from
    	"{schema}".sales
    where
    	"bill-flag" = 'gross'
    	and "type" ='generic'
    	and date("created-at")<CURRENT_DATE
    group by
    	"patient-id"
    """
p_grecency=rs_db.get_df(gen_rec)

p_grecency.columns = [c.replace('-', '_') for c in p_grecency.columns]

p_grecency['last_generic_visit'] = pd.to_datetime(p_grecency['last_generic_visit'], format="%y-%m-%d")
p_grecency['g_prev_date'] = prev_date
p_grecency['g_prev_date'] = pd.to_datetime(p_grecency['g_prev_date'], format="%y-%m-%d")

p_grecency['g_num_months'] = ((p_grecency['g_prev_date'] - p_grecency['last_generic_visit'])
                              / np.timedelta64(1, 'M'))

conditions = [
    (

        (p_grecency['g_num_months'] <= 3)
    ),

    (
            (p_grecency['g_num_months'] > 3) &
            (p_grecency['g_num_months'] <= 6)
    ),

    (
            (p_grecency['g_num_months'] > 6) &
            (p_grecency['g_num_months'] <= 12)
    ),

    (

        (p_grecency['g_num_months'] > 12)
    )
]
choices = [100, 75, 50, 25]
p_grecency['gen_recency_pct'] = np.select(conditions, choices,
                                          default=0)
p_grecency.drop('g_prev_date', axis='columns', inplace=True)
p_grecency['gen_recency_pct'].fillna(0, inplace=True)

metadata = pd.merge(left=metadata, right=p_grecency, on=['patient_id'], how='left')

metadata.fillna(0, inplace=True)

metadata['generic_likelihood'] = ((metadata['generic_bill_pct'] + metadata['gen_recency_pct']
                                   + metadata['subs_pct'] + metadata['not_return_pct'] +
                                   metadata['recency_pct']) / (5))

conditions = [
    (

        (metadata['generic_likelihood'] >= 80)
    ),

    (
            (metadata['generic_likelihood'] < 80) &
            (metadata['generic_likelihood'] >= 60)
    ),

    (
            (metadata['generic_likelihood'] < 60) &
            (metadata['generic_likelihood'] >= 50)
    ),

    (

            (metadata['generic_likelihood'] < 50) &
            (metadata['generic_likelihood'] >= 25)
    ),

    (

        (metadata['generic_likelihood'] < 25)
    )
]

choices = [5, 4, 3, 2, 1]
metadata['generic_affinity_score'] = np.select(conditions, choices, default=3)

# Pushing data for generic_affinity
generic_affinity = metadata[metadata['gross_bill_count'] > 0]
generic_affinity['refreshed_at'] = datetime.datetime.now()

logger.info('length of generic_affinity is :' + str(len(generic_affinity)))

""""""
generic_affinity = generic_affinity[
    ['patient_id', 'gross_bill_count', 'generic_bill_count', 'generic_bill_pct',
     'generic_unavailable', 'not_in_inventory', 'not_substituted', 'substituted', 'subs_pct',
     'gross_return_bill', 'generic_return_bill_count', 'return_pct', 'not_return_pct', 'last_visit',
     'prev_date', 'num_months', 'recency_pct', 'last_generic_visit', 'g_num_months',
     'gen_recency_pct', 'generic_likelihood', 'generic_affinity_score', 'refreshed_at']]

generic_affinity.columns = [c.replace('-', '_') for c in generic_affinity.columns]

# Write to PostGre
query = f''' DELETE FROM {table_name.replace("-", "_")} '''
pg.engine.execute(query)
generic_affinity.to_sql(name=table_name.replace("-", "_"), con=pg.engine, if_exists='append',
                        chunksize=500, method='multi', index=False)

# Closing the DB Connection
rs_db.close_connection()
pg.close_connection()
