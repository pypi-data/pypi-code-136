from __future__ import annotations

from typing import Optional, Union, overload

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import ColumnOrOperationOrLevel


@overload
def count(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def count(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


def count(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure equal to the number of aggregated elements.

    See also:
        :func:`atoti.agg.count_distinct`.
    """
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="COUNT", scope=scope)  # type: ignore
