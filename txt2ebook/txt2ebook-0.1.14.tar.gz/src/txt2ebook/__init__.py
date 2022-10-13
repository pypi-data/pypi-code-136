# Copyright (C) 2021,2022 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Common shared functions."""

import argparse
import logging
import sys

logger = logging.getLogger(__name__)

__version__ = "0.1.14"


def setup_logger(config: argparse.Namespace) -> None:
    """Configure the global logger.

    Args:
        config(argparse.Namespace): Config that contains arguments
    """
    logformat = {
        True: "%(levelname)5s: %(message)s",
        False: "%(message)s",
    }

    logging.basicConfig(
        level=config.debug and logging.DEBUG or logging.INFO,
        stream=sys.stdout,
        format=logformat[config.debug],
        datefmt="%Y-%m-%d %H:%M:%S",
    )
