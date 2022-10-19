# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for configuring the parsing of information from yaml in python
accessible attributes for extracting frames from videos
"""
from typing import Dict

import related
from config_builder import BaseConfigClass


@related.mutable(strict=True)
class VideoImageCreatorConfig(BaseConfigClass):
    """Class for parsing information for video image creator tool"""

    default_step_width_map: Dict[str, int] = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": -1,
        "7": -2,
        "8": -3,
        "9": -4,
        "0": -5,
    }

    step_width_map: Dict[str, int] = related.ChildField(
        cls=dict, default=default_step_width_map
    )

    video_file_extension: str = related.StringField(default=".mp4")

    video_input_dir: str = related.StringField(default="")

    video_input_path: str = related.StringField(default="")

    winname: str = related.StringField(default="VideoImageCreator")

    window_size: int = related.IntegerField(default=500)
    resize_window: bool = related.BooleanField(default=True)
