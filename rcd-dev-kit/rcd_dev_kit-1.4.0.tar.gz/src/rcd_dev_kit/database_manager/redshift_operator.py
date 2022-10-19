from typing import Any, List, Dict, Set, Optional
from sqlalchemy import create_engine, inspect, text, Table, MetaData, Column, String
from .s3_operator import S3Operator
from ..pandas_manager import detect_aws_type, check_quality_table_names
from markdownTable import markdownTable
from datetime import date
import connectorx as cx
import pandas as pd
import warnings
import sqlparse
import json
import time
import os
import re


def drop_from_s3_and_redshift(database, tables2drop_list):
    ro = RedshiftOperator(database=database)
    ddl_model = ro.get_DDL(verbose=False,
                           avoid_schema_names=["platform",
                                               "pg_catalog",
                                               "information_schema",
                                               "pv_reference",
                                               "pv_intermediary_tables",
                                               "public",
                                               "prod_pre_aggregations",
                                               "pg_automv",
                                               "admin"])
    ddl_model.fillna("", inplace=True)

    ddl_to_drop = ddl_model[ddl_model.table_name.isin(tables2drop_list)]

    unique_table_names_to_drop_df = ddl_to_drop[~ddl_to_drop['table_name'].duplicated(keep=False)]
    tables_duplicated_name_to_drop_df = ddl_to_drop[ddl_to_drop['table_name'].duplicated(keep=False)]

    for index, row in unique_table_names_to_drop_df.iterrows():
        print(f"\n - {row['schema_name']}.{row['table_name']}: ")
        ro._schema = row["schema_name"]
        ro._table = row["table_name"]
        ro.drop_from_s3_and_redshift(bucket=os.environ.get("S3_BUCKET_DATAMART"))

    if tables_duplicated_name_to_drop_df.__len__() > 0:
        print("\nSomes duplicated table names were found, please select which one you want to drop:")
        for t_name in tables_duplicated_name_to_drop_df.table_name.unique():
            duplicated_by_table_df = tables_duplicated_name_to_drop_df[tables_duplicated_name_to_drop_df['table_name'] == t_name]
            schemas = duplicated_by_table_df['schema_name'].values

            print(f"\nFor table {t_name}, you have it on {', '.join(schemas)}. From which schema you want to drop ?")
            print(f"If you answer with 'all', everything will be dropped.")
            selected_schema = input('Schema:')
            if selected_schema.lower() == 'all':
                for index, row in duplicated_by_table_df.iterrows():
                    ro._schema = row["schema_name"]
                    ro._table = row["table_name"]
                    ro.drop_from_s3_and_redshift(bucket=os.environ.get("S3_BUCKET_DATAMART"))
                print(f"Table {t_name} dropped from {', '.join(schemas)}.")
            else:
                ro._schema = selected_schema
                ro._table = t_name
                ro.drop_from_s3_and_redshift(bucket=os.environ.get("S3_BUCKET_DATAMART"))
                print(f"Table {t_name} dropped from {selected_schema}.")

