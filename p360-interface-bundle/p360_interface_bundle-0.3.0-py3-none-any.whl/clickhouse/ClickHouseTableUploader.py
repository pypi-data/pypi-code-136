from typing import Optional
from pyspark.sql import DataFrame
from p360_interface_bundle.clickhouse.ClickHouseContext import ClickHouseContext
from p360_interface_bundle.clickhouse.ClickHouseQueryExecutor import ClickHouseQueryExecutor
from p360_interface_bundle.clickhouse.types import SPARK_TO_CLICKHOUSE_TYPES


class ClickHouseTableUploader:
    __engine_map = {
        "summing_merge_tree": "ENGINE = SummingMergeTree() ORDER BY {order_column} SETTINGS index_granularity = 8192",
        "aggregating_merge_tree": "ENGINE = AggregatingMergeTree() ORDER BY {order_column} SETTINGS index_granularity = 8192",
        "log": "ENGINE = Log",
    }

    def __init__(
        self,
        clickhouse_context: ClickHouseContext,
        clickhouse_query_executor: ClickHouseQueryExecutor,
    ):
        self.__clickhouse_context = clickhouse_context
        self.__clickhouse_query_executor = clickhouse_query_executor

    def upload_overwrite(self, df: DataFrame, table_name: str, engine_type: str, order_column: Optional[str] = None):
        self.__check_engine_type(engine_type, order_column)

        (
            df.write.format("jdbc")
            .option("createTableOptions", self.__engine_map[engine_type].format(order_column=order_column))
            .option("driver", "com.clickhouse.jdbc.ClickHouseDriver")
            .option("url", f"jdbc:clickhouse://{self.__clickhouse_context.get_host()}:{self.__clickhouse_context.get_port()}")
            .option("dbtable", table_name)
            .option("user", self.__clickhouse_context.get_user())
            .option("password", self.__clickhouse_context.get_password())
            .mode("overwrite")
            .save()
        )

    def upload_append(self, df: DataFrame, table_name: str, engine_type: str, order_column: Optional[str] = None):
        self.__check_engine_type(engine_type, order_column)

        create_table_query = self.__construct_create_table_query(df, table_name, engine_type, order_column if order_column else "")

        self.__clickhouse_query_executor.execute(create_table_query)

        (
            df.write.format("jdbc")
            .option("driver", "com.clickhouse.jdbc.ClickHouseDriver")
            .option("url", f"jdbc:clickhouse://{self.__clickhouse_context.get_host()}:{self.__clickhouse_context.get_port()}")
            .option("dbtable", table_name)
            .option("user", self.__clickhouse_context.get_user())
            .option("password", self.__clickhouse_context.get_password())
            .mode("append")
            .save()
        )

    def __construct_create_table_query(self, df: DataFrame, table_name: str, engine_type: str, order_column: str) -> str:
        create_table_query = f"CREATE TABLE {table_name} ("
        clickhouse_columns = []

        for field in df.schema:
            col_name = field.name
            col_type = SPARK_TO_CLICKHOUSE_TYPES[field.dataType.simpleString()]

            if field.nullable and field.name != order_column:
                clickhouse_columns.append(f"`{col_name}` Nullable({col_type})")
            else:
                clickhouse_columns.append(f"`{col_name}` {col_type}")

        create_table_query += ", ".join(clickhouse_columns)
        create_table_query += ") "
        create_table_query += self.__engine_map[engine_type].format(order_column=order_column)

        return create_table_query

    def __check_engine_type(self, engine_type: str, order_column: Optional[str]):
        if engine_type not in self.__engine_map:
            raise Exception(f"Invalid engine type '{engine_type}', allowed types are {self.__engine_map.keys()}")

        if engine_type in ["summing_merge_tree", "aggregating_merge_tree"] and order_column is None:
            raise Exception(f"You must specify order column for engine type of '{engine_type}'")
