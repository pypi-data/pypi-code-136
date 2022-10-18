import snowflake.connector


def snowflake_create_conn():
    snowflake_username = "winash"
    snowflake_password = "myD33ksh@k@n@lu"
    snowflake_account = "kf71436.us-east-1"
    snowflake_warehouse = "COMPUTE_WH"
    snowflake_database = "FINANCE"
    snowflake_schema = "FINANCE"
    conn = snowflake.connector.connect(
        user=snowflake_username,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema
    )
    return conn


sf_table_namein = "FINANCE.BLACKROCK_QUARANTINE_RAW"
print("executing cleanup")
conn = snowflake_create_conn()
cur = conn.cursor()
print("executing cleanup on SF")

command = "update IDENTIFIER(%(tablename)s) set CARD_NUMBER = case when CARD_NUMBER is null then '5599-4639-3545-6532' else CARD_NUMBER  end, ACC_ID = case when ACC_ID is null then '80154107168255874003' else ACC_ID end, TYPE = case when TYPE='SHARATH' then 'RUPAY' else TYPE end"
bind_params = {
    "tablename": sf_table_namein,
}
results = cur.execute(command, bind_params)
conn.commit()
cur.close()
exit()


sf_table_namein = "finance.blackrock_raw_mirror"
conn = snowflake_create_conn()

cur = conn.cursor()
command = (
    "ALTER TABLE IDENTIFIER(%(tablename)s) DROP COLUMN \"ad_rule__143__result\"")

bind_params = {
    "tablename": sf_table_namein
}
results = cur.execute(command, bind_params)
conn.commit()
cur.close()


cur = conn.cursor()
print("executing truncate on SF")
command = ("TRUNCATE TABLE IDENTIFIER(%(tablename)s)")
bind_params = {
    "tablename": sf_table_namein,
}
results = cur.execute(command, bind_params)
row = cur.fetchall()
conn.commit()
cur.close()

cur = conn.cursor()
# get the rule_name and execution id - then pull them in xcom
stage_path_suffix = '2022-09-29/segmented_cc/_1664445283208/successrecords'
stage_name = '@shubh_ext_stage2/'
stage_load_data_path = stage_name + stage_path_suffix

# command = (
#     "copy into IDENTIFIER(%(tablename)s) from IDENTIFIER(%(stage_load_data_path)s)  FILE_FORMAT=(%(file_format)s) ON_ERROR=(%(on_error)s) MATCH_BY_COLUMN_NAME=(%(case_insensitive)s) PURGE=(%(purge)s)")
command = (
    "copy into IDENTIFIER(%(tablename)s) from %(stage_load_data_path)s  FILE_FORMAT='my_parquet_format' ON_ERROR='CONTINUE' MATCH_BY_COLUMN_NAME='CASE_INSENSITIVE' PURGE=FALSE")
# bind_params = {
#     "tablename": sf_table_namein,
#     "stage_load_data_path": stage_load_data_path,
#     "file_format": 'my_parquet_format',
#     "on_error": 'CONTINUE',
#     "case_insensitive": 'CASE_INSENSITIVE',
#     "purge": 'FALSE'
# }
bind_params = {
    "tablename": sf_table_namein,
    "stage_load_data_path": stage_load_data_path
}
results = cur.execute(command, bind_params)
conn.commit()
cur.close()
