from __future__ import annotations

from typing import Optional, Union, overload

from .._measures.calculated_measure import AggregatedMeasure
from .._measures.column_measure import ColumnMeasure
from .._measures.level_measure import LevelMeasure
from .._measures.udaf_measure import UdafMeasure
from ..column import Column
from ..level import Level
from ..measure_description import MeasureDescription
from ..scope import OriginScope
from ..scope._scope import Scope
from ._utils import ColumnOrOperationOrLevel


@overload
def agg(
    operand: ColumnOrOperationOrLevel,
    /,
    *,
    plugin_key: str,
) -> MeasureDescription:
    ...


@overload
def agg(
    operand: MeasureDescription,
    /,
    *,
    plugin_key: str,
    scope: Scope,
) -> MeasureDescription:
    ...


def agg(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    plugin_key: str,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure aggregating the passed operand."""
    if isinstance(operand, MeasureDescription):
        if scope is None:
            raise TypeError("Cannot aggregate a measure description without a scope.")

        if isinstance(scope, OriginScope):
            return AggregatedMeasure(
                _underlying_measure=operand,
                _plugin_key=plugin_key,
                _on_levels=scope._levels_coordinates,
            )

        return scope._create_aggregated_measure(operand, plugin_key=plugin_key)

    if scope is not None:
        raise TypeError("Cannot aggregate columns with a scope.")

    if isinstance(operand, Column):
        return ColumnMeasure(
            _column_coordinates=operand._column_coordinates,
            _plugin_key=plugin_key,
        )
    if isinstance(operand, Level):
        return AggregatedMeasure(
            _underlying_measure=LevelMeasure(operand._coordinates),
            _plugin_key=plugin_key,
            _on_levels=[operand._coordinates],
        )
    return UdafMeasure(_plugin_key=plugin_key, _operation=operand)
