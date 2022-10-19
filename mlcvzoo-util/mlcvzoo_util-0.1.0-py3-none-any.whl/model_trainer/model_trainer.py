# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for handling the training of mlcvzoo models"""

import argparse
import logging
from typing import Any, Dict, Optional, Type, cast

from config_builder import ConfigBuilder
from mlcvzoo_base.api.interfaces import Trainable
from mlcvzoo_base.api.model import Model
from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.models.model_registry import ModelRegistry

from mlcvzoo_util.logger import Logger
from mlcvzoo_util.mlcvzoo_cli_tool import MLCVZooCLITool, configure_model_argparse
from mlcvzoo_util.model_trainer.configuration import ModelTrainerConfig

logger = logging.getLogger(__name__)


class ModelTrainer(MLCVZooCLITool[ModelTrainerConfig]):
    """Class to handle the training of different models"""

    def __init__(
        self,
        configuration: ModelTrainerConfig,
    ):
        self.configuration: ModelTrainerConfig = configuration

    @staticmethod
    def create_configuration(
        yaml_config_path: str,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> ModelTrainerConfig:
        """
        Create a ModelTrainerConfig

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
            ModelTrainerConfig,
            ConfigBuilder(
                class_type=ModelTrainerConfig,
                yaml_config_path=yaml_config_path,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
            ).configuration,
        )

    @staticmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> ModelTrainerConfig:
        """
        Create a ModelTrainerConfig

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """

        return MLCVZooCLITool._create_cli_configuration(
            configuration_class=ModelTrainerConfig,
            string_replacement_map=string_replacement_map,
            configure_argparse=ModelTrainer.configure_argparse,
        )

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:
        parser.description = "Run training for the given model-config"
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
        model_config.set_inference(inference=False)
        return ModelRegistry().init_model(
            model_config=model_config, string_replacement_map=string_replacement_map
        )

    def run_training(self) -> None:
        """Runs the training with each of the models in the models attribute"""

        model = ModelTrainer.create_model(
            model_config=self.configuration.model_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        if not isinstance(model, Trainable):
            raise ValueError(
                "The ModelTrainer only works with models that inherit from the"
                "Trainable interface"
            )
        model.train()


def main() -> None:
    """
    Entry point when using the mlcvzoo-modeltrainer command line tool.
    (See [tool.poetry.scripts] section in pyproject.toml)
    """

    args = ConfigBuilder.setup_argparse(
        configure_argparse=ModelTrainer.configure_argparse
    ).parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="ModelTimer",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    configuration: ModelTrainerConfig = ModelTrainer.create_cli_configuration()

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

    model_timer = ModelTrainer(configuration=configuration)
    model_timer.run_training()


if __name__ == "__main__":
    main()
