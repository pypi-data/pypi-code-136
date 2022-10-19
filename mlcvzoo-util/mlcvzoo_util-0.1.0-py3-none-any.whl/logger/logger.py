# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for handling python logging"""

import logging
import os
import re
import sys
from datetime import datetime
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
from sys import stdout
from typing import List, Optional, Union

from mlcvzoo_base.utils import ensure_dir

logger = logging.getLogger(__name__)


class Logger:
    """Class for initializing python logging"""

    is_instantiated: bool = False

    log_handlers: List[Union[TimedRotatingFileHandler, StreamHandler]] = []  # type: ignore

    @staticmethod
    def init_logging_basic(
        log_dir: Optional[str] = None,
        log_file_postfix: Optional[str] = None,
        no_stdout: bool = False,
        root_log_level: Union[str, int] = logging.INFO,
    ) -> None:
        """
        Initializes the python logging. Per default only logging to stdout is used.
        When a log_dir is given, also an TimedRotatingFileHandler is added

        Args:
            log_dir: String, directory where the log-file is about to be stored
            log_file_postfix: String, postfix of log-file
            no_stdout: Bool, whether a standard output should be done
            root_log_level: String or int, defines root logging level

        Returns:
            None
        """

        root_log_level = Logger.get_log_level(log_level=root_log_level)

        if not Logger.is_instantiated:
            if log_dir is not None:
                if log_file_postfix is not None:
                    log_file_name = (
                        f"{log_file_postfix}_"
                        f"{datetime.now().strftime('%Y-%m-%dT_%H-%M')}.log"
                    )
                else:
                    log_file_name = (
                        f"log_{datetime.now().strftime('%Y-%m-%dT_%H-%M')}.log"
                    )

                log_file_path = os.path.join(log_dir, log_file_name)

                ensure_dir(log_file_path, verbose=True)

                time_rotating_file_handler = TimedRotatingFileHandler(
                    filename=log_file_path,
                    when="h",
                    interval=6,
                )
                time_rotating_file_handler.suffix = "%Y-%m-%d_%H.log"
                time_rotating_file_handler.extMatch = re.compile(
                    r"^\d{4}-\d{2}-\d{2}_\d{2}(\.\w+)?\.log$", re.ASCII
                )

                Logger.log_handlers.append(time_rotating_file_handler)

            if not no_stdout:
                stdout_handler = StreamHandler(stream=stdout)
                Logger.log_handlers.append(stdout_handler)

            logging.basicConfig(
                level=root_log_level,
                format="%(asctime)s %(levelname)-7.7s: "
                "[%(name)-30.30s]"
                "[%(threadName)-11.11s]"
                "[%(funcName)s():%(lineno)s] "
                "%(message)s",
                handlers=Logger.log_handlers,
            )

            Logger.is_instantiated = True
        else:
            logger.warning(
                "Logger has already been instantiated. "
                "Another call won't have any effect",
            )

    @staticmethod
    def get_log_level(log_level: Optional[Union[str, int]]) -> Union[str, int]:
        """
        Matches the correct python logging level for the
        given log_level.

        Args:
            log_level: The log level to match

        Returns:
            The matched logging level
        """
        if log_level is None:
            return logging.INFO

        _log_level = logging.getLevelName(log_level)

        if isinstance(_log_level, str) and "Level " in _log_level:
            return logging.INFO

        return _log_level  # type: ignore
