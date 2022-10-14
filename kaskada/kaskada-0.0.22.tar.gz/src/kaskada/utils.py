"""
Copyright (C) 2021 Kaskada Inc. All rights reserved.

This package cannot be used, copied or distributed without the express
written permission of Kaskada Inc.

For licensing inquiries, please contact us at info@kaskada.com.
"""

import datetime
from typing import Union
from google.protobuf.timestamp_pb2 import Timestamp
import unicodedata
import re


def normalize_col_name(column: str) -> str:
    """
    Normalize column name by replacing invalid characters with underscore
    strips accents and make lowercase
    """
    n = re.sub(r"[ ,;{}()\n\t=]+", "_", column.lower())
    return unicodedata.normalize("NFKD", n).encode("ASCII", "ignore").decode()


def get_timestamp(time: Union[str, datetime.datetime, None]):
    timestamp = None
    if isinstance(time, str):
        timestamp = Timestamp()
        timestamp.FromJsonString(time)
    elif isinstance(time, datetime.datetime):
        timestamp = Timestamp()
        timestamp.FromDatetime(time)
    elif time is not None:
        raise Exception(
            "Invalid type for timestamp. Expected `str` or `datetime.datetime`."
        )
    return timestamp
