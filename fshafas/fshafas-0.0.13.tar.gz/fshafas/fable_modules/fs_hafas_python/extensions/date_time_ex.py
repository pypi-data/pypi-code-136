from typing import Any
from ...fable_library.string import (to_text, printf)

def format_date(dt: Any, pattern: str) -> str:
    if "yyyyMMdd" == pattern:
        arg_2: int = (dt.day) or 0
        arg_1: int = (dt.month) or 0
        arg: int = (dt.year) or 0
        return to_text(printf("%04d%02d%02d"))(arg)(arg_1)(arg_2)

    else: 
        raise Exception("nyi")



def format_time(dt: Any, pattern: str) -> str:
    if "HHmm" == pattern:
        arg_1: int = (dt.minute) or 0
        arg: int = (dt.hour) or 0
        return to_text(printf("%02d%02d"))(arg)(arg_1)

    else: 
        raise Exception("nyi")



__all__ = ["format_date", "format_time"]

