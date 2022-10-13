from __future__ import annotations

import datetime
from typing import Optional
from typing import Tuple
from typing import Union

from typeguard import typechecked

from tecton_core import id_helper
from tecton_core.specs import utils
from tecton_proto import args
from tecton_proto import data
from tecton_proto.common import spark_schema_pb2

__all__ = [
    "DataSourceSpec",
    "BatchSourceSpec",
    "HiveSourceSpec",
    "FileSourceSpec",
    "SparkBatchSourceSpec",
    "RedshiftSourceSpec",
    "SnowflakeSourceSpec",
    "DatetimePartitionColumnSpec",
    "StreamSourceSpec",
    "KinesisSourceSpec",
    "KafkaSourceSpec",
    "SparkStreamSourceSpec",
]


@utils.frozen_strict
class DataSourceSpec:
    name: str
    id: str
    batch_source: BatchSourceSpec
    stream_source: Optional[StreamSourceSpec]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.virtual_data_source_pb2.VirtualDataSource) -> DataSourceSpec:
        if proto.HasField("batch_data_source"):
            batch_source = create_batch_source_from_data_proto(proto.batch_data_source)
        else:
            batch_source = None

        if proto.HasField("stream_data_source"):
            stream_source = create_stream_source_from_data_proto(proto.stream_data_source)
        else:
            stream_source = None

        return cls(
            name=proto.fco_metadata.name,
            id=id_helper.IdHelper.to_string(proto.virtual_data_source_id),
            batch_source=batch_source,
            stream_source=stream_source,
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.virtual_data_source_pb2.VirtualDataSourceArgs) -> DataSourceSpec:
        raise NotImplementedError


@typechecked
def create_batch_source_from_data_proto(
    proto: data.batch_data_source_pb2.BatchDataSource,
) -> Union[HiveSourceSpec, SparkBatchSourceSpec, FileSourceSpec, RedshiftSourceSpec, SnowflakeSourceSpec]:
    if proto.HasField("hive_table"):
        return HiveSourceSpec.from_data_proto(proto)
    if proto.HasField("spark_data_source_function"):
        return SparkBatchSourceSpec.from_data_proto(proto)
    if proto.HasField("redshift_db"):
        return RedshiftSourceSpec.from_data_proto(proto)
    if proto.HasField("snowflake"):
        return SnowflakeSourceSpec.from_data_proto(proto)
    if proto.HasField("file"):
        return FileSourceSpec.from_data_proto(proto)
    else:
        raise Exception(f"Unknown Data Source Type: {proto}")


@utils.frozen_strict
class BatchSourceSpec:
    """Base class for batch source specs, e.g. a HiveSourceSpec or SnowflakeSourceSpec."""

    timestamp_field: Optional[str]
    timestamp_format: Optional[str]
    post_processor: Optional[args.user_defined_function_pb2.UserDefinedFunction]
    spark_schema: spark_schema_pb2.SparkSchema


