# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Central module for handling the download and upload
of zip files to CVAT via their commandline interface
"""

import argparse
import logging
import sys
from typing import Dict, Optional, cast

from config_builder import ConfigBuilder

from mlcvzoo_util.cvat_annotation_handler.configuration import (
    CVATAnnotationHandlerConfig,
)
from mlcvzoo_util.cvat_annotation_handler.cvat_dumper import CVATDumper
from mlcvzoo_util.cvat_annotation_handler.cvat_uploader import PascalVOCUploader
from mlcvzoo_util.logger import Logger
from mlcvzoo_util.mlcvzoo_cli_tool import MLCVZooCLITool

logger = logging.getLogger(__name__)


class CVATAnnotationHandler(MLCVZooCLITool[CVATAnnotationHandlerConfig]):
    """
    Central class for handling the download and upload
    of zip files to CVAT via their commandline interface
    """

    def __init__(self, configuration: CVATAnnotationHandlerConfig):
        """
        Instantiates a CVATAnnotationHandler object

        Args:
            configuration: (Optional) An already existing configuration object
        """

        self.configuration: CVATAnnotationHandlerConfig = configuration

    @staticmethod
    def create_configuration(
        yaml_config_path: str,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> CVATAnnotationHandlerConfig:
        """
        Create a CVATAnnotationHandlerConfig

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
            CVATAnnotationHandlerConfig,
            ConfigBuilder(
                class_type=CVATAnnotationHandlerConfig,
                yaml_config_path=yaml_config_path,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
            ).configuration,
        )

    @staticmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> CVATAnnotationHandlerConfig:
        """
        Create a CVATAnnotationHandlerConfig

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """

        return MLCVZooCLITool._create_cli_configuration(
            configuration_class=CVATAnnotationHandlerConfig,
            string_replacement_map=string_replacement_map,
            configure_argparse=CVATAnnotationHandler.configure_argparse,
        )

    def download_all_tasks(self) -> None:
        """
        Execute all downloads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        for dump_task_config in self.configuration.dump_task_configs:
            CVATDumper.dump_task_data(
                dump_task_config=dump_task_config,
                cvat_cli_config=self.configuration.cvat_cli_config,
                disable_ssl_verify=self.configuration.cvat_cli_config.disable_ssl_verify,
            )
            logger.info("==========  DUMP TASK FINISHED  ==========\n")

    def upload_all_tasks(self) -> None:
        """
        Execute all uploads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        for upload_task_config in self.configuration.upload_task_configs:
            PascalVOCUploader.upload_task_data(
                upload_task_config=upload_task_config,
                cvat_cli_config=self.configuration.cvat_cli_config,
                disable_ssl_verify=self.configuration.cvat_cli_config.disable_ssl_verify,
            )
            logger.info("==========  UPLOAD TASK FINISHED  ==========\n")

    def run(self) -> None:
        """
        Execute all downloads and uploads that are specified in the configuration object
        of this class

        Returns:
            None
        """

        logger.info("Start to download and upload tasks")

        self.download_all_tasks()
        self.upload_all_tasks()

        logger.info("Finished to download and upload tasks")

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:
        MLCVZooCLITool.configure_argparse(parser)
        parser.description = "Download and upload annotation files from/to CVAT"


def main() -> None:
    """
    Main entry point of the CVATAnnotationHandler tool

    Returns:
        None
    """

    args = ConfigBuilder.setup_argparse(
        configure_argparse=CVATAnnotationHandler.configure_argparse
    ).parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="CVATAnnotationHandler",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    cvat_annotation_handler = CVATAnnotationHandler(
        configuration=CVATAnnotationHandler.create_cli_configuration()
    )
    cvat_annotation_handler.run()


if __name__ == "__main__":
    main()
