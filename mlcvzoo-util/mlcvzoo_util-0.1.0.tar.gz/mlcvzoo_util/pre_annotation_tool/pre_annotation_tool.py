# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for handling the generation and uploading of annotations to CVAT, which realizes that
the feature of pre-annotating annotation tasks
"""

import argparse
import logging
import os
import zipfile
from typing import Any, Dict, List, Optional, Tuple, Type, cast

import cv2
from config_builder import ConfigBuilder
from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.model import Model, ObjectDetectionModel
from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.data_preparation.utils import annotation_to_xml
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.utils import draw_on_image, generate_detector_colors
from mlcvzoo_base.utils.file_utils import get_basename, get_file_list
from tqdm import tqdm

from mlcvzoo_util.cvat_annotation_handler.cvat_annotation_handler import (
    CVATAnnotationHandler,
)
from mlcvzoo_util.image_io_utils import VideoLiveOutput
from mlcvzoo_util.logger import Logger
from mlcvzoo_util.mlcvzoo_cli_tool import (
    DictAction,
    MLCVZooCLITool,
    configure_model_argparse,
)
from mlcvzoo_util.pre_annotation_tool.configuration import PreAnnotateCVATConfig

logger = logging.getLogger(__name__)


class PreAnnotationTool(MLCVZooCLITool[PreAnnotateCVATConfig]):
    """
    Tool that generates predictions and uploads these to CVAT as initialization for new tasks
    """

    def __init__(self, configuration: PreAnnotateCVATConfig):
        """
        Instantiates a PreAnnotationTool object

        Args:
            configuration: The configuration for the PreAnnotationTool
        """

        self.configuration: PreAnnotateCVATConfig = configuration

        self.video_live_output: Optional[VideoLiveOutput] = None

    @staticmethod
    def create_configuration(
        yaml_config_path: str,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> PreAnnotateCVATConfig:
        """
        Create a PreAnnotateCVATConfig

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
            PreAnnotateCVATConfig,
            ConfigBuilder(
                class_type=PreAnnotateCVATConfig,
                yaml_config_path=yaml_config_path,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
            ).configuration,
        )

    @staticmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> PreAnnotateCVATConfig:
        """
        Create a PreAnnotateCVATConfig

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """

        return MLCVZooCLITool._create_cli_configuration(
            configuration_class=PreAnnotateCVATConfig,
            string_replacement_map=string_replacement_map,
            configure_argparse=PreAnnotationTool.configure_argparse,
        )

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:
        parser.description = (
            "Generate predictions and upload these to "
            "CVAT as initialization for new tasks"
        )
        MLCVZooCLITool.configure_argparse(parser)
        configure_model_argparse(parser=parser)

    @staticmethod
    def create_model(
        model_config: ModelConfig,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> ObjectDetectionModel:  # type: ignore[type-arg]
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
        object_detection_model: Model = ModelRegistry().init_model(  # type: ignore[type-arg]
            model_config=model_config, string_replacement_map=string_replacement_map
        )

        if not isinstance(object_detection_model, ObjectDetectionModel):
            raise ValueError(
                "This evaluation can only be used with models that "
                "inherit from 'mlcvzoo.api.model.ObjectDetectionModel'"
            )

        return object_detection_model

    def __gather_image_paths(self) -> List[str]:

        image_paths: List[str] = []

        disk_image_file_map: Dict[str, str] = {}

        input_image_types = self.configuration.input_image_type.split("|")

        input_image_paths: List[str] = []
        for input_image_type in input_image_types:
            input_image_paths.extend(
                get_file_list(
                    input_dir=self.configuration.root_image_dir,
                    search_subfolders=True,
                    file_extension=input_image_type,
                )
            )

        for image_path in input_image_paths:
            disk_image_file_map[get_basename(image_path)] = image_path

        for (
            dump_task_config
        ) in self.configuration.cvat_annotation_handler_config.dump_task_configs:
            source_zip_file = zipfile.ZipFile(dump_task_config.target_zip_path)

            logger.debug("Get image paths from '%s'" % dump_task_config.target_zip_path)

            task_image_paths = (
                source_zip_file.read("ImageSets/Main/default.txt")
                .decode("utf-8")
                .split("\n")
            )

            for task_image_path in task_image_paths:
                task_image_basename = get_basename(task_image_path)
                if task_image_basename in disk_image_file_map:
                    image_paths.append(disk_image_file_map[task_image_basename])

        logger.debug("Gathered '%s' image paths for prediction." % len(image_paths))

        return image_paths

    def generate_annotations(self) -> None:
        """
        Generate PASCAL-VOC annotations using the configured model and
        store these annotations at the configured location

        Returns:
            None
        """

        object_detection_model: ObjectDetectionModel = PreAnnotationTool.create_model(  # type: ignore[type-arg]
            model_config=self.configuration.model_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        image_paths: List[str] = self.__gather_image_paths()

        process_bar = tqdm(image_paths, desc="Generate predictions")

        if self.configuration.show_predictions:
            self.video_live_output = VideoLiveOutput(mode=VideoLiveOutput.MODE_STEP)

        rgb_colors: List[Tuple[int, int, int]] = []
        if self.video_live_output is not None:
            rgb_colors = generate_detector_colors(
                num_classes=object_detection_model.num_classes
            )

        for image_path in process_bar:

            if (
                self.video_live_output is not None
                and self.video_live_output.is_terminated()
            ):
                break

            image = cv2.imread(image_path)

            predicted_annotation: BaseAnnotation = BaseAnnotation(
                image_path=image_path,
                annotation_path=os.path.join(
                    self.configuration.output_xml_dir, f"{get_basename(image_path)}.xml"
                ),
                image_shape=(image.shape[0], image.shape[1]),
                image_dir="",
                replacement_string="",
                annotation_dir=self.configuration.output_xml_dir,
                classifications=[],
                bounding_boxes=[],
                segmentations=[],
            )

            if not os.path.isfile(predicted_annotation.annotation_path) or (
                os.path.isfile(predicted_annotation.annotation_path)
                and self.configuration.overwrite_existing_annotations
            ):

                # TODO: When ReadFromFile model is supporting images, then switch
                #       to predict on image and not image-path
                _, predicted_bounding_boxes = object_detection_model.predict(
                    data_item=image_path
                )

                logger.info("Predicted bounding boxes: %s" % predicted_bounding_boxes)

                if self.video_live_output is not None:
                    self.video_live_output.output_frame(
                        draw_on_image(
                            frame=image,
                            rgb_colors=rgb_colors,
                            bounding_boxes=predicted_bounding_boxes,
                            thickness=5,
                        )
                    )

                predicted_annotation.bounding_boxes = predicted_bounding_boxes

                annotation_to_xml(
                    annotation=predicted_annotation,
                )

    def run(self) -> None:
        """
        Generate and upload the annotations to the CVAT instance

        1. Download all task information
        2. Parse the image-paths utilizing the information of the downloaded
           tasks
        3. Run the model based on the gathered image paths and generate the
           respective annotation files
        4. Uploaded the annotations to CVAT

        Returns:
            None
        """

        cvat_annotation_handler_instance = CVATAnnotationHandler(
            configuration=self.configuration.cvat_annotation_handler_config
        )

        cvat_annotation_handler_instance.download_all_tasks()

        if self.configuration.generate_annotations:
            self.generate_annotations()

        cvat_annotation_handler_instance.upload_all_tasks()


def main() -> None:
    """
    Entry point when using the mlcvzoo-preannotator command line tool.
    (See [tool.poetry.scripts] section in pyproject.toml)
    """

    args = ConfigBuilder.setup_argparse(
        configure_argparse=PreAnnotationTool.configure_argparse
    ).parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="PreAnnotationTool",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    configuration: PreAnnotateCVATConfig = PreAnnotationTool.create_cli_configuration()

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

    pre_annotation_tool = PreAnnotationTool(configuration=configuration)
    pre_annotation_tool.run()


if __name__ == "__main__":
    main()
