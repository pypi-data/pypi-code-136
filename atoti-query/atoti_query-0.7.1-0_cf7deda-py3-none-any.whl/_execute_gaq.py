from datetime import timedelta
from typing import Iterable, Optional, Protocol

import pandas as pd
from atoti_core import BaseCondition, BaseLevel, BaseMeasure


class _ExecuteGaq(Protocol):  # pyright: ignore[reportUnusedClass]
    def __call__(
        self,
        *,
        cube_name: str,
        measures: Iterable[BaseMeasure],
        levels: Iterable[BaseLevel],
        filter: Optional[BaseCondition] = None,  # pylint: disable=redefined-builtin
        include_totals: bool,
        scenario: str,
        timeout: timedelta,
    ) -> pd.DataFrame:
        ...
