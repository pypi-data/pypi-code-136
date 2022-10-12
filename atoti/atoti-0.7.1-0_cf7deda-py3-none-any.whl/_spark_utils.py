from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Dict, Mapping

if TYPE_CHECKING:
    # Spark is only imported for type checking as we don't want it as a dependency
    from pyspark.sql import (  # pylint: disable=undeclared-dependency, nested-import
        DataFrame,
        SparkSession,
    )

_SPARK_PROPERTIES = {"spark.sql.parquet.outputTimestampType": "TIMESTAMP_MICROS"}


def write_spark_to_parquet(
    dataframe: DataFrame,
    *,
    directory: Path,
) -> None:
    session = dataframe.sql_ctx.sparkSession
    # Modify output format of timestamp columns
    # https://github.com/apache/spark/blob/7281784883d6bacf3d024397fd90edf65c06e02b/sql/catalyst/src/main/scala/org/apache/spark/sql/internal/SQLConf.scala#L399
    previous_props = _set_properties(_SPARK_PROPERTIES, session=session)
    try:
        dataframe.write.parquet(_to_hadoop_file_path(directory))
    finally:
        _set_properties(previous_props, session=session)


def _to_hadoop_file_path(path: Path) -> str:
    return path.as_uri()


def _set_properties(
    properties: Mapping[str, str],
    /,
    *,
    session: SparkSession,
) -> Dict[str, str]:
    """Set the given properties to the session and return the previous ones."""
    previous = {}
    for name, value in properties.items():
        previous[name] = session.conf.get(name, default=None)
        if value is None:
            session.conf.unset(name)
        else:
            session.conf.set(name, value)
    return previous