@utils.frozen_strict
class HiveSourceSpec(BatchSourceSpec):
    database: str
    table: str
    datetime_partition_columns: Tuple[DatetimePartitionColumnSpec, ...]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.BatchDataSource) -> HiveSourceSpec:
        # Needed for canary backwards compatability. Can be deleted on the following release.
        if proto.date_partition_column and not proto.datetime_partition_columns:
            proto.datetime_partition_columns.append(
                data.batch_data_source_pb2.DatetimePartitionColumn(
                    column_name=proto.date_partition_column,
                    format_string="%Y-%m-%d",
                    minimum_seconds=24 * 60 * 60,
                )
            )

        return cls(
            timestamp_field=utils.get_field_or_none(proto.timestamp_column_properties, "column_name"),
            timestamp_format=utils.get_field_or_none(proto.timestamp_column_properties, "format"),
            post_processor=utils.get_field_or_none(proto, "raw_batch_translator"),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            table=utils.get_field_or_none(proto.hive_table, "table"),
            database=utils.get_field_or_none(proto.hive_table, "database"),
            datetime_partition_columns=tuple(
                DatetimePartitionColumnSpec.from_data_proto(column) for column in proto.datetime_partition_columns
            ),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.HiveDataSourceArgs) -> HiveSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class FileSourceSpec(BatchSourceSpec):
    uri: Optional[str]
    file_format: Optional[str]
    convert_to_glue_format: bool
    schema_uri: Optional[str]
    schema_override: Optional[spark_schema_pb2.SparkSchema]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.BatchDataSource) -> FileSourceSpec:
        return cls(
            timestamp_field=utils.get_field_or_none(proto.timestamp_column_properties, "column_name"),
            timestamp_format=utils.get_field_or_none(proto.timestamp_column_properties, "format"),
            post_processor=utils.get_field_or_none(proto, "raw_batch_translator"),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            uri=utils.get_field_or_none(proto.file, "uri"),
            file_format=utils.get_field_or_none(proto.file, "format"),
            convert_to_glue_format=proto.file.convert_to_glue_format,
            schema_uri=utils.get_field_or_none(proto.file, "schema_uri"),
            schema_override=utils.get_field_or_none(proto.file, "schema_override"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.FileDataSourceArgs) -> FileSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class SparkBatchSourceSpec(BatchSourceSpec):
    function: args.user_defined_function_pb2.UserDefinedFunction
    supports_time_filtering: bool

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.BatchDataSource) -> SparkBatchSourceSpec:
        return cls(
            timestamp_field=None,
            timestamp_format=None,
            post_processor=None,
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            supports_time_filtering=proto.spark_data_source_function.supports_time_filtering,
            function=utils.get_field_or_none(proto.spark_data_source_function, "function"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.SparkBatchConfigArgs) -> SparkBatchSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class RedshiftSourceSpec(BatchSourceSpec):
    endpoint: str
    cluster_id: Optional[str]
    table: Optional[str]
    query: Optional[str]
    temp_s3: Optional[str]

    def __attrs_post_init__(self):
        assert self.table or self.query, "Invalid RedshiftSourceSpec: no table or query provided."

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.BatchDataSource) -> RedshiftSourceSpec:
        return cls(
            timestamp_field=utils.get_field_or_none(proto.timestamp_column_properties, "column_name"),
            timestamp_format=utils.get_field_or_none(proto.timestamp_column_properties, "format"),
            post_processor=utils.get_field_or_none(proto, "raw_batch_translator"),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            endpoint=utils.get_field_or_none(proto.redshift_db, "endpoint"),
            cluster_id=utils.get_field_or_none(proto.redshift_db, "cluster_id"),
            table=utils.get_field_or_none(proto.redshift_db, "table"),
            query=utils.get_field_or_none(proto.redshift_db, "query"),
            temp_s3=utils.get_field_or_none(proto.redshift_db, "temp_s3"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.RedshiftDataSourceArgs) -> RedshiftSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class SnowflakeSourceSpec(BatchSourceSpec):
    database: str
    schema: str
    warehouse: Optional[str]
    url: Optional[str]
    role: Optional[str]
    table: Optional[str]
    query: Optional[str]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.BatchDataSource) -> SnowflakeSourceSpec:
        return cls(
            timestamp_field=utils.get_field_or_none(proto.timestamp_column_properties, "column_name"),
            timestamp_format=utils.get_field_or_none(proto.timestamp_column_properties, "format"),
            post_processor=utils.get_field_or_none(proto, "raw_batch_translator"),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            url=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "url"),
            database=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "database"),
            schema=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "schema"),
            warehouse=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "warehouse"),
            role=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "role"),
            table=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "table"),
            query=utils.get_field_or_none(proto.snowflake.snowflakeArgs, "query"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.SnowflakeDataSourceArgs) -> SnowflakeSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class DatetimePartitionColumnSpec:
    column_name: str
    format_string: str
    minimum_seconds: int

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.batch_data_source_pb2.DatetimePartitionColumn) -> DatetimePartitionColumnSpec:
        return cls(
            column_name=utils.get_field_or_none(proto, "column_name"),
            format_string=utils.get_field_or_none(proto, "format_string"),
            minimum_seconds=utils.get_field_or_none(proto, "minimum_seconds"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.DatetimePartitionColumnArgs) -> DatetimePartitionColumnSpec:
        raise NotImplementedError


@typechecked
def create_stream_source_from_data_proto(
    proto: data.stream_data_source_pb2.StreamDataSource,
) -> Union[KinesisSourceSpec, KafkaSourceSpec, SparkStreamSourceSpec]:
    if proto.HasField("kinesis_data_source"):
        return KinesisSourceSpec.from_data_proto(proto)
    if proto.HasField("kafka_data_source"):
        return KafkaSourceSpec.from_data_proto(proto)
    if proto.HasField("spark_data_source_function"):
        return SparkStreamSourceSpec.from_data_proto(proto)
    else:
        raise Exception(f"Unknown Data Source Type: {proto}")


@utils.frozen_strict
class StreamSourceSpec:
    """Base class for stream source specs, e.g. a KinesisSourceSpec or KafkaSourceSpec."""

    deduplication_column_names: Tuple[str, ...]
    post_processor: Optional[args.user_defined_function_pb2.UserDefinedFunction]
    options: Tuple[data.stream_data_source_pb2.StreamDataSource.Option, ...]
    watermark_delay_threshold: datetime.timedelta
    spark_schema: spark_schema_pb2.SparkSchema


@utils.frozen_strict
class KinesisSourceSpec(StreamSourceSpec):
    stream_name: str
    region: str
    initial_stream_position: args.data_source_config_pb2.InitialStreamPosition

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.stream_data_source_pb2.StreamDataSource) -> KinesisSourceSpec:
        return cls(
            deduplication_column_names=utils.get_tuple_from_repeated_field(proto.deduplication_column_names),
            post_processor=utils.get_field_or_none(proto, "raw_stream_translator"),
            options=utils.get_tuple_from_repeated_field(proto.options),
            watermark_delay_threshold=proto.stream_config.watermark_delay_threshold.ToTimedelta(),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            stream_name=utils.get_field_or_none(proto.kinesis_data_source, "stream_name"),
            region=utils.get_field_or_none(proto.kinesis_data_source, "region"),
            initial_stream_position=proto.stream_config.initial_stream_position,
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.KinesisDataSourceArgs) -> KinesisSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class KafkaSourceSpec(StreamSourceSpec):
    bootstrap_servers: str
    topics: str
    ssl_keystore_location: Optional[str]
    ssl_keystore_password_secret_id: Optional[str]
    ssl_truststore_location: Optional[str]
    ssl_truststore_password_secret_id: Optional[str]
    security_protocol: Optional[str]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.stream_data_source_pb2.StreamDataSource) -> KafkaSourceSpec:
        return cls(
            deduplication_column_names=utils.get_tuple_from_repeated_field(proto.deduplication_column_names),
            post_processor=utils.get_field_or_none(proto, "raw_stream_translator"),
            options=utils.get_tuple_from_repeated_field(proto.options),
            watermark_delay_threshold=proto.stream_config.watermark_delay_threshold.ToTimedelta(),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            bootstrap_servers=utils.get_field_or_none(proto.kafka_data_source, "bootstrap_servers"),
            topics=utils.get_field_or_none(proto.kafka_data_source, "topics"),
            ssl_keystore_location=utils.get_field_or_none(proto.kafka_data_source, "ssl_keystore_location"),
            ssl_keystore_password_secret_id=utils.get_field_or_none(
                proto.kafka_data_source, "ssl_keystore_password_secret_id"
            ),
            ssl_truststore_location=utils.get_field_or_none(proto.kafka_data_source, "ssl_truststore_location"),
            ssl_truststore_password_secret_id=utils.get_field_or_none(
                proto.kafka_data_source, "ssl_truststore_password_secret_id"
            ),
            security_protocol=utils.get_field_or_none(proto.kafka_data_source, "security_protocol"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.KafkaDataSourceArgs) -> KafkaSourceSpec:
        raise NotImplementedError


@utils.frozen_strict
class SparkStreamSourceSpec(StreamSourceSpec):
    function: args.user_defined_function_pb2.UserDefinedFunction

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.stream_data_source_pb2.StreamDataSource) -> SparkStreamSourceSpec:
        return cls(
            deduplication_column_names=utils.get_tuple_from_repeated_field(proto.deduplication_column_names),
            post_processor=utils.get_field_or_none(proto, "raw_stream_translator"),
            options=utils.get_tuple_from_repeated_field(proto.options),
            watermark_delay_threshold=proto.stream_config.watermark_delay_threshold.ToTimedelta(),
            spark_schema=utils.get_field_or_none(proto, "spark_schema"),
            function=utils.get_field_or_none(proto.spark_data_source_function, "function"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.data_source_pb2.SparkStreamConfigArgs) -> SparkStreamSourceSpec:
        raise NotImplementedError
