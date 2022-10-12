from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import BASIC_ARGS_DOC, BASIC_DOC, ColumnOrOperationOrLevel


@overload
def count_distinct(operand: ColumnOrOperationOrLevel, /) -> MeasureDescription:
    ...


@overload
def count_distinct(
    operand: MeasureDescription, /, *, scope: Scope
) -> MeasureDescription:
    ...


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="distinct count",
    example="""
        >>> m["Price.DISTINCT_COUNT"] = tt.agg.count_distinct(table["Price"])
        >>> cube.query(m["Price.DISTINCT_COUNT"])
          Price.DISTINCT_COUNT
        0                    3""".replace(
        "\n", "", 1
    ),
)
def count_distinct(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return agg(operand, plugin_key="DISTINCT_COUNT", scope=scope)  # type: ignore
