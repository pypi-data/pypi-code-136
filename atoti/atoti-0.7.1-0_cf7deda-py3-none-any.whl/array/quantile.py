from __future__ import annotations

from typing import Union

from atoti_core import doc

from .._docs_utils import QUANTILE_DOC
from .._measures.generic_measure import GenericMeasure
from .._runtime_type_checking_utils import PercentileInterpolation, PercentileMode
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import QUANTILE_STD_AND_VAR_DOC_KWARGS, check_array_type


@doc(QUANTILE_DOC, **QUANTILE_STD_AND_VAR_DOC_KWARGS)
def quantile(
    measure: MeasureDescription,
    /,
    q: Union[float, MeasureDescription],
    *,
    mode: PercentileMode = "inc",
    interpolation: PercentileInterpolation = "linear",
) -> MeasureDescription:
    if isinstance(q, float):
        if q < 0 or q > 1:
            raise ValueError("Quantile must be between 0 and 1.")
    check_array_type(measure)
    return GenericMeasure(
        "CALCULATED_QUANTILE",
        mode,
        interpolation,
        [measure, _convert_to_measure_description(q)],
    )
