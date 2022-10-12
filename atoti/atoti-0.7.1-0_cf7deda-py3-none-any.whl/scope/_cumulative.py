from typing import Optional, Union

from atoti_core import deprecated

from ..level import Level
from .cumulative_scope import CumulativeScope, _TimePeriodWindow


def _normalize_period_to_iso_8601(period: str, /) -> str:
    if "P" in period:
        return period
    normalized_period = f"-P{period[1:]}" if period[0] == "-" else f"P{period}"
    deprecated(
        f"Missing duration designator (P) in {period}, use {normalized_period} instead."
    )
    return normalized_period


def cumulative(
    level: Level,
    *,
    dense: bool = False,
    partitioning: Optional[Level] = None,
    window: Union[Optional[range], _TimePeriodWindow] = None,
) -> CumulativeScope:
    if isinstance(window, tuple):
        if window[0] is None:
            window = None, _normalize_period_to_iso_8601(window[1])
        elif window[1] is None:
            window = _normalize_period_to_iso_8601(window[0]), None
        elif window[0] is not None and window[1] is not None:
            window = _normalize_period_to_iso_8601(
                window[0]
            ), _normalize_period_to_iso_8601(window[1])

    deprecated(
        "Creating a scope with this function is deprecated. Initialize a CumulativeScope directly instead."
    )

    return CumulativeScope(
        level=level,
        dense=dense,
        window=window,
        partitioning=partitioning,
    )