def data_warehouse_quality_report(report_file_name: str = "datawarehouse_quality_report"):
    ro = RedshiftOperator(database="oip")

    ddl_model = ro.get_DDL(verbose=True,
                           avoid_schema_names=["platform",
                                               "pg_catalog",
                                               "information_schema",
                                               "pv_reference",
                                               "pv_intermediary_tables",
                                               "public",
                                               "prod_pre_aggregations",
                                               "pg_automv",
                                               "admin"])
    ddl_model.fillna("", inplace=True)
    tables_info_df = read_from_redshift(database='oip', schema='pg_catalog', table='svv_table_info', method="auto")
    tables_info_df = tables_info_df[['database', 'schema', 'table', 'tbl_rows', 'empty']]

    string_check = re.compile("[\s@\-!#$%^&*+()<>?/\|}{~:]")

    if os.path.exists(f"{report_file_name}.txt"):
        os.remove(f"{report_file_name}.txt")
    quality_report = open(f"{report_file_name}.txt", "a+")
    quality_report.write("Data Warehouse Quality Report\n\n")
    quality_report.write(
        "This report aims to help the developers cleaning/improving their tables on our Data Warehouse.\n"
        "All the comments are done owner-wise in order to help the users identifying more easily which tables are "
        "related to each user.\n\n")

    for user_i in ddl_model["owner_user"].unique():
        print(f"{user_i}  ✅")
        redshift_df = ddl_model.loc[ddl_model["owner_user"] == user_i]
        redshift_df_info = pd.merge(redshift_df, tables_info_df, left_on=['schema_name', 'table_name'],
                                    right_on=['schema', 'table'])
        tables_without_descr_df = \
        redshift_df[(redshift_df["table_description"] == "") | (redshift_df["columns_description"] == "")][
            ["schema_name", "table_name"]]

        tables_contains_last_update_df = redshift_df[
            redshift_df["table_description"].str.contains("Last Update", case=False)]

        tables_last_update_df = tables_contains_last_update_df.copy()
        tables_last_update_df["last_update"] = tables_contains_last_update_df["table_description"].apply(
            lambda x: re.findall(r'.*\n\s*last update\s*:(.*)\n', x.lower())[0].strip().replace(" ", "").replace("–",
                                                                                                                 "/").replace(
                "-", "/").replace(".", "").split("/")[-1])

        tables_last_update_nonint_df = tables_last_update_df[~tables_last_update_df["last_update"].str.isdigit()]
        tables_last_update_int_df = tables_last_update_df[tables_last_update_df["last_update"].str.isdigit()]
        tables_last_update_old_df = tables_last_update_int_df[
            tables_last_update_int_df["last_update"].astype('int') < 2022]

        bad_table_names = []
        bad_column_names = []
        for index, row in redshift_df.iterrows():
            table_name = row['table_name']
            schema_name = row['schema_name']
            create_table_queries = row["create_query"]

            column_names = re.findall(r'.*\t,?(.*) (TIME\S|SMALLINT|INTEGER|BIGINT|DECIMAL|REAL|DOUBLE|'
                                      r'BOOLEAN|CHAR|VARCHAR|DATE|GEOMETRY|GEOGRAPHY|HLLSKETCH|SUPER|'
                                      r'VARBYTE).*\n', create_table_queries)
            column_names = [col[0].replace('"', '') for col in column_names]

            if not table_name.isascii() or (string_check.search(table_name) is not None):
                table_name_df = pd.DataFrame(data={'schema_name': [schema_name], 'table_name': [table_name]})
                bad_table_names.append(table_name_df)

            bad_columns = [col for col in column_names if (not col.isascii() or (string_check.search(col) is not None))]
            if bad_columns.__len__() > 0:
                bad_column_names.append([schema_name, table_name, bad_columns])

        quality_report.write(f"\n \n---> Tables from {user_i}:\n \n")
        quality_report.write(f"\t - Tables having a non-standard Name:\n")
        if bad_table_names.__len__() > 0:
            bad_table_names_df = pd.concat(bad_table_names, ignore_index=True)
            quality_report.write(
                markdownTable(bad_table_names_df.to_dict(orient='records'))
                    .setParams(row_sep='topbottom',
                               padding_width=5,
                               padding_weight='left').getMarkdown().replace("`", "").replace("\n", "\n\t"))
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")

        quality_report.write(f"\t - Tables having non-standard Column Names\n")
        if bad_column_names.__len__() > 0:
            for tab_i in bad_column_names:
                quality_report.write(f"\t\tTable: {tab_i[0]}.{tab_i[1]}:\n")

                for col_i in tab_i[2]:
                    quality_report.write(f"\t\t\t: {col_i}\n")
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")

        quality_report.write(f"\t - Tables missing Descriptions and/or Column Descriptions:\n")
        if tables_without_descr_df.__len__() > 0:
            quality_report.write(
                markdownTable(tables_without_descr_df.to_dict(orient='records'))
                    .setParams(row_sep='topbottom',
                               padding_width=5,
                               padding_weight='left').getMarkdown().replace("`", "").replace("\n", "\n\t"))
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")

        quality_report.write(
            f"\t - Tables with less than 5 rows (TO VERIFY IF IT'S INDEED CONSISTENT AND NOTHING IS WRONG):\n")
        tables_less_five_df = redshift_df_info[redshift_df_info["tbl_rows"] < 5][['schema', 'table', 'tbl_rows']]
        if tables_less_five_df.__len__() > 0:
            quality_report.write(
                markdownTable(tables_less_five_df.to_dict(orient='records'))
                    .setParams(row_sep='topbottom',
                               padding_width=5,
                               padding_weight='left').getMarkdown().replace("`", "").replace("\n", "\n\t"))
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")

        quality_report.write(
            f"\t - Tables whose description has a 'Last Update' topic dating longer than 2022 or has a non-standard object. "
            f"(TO VERIFY IF IT'S INDEED CONSISTENT AND NOTHING IS WRONG).\n"
            f"\t   In case you've put 22 instead of 2022, please correct it as well :) :\n")
        if tables_last_update_df.__len__() > 0:
            tables_last_update_old_and_wrong_df = pd.concat([tables_last_update_nonint_df, tables_last_update_old_df],
                                                            ignore_index=True)
            tables_last_update_old_and_wrong_df = tables_last_update_old_and_wrong_df[
                ["schema_name", "table_name", "last_update"]]
            if tables_last_update_old_df.__len__() > 0:
                quality_report.write(
                    markdownTable(tables_last_update_old_and_wrong_df.to_dict(orient='records'))
                        .setParams(row_sep='topbottom',
                                   padding_width=5,
                                   padding_weight='left').getMarkdown().replace("`", "").replace("\n", "\n\t"))
            else:
                quality_report.write(f"\t   ✅ Everything is fine !")
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")

        quality_report.write(f"\t - Tables with duplicated names but in different schemas: \n")
        duplicated_table_names_df = redshift_df[redshift_df['table_name'].duplicated(keep=False)][
            ['schema_name', 'table_name']].sort_values(by='table_name', ascending=True)
        if duplicated_table_names_df.__len__() > 0:
            quality_report.write(
                markdownTable(duplicated_table_names_df.to_dict(orient='records'))
                    .setParams(row_sep='topbottom',
                               padding_width=5,
                               padding_weight='left').getMarkdown().replace("`", "").replace("\n", "\n\t"))
        else:
            quality_report.write(f"\t   ✅ Everything is fine !")
        quality_report.write("\n\n")
    quality_report.close()

    print("Data Warehouse Quality Report Generated Successfully. 🔥")


