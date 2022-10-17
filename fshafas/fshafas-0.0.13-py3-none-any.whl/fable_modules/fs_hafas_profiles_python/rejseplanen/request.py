from __future__ import annotations
from ...fs_hafas_python.types_raw_hafas_client import (RawRequestClient, RawRequestAuth, RawRequest)

request: RawRequest = RawRequest("de", [], RawRequestClient("DK", "", "AND", ""), "DK.9", "1.43", RawRequestAuth("AID", "irkmpm9mdznstenr-android"))

__all__ = ["request"]

