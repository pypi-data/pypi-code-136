from pathlib import Path
from typing import Any, Dict, Mapping, Optional

import pyarrow as pa

from .type import (
    BOOLEAN,
    DOUBLE,
    DOUBLE_ARRAY,
    FLOAT,
    FLOAT_ARRAY,
    INT,
    INT_ARRAY,
    LOCAL_DATE,
    LOCAL_DATE_TIME,
    LOCAL_TIME,
    LONG,
    LONG_ARRAY,
    STRING,
    ZONED_DATE_TIME,
    DataType,
)

_ARROW_TYPES: Mapping[Any, DataType] = {
    pa.bool_(): BOOLEAN,
    pa.date32(): LOCAL_DATE,
    pa.float32(): FLOAT,
    pa.float64(): DOUBLE,
    pa.int32(): INT,
    pa.int64(): LONG,
    pa.list_(pa.float32()): FLOAT_ARRAY,
    pa.list_(pa.float64()): DOUBLE_ARRAY,
    pa.list_(pa.int32()): INT_ARRAY,
    pa.list_(pa.int64()): LONG_ARRAY,
    pa.string(): STRING,
    pa.timestamp("ns"): LOCAL_DATE_TIME,
    pa.timestamp("s"): LOCAL_DATE_TIME,
    pa.time64("ns"): LOCAL_TIME,
    pa.null(): STRING,
}

DEFAULT_MAX_CHUNKSIZE = 1_000


def write_arrow_to_file(
    table: pa.Table,  # pyright: ignore[reportUnknownParameterType]
    /,
    *,
    max_chunksize: int = DEFAULT_MAX_CHUNKSIZE,
    filepath: Path,
) -> None:
    with pa.ipc.new_file(filepath, table.schema) as writer:
        for batch in table.to_batches(max_chunksize=max_chunksize):
            writer.write(batch)


def _get_data_type_from_arrow_type(arrow_type: Any, /, *, name: str) -> DataType:
    try:
        return _ARROW_TYPES[arrow_type]
    except KeyError as error:
        raise ValueError(f"'{name}' has unsupported type: '{arrow_type}'.") from error


def get_data_types_from_arrow(
    table: pa.Table,  # pyright: ignore[reportUnknownParameterType]
    /,
) -> Dict[str, DataType]:
    arrow_types = [
        arrow_type.value_type
        if isinstance(arrow_type, pa.DictionaryType)
        else arrow_type
        for arrow_type in table.schema.types
    ]
    return {
        table.column_names[i]: (
            ZONED_DATE_TIME
            if isinstance(arrow_type, pa.TimestampType) and arrow_type.tz is not None
            else _get_data_type_from_arrow_type(arrow_type, name=table.column_names[i])
        )
        for i, arrow_type in enumerate(arrow_types)
    }


def get_corresponding_arrow_type(data_type: DataType, /) -> Optional[Any]:
    # Converting `ZONED_DATE_TIME` to an Arrow type is too complicated.
    # It will fall back to the type inferred by Arrow.
    if data_type == ZONED_DATE_TIME:
        return None

    return next(
        arrow_type
        for arrow_type, arrow_data_type in _ARROW_TYPES.items()
        if arrow_data_type == data_type
    )
