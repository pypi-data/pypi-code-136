from .cte import (
    INPUT_DP,
    INPUT_JSON_FP,
    MANIFEST_JSON_FP,
    OUTPUT_DP,
    OUTPUT_JSON_FP,
    ROOT,
    TMP,
)
from ..parsers import DotDict


class FileSystem(DotDict):
    def __init__(self, tool="toolname", ensure_output_dp: bool = True):
        self.fs = dict(
            root=ROOT,
            tmp=TMP,
            idp=INPUT_DP,
            odp=OUTPUT_DP,
            ifp=INPUT_JSON_FP,
            ofp=OUTPUT_JSON_FP,
            mfp=MANIFEST_JSON_FP,
        )
        self.fs["tdp"] = self.fs.get("odp") / tool
        super().__init__(self.fs, name="FileSystem")

        if ensure_output_dp:
            self.tdp.mkdir(
                parents=True, exist_ok=True
            )  # ensure tool output directory exists (not guaranteed by the batchx!)
        return
