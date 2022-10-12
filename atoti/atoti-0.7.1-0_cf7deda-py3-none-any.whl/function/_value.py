from typing import Iterable, Optional

from atoti_core import deprecated

from .._warn_about_required_levels import warn_about_required_levels
from ..agg import single_value
from ..column import Column
from ..level import Level
from ..measure_description import MeasureDescription


def value(
    column: Column, *, levels: Optional[Iterable[Level]] = None
) -> MeasureDescription:

    if levels != None:
        raise ValueError(
            "Levels are no longer supported. Use `where()` to restrict the visibility of the measure."
        )

    warn_about_required_levels(
        origin_scope_levels=f"the levels built on the `{column._table_name}` table's key columns: {column._table_keys}"
    )

    deprecated("`value()` has been deprecated. Use `agg.single_value()` instead.")
    return single_value(column)
