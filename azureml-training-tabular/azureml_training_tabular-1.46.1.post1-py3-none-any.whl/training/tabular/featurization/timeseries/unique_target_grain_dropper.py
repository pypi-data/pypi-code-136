# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Drop unique target value grains from dataset."""

from typing import Any, List, Optional, Set, Tuple
import logging
import numpy as np
import pandas as pd

from ..._diagnostics.debug_logging import function_debug_log_wrapped
from ..._types import GrainType
from ...timeseries._time_series_data_set import TimeSeriesDataSet
from ..._constants import TimeSeriesInternal
from ...featurization.utilities import _get_num_unique
from .grain_dropper import GrainDropper
from .unique_target_grain_dropper_base import UniqueTargetGrainDropperBase


class UniqueTargetGrainDropper(GrainDropper, UniqueTargetGrainDropperBase):
    """Uniqe target grain dropper."""

    def __init__(self,
                 target_rolling_window_size: int = 0,
                 target_lags: Optional[List[int]] = None,
                 n_cross_validations: Optional[int] = None,
                 cv_step_size: Optional[int] = None,
                 max_horizon: int = TimeSeriesInternal.MAX_HORIZON_DEFAULT,
                 **kwargs: Any) -> None:
        """
        Constructor.

        :param target_rolling_window_size: The size of a target rolling window.
        :param target_lags: The size of a lag of a lag operator.
        :param n_cross_validations: The number of cross validations.
        :param cv_step_size: The number of steps to move validation set.
        :param max_horizon: The maximal horizon.
        :raises: ConfigException
        """
        UniqueTargetGrainDropperBase.__init__(self)
        GrainDropper.__init__(
            self, target_rolling_window_size, target_lags, n_cross_validations, cv_step_size, max_horizon,
            drop_single_grain=False, drop_unknown=False)
        self._last_X = None  # type: Optional[pd.DataFrame]
        self._last_y = None  # type: Optional[np.ndarray]

    @function_debug_log_wrapped(logging.INFO)
    def _fit(self, X: TimeSeriesDataSet, y: Any = None) -> 'UniqueTargetGrainDropper':
        target_col = X.target_column_name

        dfs = []
        for grain, df in X.groupby_time_series_id():
            # short grain and all missing value won't be handled by unique target grain dropper.
            n_unique = _get_num_unique(df[target_col], ignore_na=True)
            if n_unique != 1 or not self.is_df_long(df, X):
                self._grains_to_keep.append(grain)
            else:
                self._grains_to_drop.append(grain)
                dfs.append(df.tail(1))

        if dfs:
            self._last_X = pd.concat(dfs, sort=False)
            self._last_y = self._last_X.pop(target_col).values

        return self

    def _validate_transformed_data(self, df: TimeSeriesDataSet, dropped_grains: List[GrainType]) -> None:
        pass

    @property
    def last_X_y(self) -> Tuple[Optional[pd.DataFrame], Optional[np.ndarray]]:
        """The last X and y observed during fit."""
        return self._last_X, self._last_y

    @property
    def unique_target_grains(self) -> Set[str]:
        """The unique target grains."""
        return set(self._grains_to_drop)

    @property
    def has_unique_target_grains(self) -> bool:
        """The flag that shows whether the transformer contains unique target grain or not."""
        total_grains = len(self._grains_to_keep) + len(self.unique_target_grains)
        if total_grains > 1:
            return len(self.unique_target_grains) > 0
        elif self.drop_single_grain:
            return len(self.unique_target_grains) > 0
        else:
            return False
