from __future__ import annotations

from typing import Optional, Union, overload

from ...agg._agg import agg
from ...agg._utils import ColumnOrOperationOrLevel
from ...measure_description import MeasureDescription
from ...scope._scope import Scope


@overload
def distinct(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription], /
) -> MeasureDescription:
    ...


@overload
def distinct(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Scope,
) -> MeasureDescription:
    ...


def distinct(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return an array measure representing the distinct values of the passed measure."""
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="DISTINCT", scope=scope)  # type: ignore
