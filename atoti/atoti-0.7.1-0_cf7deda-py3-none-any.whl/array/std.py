from __future__ import annotations

from atoti_core import doc

from .._docs_utils import STD_AND_VAR_DOC, STD_DOC_KWARGS
from .._runtime_type_checking_utils import VarianceMode
from ..math import sqrt
from ..measure_description import MeasureDescription
from ._utils import QUANTILE_STD_AND_VAR_DOC_KWARGS, check_array_type
from .var import var


@doc(
    STD_AND_VAR_DOC,
    **{**STD_DOC_KWARGS, **QUANTILE_STD_AND_VAR_DOC_KWARGS},
)
def std(
    measure: MeasureDescription, /, *, mode: VarianceMode = "sample"
) -> MeasureDescription:
    check_array_type(measure)
    return sqrt(var(measure, mode=mode))
