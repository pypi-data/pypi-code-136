# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for defining all configuration classes that
are used in the context of the CVATAnnotationHandler
"""

import logging
import os
import sys
from getpass import getpass
from typing import List, Optional

import related
from config_builder import BaseConfigClass

logger = logging.getLogger(__name__)


@related.mutable(strict=True)
class CVATCLIConfig(BaseConfigClass):
    """
    Configuration class for defining parameters that are needed for
    the CVAT commandline-interface
    """

    cli_path: str = related.StringField()
    server_host: str = related.StringField()
    auth: str = related.StringField()
    disable_ssl_verify: bool = related.BooleanField(required=False, default=False)
    server_port: Optional[int] = related.ChildField(
        cls=int, required=False, default=None
    )
    password_path: Optional[str] = related.ChildField(
        cls=str, required=False, default=None
    )
    python_executable: str = related.StringField(required=False, default=sys.executable)

    def create_base_command_string(self) -> str:
        """
        Create the base string that is needed to call the CVAT commandline-interface

        Returns:
            The created string
        """
        auth: str = self.auth

        if ":" not in auth:
            if self.password_path is not None:
                if os.path.isfile(self.password_path):
                    with open(self.password_path, "r") as password_file:
                        password = password_file.readline().strip()

                        auth = f"{self.auth}:{password}"
                else:
                    if self.password_path != "":
                        logger.warning(
                            "The provided password-path does not exists! "
                            "Therefore, only the provided cvat_cli_config.auth config attribute "
                            "will be used! password_path: '%s'" % self.password_path
                        )
            else:
                logger.info(
                    "Neither a password is given in the auth parameter, nor a "
                    "password file is given, please enter the password"
                )
                password = getpass()
                auth = f"{auth}:{password}"

        if self.server_port is not None:
            base_command = f"%s %s --server-host %s --server-port %s --auth %s" % (
                self.python_executable,
                self.cli_path,
                self.server_host,
                self.server_port,
                auth,
            )
        else:
            base_command = "%s %s --server-host %s --auth %s" % (
                self.python_executable,
                self.cli_path,
                self.server_host,
                auth,
            )

        return base_command


@related.mutable(strict=True)
class CVATTaskInfoConfig(BaseConfigClass):
    """
    Configuration class that defines attributes that are specific for
    a CVAT task
    """

    VALID_FORMATS = [
        "COCO 1.0",
        "CVAT for images 1.1",
        "CVAT for video 1.1",
        "Datumaro 1.0",
        "LabelMe 3.0",
        "MOT 1.1",
        "MOTS PNG 1.0",
        "PASCAL VOC 1.1",
        "Segmentation mask 1.1",
        "TFRecord 1.0",
        "YOLO 1.1",
        "ImageNet 1.0",
        "CamVid 1.0",
    ]

    task_ID: int = related.IntegerField()
    annotation_format: str = related.StringField(
        required=False, default="PASCAL VOC 1.1"
    )

    def check_values(self) -> bool:
        return self.annotation_format in self.VALID_FORMATS


@related.mutable(strict=True)
class CVATTaskDumpConfig(BaseConfigClass):
    """
    Configuration class that defines attributes that are specific for a
    dump of a CVAT task.
    """

    task_info: CVATTaskInfoConfig = related.ChildField(cls=CVATTaskInfoConfig)

    # if value is empty, the task will be downloaded to a tmp-file
    target_zip_path: str = related.StringField(required=False, default="")

    # Whether to extract or not the data of the downloaded zip file.
    # The data is extracted to the directory with the base-name of the "target_zip_path"
    extract_data: bool = related.BooleanField(required=False, default=True)

    zip_extract_dir: str = related.StringField(required=False, default="")

    move_extracted_data_to_dataset_dir: bool = related.BooleanField(
        required=False, default=False
    )

    # directory where the xml-files of the downloaded zip-file should be copied to,
    # in order to generate an overall directory for tasks which share the same directory-tree
    # NOTE: this will trigger the extraction of the downloaded zip-file
    dataset_dir: str = related.StringField(required=False, default="")

    # whether to use trigger an new download of a zip-file or to use an already
    # existing zip-file (when it exists)
    overwrite_existing_zip: bool = related.BooleanField(required=False, default=False)

    # delete all generated files during the dumping-routine of this CVAT task
    clean_up_dump_data: bool = related.BooleanField(required=False, default=False)


@related.mutable(strict=True)
class CVATTaskUploadConfig(BaseConfigClass):
    """
    Configuration class that defines attributes that are specific for an
    upload of a CVAT task.
    """

    task_info: CVATTaskInfoConfig = related.ChildField(cls=CVATTaskInfoConfig)

    execute_upload: bool = related.BooleanField()

    # is required because the information of "labelmap.txt" and "Main/default.txt" has to
    # be known for creating a zip-file which can be uploaded.
    source_zip_path: str = related.StringField()

    # whether to use the annotations from the dumped zip-file
    # or to use the annotations provided in the "prediction_data_dir"
    use_prediction_data: bool = related.BooleanField()

    # directory where generated annotations are stored
    prediction_data_dir: str = related.StringField(required=False, default="")

    # by default the "source_zip_path" is used with an "_upload" extension
    # This path defines the location for the zip-file which will be uploaded to the CVAT task
    target_zip_path: str = related.StringField(required=False, default="")

    # delete all generated files during the dumping-routine of this CVAT task
    clean_up_dump_data: bool = related.BooleanField(required=False, default=False)

    # delete all generated files during the uploaded-routine of this CVAT task
    clean_up_upload_data: bool = related.BooleanField(required=False, default=False)


@related.mutable(strict=False)
class CVATAnnotationHandlerConfig(BaseConfigClass):
    """
    Central configuration class for the CVATAnnotationHandler
    """

    cvat_cli_config: CVATCLIConfig = related.ChildField(cls=CVATCLIConfig)

    execute_tasks_separately: bool = related.BooleanField(required=False, default=True)

    dump_task_configs: List[CVATTaskDumpConfig] = related.SequenceField(
        cls=CVATTaskDumpConfig, required=False, default=[]
    )
    upload_task_configs: List[CVATTaskUploadConfig] = related.SequenceField(
        cls=CVATTaskUploadConfig, required=False, default=[]
    )
