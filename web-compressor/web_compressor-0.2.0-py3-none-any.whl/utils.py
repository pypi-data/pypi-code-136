"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

import mimetypes
from pathlib import Path
import sys
from typing import Union


def is_loaded(targets: Union[list, str]) -> bool:
    """
    Determine wether module(s) has/have been loaded

    :param targets: list | str Single module or list thereof
    :return: bool Loading status
    """

    if isinstance(targets, str):
        targets = [targets]

    for target in targets:
        status = False

        for module in sys.modules:
            if target == module.split(".")[0]:
                status = True
                break

        if not status:
            return False

    return True


def append2file(file: Path, part: str) -> Path:
    """
    Appends string to filename (right before its extension)

    :param file: pathlib.Path Original file
    :param part: str String to be appended
    :return: pathlib.Path Target file
    """

    return Path(file.parents[0], f"{file.stem}.{part}{file.suffix}")


def get_mime(filename: str) -> Union[str, None]:
    """
    Guesses MIME type from filename

    :param filename: str
    :return: str | None
    """

    return mimetypes.guess_type(filename)[0]


def read_file(data_file: Path) -> bytes:
    """
    Reads file contents

    :param data_file: pathlib.Path Path to file
    :return: bytes File contents
    """

    # Create data array
    data = bytes()

    # Determine buffer size
    bufsize = 65536  # 2^16 or 64KiB

    # For more information,
    # see https://stackoverflow.com/a/66285848
    # Read file ..
    with data_file.open("rb") as file:
        # .. one chunk at a time ..
        while chunk := file.read(bufsize):
            # .. update hash
            data += chunk

    return data
