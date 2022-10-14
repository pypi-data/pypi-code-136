from typing import List
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.dbutils import DBUtils
from abc import ABCMeta, abstractmethod
from pyspark.sql.context import SQLContext
from pyspark.sql.session import SparkSession
from delta_table.utils.logger import logger, LogMessage

logger = logger()

# https://docs.databricks.com/spark/latest/spark-sql/language-manual/sql-ref-datatypes.html#language-mappings
DATA_TYPE_MAP = {
    'TINYINT': T.ByteType(),
    'SMALLINT': T.ShortType(),
    'INT': T.IntegerType(),
    'BIGINT': T.LongType(),
    'FLOAT': T.FloatType(),
    'DOUBLE': T.DoubleType(),
    'STRING': T.StringType(),
    'BINARY': T.BinaryType(),
    'BOOLEAN': T.BooleanType(),
    'TIMESTAMP': T.TimestampType(),
    'DATE': T.DateType(),
    'STRUCT': T.StructType()
}

def upsert_to_delta_with_sql(micro_batch_output_df, batchId, merge_sql_stmt):
    """
    Given a merge_sql_stmt, this is the template function for
    delta table upserts.
    """

    micro_batch_output_df.createOrReplaceTempView("updates")
    micro_batch_output_df._jdf.sparkSession().sql(merge_sql_stmt)


def process_micro_batch(micro_batch_output_df, batchId, merge_sql_stmt, unique_id_list=[]):
    """
    Process a micro batch
    """
    if len(unique_id_list) > 0:
        micro_batch_output_df = micro_batch_output_df.dropDuplicates(unique_id_list)
    #micro_batch_output_df = micro_batch_output_df.withColumn("filename", F.input_file_name())
    upsert_to_delta_with_sql(micro_batch_output_df, batchId, merge_sql_stmt)


class DeltaTableColumn:
    """Delta table column

    Create a column for a delta table.  A list of DeltaTableColumn
    are used to create a delta table.

    Args:
        column_name (str): The name of the column
        **kw: Keyword arguments to pass to the column

        Required keyword arguments:
            data_type (str): The data type of the column, must be in DATA_TYPE_MAP

        Optional keyword arguments:
            nulls_allowed (bool): Whether the column is nullable, defaults to True
            is_unique_id (bool): Whether the column is a unique id, defaults to False
            is_partition_key (bool): Whether the column is a partition key, defaults to False

    Example:
        >>> DeltaTableColumn(column_name="id", data_type="int")
    """

    def __init__(self, column_name: str, **kw) -> None:
        self.name = column_name
        self.kw = kw

    @property
    def sql_data_type(self) -> str:
        try:
            return self.kw.get('data_type').upper()
        except Exception as error:
            log_msg = LogMessage()
            log_msg.add('error', str(error))
            log_msg.add('column_name', self.name)
            log_msg.add('message', 'data_type is a required parameter')
            logger.error(str(log_msg))
            raise Exception(f"Error getting data_type for column {self.name}") from error

    @property
    def pyspark_data_type(self) -> str:
        return DATA_TYPE_MAP[self.sql_data_type]

    @property
    def nulls_allowed(self) -> bool:
        if 'nulls_allowed' in self.kw:
            return self.kw.get('nulls_allowed')
        else:
            return True

    @property
    def is_unique_id(self) -> bool:
        if 'is_unique_id' in self.kw:
            return self.kw.get('is_unique_id')
        else:
            return False

    @property
    def is_partition_column(self) -> bool:
        if 'is_partition_column' in self.kw:
            return self.kw.get('is_partition_column')
        else:
            return False

