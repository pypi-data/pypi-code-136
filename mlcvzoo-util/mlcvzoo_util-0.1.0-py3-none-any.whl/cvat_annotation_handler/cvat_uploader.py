# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for handling the upload of zip files to CVAT via their commandline interface"""

import logging
import os
import zipfile
from typing import Dict

import yaml
from mlcvzoo_base.utils import ensure_dir, get_file_list
from related import to_yaml

from mlcvzoo_util.cvat_annotation_handler.configuration import (
    CVATCLIConfig,
    CVATTaskInfoConfig,
    CVATTaskUploadConfig,
)
from mlcvzoo_util.cvat_annotation_handler.utils import run_command_in_process

logger = logging.getLogger(__name__)


class PascalVOCUploader:
    """
    Class for handling the upload of zip files to CVAT via their commandline-interface
    """

    @staticmethod
    def upload_task_data(
        upload_task_config: CVATTaskUploadConfig,
        cvat_cli_config: CVATCLIConfig,
        disable_ssl_verify: bool = False,
    ) -> None:
        """
        Execute the upload of a single zip file to the CVAT instance

        Args:
            upload_task_config: Configuration of the task that is to be uploaded
            cvat_cli_config: Basis configuration that is needed for the communication between
                             the commandline-interface and CVAT
            disable_ssl_verify: Whether to allow uncertified https connections

        Returns:
            None
        """

        logger.info(
            "\n========== UPLOAD TASK ==========\n" "Task config: \n" "'''\n%s'''\n",
            to_yaml(
                upload_task_config,
                yaml_package=yaml,
                dumper_cls=yaml.Dumper,
            ),
        )

        if upload_task_config.use_prediction_data:
            target_zip_path = PascalVOCUploader.write_upload_zip_file(
                upload_task_config=upload_task_config
            )
        else:
            target_zip_path = upload_task_config.source_zip_path
            upload_task_config.target_zip_path = target_zip_path

        if upload_task_config.execute_upload:
            PascalVOCUploader.call_cvat_upload_via_cli(
                cvat_cli_config=cvat_cli_config,
                target_zip_path=target_zip_path,
                task_info=upload_task_config.task_info,
                disable_ssl_verify=disable_ssl_verify,
            )

        if upload_task_config.clean_up_upload_data:
            PascalVOCUploader.__post_clean_up(
                source_zip_path=upload_task_config.source_zip_path,
                target_zip_path=target_zip_path,
            )

    @staticmethod
    def __post_clean_up(source_zip_path: str, target_zip_path: str) -> None:
        if os.path.isfile(source_zip_path):
            logger.info("(UPLOAD) Clean up dump zip file: '%s'", source_zip_path)
            os.remove(source_zip_path)

        if os.path.isfile(target_zip_path):
            logger.info("(UPLOAD) Clean up upload zip file: '%s'", target_zip_path)
            os.remove(target_zip_path)

    @staticmethod
    def call_cvat_upload_via_cli(
        cvat_cli_config: CVATCLIConfig,
        target_zip_path: str,
        task_info: CVATTaskInfoConfig,
        disable_ssl_verify: bool = False,
    ) -> None:
        """
        Upload a zip file to CVAT.

        Args:
            cvat_cli_config: Basis configuration that is needed for the communication between
                             the commandline-interface and CVAT
            target_zip_path: The zip file to upload
            task_info: Configuration for the specific task
            disable_ssl_verify: Whether to allow uncertified https connections

        Returns:
            None
        """

        # ================================
        # UPLOAD TASK DATA
        command = PascalVOCUploader.__create_cvat_upload_cli_command(
            base_command=cvat_cli_config.create_base_command_string(),
            target_zip_path=target_zip_path,
            task_info=task_info,
        )
        logger.info(
            "Upload annotation data: Task-ID=%s, " "zip-path=%s",
            task_info.task_ID,
            target_zip_path,
        )
        return_code = run_command_in_process(
            command=command, disable_ssl_verify=disable_ssl_verify
        )

        if return_code != 0:
            raise ValueError(f"Upload did not succeed, return-code={return_code}")

    @staticmethod
    def __create_cvat_upload_cli_command(
        base_command: str, target_zip_path: str, task_info: CVATTaskInfoConfig
    ) -> str:

        return (
            f"{base_command} upload "
            f"{task_info.task_ID} "
            f"{target_zip_path} "
            f"--format '{task_info.annotation_format}'"
        )

    @staticmethod
    def write_upload_zip_file(upload_task_config: CVATTaskUploadConfig) -> str:
        """
        Create a zip file based on generated PASCAL-VOC xml files,
        that can be uploaded to a CVAT instance.

        Args:
            upload_task_config: Configuration that states where to find the prediction data
                                and where the zip file should be saved

        Returns:
            The path to the zip file that has been written to disk
        """

        # Generate path to the zip-file which should be uploaded to CVAT
        if upload_task_config.target_zip_path == "":
            target_zip_path = upload_task_config.source_zip_path.replace(
                ".zip", "_upload.zip"
            )
        else:
            target_zip_path = upload_task_config.target_zip_path

        # CLEAN UP old upload zip-file
        if os.path.isfile(target_zip_path):
            logger.info("(UPLOAD) Clean up zip file: '%s'", target_zip_path)
            os.remove(target_zip_path)

        return PascalVOCUploader.__write_prediction_data_to_zip(
            source_zip_path=upload_task_config.source_zip_path,
            target_zip_path=target_zip_path,
            prediction_data_dir=upload_task_config.prediction_data_dir,
        )

    @staticmethod
    def __write_prediction_data_to_zip(
        source_zip_path: str, target_zip_path: str, prediction_data_dir: str
    ) -> str:

        if not os.path.isdir(prediction_data_dir):
            raise ValueError(
                f"prediction_data_dir='{prediction_data_dir}' does not exist! "
                "Please specify a directory in order to generate"
                "a prediction zip file for the upload to CVAT!"
            )

        # Open zip-file to write data which will be uploaded to the CVAT task
        ensure_dir(file_path=target_zip_path, verbose=True)
        target_zip_file = zipfile.ZipFile(  # pylint: disable=consider-using-with
            target_zip_path, "w"
        )

        # Open original zip file to read content that shouldbe copied
        source_zip_file = zipfile.ZipFile(
            source_zip_path
        )  # pylint: disable=consider-using-with
        original_zip_paths = zipfile.ZipFile.namelist(source_zip_file)
        for file_path in original_zip_paths:
            # Copy the 'labelmap.txt' of the original zip file to the one
            # that is uploaded
            if file_path == "labelmap.txt":
                target_zip_file.writestr(
                    zinfo_or_arcname="labelmap.txt",
                    data=source_zip_file.read("labelmap.txt"),
                )

            # Copy every file of the 'ImageSets' folder of the original zip file,
            # to the zip file that is uploaded
            if file_path.split("/")[0] == "ImageSets":
                target_zip_file.writestr(
                    zinfo_or_arcname=file_path, data=source_zip_file.read(file_path)
                )

        # NOTE:
        # - The annotations are defined in the download cvat zip file
        # - Therefore it is enough to specify a root directory where
        #   all xml files can be parsed from.
        # - The decision which xml files should be put in the upload
        #   zip file, is made on the basis of the information from the
        #   downloaded zip file from "ImageSets/Main/default.txt"
        predicted_xml_paths = get_file_list(
            input_dir=prediction_data_dir,
            file_extension=".xml",
            search_subfolders=True,
        )

        predicted_xml_paths_map: Dict[str, str] = {}
        for predicted_xml_path in predicted_xml_paths:
            predicted_xml_paths_map[
                os.path.basename(predicted_xml_path).replace(".xml", "")
            ] = predicted_xml_path

        # Get all xml paths that are part of the task (represented by the zip)
        annotation_xml_files = (
            source_zip_file.read("ImageSets/Main/default.txt")
            .decode("utf-8")
            .split("\n")
        )

        # Write annotation data to zip-file
        for annotation_xml_path in annotation_xml_files:
            annotation_file_name = os.path.basename(annotation_xml_path)

            if annotation_file_name in predicted_xml_paths_map:

                logger.debug(
                    "Add xml file to upload zip-file: '%s'",
                    predicted_xml_paths_map[annotation_file_name],
                )
                with open(
                    file=predicted_xml_paths_map[annotation_file_name], encoding="utf8"
                ) as prediction_file:
                    target_zip_file.writestr(
                        zinfo_or_arcname=f"Annotations/{annotation_xml_path}.xml",
                        data="".join(prediction_file.readlines()),
                    )

        source_zip_file.close()
        target_zip_file.close()

        logger.info(
            "Generated prediction zip file '%s' for upload to cvat.", target_zip_path
        )

        return target_zip_path
