from __future__ import annotations
from typing import Optional
from ...fable_library.option import default_arg
from ..context import Context
from ..extra_types import Icon
from ..types_raw_hafas_client import RawIco

def parse_icon(ctx: Context, i: RawIco) -> Optional[Icon]:
    match_value: Optional[str] = i.res
    (pattern_matching_result, res_1) = (None, None)
    if match_value is not None:
        if match_value != "Empty":
            pattern_matching_result = 0
            res_1 = match_value

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return Icon(res_1, default_arg(default_arg(i.text, i.txt), i.txt_s))

    elif pattern_matching_result == 1:
        return None



__all__ = ["parse_icon"]

