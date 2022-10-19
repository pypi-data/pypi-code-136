# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for configuring the parsing of information from yaml in python
accessible attributes for the PreAnnotationTool class
"""

import related
from config_builder import BaseConfigClass
from mlcvzoo_base.configuration.model_config import ModelConfig
from mlcvzoo_base.configuration.structs import OpenCVImageFormats

from mlcvzoo_util.cvat_annotation_handler.configuration import (
    CVATAnnotationHandlerConfig,
)


@related.mutable(strict=False)
class PreAnnotateCVATConfig(BaseConfigClass):
    """
    Main configuration class for the PreAnnotationTool
    """

    model_config: ModelConfig = related.ChildField(cls=ModelConfig)

    cvat_annotation_handler_config: CVATAnnotationHandlerConfig = related.ChildField(
        cls=CVATAnnotationHandlerConfig
    )

    root_image_dir: str = related.StringField()
    input_image_type: str = related.StringField()
    output_xml_dir: str = related.StringField()

    generate_annotations: bool = related.BooleanField()
    overwrite_existing_annotations: bool = related.BooleanField()

    show_predictions: bool = related.BooleanField(required=False, default=False)

    def check_values(self) -> bool:
        return True
