from __future__ import annotations
from typing import Optional
from ..context import Context

def parse_prognosis_type(ctx: Context, p: Optional[str]=None) -> Optional[str]:
    (pattern_matching_result,) = (None,)
    if p is not None:
        if p == "PROGNOSED":
            pattern_matching_result = 0

        elif p == "CALCULATED":
            pattern_matching_result = 1

        else: 
            pattern_matching_result = 2


    else: 
        pattern_matching_result = 2

    if pattern_matching_result == 0:
        return "prognosed"

    elif pattern_matching_result == 1:
        return "calculated"

    elif pattern_matching_result == 2:
        return None



__all__ = ["parse_prognosis_type"]

