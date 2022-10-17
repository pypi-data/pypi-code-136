# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Drop unique target value grains for distributed tasks."""
from typing import Dict, List, Optional, Set, Tuple, Generator
import numpy as np
import pandas as pd
import itertools

from azureml.automl.core.shared import constants

from ..unique_target_grain_dropper import UniqueTargetGrainDropper
from ..unique_target_grain_dropper_base import UniqueTargetGrainDropperBase
from .aggregate_transformer import AutoMLAggregateTransformer


class AggregatedUniqueTargetGrainDropper(AutoMLAggregateTransformer, UniqueTargetGrainDropperBase):
    """Aggregated unique target grain dropper for distributed forecasting tasks."""
    def __init__(self, mapping: Dict[str, UniqueTargetGrainDropper]) -> None:
        AutoMLAggregateTransformer.__init__(self, mapping)
        UniqueTargetGrainDropperBase.__init__(self)
        self._allow_empty_output = True
        for dropper in mapping.values():
            dropper.drop_single_grain = True

    def _unique_target_grains_dropper_generator(self) -> Generator[UniqueTargetGrainDropper, None, None]:
        return filter(lambda x: x.has_unique_target_grains, self.mapping.values())

    @property
    def has_unique_target_grains(self) -> bool:
        return next(self._unique_target_grains_dropper_generator(), None) is not None

    @property
    def unique_target_grains(self) -> Set[str]:
        return set(itertools.chain.from_iterable(
            map(lambda x: x.unique_target_grains, self._unique_target_grains_dropper_generator())))

    @property
    def grains_to_keep(self) -> List[str]:
        return list(itertools.chain.from_iterable(map(lambda x: x.grains_to_keep, self._mapping.values())))

    @property
    def last_X_y(self) -> Tuple[Optional[pd.DataFrame], Optional[np.ndarray]]:
        """Last X and y in the fit data."""
        dfs = []
        for dropper in self._unique_target_grains_dropper_generator():
            last_X, last_y = dropper.last_X_y
            if last_X is not None:
                last_X[constants.TimeSeriesInternal.DUMMY_TARGET_COLUMN] = last_y
                dfs.append(last_X)

        if dfs:
            last_X = pd.concat(dfs, sort=False)
            last_y = last_X.pop(constants.TimeSeriesInternal.DUMMY_TARGET_COLUMN).values
            return last_X, last_y
        else:
            return None, None
