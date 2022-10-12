from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import BASIC_ARGS_DOC, BASIC_DOC, ColumnOrOperationOrLevel


@overload
def prod(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def prod(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="product",
    example="""
        >>> m["Other.PROD"] = tt.agg.prod(table["Other"])
        >>> cube.query(m["Other.PROD"])
          Other.PROD
        0          4""".replace(
        "\n", "", 1
    ),
)
def prod(  # pylint: disable=redefined-builtin
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="MULTIPLY", scope=scope)  # type: ignore
