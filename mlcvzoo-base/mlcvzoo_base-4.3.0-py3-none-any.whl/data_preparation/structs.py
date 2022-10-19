# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for enumerating options of formats"""
from enum import auto

from mlcvzoo_base.configuration.structs import BaseType

try:
    # python3.10
    from enum import StrEnum  # type: ignore
except ImportError:
    from backports.strenum import StrEnum


class CSVOutputStringFormats(BaseType):
    BASE: str = "BASE"
    YOLO: str = "YOLO"


class MOTChallengeFormats(StrEnum):
    MOT15 = auto()
    MOT1617 = auto()
    MOT20 = auto()
