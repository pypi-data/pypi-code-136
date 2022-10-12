from datetime import timedelta
from typing import Literal, Protocol

import pandas as pd
from atoti_core import EMPTY_MAPPING, Context


class _QueryMdx(Protocol):  # pyright: ignore[reportUnusedClass]
    def __call__(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: timedelta = timedelta(seconds=30),
        mode: Literal["pretty", "raw"] = "pretty",
        context: Context = EMPTY_MAPPING
    ) -> pd.DataFrame:
        ...
