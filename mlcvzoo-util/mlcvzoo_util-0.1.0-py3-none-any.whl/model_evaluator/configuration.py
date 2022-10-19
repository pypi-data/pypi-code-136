# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for configuring the parsing of information from yaml in python
accessible attributes for the Evaluation Runner (ER) class
"""

from typing import List, Optional

import related
from config_builder import BaseConfigClass
from mlcvzoo_base.configuration.annotation_handler_config import AnnotationHandlerConfig
from mlcvzoo_base.configuration.mlfow_config import MLFlowConfig
from mlcvzoo_base.configuration.model_config import ModelConfig

from mlcvzoo_util.model_evaluator.structs import CheckpointLoggingModes


@related.mutable(strict=True)
class ModelEvaluatorMLflowConfig(BaseConfigClass):
    """Class for parsing information for mlflow"""

    config: MLFlowConfig = related.ChildField(cls=MLFlowConfig)

    checkpoint_log_mode: str = related.StringField(
        required=False, default=CheckpointLoggingModes.NONE
    )


@related.mutable(strict=True)
class CheckpointConfig(BaseConfigClass):
    """Class for parsing information about model checkpoints to evaluate"""

    checkpoint_dir: str = related.StringField()
    checkpoint_format: str = related.StringField()
    ignore: List[str] = related.SequenceField(cls=str, required=False, default=[])


@related.mutable(strict=True)
class ModelEvaluatorConfig(BaseConfigClass):
    """Class for parsing information from yaml in respective hierarchy"""

    iou_thresholds: List[float] = related.SequenceField(float)

    checkpoint_config: Optional[CheckpointConfig] = related.ChildField(
        cls=CheckpointConfig, required=False, default=None
    )

    mlflow_config: Optional[ModelEvaluatorMLflowConfig] = related.ChildField(
        cls=ModelEvaluatorMLflowConfig, required=False, default=None
    )


@related.mutable(strict=True)
class ModelEvaluatorCLIConfig(ModelEvaluatorConfig):
    """Class for parsing information from yaml in respective hierarchy"""

    iou_thresholds: List[float] = related.SequenceField(float)

    model_config: ModelConfig = related.ChildField(cls=ModelConfig)

    checkpoint_config: CheckpointConfig = related.ChildField(cls=CheckpointConfig)

    annotation_handler_config: AnnotationHandlerConfig = related.ChildField(
        cls=AnnotationHandlerConfig
    )

    mlflow_config: Optional[ModelEvaluatorMLflowConfig] = related.ChildField(
        cls=ModelEvaluatorMLflowConfig, required=False, default=None
    )
