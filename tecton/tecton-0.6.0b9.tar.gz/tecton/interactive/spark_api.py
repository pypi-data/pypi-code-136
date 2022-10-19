from datetime import datetime

from tecton import conf
from tecton._internals import errors
from tecton.interactive.data_frame import TectonDataFrame
from tecton.tecton_context import TectonContext
from tecton_core import specs
from tecton_core.query import builder
from tecton_core.query import nodes
from tecton_spark import data_source_helper


def get_dataframe_for_data_source(
    data_source: specs.DataSourceSpec,
    start_time: datetime,
    end_time: datetime,
    apply_translator: bool,
) -> TectonDataFrame:
    if conf.get_bool("QUERYTREE_ENABLED"):
        return get_dataframe_for_data_source_query_tree(data_source, start_time, end_time, apply_translator)
    else:
        return get_dataframe_for_data_source_legacy(data_source, start_time, end_time, apply_translator)


def get_dataframe_for_data_source_legacy(
    data_source: specs.DataSourceSpec,
    start_time: datetime,
    end_time: datetime,
    apply_translator: bool,
) -> TectonDataFrame:
    spark = TectonContext.get_instance()._spark
    if isinstance(data_source.batch_source, specs.SparkBatchSourceSpec):
        if not data_source.batch_source.supports_time_filtering and (start_time or end_time):
            raise errors.DS_INCORRECT_SUPPORTS_TIME_FILTERING

        df = data_source_helper.get_ds_dataframe(
            spark,
            data_source=data_source,
            consume_streaming_data_source=False,
            start_time=start_time,
            end_time=end_time,
        )
        return TectonDataFrame._create(df)
    elif apply_translator:
        timestamp_key = data_source.batch_source.timestamp_field
        if not timestamp_key and (start_time or end_time):
            raise errors.DS_DATAFRAME_NO_TIMESTAMP

        df = data_source_helper.get_ds_dataframe(
            spark,
            data_source=data_source,
            consume_streaming_data_source=False,
            start_time=start_time,
            end_time=end_time,
        )
        return TectonDataFrame._create(df)
    else:
        if start_time is not None or end_time is not None:
            raise errors.DS_RAW_DATAFRAME_NO_TIMESTAMP_FILTER

        df = data_source_helper.get_non_dsf_raw_dataframe(spark, data_source.batch_source)
        return TectonDataFrame._create(df)


def get_dataframe_for_data_source_query_tree(
    data_source: specs.DataSourceSpec,
    start_time: datetime,
    end_time: datetime,
    apply_translator: bool,
) -> TectonDataFrame:
    spark = TectonContext.get_instance()._spark
    if isinstance(data_source.batch_source, specs.SparkBatchSourceSpec):
        if not data_source.batch_source.supports_time_filtering and (start_time or end_time):
            raise errors.DS_INCORRECT_SUPPORTS_TIME_FILTERING

        node = builder.build_datasource_scan_node(
            data_source, for_stream=False, start_time=start_time, end_time=end_time
        )
        return TectonDataFrame._create(node)

    elif apply_translator:
        timestamp_key = data_source.batch_source.timestamp_field
        if not timestamp_key and (start_time or end_time):
            raise errors.DS_DATAFRAME_NO_TIMESTAMP

        node = builder.build_datasource_scan_node(
            data_source, for_stream=False, start_time=start_time, end_time=end_time
        )
        return TectonDataFrame._create(node)
    else:
        if start_time is not None or end_time is not None:
            raise errors.DS_RAW_DATAFRAME_NO_TIMESTAMP_FILTER

        node = nodes.RawDataSourceScanNode(data_source).as_ref()
        return TectonDataFrame._create(node)
