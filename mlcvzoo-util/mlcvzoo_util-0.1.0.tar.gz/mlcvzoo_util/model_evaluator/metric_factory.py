# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for the definition of a generic MetricFactory which provides
interface methods. These interfaces are consumed by the ModelEvaluator
in order to implement a generic metric computation functionally.
"""

import logging
import os
from abc import ABC
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

import mlflow
from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.model import Model, ObjectDetectionModel
from mlcvzoo_base.evaluation.object_detection.data_classes import (
    ODModelEvaluationMetrics,
)
from mlcvzoo_base.evaluation.object_detection.metrics_computation import (
    MetricsComputation,
)
from mlcvzoo_base.evaluation.object_detection.metrics_logging import (
    log_od_metrics_to_mlflow,
)
from mlcvzoo_base.evaluation.object_detection.model_evaluation import (
    evaluate_with_model,
)

from mlcvzoo_util.model_evaluator.configuration import ModelEvaluatorConfig
from mlcvzoo_util.model_evaluator.structs import CheckpointInfo, CheckpointLoggingModes

ModelType = TypeVar("ModelType", bound=Model[Any, Any, Any])
EvaluationMetricType = TypeVar("EvaluationMetricType")

logger = logging.getLogger(__name__)


class MetricFactory(ABC, Generic[ModelType, EvaluationMetricType]):
    """
    Super class for defining interfaces for metric computations.
    """

    @staticmethod
    def compute_metrics(
        inference_model: ModelType,
        gt_annotations: List[BaseAnnotation],
        model_evaluator_config: ModelEvaluatorConfig,
    ) -> EvaluationMetricType:
        raise NotImplementedError(
            "Must be implemented by sub-class: compute_metrics(...)"
        )

    @staticmethod
    def determine_best_checkpoint(
        evaluated_checkpoint_metrics: Dict[str, EvaluationMetricType],
    ) -> CheckpointInfo:
        raise NotImplementedError(
            "Must be implemented by sub-class: determine_best_checkpoint(...)"
        )

    @staticmethod
    def log_results(
        checkpoint_log_mode: str,
        evaluated_checkpoint_metrics: Dict[str, EvaluationMetricType],
        best_checkpoint: CheckpointInfo,
    ) -> None:
        raise NotImplementedError("Must be implemented by sub-class: log_results(...)")


class ODMetricFactory(
    MetricFactory[ObjectDetectionModel, ODModelEvaluationMetrics]  # type: ignore[type-arg]
):
    """
    Implements the MetricFactory in order to provide an
    generic evaluation of ObjectDetectionModels.
    """

    @staticmethod
    def compute_metrics(
        inference_model: ObjectDetectionModel,  # type: ignore[type-arg]
        gt_annotations: List[BaseAnnotation],
        model_evaluator_config: ModelEvaluatorConfig,
    ) -> ODModelEvaluationMetrics:

        return evaluate_with_model(
            model=inference_model,
            gt_annotations=gt_annotations,
            iou_thresholds=model_evaluator_config.iou_thresholds,
        )

    @staticmethod
    def determine_best_checkpoint(
        evaluated_checkpoint_metrics: Dict[str, ODModelEvaluationMetrics],
    ) -> CheckpointInfo:
        """
        Determine the best checkpoint based on the given overall AP metric per checkpoint.

        Returns:
            A CheckpointInfo object stating the best checkpoint
        """
        best_checkpoint = CheckpointInfo(path="", score=0.0)

        for ckpt, model_metrics in evaluated_checkpoint_metrics.items():
            current_map = MetricsComputation.compute_average_ap(
                model_metrics=model_metrics
            )

            if current_map > best_checkpoint.score:
                best_checkpoint = CheckpointInfo(path=ckpt, score=current_map)

        return best_checkpoint

    @staticmethod
    def log_results(
        checkpoint_log_mode: str,
        evaluated_checkpoint_metrics: Dict[str, ODModelEvaluationMetrics],
        best_checkpoint: CheckpointInfo,
    ) -> None:
        """
        Logs evaluated metrics, checkpoints and parameters to mlflow as
        specified in configuration file.

        Returns:
            None
        """

        # TODO: Add feature that determines the epoch from a given checkpoint path.
        #       Use it to fill the step parameter correctly.
        for step, (ckpt, metrics) in enumerate(evaluated_checkpoint_metrics.items()):
            for iou in metrics.metrics_dict:
                log_od_metrics_to_mlflow(
                    model_specifier=metrics.model_specifier,
                    metrics_dict=metrics.metrics_dict,
                    iou_threshold=float(iou),
                    step=step,
                )

        logger.info(f"Logged metrics for all evaluated checkpoints")

        if not mlflow.active_run():
            logger.warning(
                "No mlflow run is active, "
                "logging of checkpoint artifacts will not take place"
            )
            return

        if checkpoint_log_mode.lower() == CheckpointLoggingModes.ALL:
            for ckpt in evaluated_checkpoint_metrics:
                mlflow.log_artifact(ckpt)

        elif checkpoint_log_mode.lower() == CheckpointLoggingModes.BEST:
            if not os.path.isfile(best_checkpoint.path):
                raise FileNotFoundError("Could not find a best checkpoint!")

            mlflow.log_artifact(best_checkpoint.path)
        elif checkpoint_log_mode.lower() == CheckpointLoggingModes.NONE:
            pass
        else:
            raise ValueError(
                f"The specified value for parameter: "
                f"'{checkpoint_log_mode}' "
                f"'checkpoint_log_mode' is invalid! Only 'all' and 'best' is allowed!"
            )

        logger.info(
            f"Logged evaluated checkpoints as specified in config: "
            f"'{checkpoint_log_mode}"
        )


__metric_factory_dict: Dict[Type[Model], Type[MetricFactory]] = {  # type: ignore[type-arg]
    ObjectDetectionModel: ODMetricFactory,
}


def get_factory(inference_model: Model) -> Optional[Type[MetricFactory]]:  # type: ignore[type-arg]
    for key, value in __metric_factory_dict.items():
        if isinstance(inference_model, key):
            return value

    return None
