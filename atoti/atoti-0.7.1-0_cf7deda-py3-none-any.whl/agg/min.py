from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import BASIC_ARGS_DOC, BASIC_DOC, ColumnOrOperationOrLevel


@overload
def min(  # pylint: disable=redefined-builtin
    operand: ColumnOrOperationOrLevel, /
) -> MeasureDescription:
    ...


@overload
def min(  # pylint: disable=redefined-builtin
    operand: MeasureDescription, /, *, scope: Scope
) -> MeasureDescription:
    ...


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="minimum",
    example="""
        >>> m["Minimum Price"] = tt.agg.min(table["Price"])
        >>> cube.query(m["Minimum Price"])
          Minimum Price
        0         12.50""".replace(
        "\n", "", 1
    ),
)
def min(  # pylint: disable=redefined-builtin
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="MIN", scope=scope)  # type: ignore
