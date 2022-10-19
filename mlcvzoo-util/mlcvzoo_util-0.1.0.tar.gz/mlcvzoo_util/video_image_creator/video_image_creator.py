# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for extracting frames from videos. In the context of the mlcvzoo, this
is used to build training datasets.
"""

import argparse
import copy
import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional, cast

import cv2
import numpy as np
from config_builder import ConfigBuilder
from mlcvzoo_base.utils.file_utils import ensure_dir, get_file_list

from mlcvzoo_util.logger import Logger
from mlcvzoo_util.mlcvzoo_cli_tool import MLCVZooCLITool
from mlcvzoo_util.video_image_creator.configuration import VideoImageCreatorConfig

logger = logging.getLogger(__name__)


class VideoImageCreator(MLCVZooCLITool[VideoImageCreatorConfig]):

    """
    Tool to step through video and manually sort out frames to use as training data.
    When executed, displays every frame in given video separately. User is able to
    execute following commands:
    - Exit: 'q', 'Q', 'Esc'
    - Save current frame as .jpg: 's'
    - Change step size: '1' for 1 step, '2' for step, ...

    (See ./config/templates/tools/video-image-creator_template.yaml for example)
    """

    MODES: List[str] = ["terminate", "run"]

    def __init__(
        self,
        configuration: VideoImageCreatorConfig,
    ) -> None:
        self.video_files: List[str] = []

        self.current_pos: int = 0
        self.current_frame: Optional[np.ndarray] = None  # type: ignore[type-arg]
        self.current_video_capture: Optional[cv2.VideoCapture] = None
        self.current_video_path: Optional[str] = None

        self.configuration: VideoImageCreatorConfig = configuration

        self.step_width_map: Dict[int, int] = {}
        for key in self.configuration.step_width_map.keys():
            self.step_width_map[ord(key)] = self.configuration.step_width_map[key]

        self.mode = "run"
        self.frame = 0
        self.resized_window = False
        self.step_width = 1

        cv2.namedWindow(self.configuration.winname, cv2.WINDOW_NORMAL)

        self.video_files = []
        if os.path.isdir(self.configuration.video_input_dir):
            self.video_files.extend(
                get_file_list(
                    input_dir=self.configuration.video_input_dir,
                    search_subfolders=True,
                    file_extension=self.configuration.video_file_extension,
                )
            )
        elif os.path.isfile(self.configuration.video_input_path):
            self.video_files.append(self.configuration.video_input_path)
        else:
            logger.error(
                "Could not init a video file. Please provide a correct parameter for "
                " 'video_input_dir' or 'video_input_path'"
            )

        if len(self.video_files) == 0:
            raise ValueError("No videos found for the given configuration!")
        else:
            logger.info("Input Video: ")
            self.__print_videos()

    @staticmethod
    def create_configuration(
        yaml_config_path: str,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> VideoImageCreatorConfig:
        """
        Create a VideoImageCreatorConfig

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
            VideoImageCreatorConfig,
            ConfigBuilder(
                class_type=VideoImageCreatorConfig,
                yaml_config_path=yaml_config_path,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
            ).configuration,
        )

    @staticmethod
    def create_cli_configuration(
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> VideoImageCreatorConfig:
        """
        Create a VideoImageCreatorConfig

        Args:
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
        Returns:
            The created configuration
        """

        return MLCVZooCLITool._create_cli_configuration(
            configuration_class=VideoImageCreatorConfig,
            string_replacement_map=string_replacement_map,
            configure_argparse=VideoImageCreator.configure_argparse,
        )

    @staticmethod
    def configure_argparse(
        parser: argparse.ArgumentParser,
    ) -> None:

        MLCVZooCLITool.configure_argparse(parser)

        parser.description = (
            "Tool for generating training images from given video files"
        )

    def __print_videos(self) -> None:

        """
        Prints every video path specified in video_image_creator_yaml
        """
        for video_path in self.video_files:
            logger.info("  - %s", video_path)

    def __output_frame(self, frame: Optional[np.ndarray]) -> bool:  # type: ignore[type-arg]

        """
        Displays current frame incl. information about video name,
        current frame number and video FPS. While displaying frame,
        user can change step size according to step_width_map provided
        in video_image_creator_config_yaml. Also, user can save the current
        frame as single .jpg by pressing 's'

        Args:
            frame: N-dimensional Array representing single frame of video

        Returns:
            modified_value: Boolean which indicates if step size has changed

        """

        modified_value = False

        if (
            self.current_video_path is not None
            and self.current_video_capture is not None
            and frame is not None
        ):

            output_frame = copy.deepcopy(frame)

            # will only be executed once
            if not self.resized_window:
                scale_factor = frame.shape[1] / frame.shape[0]

                if self.configuration.resize_window is True:
                    window_height = self.configuration.window_size
                else:
                    window_height = frame.shape[0]

                cv2.resizeWindow(
                    winname=self.configuration.winname,
                    height=window_height,
                    width=int(window_height * scale_factor),
                )

                self.resized_window = True

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Video: {os.path.basename(self.current_video_path)}",
                org=(20, 40),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Current frame number: {self.current_pos}/"
                f"{self.current_video_capture.get(cv2.CAP_PROP_FRAME_COUNT)}",
                org=(20, 80),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            output_frame = cv2.putText(
                img=output_frame,
                text=f"Video FPS: {self.current_video_capture.get(cv2.CAP_PROP_FPS)}",
                org=(20, 120),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(0, 0, 0),
                thickness=3,
                lineType=cv2.LINE_AA,
            )

            cv2.imshow(self.configuration.winname, output_frame)

            key = cv2.waitKey(0) & 0xFF
            if key in self.step_width_map.keys():
                logger.info("set step-width to %s", self.step_width_map[key])
                self.step_width = self.step_width_map[key]

                modified_value = True

            elif key == 27 or key == ord("q") or key == ord("Q"):
                self.close()
            elif key == ord("s"):
                logger.info("save image ...")
                self.__write_frame(frame=frame)
            else:
                logger.info("next image...")

            self.frame += 1

            del output_frame

        return modified_value

    def __write_frame(self, frame: Optional[np.ndarray]) -> None:  # type: ignore[type-arg]

        """
        Saves given frame as .jpg to same directory as input video

        Args:
            frame: N-dimensional Array representing single frame of video

        Returns:
            None
        """

        if (
            frame is not None
            and self.current_video_path is not None
            and self.current_video_capture is not None
        ):

            video_fps = self.current_video_capture.get(cv2.CAP_PROP_FPS)
            video_pos = self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES)

            timestamp = datetime.utcfromtimestamp(1 / video_fps * video_pos).strftime(
                "%H-%M-%S-%f"
            )

            video_name_base = os.path.basename(self.current_video_path).replace(
                self.configuration.video_file_extension, ""
            )

            output_path = os.path.join(
                os.path.dirname(self.current_video_path),
                video_name_base,
                f"{video_name_base}_{timestamp}.jpg",
            )

            if not os.path.isfile(output_path):
                ensure_dir(file_path=output_path, verbose=True)

                logger.info("Write image to %s", output_path)
                cv2.imwrite(output_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            else:
                logger.info("Image already exist at %s", output_path)

    def __reset(self) -> None:
        """
        Closes current video and resets current_video variables to None
        """

        if self.current_video_capture is not None:
            self.current_video_capture.release()

        self.current_video_capture = None
        self.current_video_path = None

        logger.info("Reset video. Videos left: ")
        self.__print_videos()

    def run(self) -> None:
        """
        Wrapper function for executing the video_image_creator
        """

        modified_value = False

        logger.info(
            "Press 'Esc', 'q' or 'Q' to exit.\n"
            "Press 's' for saving current frame.\n"
            "step_width_map: \n"
            "%s\n"
            "Press any other key to step through video.",
            json.dumps(obj=self.step_width_map, indent=2),
        )
        while self.mode != "terminate":

            if self.current_video_capture is None:
                if len(self.video_files) == 0:
                    self.mode = "terminate"
                    break
                else:
                    self.current_video_path = self.video_files.pop()

                    logger.info("Start with video %s", self.current_video_path)
                    self.current_video_capture = cv2.VideoCapture(
                        self.current_video_path
                    )

            if not modified_value:
                self.current_pos = (
                    self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES)
                    + self.step_width
                    - 1
                )
                self.goto_frame(frame_position=self.current_pos)

                logger.info(
                    "Read frame at position: %s",
                    self.current_video_capture.get(cv2.CAP_PROP_POS_FRAMES),
                )
                read, self.current_frame = self.current_video_capture.read()

                if not read:
                    logger.info("Video finished. Read new video ...")
                    self.__reset()
                    continue
            else:
                logger.info("stay at pos")

            modified_value = self.__output_frame(frame=self.current_frame)

    def goto_frame(self, frame_position: int) -> None:
        """
        Takes integer specifying which frame should be displayed
        next and sets the frame accordingly.

        Args:
            frame_position: Integer specifying which frame_position to be set next

        Returns:
            None
        """

        if self.current_video_capture is not None:
            frame_position = max(0, frame_position)

            logger.info("set frame position to %s", frame_position)
            self.current_video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_position)

    def __del__(self):  # type: ignore
        if self.current_video_capture is not None:
            self.current_video_capture.release()

    def close(self) -> None:

        """
        Destroys the current window
        """

        self.mode = "terminate"
        cv2.destroyAllWindows()


def main() -> None:
    """
    Entry point when using the video-image-creator command line tool.
    (See [tool.poetry.scripts] section in pyproject.toml)
    """

    args = ConfigBuilder.setup_argparse(
        configure_argparse=VideoImageCreator.configure_argparse
    ).parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="VideoImageCreator",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    video_image_creator = VideoImageCreator(
        configuration=VideoImageCreator.create_cli_configuration()
    )
    video_image_creator.run()


if __name__ == "__main__":
    main()
