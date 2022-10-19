# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for handling the download of zip files to CVAT via their commandline interface"""

import logging
import os
import shutil

import yaml
from mlcvzoo_base.utils import ensure_dir, get_file_list
from mlcvzoo_base.utils.file_utils import extract_zip_data
from related import to_yaml

from mlcvzoo_util.cvat_annotation_handler.configuration import (
    CVATCLIConfig,
    CVATTaskDumpConfig,
    CVATTaskInfoConfig,
)
from mlcvzoo_util.cvat_annotation_handler.utils import run_command_in_process

logger = logging.getLogger(__name__)


class CVATDumper:
    """
    Class for handling the download of zip files to CVAT via their commandline interface
    """

    @staticmethod
    def dump_task_data(
        dump_task_config: CVATTaskDumpConfig,
        cvat_cli_config: CVATCLIConfig,
        disable_ssl_verify: bool = False,
    ) -> None:
        """
        Execute the download of a single zip file to the CVAT instance

        Args:
            dump_task_config: Configuration of the task that is to be downloaded
            cvat_cli_config: Basis configuration that is needed for the communication between
                             the commandline-interface and CVAT
            disable_ssl_verify: Whether to allow uncertified https connections

        Returns:
            None
        """

        logger.info(
            "\n==========  DUMP TASK  ==========\n" "'''\n%s'''\n",
            to_yaml(dump_task_config, yaml_package=yaml, dumper_cls=yaml.Dumper),
        )

        target_zip_path = CVATDumper.__create_target_zip_path(
            dump_task_config=dump_task_config
        )

        if CVATDumper.__pre_clean_up_and_determine_skip(
            overwrite_existing_zip=dump_task_config.overwrite_existing_zip,
            target_zip_path=target_zip_path,
        ):
            return

        # ================================
        # DOWNLOAD TASK DATA
        CVATDumper.call_cvat_dump_via_cli(
            cvat_cli_config=cvat_cli_config,
            target_zip_path=target_zip_path,
            task_info=dump_task_config.task_info,
            disable_ssl_verify=disable_ssl_verify,
        )

        zip_extract_dir = CVATDumper.__create_zip_extract_dir_path(
            target_zip_path=target_zip_path,
            zip_extract_dir=dump_task_config.zip_extract_dir,
        )

        # ================================
        # extract and move data
        if dump_task_config.extract_data:
            extract_zip_data(
                zip_path=target_zip_path,
                zip_extract_dir=zip_extract_dir,
            )

        if dump_task_config.move_extracted_data_to_dataset_dir is not None:
            CVATDumper.__extract_and_copy_annotations_to_data_dir(
                target_zip_path=target_zip_path,
                zip_extract_dir=zip_extract_dir,
                dataset_dir=dump_task_config.dataset_dir,
            )

        # ================================
        # post clean up
        if dump_task_config.clean_up_dump_data:
            CVATDumper.__post_clean_up(
                target_zip_path=target_zip_path,
                zip_extract_dir=zip_extract_dir,
            )

    @staticmethod
    def call_cvat_dump_via_cli(
        cvat_cli_config: CVATCLIConfig,
        target_zip_path: str,
        task_info: CVATTaskInfoConfig,
        disable_ssl_verify: bool = False,
    ) -> None:
        """
        Download a zip file from CVAT.

        Args:
            cvat_cli_config: Basis configuration that is needed for the communication between
                             the commandline-interface and CVAT
            target_zip_path: The zip file to upload
            task_info: Configuration for the specific task
            disable_ssl_verify: Whether to allow uncertified https connections

        Returns:
            None
        """

        ensure_dir(file_path=target_zip_path, verbose=True)
        command = CVATDumper.__create_cvat_dump_cli_command(
            base_command=cvat_cli_config.create_base_command_string(),
            target_zip_path=target_zip_path,
            task_info=task_info,
        )

        logger.info(
            "Dump annotation data: Task-ID=%s, " "zip-path=%s",
            task_info.task_ID,
            target_zip_path,
        )
        return_code = run_command_in_process(
            command=command, disable_ssl_verify=disable_ssl_verify
        )

        if return_code != 0:
            raise IOError(f"CVAT download did not succeed, return-code={return_code}")

    @staticmethod
    def __create_target_zip_path(dump_task_config: CVATTaskDumpConfig) -> str:

        if dump_task_config.target_zip_path == "":
            target_zip_path: str = os.path.join("tmp", "tmp-task.zip")
            logger.debug(
                "dump_task_config.target_zip_path is not set, therefore the default '%s' "
                "will be used to store the downloaded task:",
                target_zip_path,
            )
        else:
            target_zip_path = dump_task_config.target_zip_path

        return target_zip_path

    @staticmethod
    def __create_zip_extract_dir_path(
        target_zip_path: str, zip_extract_dir: str
    ) -> str:

        if not os.path.isdir(zip_extract_dir):
            zip_extract_dir = target_zip_path.replace(".zip", "")
            logger.debug(
                "dump_task_config.target_zip_path is not set, therefore the default '%s' "
                "will be used to store the downloaded task:",
                zip_extract_dir,
            )

        return zip_extract_dir

    @staticmethod
    def __pre_clean_up_and_determine_skip(
        overwrite_existing_zip: bool, target_zip_path: str
    ) -> bool:

        if os.path.isfile(target_zip_path):
            if overwrite_existing_zip:
                logger.info("Clean up old dump data, remove '%s'", target_zip_path)
                os.remove(target_zip_path)
            else:
                logger.info(
                    "Skip download since zip-file '%s' exists and should not be overwritten",
                    target_zip_path,
                )
                return True

        return False

    @staticmethod
    def __post_clean_up(target_zip_path: str, zip_extract_dir: str) -> None:
        if os.path.isfile(target_zip_path):
            logger.debug("(DUMP) Clean up zip file: '%s'", target_zip_path)
            os.remove(target_zip_path)

        if os.path.isdir(zip_extract_dir):
            logger.debug(
                "(DUMP) Clean up zip extraction directory: '%s'", zip_extract_dir
            )
            shutil.rmtree(zip_extract_dir)

    @staticmethod
    def __create_cvat_dump_cli_command(
        base_command: str, target_zip_path: str, task_info: CVATTaskInfoConfig
    ) -> str:

        return (
            f"{base_command} dump "
            f"{task_info.task_ID} "
            f"{target_zip_path} "
            f"--format '{task_info.annotation_format}'"
        )

    @staticmethod
    def __extract_and_copy_annotations_to_data_dir(
        target_zip_path: str,
        zip_extract_dir: str,
        dataset_dir: str,
    ) -> None:

        if not os.path.isdir(dataset_dir):
            logger.warning(
                "Path to dataset_dir='%s' does not exist! "
                "Skip the extraction and move of annotation data.",
                dataset_dir,
            )
            return

        extract_zip_data(zip_path=target_zip_path, zip_extract_dir=zip_extract_dir)

        zip_annotation_dir = os.path.join(zip_extract_dir, "Annotations")

        annotation_file_paths = get_file_list(
            input_dir=zip_extract_dir, search_subfolders=True, file_extension=".xml"
        )

        for annotation_path in annotation_file_paths:

            dataset_annotation_path = annotation_path.replace(
                zip_annotation_dir, dataset_dir
            )

            ensure_dir(file_path=dataset_annotation_path, verbose=True)

            logger.debug(
                "Copy annotation '%s' to zip '%s'",
                annotation_path,
                dataset_annotation_path,
            )

            shutil.copy(src=annotation_path, dst=dataset_annotation_path)
