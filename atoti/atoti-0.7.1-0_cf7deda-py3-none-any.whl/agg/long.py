from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import BASIC_ARGS_DOC, BASIC_DOC, ColumnOrOperationOrLevel


@overload
def long(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def long(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="sum of the positive values",
    example="""
        >>> m["Quantity.LONG"] = tt.agg.long(table["Quantity"])
        >>> cube.query(m["Quantity.LONG"])
          Quantity.LONG
        0         1,110""".replace(
        "\n", "", 1
    ),
)
def long(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="LONG", scope=scope)  # type: ignore
