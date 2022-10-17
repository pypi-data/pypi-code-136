from typing import Dict, Any
from decimal import Decimal
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
from pyspark.sql import functions as f
from featurestorebundle.feature.FeatureStore import FeatureStore
from featurestorebundle.entity.EntityGetter import EntityGetter


class StatisticsComputer:
    def __init__(self, spark: SparkSession, dbutils: DBUtils, feature_store: FeatureStore, entity_getter: EntityGetter):
        self.__spark = spark
        self.__dbutils = dbutils
        self.__feature_store = feature_store
        self.__entity_getter = entity_getter

    # pylint: disable=too-many-locals
    def compute(self) -> Dict[str, Dict[str, Any]]:
        self.__spark.sparkContext.setCheckpointDir("dbfs:/tmp/checkpoints")

        entity = self.__entity_getter.get()
        features = self.__feature_store.get_latest(entity_name=entity.name, exclude_tags=["private"], skip_incomplete_rows=True)
        features = features.checkpoint()
        metadata = self.__feature_store.get_metadata(entity.name, exclude_tags=["private"])
        metadata_rows = metadata.collect()

        categorical_cols = [row.feature for row in metadata_rows if row.variable_type == "categorical"]
        numerical_cols = [row.feature for row in metadata_rows if row.variable_type == "numerical"]
        binary_cols = [row.feature for row in metadata_rows if row.variable_type == "binary"]

        numerical_features_statistics = features.select(
            *[f.max(col).alias(f"{col}_max") for col in numerical_cols],
            *[f.min(col).alias(f"{col}_min") for col in numerical_cols],
            *[f.avg(col).alias(f"{col}_avg") for col in numerical_cols],
            *[f.count(f.when(f.col(col).isNull(), col)).alias(f"{col}_cnt_nulls") for col in numerical_cols],
            *[f.count(f.when(f.col(col).isNotNull(), col)).alias(f"{col}_cnt_not_nulls") for col in numerical_cols],
        )

        binary_features_statistics = features.select(
            *[f.max(f.col(col).cast("byte")).alias(f"{col}_max") for col in binary_cols],
            *[f.min(f.col(col).cast("byte")).alias(f"{col}_min") for col in binary_cols],
            *[f.avg(f.col(col).cast("byte")).alias(f"{col}_avg") for col in binary_cols],
            *[f.count(f.when(f.col(col).isNull(), col)).alias(f"{col}_cnt_nulls") for col in binary_cols],
            *[f.count(f.when(f.col(col).isNotNull(), col)).alias(f"{col}_cnt_not_nulls") for col in binary_cols],
        )

        categorical_features_statistics = features.select(
            *[f.countDistinct(col).alias(f"{col}_distinct_count") for col in categorical_cols],
            *[f.collect_set(col).alias(f"{col}_distinct_values") for col in categorical_cols],
            *[f.count(f.when(f.col(col).isNull(), col)).alias(f"{col}_cnt_nulls") for col in categorical_cols],
            *[f.count(f.when(f.col(col).isNotNull(), col)).alias(f"{col}_cnt_not_nulls") for col in categorical_cols],
        )

        numerical_statistics_rows = numerical_features_statistics.collect()
        binary_statistics_rows = binary_features_statistics.collect()
        categorical_statistics_rows = categorical_features_statistics.collect()

        numerical_statistics_dict = numerical_statistics_rows[0].asDict() if numerical_statistics_rows else {}
        binary_statistics_dict = binary_statistics_rows[0].asDict() if binary_statistics_rows else {}
        categorical_statistics_dict = categorical_statistics_rows[0].asDict() if categorical_statistics_rows else {}

        self.__convert_decimals(numerical_statistics_dict)
        self.__convert_decimals(binary_statistics_dict)
        self.__convert_decimals(categorical_statistics_dict)

        statistics = {}

        for col in numerical_cols:
            statistics[col] = {
                "min_value": numerical_statistics_dict[f"{col}_min"],
                "max_value": numerical_statistics_dict[f"{col}_max"],
                "avg_value": numerical_statistics_dict[f"{col}_avg"],
                "null_count": numerical_statistics_dict[f"{col}_cnt_nulls"],
                "not_null_count": numerical_statistics_dict[f"{col}_cnt_not_nulls"],
            }

        for col in binary_cols:
            statistics[col] = {
                "min_value": binary_statistics_dict[f"{col}_min"],
                "max_value": binary_statistics_dict[f"{col}_max"],
                "avg_value": binary_statistics_dict[f"{col}_avg"],
                "null_count": binary_statistics_dict[f"{col}_cnt_nulls"],
                "not_null_count": binary_statistics_dict[f"{col}_cnt_not_nulls"],
            }

        for col in categorical_cols:
            statistics[col] = {
                "distinct_values_count": categorical_statistics_dict[f"{col}_distinct_count"],
                "distinct_values": categorical_statistics_dict[f"{col}_distinct_values"],
                "null_count": categorical_statistics_dict[f"{col}_cnt_nulls"],
                "not_null_count": categorical_statistics_dict[f"{col}_cnt_not_nulls"],
            }

        self.__dbutils.fs.rm(self.__spark.sparkContext.getCheckpointDir(), recurse=True)

        return statistics

    def __convert_decimals(self, statistics: Dict[str, Any]):
        for key, val in statistics.items():
            if isinstance(val, Decimal):
                statistics[key] = float(val)
