# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

from typing import List, Optional

import related
from config_builder import BaseConfigClass
from mlcvzoo_base.configuration.device_query import ModelTimerDeviceQueryConfig
from mlcvzoo_base.configuration.mlfow_config import MLFlowConfig
from mlcvzoo_base.configuration.model_config import ModelConfig


@related.mutable(strict=True)
class ModelTimerConfig(BaseConfigClass):
    test_image_path: str = related.StringField(required=True)

    device_query: ModelTimerDeviceQueryConfig = related.ChildField(
        cls=ModelTimerDeviceQueryConfig,
    )

    model_config: ModelConfig = related.ChildField(cls=ModelConfig)

    mlflow_config: Optional[MLFlowConfig] = related.ChildField(
        cls=MLFlowConfig, required=False, default=None
    )

    number_of_runs: int = related.IntegerField(required=False, default=100)

    # Number of runs that are not accounted for determining the average runtime
    number_of_warm_up_runs: int = related.IntegerField(required=False, default=3)
