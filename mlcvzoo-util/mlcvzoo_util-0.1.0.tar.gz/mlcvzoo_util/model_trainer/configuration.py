# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for parsing information from yaml in python accessible attributes for the ModelSuite class.
"""
from typing import List

import related
from config_builder import BaseConfigClass
from mlcvzoo_base.configuration.model_config import ModelConfig


@related.mutable(strict=False)
class ModelTrainerConfig(BaseConfigClass):
    """
    Class for parsing general information about the model suite and also further information
    in respective hierarchy
    """

    model_config: ModelConfig = related.ChildField(cls=ModelConfig)
