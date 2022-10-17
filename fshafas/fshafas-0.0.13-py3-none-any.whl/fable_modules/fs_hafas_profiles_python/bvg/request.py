from __future__ import annotations
from ...fs_hafas_python.types_raw_hafas_client import (RawRequestClient, RawRequestAuth, RawRequest)

request: RawRequest = RawRequest("de", [], RawRequestClient("BVG", "6020000", "IPA", "FahrInfo"), "BVG.1", "1.44", RawRequestAuth("AID", "YoJ05NartnanEGCj"))

__all__ = ["request"]