def find_tables_by_column_name(column_name: str, database: Optional[str] = None, verbose: bool = False) -> pd.DataFrame:
    """
    For a given column name, this function will return a Dataframe containing the table name, the schema name and the
    column description of all the tables having this column.

    :param column_name: Name of the column to be searched.
    :param database: In which database this column should be searched.
    :param verbose: Details of the Redshift Operator call on the tables.
    :return:
    """
    print("📮 Connecting to Redshift...")
    db = os.environ.get("REDSHIFT_DB") if database is None else database
    ro = RedshiftOperator(database=db)

    print(f"📋 Getting tables w.r.t the column: {column_name}")
    df_by_column = ro.get_tables_by_column_name(col_name=column_name, verbose=verbose)

    ro.conn.close()
    print("✅ Process finished successfully!")

    return df_by_column


def send_metadata_to_redshift(table_name: str, database: Optional[str] = None, file_path: str = "table_metadata.json",
                              first_data: date = None, last_data: date = None):
    """
    Use this function to send the Table and Column Descriptions to Redshift. There is a standard JSON file which this
    function reads to retrieve all the mandatory descriptions.

    :param table_name: Table name.
    :param first_data: The most ancient date present regarded by your data -> [DD-MM-YYYY].
    :param last_data: The most recent date present regarded by your data -> [DD-MM-YYYY].
    :param database: Redshift database name.
    :param file_path: Path to the JSON file.
    :return:
    """
    if (not first_data) or (not last_data):
        raise NameError("first_data or last_data are missing. "
                        "Please, pass these values under the following format: datetime.date(year, month, day).")

    print(f"🎬 Reading the {file_path} ...")
    table_metadata_dict = json.loads(open(file_path).read())

    # print("📮 Connecting to Redshift...")
    db = os.environ.get("REDSHIFT_DB") if database is None else database
    ro = RedshiftOperator(database=db)

    source_track_df_list = []
    print("💿 Generating the SQL Query from the JSON...")
    list_tables = [table["name"] for table in table_metadata_dict["tables"]]
    try:
        table_id = list_tables.index(table_name)
        table = table_metadata_dict["tables"][table_id]
    except ValueError:
        print("❌ Exiting the process...")
        print(f"😰 The chosen table {table_name} is not present on the json file.")
        raise

    print(f"\t📌 {table['name']}:")
    for key, value in table['details'].items():
        if key == "description":
            if len(value) > 600:
                raise OverflowError(f"❌ {key.capitalize()} value for table {table['name']} is too long. "
                                    "Please, limit yourself to 600 chars max.")
        else:
            if len(value) > 400:
                raise OverflowError(f"❌ {key.capitalize()} value for table {table['name']} is too long. "
                                    "Please, limit yourself to 400 chars max.")

    print(f"\t\t🛠 Checking the metadata constraints...")
    table_description_str = f"Country: {table['details']['country']}\n\n" \
                            f"Table Schema: {table['details']['table_schema']}\n\n" \
                            f"Description: {table['details']['description']}\n\n" \
                            f"Source Name: {', '.join(table['details']['source_name'])}\n\n" \
                            f"Source UUID: {', '.join(table['details']['source_uuid'])}\n\n" \
                            f"Geographical Coverage: {table['details']['geographical_coverage']}\n\n" \
                            f"Geographical Granularity: {table['details']['geographical_granularity']}\n\n" \
                            f"Update Frequency: {table['details']['update_frequency']}\n\n" \
                            f"Last Update: {date.today().strftime('%d-%m-%Y')}\n\n" \
                            f"First Data: {first_data.strftime('%d-%m-%Y')}\n\n" \
                            f"Last Data: {last_data.strftime('%d-%m-%Y')}\n\n" \
                            f"Caveats: {table['details']['caveats']}\n\n" \
                            f"Additional Info: {table['details']['additional_information']}\n\n" \
                            f"Update Process: {table['details']['update_process']}\n\n" \
                            f"Import Format: {table['details']['file_import_format']}\n\n" \
                            f"Import Separator: {table['details']['file_import_separator']}\n\n" \
                            f"Table Type: {table['details']['table_type']}"

    table_description_sql = f"COMMENT ON table {table['details']['table_schema']}.{table['name']} " \
                            f"IS '{table_description_str}';"

    source_track_df_list.append(
        pd.DataFrame(
            data={"table_name": [table['name']],
                  "source_name": [', '.join(table['details']['source_name'])],
                  "source_link": [', '.join(table['details']['source_link'])]}
        ))

    columns_description_sql_lst = []
    for column in table["columns"]:
        sql = f"COMMENT ON column {table['details']['table_schema']}.{table['name']}.{column['name']} " \
              f"IS '{column['description']}';"
        columns_description_sql_lst.append(sql)
    columns_description_sql = "\n".join(columns_description_sql_lst)

    print("\t\t📋 Launching Table Description query...")
    ro.conn.execution_options(isolation_level="AUTOCOMMIT").execute(text(table_description_sql))

    print("\t\t🏛 Launching Columns Description query...")
    ro.conn.execution_options(isolation_level="AUTOCOMMIT").execute(text(columns_description_sql))

    print(f"\t\t🎉 Metadata insertion finished for {table['name']}")
    ro.conn.close()

    # if database == "oip":
    #     print("🎁 Updating admin.global_sources_track_table table with the new source_link's.")
    #     new_sources_df = pd.concat(source_track_df_list, ignore_index=True)
    #     need_update_tables = new_sources_df.table_name.values
    #
    #     global_sources_df = read_from_redshift(database="oip", method="auto",
    #                                            schema="admin", table="global_sources_track_table")
    #
    #     tables_not_changed_df = global_sources_df[~global_sources_df.table_name.isin(need_update_tables)]
    #     updated_sources_df = pd.concat([tables_not_changed_df, new_sources_df], ignore_index=True)
    #
    #     send_to_redshift(database="oip", schema="admin", table="global_sources_track_table",
    #                      df=updated_sources_df, check=True, send_metadata=False, drop=True)

    print("✅ Process finished successfully!")


