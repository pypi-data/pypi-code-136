from __future__ import annotations
from typing import (Optional, Callable, Any)
from ...fable_library.option import (map, some)
from ..context import Context
from ..types_hafas_client import (Hint, Status)
from ..types_raw_hafas_client import RawRem

default_hint: Hint = Hint("hint", None, None, "", None)

default_status: Status = Status("status", None, None, "", None)

def parse_hint(ctx: Context, h: RawRem) -> Optional[Any]:
    text: str
    match_value: Optional[str] = h.txt_n
    if match_value is None:
        text = ""

    else: 
        txt_n: str = match_value
        text = txt_n.strip()

    code: Optional[str] = h.code if (h.code != "") else None
    def trim(s: Optional[str]=None, ctx: Context=ctx, h: RawRem=h) -> Optional[str]:
        def mapping(s_1: str, s: Optional[str]=s) -> str:
            return s_1.strip()

        return map(mapping, s)

    if h.type == "M":
        return some(Status(default_status.type, code, trim(h.txt_s), text, default_status.trip_id))

    elif "AI".find(h.type) >= 0:
        return some(Hint(default_hint.type, code, default_hint.summary, text, default_hint.trip_id))

    elif "DURNYQP".find(h.type) >= 0:
        return some(Status(default_status.type, code, default_status.summary, text, default_status.trip_id))

    else: 
        return None



__all__ = ["default_hint", "default_status", "parse_hint"]

