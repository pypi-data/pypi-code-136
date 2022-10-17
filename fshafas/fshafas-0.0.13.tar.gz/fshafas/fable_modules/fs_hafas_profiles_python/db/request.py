from __future__ import annotations
from ...fs_hafas_python.types_raw_hafas_client import (RawRequestClient, RawRequestAuth, RawRequest)

request: RawRequest = RawRequest("de", [], RawRequestClient("DB", "21120000", "AND", "DB Navigator"), "DB.R21.12.a", "1.34", RawRequestAuth("AID", "n91dB8Z77MLdoR0K"))

__all__ = ["request"]