def send_to_redshift(database: str,
                     schema: str,
                     table: str,
                     df: pd.DataFrame,
                     from_bucket: Optional[str] = None,
                     send_metadata: bool = True,
                     json_path: str = "table_metadata.json",
                     first_data: Optional[date] = None,
                     last_data: Optional[date] = None,
                     **kwargs: Any, ) -> None:
    """
    Function send_to_redshift.
    Use this function to send data to s3 bucket and redshift(using copy).

    Args:
        database (str): The name of database in redshift.
        schema(str): The name of schema in redshift&s3.
        table(str): The name of the table to save.
        df(pd.DataFrame): The dataframe to send.
        from_bucket(str): S3 Bucket from where the table will be retrieved.
        send_metadata(bool): It will call the send_metadata_to_redshift() function in order to retrieve the
                             metadata descriptions from the local json file.
        json_path(str): The path to the json file containing the Table and Columns Descriptions.
        first_data(str): The most ancient date present regarded by your data.
        last_data(str): The most recent date present regarded by your data.

    Kwargs:
        check(bool): False by default. If True, check the column type and length is consistent as current table in
                     redshift.
        drop(bool): (Avoid to use!) False by default. If True, drop the datatable which exists already.
        debug(bool): False by default. If True, print debug information.
        dct_aws_type(Dict): Dictionary of column name as key, AWS as value. Generated by pandas_manager.detect_aws_type
                            by default, manuel input is possible)
        bucket(str): Datamart bucket by default. S3 Bucket name to save the data.


    Examples:
        >>> from rcd_dev_kit import database_manager
        >>> database_manager.send_to_redshift(database="my_database", schema="my_schema", table="my_table", df=my_dataframe, dct_aws_type=my_dct_aws_type)
    """
    # Check if the column names agree with the SQL standards. It must not have accented letters or any special
    # character.
    check_quality_table_names(table_name=table, df=df)

    so = S3Operator()
    if not from_bucket:
        if database == "staging":
            so.bucket = kwargs.get("bucket", os.environ.get("S3_BUCKET_DEV"))
            if so.bucket is None:
                raise ValueError("❌ Environment variable missing: S3_BUCKET_DEV")
        else:
            so.bucket = kwargs.get("bucket", os.environ.get("S3_BUCKET_DATAMART"))
            if so.bucket is None:
                raise ValueError("❌ Environment variable missing: S3_BUCKET_DATAMART")
    else:
        so.bucket = from_bucket

    ro = RedshiftOperator(database=database, debug=kwargs.get("debug", False))
    ro.schema = schema
    ro.table = table
    ro.aws_type = kwargs.get("dct_aws_type", detect_aws_type(df=df))

    if kwargs.get("drop") is True:
        ro.drop_from_s3_and_redshift(bucket=so.bucket)

    so.send_to_s3_obj(df=df, s3_file_path=os.path.join(schema, f"{table}.csv"), sep="|")
    ro.process_table(bucket=kwargs.get("bucket", so.bucket), sep="|", check=kwargs.get("check", False))

    if send_metadata:
        try:
            send_metadata_to_redshift(table_name=table, database=database, file_path=json_path,
                                      first_data=first_data, last_data=last_data)
        except ValueError:
            print(f"🔍 Please check if the name is correct or set send_metadata to false.")
            raise
        except FileNotFoundError:
            print(f"⁉️ The JSON file containing all metadata was not found. Please, either check if the "
                  f"file path passed is correct, or set send_metadata to False.")
            raise
        finally:
            ro.conn.close()
    else:
        if table != "global_sources_track_table":
            warnings.warn("🥲 It seems that you are not sending this table with its metadata. "
                          "Remember that it's important to have a well commented data warehouse. Please, add a.s.a.p a "
                          "table_metadata.json file to your project containing the table's metadata."
                          "For the .json template, please check https://github.com/OpenInnovationProgram/rcd-dev-kit/blob/main/table_metadata.example.json .",
                          ResourceWarning)