class DeltaTable:
    """
    Wrapper for delta tables
    """

    # _DEFAULT_COLUMNS = [DeltaTableColumn('filename',
    #                                     data_type='STRING',
    #                                     nulls_allowed=True,
    #                                     is_unique_id=False)]

    _DEFAULT_COLUMNS = []

    def __init__(self, schema_name: str,
                 table_name: str,
                 upload_path: str,
                 column_list: List[DeltaTableColumn] = [],
                 **kw) -> None:
        self.schema_name = schema_name
        self.table_name = table_name
        self.upload_path = upload_path
        self.columns = self._get_column_list(column_list)
        self.kw = kw
        self.etl_code_stmts = self.create_table_etl_code()

    # def set_default_columns(self, default_columns = None) -> None:
    #     """
    #     set the default columns
    #     """
    #     if default_columns is None:
    #         self.default_columns = self._DEFAULT_COLUMNS
    #     elif default_columns == []:
    #         self.default_columns = []
    #     else:
    #         self.default_columns = default_columns

    @property
    def default_columns(self) -> List[DeltaTableColumn]:
        return self._DEFAULT_COLUMNS

    def _get_column_list(self, column_list):
        column_list.extend(self.default_columns)
        return column_list

    @property
    def partition_columns(self) -> List[str]:
        return [column.name for column in self.columns if column.is_partition_column]

    @property
    def unique_identifier_columns(self) -> List[str]:
        return [column.name for column in self.columns if column.is_unique_id]

    @property
    def default_column_names(self) -> List[str]:
        return [column.name for column in self.default_columns]

    @property
    def file_table_schema(self):
        """schema excluding self.default_columns"""
        struct_field_list = self.etl_code_stmts['struct_field_list'].copy()
        all_col_names = [col.name for col in struct_field_list]
        for default_col in self.default_column_names:
            if default_col in all_col_names:
                del struct_field_list[all_col_names.index(default_col)]
        return T.StructType(struct_field_list)

    @property
    def table_schema(self):
        return T.StructType(self.etl_code_stmts['struct_field_list'])

    @property
    def create_table_query_str(self):
        return self.etl_code_stmts['create_table_query_str']

    @property
    def upsert_sql_str(self):
        return self.etl_code_stmts['upsert_sql_str']

    @property
    def checkpoint_base_path(self):
        return f"/tmp/delta/{self.schema_name}/{self.table_name}"

    @property
    def checkpoint_path(self):
        return f"{self.checkpoint_base_path}/_checkpoints"

    @property
    def write_path(self):
        return f"/delta/{self.schema_name}/{self.table_name}"

    def create_table_etl_code(self) -> dict:
        """
        Create sql and schema statements necessary for delta table ETL
        """
        # Start the upsert SQL string
        upsert_sql_str = f"MERGE INTO {self.schema_name}.{self.table_name} t USING updates s ON "

        i = 0
        for unique_id in self.unique_identifier_columns:
            upsert_sql_str += f"s.{unique_id} = t.{unique_id} "
            i += 1
            if i < len(self.unique_identifier_columns):
                upsert_sql_str += ", "

        upsert_sql_str += "WHEN MATCHED THEN UPDATE SET "

        # Loop through all columns and create the rest of the ETL code
        struct_field_list = []
        create_table_query_str = f"CREATE TABLE IF NOT EXISTS {self.schema_name}.{self.table_name} ( db_id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1), "
        merge_update_set_str = ""
        merge_insert_str = ""
        merge_insert_values_str = ""
        num_columns = len(self.columns)
        i = 0
        j = 0
        for column in self.columns:
            j += 1
            struct_field_list.append(T.StructField(column.name, column.pyspark_data_type, column.nulls_allowed))
            create_table_query_str += f"{column.name} {column.sql_data_type} "
            if not column.is_unique_id:
                merge_update_set_str += f"t.{column.name} = s.{column.name} "
                if j < num_columns:
                    merge_update_set_str += ", "
            merge_insert_str += f"t.{column.name}"
            merge_insert_values_str += f"s.{column.name}"
            i += 1
            if i < num_columns:
                create_table_query_str += ", "
                merge_insert_str += ", "
                merge_insert_values_str += ", "


        if len(self.partition_columns) > 0:
            create_table_query_str += ") PARTITIONED BY ( "
            k = 0
            for partition_column in self.partition_columns:
                create_table_query_str += partition_column
                k += 1
                if k < len(self.partition_columns):
                    create_table_query_str += ", "

        create_table_query_str += " )"
        upsert_sql_str += f"{merge_update_set_str} WHEN NOT MATCHED THEN INSERT ({merge_insert_str}) VALUES ({merge_insert_values_str})"

        return {
            'struct_field_list': struct_field_list,
            'create_table_query_str': create_table_query_str,
            'upsert_sql_str': upsert_sql_str
        }

    def create_if_not_exists(self, sql_context: SQLContext) -> None:
        """
        create the delta table if it doesn't exist
        """
        sql_context.sql(self.create_table_query_str)

    def delete(self, dbutils: DBUtils) -> None:
        """
        delete the delta table
        """
        dbutils.fs.rm(f"/delta/{self.schema_name}/{self.table_name}", recurse=True)
        dbutils.fs.rm(self.checkpoint_base_path, recurse=True)

    def read_stream(self, spark: SparkSession, **kw):
        """
        read in the stream to a dataframe
        """

        format = kw.get('cloudFiles_format') or 'csv'
        header = kw.get('header') or 'true'
        multiline = kw.get('multiLine') or 'true'
        escape = kw.get('escape') or "\""

        df = spark.readStream.format('cloudFiles') \
            .schema(self.file_table_schema) \
            .option('cloudFiles.format', format) \
            .option('header', header) \
            .option('multiLine', multiline) \
            .option('escape', escape) \
            .option("cloudFiles.schemaLocation", self.checkpoint_path) \
            .load(self.upload_path)
        return df

    def write_stream(self, spark: SparkSession, df) -> None:
        """
        write stream from a dataframe to a delta table
        this will only run for updated data and stop once there is no new data
        """
        df.writeStream.format('delta') \
            .foreachBatch(lambda df, batchId: process_micro_batch(df, batchId, self.upsert_sql_str, self.unique_identifier_columns)) \
            .option('checkpointLocation', self.checkpoint_path) \
            .outputMode("update") \
            .trigger(availableNow=True) \
            .start()


    def stream(self, spark: SparkSession, **kw) -> None:
        """
        stream data from s3 to a delta table

        References:
            + https://hackersandslackers.com/structured-streaming-in-pyspark/
        """
        log_msg = LogMessage()
        log_msg.add('summary', f"uploading {self.schema_name}.{self.table_name} to a delta table using AutoLoader")
        log_msg.add('upload_path', self.upload_path)
        log_msg.add('checkpoint_path', self.checkpoint_path)
        log_msg.add('write_path', self.write_path)
        log_msg.add('create_table_query_str', self.create_table_query_str)
        log_msg.add('upsert_sql_str', self.upsert_sql_str)
        print(str(log_msg))
        logger.info(str(log_msg))
        log_msg.clear()

        df = self.read_stream(spark, **kw)

        print(df.printSchema())

        self.write_stream(spark, df)
