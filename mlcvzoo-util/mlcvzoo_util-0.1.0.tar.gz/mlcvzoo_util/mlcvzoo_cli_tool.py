# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for the definition of a super class for any mlcvzoo module that is
providing a commandline interface.
"""

import argparse
import logging
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Generic, Optional, Type, TypeVar, cast

from config_builder import BaseConfigClass, ConfigBuilder

ConfigurationType = TypeVar("ConfigurationType", bound=BaseConfigClass)


class DictAction(argparse.Action):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(DictAction, self).__init__(*args, **kwargs)
        self.nargs = "+"

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Any,
        option_string: Optional[Any] = None,
    ) -> None:
        # Get or create initial parameter value list
        current_values = getattr(namespace, self.dest, []) or []
        setattr(namespace, self.dest, current_values)

        # Get and store new parameter values
        parameter_values = getattr(namespace, self.dest)
        parameter_values.append(dict(v.split(":") for v in values))


class MLCVZooCLITool(ABC, Generic[ConfigurationType]):
    @staticmethod
    @abstractmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> ConfigurationType:
        """
        Create a configuration of type ConfigurationType

        Expected implementation:

        return cast(
            YourConfigurationClass,
            YourCLITool._create_cli_configuration(
                configuration_class=YourConfigurationClass,
                string_replacement_map=string_replacement_map,
                configure_argparse=YourCLITool.configure_argparse,
            )
        )

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """
        raise NotImplementedError(
            "Must be implemented by sub-class: create_cli_configuration(...)."
        )

    @staticmethod
    def _create_cli_configuration(
        configuration_class: Type[ConfigurationType],
        string_replacement_map: Optional[Dict[str, str]] = None,
        configure_argparse: Optional[Callable[[argparse.ArgumentParser], None]] = None,
    ) -> ConfigurationType:
        return cast(
            ConfigurationType,
            ConfigBuilder(
                class_type=configuration_class,
                string_replacement_map=string_replacement_map,
                configure_argparse=configure_argparse,
                use_argparse=True,
            ).configuration,
        )

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:

        log_dir_option = "log-dir"
        log_level_option = "log-level"

        parser.add_argument(
            f"--{log_dir_option}",
            help="Directory where log-files should be written to",
            type=str,
        )

        parser.add_argument(
            f"--{log_level_option}",
            help="Define the logging level",
            type=str,
            default=logging.INFO,
            choices=logging._nameToLevel.keys(),
        )


def configure_model_argparse(
    parser: argparse.ArgumentParser,
) -> None:
    parser.add_argument(
        "--class-type",
        help="Class type of the model, respectively "
        "the string identifier of a model that is "
        "registered in the ModelRegistry of the mlcvzoo",
        type=str,
    )
    parser.add_argument(
        "--constructor-parameters",
        help="A list of key-value pairs "
        "in the format KEY:VALUE that should overwrite parameter of the model constructor",
        action=DictAction,
    )