def read_from_redshift(database: str, method: str, **kwargs) -> pd.DataFrame:
    """
    Function read_from_redshift.
    Use this function to read data from redshift.

    Args:
        database(str): The name of database in redshift.
        method(str): Default "auto", retreive data with limit and select, or "sql" retreive data with sql query.
    Kwargs:
        schema(str): The name of schema in redshift.
        table(str): The name of the table in redshift.
        limit(int): The line limit to read. Default None.
        select(str): The content to select. Default "*".

        debug(bool): False by default. If True, print debug information.

    Examples:
        >>> from rcd_dev_kit import database_manager
        >>> database_manager.read_from_redshift(database="my_database", method="auto", schema="my_schema", table="my_table")
        >>> database_manager.read_from_redshift(database="my_database", method="sql", sql_query='SELECT * FROM my_schema.my_table')
    """
    ro = RedshiftOperator(database=database, debug=kwargs.get("debug", False))
    ro.schema = kwargs.get("schema")
    ro.table = kwargs.get("table")
    if method == "auto":
        df_from_redshift = ro.read_from_redshift(limit=kwargs.get("limit", None), select=kwargs.get("select", "*"))
    elif method == "sql":
        df_from_redshift = ro.read_sql_from_redshift(sql_query=kwargs.get("sql_query", None))
    else:
        raise ValueError(f"Unrecognized method: {method}")
    return df_from_redshift


