# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module that provides a generic component for measuring runtimes of mlcvzoo models"""

import argparse
import logging
import time
from typing import Any, Dict, List, Optional, Type, cast

import cv2
import mlflow
from config_builder import ConfigBuilder
from mlcvzoo_base.api.model import Model
from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.configuration.structs import MLFlowExperimentTypes
from mlcvzoo_base.metrics.mlflow.mlflow_runner import MLFLowRunner
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.utils.gpu_util import GpuInfo, get_device_info

from mlcvzoo_util.logger import Logger
from mlcvzoo_util.mlcvzoo_cli_tool import MLCVZooCLITool, configure_model_argparse
from mlcvzoo_util.model_timer.configuration import ModelTimerConfig

logger = logging.getLogger(__name__)


class ModelTimer(MLCVZooCLITool[ModelTimerConfig]):
    """
    Utility class for measuring the individual inference time of a group of models
    specified in the ModelTimer config file and logging the results to MLFlow.
    """

    def __init__(self, configuration: ModelTimerConfig) -> None:
        self.configuration: ModelTimerConfig = configuration

        self.mlflow_runner: Optional[MLFLowRunner] = None
        if self.configuration.mlflow_config is not None:
            self.mlflow_runner = MLFLowRunner(
                configuration=self.configuration.mlflow_config,
            )
        else:
            logger.info(
                "Not able to create MLFLowRunner since no MLFlowConfig was "
                "set in ModelTimerConfig.mlflow_config. "
                "Just logging execution time information to standard output."
            )

        self.inference_time_mean: Optional[float] = None
        self.inference_time_list: List[float] = []

    @staticmethod
    def create_configuration(
        yaml_config_path: str,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> ModelTimerConfig:
        """
        Create a ModelTimerConfig

        Args:
            yaml_config_path:  A yaml filepath where to build the configuration
                               object from
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
            no_checks: Whether the configuration object should be checked for mutual exclusiveness
                       and the "check_values" method for each attribute of the supertype
                       "BaseConfigClass" should be called
        Returns:
            The created configuration
        """

        return cast(
            ModelTimerConfig,
            ConfigBuilder(
                class_type=ModelTimerConfig,
                yaml_config_path=yaml_config_path,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
            ).configuration,
        )

    @staticmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> ModelTimerConfig:
        """
        Create a ModelTimerConfig

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """

        return MLCVZooCLITool._create_cli_configuration(
            configuration_class=ModelTimerConfig,
            string_replacement_map=string_replacement_map,
            configure_argparse=ModelTimer.configure_argparse,
        )

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:
        parser.description = (
            "Tool for measuring the individual inference time of a "
            "group of models specified in the ModelTimer config file "
            "and optionally log the results to MLFlow."
        )
        MLCVZooCLITool.configure_argparse(parser)
        configure_model_argparse(parser=parser)

    @staticmethod
    def create_model(
        model_config: ModelConfig,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> Model:  # type: ignore[type-arg]
        """
        Creates a model based on the given config

        Args:
            model_config: The model config that should be used
                          for creating a model
            string_replacement_map: (Optional) A dictionary that defines placeholders which can
                                    be used while parsing a configuration file. They can be
                                    understood as variables that can be used to define configs
                                    that are valid across multiple devices.
        Returns:
            The created model
        """
        # In order to be able to load the checkpoints that
        # should be evaluated, we need an inference model
        model_config.set_inference(inference=True)
        return ModelRegistry().init_model(
            model_config=model_config, string_replacement_map=string_replacement_map
        )

    def run(self) -> None:
        """
        Run the models specified in the ModelTimer config file, measure their inference time and log the results
        (inference time based on epoch time and bare process time as well as their means) to MLFlow.
        """
        model = ModelTimer.create_model(
            model_config=self.configuration.model_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        image = cv2.imread(self.configuration.test_image_path)

        if self.mlflow_runner is not None:
            self.mlflow_runner.start_mlflow_run(
                experiment_name=MLFlowExperimentTypes.TIMING,
                run_name=model.get_name(),
            )
            logger.info("Log mlflow metrics for model '%s'", model.__class__)

        # TODO: Use the interface method in future implementations that state
        #       whether the model is running on gpu or cpu
        # mlflow.log_param(key="device_type", value="TODO")

        gpu_info: Optional[GpuInfo] = get_device_info(
            device_query=self.configuration.device_query,
        )

        if gpu_info is not None and mlflow.active_run() is not None:
            # log gpu info to mlflow
            mlflow.log_param(key="device_name", value=gpu_info.name)

        # perform warm-up
        for _ in range(0, self.configuration.number_of_warm_up_runs):
            start_epoch_time = time.time_ns()
            model.predict(data_item=image)
            logger.info("warm-up-time: %dms", time.time_ns() - start_epoch_time)

        # perform benchmarked inference
        for run_index in range(0, self.configuration.number_of_runs):
            start_epoch_time = time.time_ns()

            model.predict(data_item=image)

            self.inference_time_list.append(
                (time.time_ns() - start_epoch_time) / 1000 / 1000
            )

            if mlflow.active_run() is not None:
                mlflow.log_metric(
                    key="runtime_ms",
                    value=self.inference_time_list[-1],
                    step=run_index,
                )
            logger.info("runtime: %dms", self.inference_time_list[-1])

        if len(self.inference_time_list) > 0:
            self.inference_time_mean = sum(self.inference_time_list) / len(
                self.inference_time_list
            )
            logger.info("runtime-mean: %dms", self.inference_time_mean)
            if mlflow.active_run() is not None:
                mlflow.log_metric("runtime-mean_ms", value=self.inference_time_mean)

        if self.mlflow_runner is not None:
            self.mlflow_runner.end_run()


def main() -> None:
    """
    Entry point when using the mlcvzoo-modeltimer command line tool.
    (See [tool.poetry.scripts] section in pyproject.toml)
    """

    args = ConfigBuilder.setup_argparse(
        configure_argparse=ModelTimer.configure_argparse
    ).parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="ModelTimer",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    configuration: ModelTimerConfig = ModelTimer.create_cli_configuration()

    configuration.model_config.update_class_type(
        args_dict=vars(args),
    )

    model_type: Optional[Type[Model[Any, Any, Any]]] = ModelRegistry().get_model_type(
        class_type=configuration.model_config.class_type
    )

    if model_type:
        configuration.model_config.update_constructor_parameters(
            args_dict=vars(args),
            model_type=model_type,
        )
    else:
        raise ValueError(
            f"Model type '{configuration.model_config.class_type}' is not registered. "
            f"Use one of '{list(ModelRegistry().get_registered_models().keys())}'",
        )

    model_timer = ModelTimer(configuration=configuration)
    model_timer.run()


if __name__ == "__main__":
    main()
