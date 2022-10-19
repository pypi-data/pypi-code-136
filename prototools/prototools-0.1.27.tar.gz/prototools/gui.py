import os
from typing import Optional

try:
    if os.name == "nt":
        from ctypes import c_int, WINFUNCTYPE, windll
        from ctypes.wintypes import HWND, LPCWSTR, UINT
except:
    pass


def messagebox(
    caption: Optional[str] = None, 
    text: Optional[str] = None,
    flags: Optional[int] = None
) -> None:
    caption = "ProtoTools" if caption is None else caption
    text = "" if text is None else text
    flags = 0 if flags is None else flags
    prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
    paramflags = (1, "hwnd", 0), (1, "text", text), (1, "caption", caption), (1, "flags", flags)
    MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)
    MessageBox()