class RedshiftOperator:
    """
    RedshiftOperator, build redshift connection, read data from or send data to redshift.

    Args:
        database (str): The database for connection.

    Examples:
        >>> from rcd_dev_kit import database_manager
        >>> ro = database_manager.RedshiftOperator()
        >>> ro.read_from_redshift(schema="my_schema", table="my_table", limit=10)
    """

    def __init__(self,
                 database: str = os.environ.get("REDSHIFT_DB"), debug: bool = False) -> None:
        self.redshift_user = os.environ.get("REDSHIFT_USER")
        self.redshift_password = os.environ.get("REDSHIFT_PASSWORD")
        self.redshift_host = os.environ.get("REDSHIFT_HOST")
        self.redshift_port = os.environ.get("REDSHIFT_PORT")
        self.redshift_database = database
        if database is None:
            raise ValueError(f"❌Input database not defined in .env")
        self.engine = create_engine(
            f"redshift+psycopg2://{self.redshift_user}:{self.redshift_password}@{self.redshift_host}:{self.redshift_port}/{self.redshift_database}",
            echo=debug,
        )
        self.conn = self.engine.connect()
        self._schema = None
        self._table = None
        self._aws_type = dict()
        self.df_std_error = None
        self.s3_bucket = None
        self.ddl_table = None
        # Session = sessionmaker(bind=self.engine)
        # self.session = Session()

    """
        property
    """

    @property
    def schema(self) -> str:
        return self._schema

    @schema.setter
    def schema(self, schema: str) -> None:
        print(f"☑️Setting schema to {schema}")
        self._schema = schema

    @property
    def table(self) -> str:
        return self._table

    @table.setter
    def table(self, table: str) -> None:
        print(f"☑️Setting table to {table}")
        self._table = table

    @property
    def aws_type(self):
        return self._aws_type

    @aws_type.setter
    def aws_type(self, dct_aws_type: Dict) -> None:
        print(f"☑️Setting AWS type: {dct_aws_type}")
        self._aws_type = dct_aws_type

    """
        read method
    """

    def read_from_redshift(self, limit: bool = None, select: str = "*", method: str = "pandas") -> pd.DataFrame:
        sql_limit = limit if limit else "NULL"
        query = f"SELECT {select} FROM {self._schema}.{self._table} LIMIT {sql_limit}"
        if method == "pandas":
            df_result = pd.read_sql_query(query, self.engine)
        if method == "ctx":
            df_result = cx.read_sql(
                f"redshift+psycopg2://{self.redshift_user}:{self.redshift_password}@{self.redshift_host}:{self.redshift_port}/{self.redshift_database}",
                query, partition_num=8, return_type="pandas", )
        return df_result

    def read_sql_from_redshift(self, sql_query: str) -> pd.DataFrame:
        df_result = pd.read_sql_query(sql_query, self.engine)
        return df_result

    """
         table oriented method
    """

    def detect_table(self, ddl=False) -> bool:
        inspect_engine = inspect(self.engine)
        if not ddl:
            table_exists = inspect_engine.has_table(schema=self._schema, table_name=self._table)
        else:
            table_exists = inspect_engine.has_table(schema="admin", table_name="v_generate_tbl_ddl")
        return table_exists

    def clean_table(self) -> None:
        self.conn.execute(f"TRUNCATE TABLE {self._schema}.{self._table}")

    def drop_table(self) -> None:
        metadata = MetaData()
        datatable = Table(self._table, metadata, schema=self._schema)
        datatable.drop(self.engine, checkfirst=False)

    def create_table(self) -> None:
        assert (self._aws_type is not None), f"❌ dct_aws_type is not defined when creating table!"
        print(f"🔁{self._schema}.{self._table} structure doesn't exist, creating...")
        metadata = MetaData()
        query_tuple = tuple(
            Column(column_name, aws_type)
            for column_name, aws_type in self._aws_type.items()
        )
        datatable = Table(self._table, metadata, *query_tuple, schema=self._schema)
        datatable.create(self.engine, checkfirst=True)
        print(f"🏗Table Structure Created!")

    def get_current_structure(self) -> List:
        print(f"❗️{self._schema}.{self._table} structure exists, retrieving current structure...")
        get_current_len_query = f"""
        SELECT table_schema, table_name, column_name, data_type, character_maximum_length
        FROM information_schema.columns
        WHERE table_schema = '{self._schema}'
        AND table_name = '{self._table}'
        AND data_type = 'character varying'
        ORDER BY table_name;
        """
        df_current_structure = self.conn.execute(get_current_len_query)
        lst_current_structure = [(row[2], row[4]) for row in df_current_structure]
        return lst_current_structure

    def check_structure_consistency(self) -> Set:
        assert (self._aws_type is not None), f"❌ dct_aws_type is not defined when checking consistency!"
        # check varchar type
        lst_current_structure = self.get_current_structure()
        lst_new_structure = [(column_name, aws_type.length)
                             for column_name, aws_type in self._aws_type.items()
                             if isinstance(aws_type, String)]
        new_varchar = set(lst_new_structure) - set(lst_current_structure)
        return new_varchar

    def update_structure(self, iter_new_structure: Set) -> None:
        print(f"⚠️There are some columns need update: {iter_new_structure}")
        self.clean_table()
        for column, new_len in iter_new_structure:
            update_query = f"""
            ALTER TABLE "{self._schema}"."{self._table}"
            ALTER COLUMN "{column}" TYPE varchar({new_len});
            """
            self.conn.execution_options(isolation_level="AUTOCOMMIT").execute(update_query)
        print(f"✨Table Structure Updated!")

    def copy_from_s3(self,
                     bucket: str,
                     prefix: str,
                     s3_table: str,
                     sep: str,
                     redshift_schema: str,
                     redshift_table: str) -> None:
        s3_file_path = os.path.join(bucket, prefix, f"{s3_table}.csv")
        query = f"""
        COPY {redshift_schema}.{redshift_table} 
        FROM 's3://{s3_file_path}' 
        WITH CREDENTIALS 'aws_access_key_id={os.environ.get('AWS_ACCESS_KEY_ID')};aws_secret_access_key={os.environ.get('AWS_SECRET_ACCESS_KEY')}'
        REGION '{os.environ.get('AWS_DEFAULT_REGION')}'
        DELIMITER '{sep}'
        REMOVEQUOTES
        IGNOREHEADER 1
        """
        result = self.conn.execution_options(autocommit=True).execute(query)
        result.close()
        print(f"🥳Table is copied to redshift from S3.\n")

    def unload_to_s3(self, quotes: bool = False):
        table_name = f'"{self.table.lower()}"' if quotes else self.table.lower()
        query = f"""
                UNLOAD ('SELECT * FROM {self.redshift_database.lower()}.{self.schema.lower()}.{table_name.lower()}')
                to 's3://oip-openinnovationprogram-datamart/big_data_format/{self.schema.lower()}/{table_name.lower()}/'
                WITH CREDENTIALS 'aws_access_key_id={os.environ.get("AWS_ACCESS_KEY_ID")};aws_secret_access_key={os.environ.get("AWS_SECRET_ACCESS_KEY")}'
                REGION 'eu-west-3'
                PARALLEL ON
                FORMAT PARQUET
                MAXFILESIZE 5 gb
                ALLOWOVERWRITE;
                """
        result = self.conn.execution_options(autocommit=True).execute(query)
        result.close()

    def load_std_error(self) -> None:
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM stl_load_errors"))
            self.df_std_error = pd.DataFrame(result, columns=["userid", "slice", "tbl", "starttime", "session",
                                                              "query", "filename", "line_number", "colname", "type",
                                                              "col_length", "position", "raw_line", "raw_field_value",
                                                              "err_code", "err_reason", "is_partial", "start_offset"]) \
                .sort_values(by=["starttime"], ascending=[False])

    # def load_svv_table_info(self) -> None:
    #     with self.engine.connect() as connection:
    #         result = connection.execute(text("select * from pg_catalog.svv_table_info;"))
    #         self.df_std_error = pd.DataFrame(result, columns=["database", "slice", "tbl", "starttime", "session",
    #                                                           "query", "filename", "line_number", "colname", "type",
    #                                                           "col_length", "position", "raw_line", "raw_field_value",
    #                                                           "err_code", "err_reason", "is_partial", "start_offset"]) \
    #             .sort_values(by=["starttime"], ascending=[False])

    """
      summary method
    """

    def process_table(self, bucket: str, sep: str, check: bool = False) -> None:
        table_exists = self.detect_table()
        if table_exists and (check is False):
            pass
        elif table_exists and (check is True):
            iter_new_structure = self.check_structure_consistency()
            if len(iter_new_structure) > 0:
                self.update_structure(iter_new_structure=iter_new_structure)
            else:
                print(f"🥳Table Structure is consistent!")
        else:
            self.create_table()
        self.clean_table()

        self.copy_from_s3(bucket=bucket, prefix=self._schema, s3_table=self._table, sep=sep,
                          redshift_schema=self._schema, redshift_table=self._table)

    def drop_from_s3_and_redshift(self, bucket: str = os.environ.get("S3_BUCKET_DEV")):
        """
        If we want to drop a table from both Redshift and S3 at once, we can simply call this function.
        :param bucket: Bucket name on s3 where the object is placed.
        :return:
        """
        so = S3Operator()
        so.bucket = bucket
        so.prefix = self.schema

        if self.detect_table():
            print("✂️ Dropping Redshift Table...")
            self.drop_table()
        else:
            print(f"\t🔍 Redshift | Table {self.table} doesn't exist on {self.schema}. Thus, no need to drop...")

        if so.table_exists(self.table):
            print("✂️ Removing S3 Object...")
            so.remove_object(self.table)
        else:
            print(f"\t🔍 S3 | Object {self.table}.csv doesn't exist on prefix {self.schema}. Thus, no need to drop...")

    def generate_DDL(self):
        """
        This function launches the query present in v_generate_tbl_ddl.sql to assemble the DDL queries from all the
        redshift tables into a single one.
        :return:
        """
        query = (open(os.path.join(os.path.dirname(__file__), "../sql_utils/v_generate_tbl_ddl.sql"), "r")
                 .read()
                 .replace("%", "%%"))
        self.conn.execution_options(isolation_level="AUTOCOMMIT").execute(text(query))

    def get_DDL(self,
                schema_names: Optional[List[str]] = None,
                avoid_schema_names: Optional[List[str]] = None,
                table_names: Optional[List[str]] = None,
                avoid_table_names: Optional[List[str]] = None,
                verbose: bool = True,
                output_to: Optional[str] = None) -> pd.DataFrame:
        """
        This function makes a Redshift request to retrieve the v_generate_tbl_ddl table responsible for
        stocking the ddl queries from all the redshift tables.

        :param schema_names: List os schemas to be considered if customization is needed.
        :param avoid_schema_names: List of schemas to be excluded if any.
        :param table_names: List of tables to be considered if customization is needed.
        :param avoid_table_names:List of tables to be excluded if any.
        :param verbose: Print details.
        :param output_to: If we want to export this table somewhere, tha path must be passed here.
        :return:
        """
        # Generate the DDL table.
        self.generate_DDL()
        time.sleep(2)  # Allow a little of time for the query to finish executing.

        if avoid_schema_names is None:
            avoid_schema_names = ["public", "pv_reference", "platform", "pv_intermediary_tables", "pg_catalog",
                                  "information_schema"]

        print("⏳ Generating the DDL Table. It can take a while...")
        query = f"select * from admin.v_generate_tbl_ddl"
        result = self.conn.execute(text(query)).all()
        if not schema_names:
            schema_names = list(set([record.schemaname for record in result]))

        dfs = []
        for schema in set(schema_names).difference(avoid_schema_names):
            if verbose:
                print(schema)
            if not table_names:
                table_names_list = list(set([record.tablename for record in result if record.schemaname == schema]))
                if avoid_table_names:  # Exclude the tables if any.
                    table_names_list = set(table_names_list).difference(avoid_table_names)
            else:
                # Intercession between both sets.
                table_names_list = list(set(table_names) &
                                        set([record.tablename for record in result if record.schemaname == schema]))

            for table in table_names_list:
                if verbose:
                    print(f" - {table}")
                entire_query_str = ""
                for record in result:
                    if (record.schemaname == schema) and (record.tablename == table):
                        line = (record.ddl.replace(" ", " ").replace("'\"", "'").replace("\"'", "'").replace('""', '"'))
                        if line.count("'") > 2:
                            line = "'".join([line.split("'")[0], "''".join(line.split("'")[1:-1]), line.split("'")[-1]])
                        entire_query_str += f"{line}\n"

                entire_query_str = entire_query_str.replace(".year ", '."year" ') \
                    .replace(".level ", '."level" ') \
                    .replace(".region ", '."region" ') \
                    .replace(".names ", '."names" ') \
                    .replace(".type ", '."type" ') \
                    .replace(".role ", '."role" ') \
                    .replace(".provider ", '."provider" ') \
                    .replace(".location ", '."location" ') \
                    .replace(".index ", '."index" ')

                owner_user = (
                    re.findall(r'ALTER TABLE .* owner to (\"?.+\"?);', entire_query_str)[-1].replace('"', '')
                    if len(re.findall(r'ALTER TABLE .* owner to (\"?.+\"?);', entire_query_str)) > 0
                    else ""
                )

                corrected_query = sqlparse.split(entire_query_str)

                create_sql = "".join([statement for statement in corrected_query if
                                      "CREATE TABLE IF NOT EXISTS".lower() in statement.lower()])
                create_sql = ";\n".join(create_sql.split(";\n")[1:])
                primary_key = (
                    re.findall(r",PRIMARY KEY \((\w+)\)", create_sql)[-1]
                    if len(re.findall(r",PRIMARY KEY \((\w+)\)", create_sql)) > 0
                    else ""
                )
                unique_key = (
                    re.findall(r",UNIQUE \((\w+)\)", create_sql)[-1]
                    if len(re.findall(r",UNIQUE \((\w+)\)", create_sql)) > 0
                    else ""
                )
                comment_table_sql = "".join(
                    [
                        statement
                        for statement in corrected_query
                        if "COMMENT ON table".lower() in statement.lower()
                    ]
                )
                comment_columns_sql = "\n".join(
                    [
                        statement
                        for statement in corrected_query
                        if "COMMENT ON column".lower() in statement.lower()
                    ]
                )
                foreign_key_sql = "\n".join(
                    [
                        statement
                        for statement in corrected_query
                        if "FOREIGN KEY".lower() in statement.lower()
                    ]
                )

                # Check if the column names agree with the SQL standards. It must not have accented letters or any special character.
                # For some reason, when we retrieve the DDL from Redshift, it gives the CREATE TABLE Sql correctly but not
                # the COMMENT ON Sql script. Whenever a column name has a non-ASCII name, we must parse it as string (under quotes).
                # This script down below corrects the COMMENT ON string with the quotes notation.
                sql_columns = re.findall(r"\n\t[,]*\"([.\S]+)\"\s+", create_sql)
                string_check = re.compile(r"[@\-!#$%^&*+()<>?/\|}{~:]")
                for var in sql_columns:
                    if not var.isascii() or (string_check.search(var) is not None):
                        comment_columns_sql = comment_columns_sql.replace(
                            f".{var} IS", f'."{var}" IS'
                        )

                df = pd.DataFrame(
                    {
                        "schema_name": schema,
                        "table_name": table,
                        "primary_key": primary_key,
                        "unique_key": unique_key,
                        "create_query": create_sql,
                        "table_description": comment_table_sql.strip(),
                        "columns_description": comment_columns_sql.strip(),
                        "foreign_keys": foreign_key_sql.strip(),
                        "owner_user": owner_user.strip()
                    },
                    index=[1],
                )
                dfs.append(df)

        print("DDL Table generated!")
        if len(dfs) > 0:
            self.ddl_table = pd.concat(dfs, ignore_index=True).reset_index(drop=True)
            self.ddl_table.sort_values(["schema_name", "table_name"], ascending=[1, 1], ignore_index=True, inplace=True)
        else:
            self.ddl_table = pd.DataFrame(columns=["schema_name", "table_name", "primary_key", "unique_key",
                                                   "create_query", "table_description", "columns_description",
                                                   "foreign_keys", "owner_user"])

        if output_to is not None:
            print("Exporting table to folder.")
            if not os.path.exists(output_to):
                os.makedirs(output_to)
            self.ddl_table.to_csv(os.path.join(output_to, "ddl_model.txt"), sep="\t", encoding="utf-8", index=False)
            print(f"🥳DDL now is available in {output_to}/ddl_model.txt\n")

        return self.ddl_table

    def get_tables_by_column_name(self, col_name: str, verbose=False) -> pd.DataFrame:
        """
        For a given column name, this function will return a Dataframe containing the table name, the schema name
        and the column description of all the tables having this column.
        :param col_name: Name of the column to be searched.
        :param verbose: Details of the Redshift Operator call on the tables.
        :return:
        """
        if self.ddl_table is None:
            self.get_DDL(verbose=verbose)

        df_filtered = self.ddl_table[self.ddl_table.create_query.str.contains(f'[\s,"]{col_name}[\s"]')]

        schema_names_lst = df_filtered["schema_name"].values
        table_names_lst = df_filtered["table_name"].values
        columns_description = df_filtered["columns_description"].apply(
            lambda x: re.findall(f"\\.{col_name} IS '(.*)';", x)[0] if
            len(re.findall(f"\\.{col_name} IS '(.*)';", x)) > 0 else "").values

        data = {'schema_name': schema_names_lst, 'table_name': table_names_lst,
                'column_name': col_name, 'column_description': columns_description}

        return pd.DataFrame(data=data)
