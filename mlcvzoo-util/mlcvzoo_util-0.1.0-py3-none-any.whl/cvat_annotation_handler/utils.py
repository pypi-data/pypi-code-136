# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for storing utility functions that are needed for the cvat_annotation_handler package"""

import logging
import os
import shlex
import subprocess
import sys

logger = logging.getLogger(__name__)


def run_command_in_process(command: str, disable_ssl_verify: bool = False) -> int:
    """
    Run the CVAT commandline-interface in subprocess

    Args:
        command: The concrete command to be executed
        disable_ssl_verify: Whether to allow uncertified https connections

    Returns:

    """
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(sys.path)
    env["PYTHONPATH"] += os.pathsep + os.getcwd()

    if disable_ssl_verify:
        env["CURL_CA_BUNDLE"] = ""

    logger.info(f"Run command: {command}")

    result = subprocess.run(shlex.split(command), env=env)
    logger.info(f"Executed command: {command}, result.returncode: {result.returncode}")

    return result.returncode
