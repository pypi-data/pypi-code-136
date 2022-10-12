from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from .._docs_utils import STD_AND_VAR_DOC, VAR_DOC_KWARGS
from .._runtime_type_checking_utils import VarianceMode
from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._count import count
from ._utils import QUANTILE_STD_AND_VAR_DOC_KWARGS, SCOPE_DOC, ColumnOrOperationOrLevel
from .mean import mean
from .square_sum import square_sum


@overload
def var(
    operand: ColumnOrOperationOrLevel, /, *, mode: VarianceMode = "sample"
) -> MeasureDescription:
    ...


@overload
def var(
    operand: MeasureDescription,
    /,
    *,
    mode: VarianceMode = "sample",
    scope: Scope,
) -> MeasureDescription:
    ...


@doc(
    STD_AND_VAR_DOC,
    SCOPE_DOC,
    **{**VAR_DOC_KWARGS, **QUANTILE_STD_AND_VAR_DOC_KWARGS},
)
def var(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    *,
    mode: VarianceMode = "sample",
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    # The type checkers cannot see that the `@overload` above ensure that these calls are valid.
    size = count(operand, scope=scope)  # type: ignore
    mean_value = mean(operand, scope=scope)  # type: ignore
    population_var = square_sum(operand, scope=scope) / size - mean_value * mean_value  # type: ignore
    if mode == "population":
        return population_var
    # Apply Bessel's correction
    return population_var * size / (size - 1)
