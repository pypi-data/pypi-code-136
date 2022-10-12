from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import BASIC_ARGS_DOC, BASIC_DOC, ColumnOrOperationOrLevel


@overload
def mean(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def mean(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="mean",
    example="""
        >>> m["Quantity.MEAN"] = tt.agg.mean(table["Quantity"])
        >>> cube.query(m["Quantity.MEAN"])
          Quantity.MEAN
        0        370.00""".replace(
        "\n", "", 1
    ),
)
def mean(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="MEAN", scope=scope)  # type: ignore
