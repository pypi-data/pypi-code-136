from typing import Iterable

import pandas as pd
import pyarrow as pa

from ._parse_level_coordinates import parse_level_coordinates


def arrow_to_pandas(
    table: pa.Table,  # pyright: ignore[reportUnknownParameterType]
) -> pd.DataFrame:
    # Fast for small tables (less than 100k lines) but can take several seconds for larger datasets.
    dataframe: pd.DataFrame = table.to_pandas()
    column_names: Iterable[str] = table.column_names
    level_coordinates = {
        column_name: parse_level_coordinates(column_name)
        for column_name in column_names
    }
    return dataframe.rename(
        columns={
            column_name: level_coordinates.level_name
            for column_name, level_coordinates in level_coordinates.items()
            if level_coordinates is not None
        }
    )
