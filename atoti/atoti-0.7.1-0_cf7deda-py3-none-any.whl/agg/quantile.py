from __future__ import annotations

from typing import Optional, Union, overload

from atoti_core import doc

from .._docs_utils import QUANTILE_DOC
from .._runtime_type_checking_utils import PercentileInterpolation, PercentileMode
from ..array import quantile as array_quantile
from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._utils import QUANTILE_STD_AND_VAR_DOC_KWARGS, SCOPE_DOC, ColumnOrOperationOrLevel
from ._vector import vector


@overload
def quantile(
    operand: ColumnOrOperationOrLevel,
    /,
    q: Union[float, MeasureDescription],
    *,
    mode: PercentileMode = "inc",
    interpolation: PercentileInterpolation = "linear",
) -> MeasureDescription:
    ...


@overload
def quantile(
    operand: MeasureDescription,
    /,
    q: Union[float, MeasureDescription],
    *,
    mode: PercentileMode = "inc",
    interpolation: PercentileInterpolation = "linear",
    scope: Scope,
) -> MeasureDescription:
    ...


@doc(QUANTILE_DOC, SCOPE_DOC, **QUANTILE_STD_AND_VAR_DOC_KWARGS)
def quantile(
    operand: Union[ColumnOrOperationOrLevel, MeasureDescription],
    /,
    q: Union[float, MeasureDescription],
    *,
    mode: PercentileMode = "inc",
    interpolation: PercentileInterpolation = "linear",
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return array_quantile(
        # The type checkers cannot see that the `@overload` above ensure that this call is valid.
        vector(operand, scope=scope),  # type: ignore
        q=q,
        mode=mode,
        interpolation=interpolation,
    )
