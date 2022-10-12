from __future__ import annotations

from typing import Optional, Union, overload

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import ColumnOrOperationOrLevel


@overload
def vector(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def vector(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


def vector(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return an array measure representing the values of the passed operand across the specified scope."""
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="VECTOR", scope=scope)  # type: ignore
