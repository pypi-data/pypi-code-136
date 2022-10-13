# -*- coding: UTF-8 -*-

from os import makedirs
from os.path import dirname, realpath, exists


def ensure_folder(path: str):
    """
    Read the file path and recursively create the folder structure if needed.
    """
    folder_path: str = dirname(realpath(path))
    try:
        make_dirs(folder_path)
    except FileExistsError:
        pass


def make_dirs(path: str):
    """Checks if a folder path exists and create one if not."""
    if not exists(path):
        makedirs(path)


def folder(value: str) -> str:
    """
    Return `value` as path and recursively
    create the folder structure if needed.
    """
    value: str = realpath(value)
    make_dirs(value)
    return value


def file(value: str) -> str:
    """
    Return `value` as path and recursively
    create the folder structure if needed.
    """
    value: str = realpath(value)
    ensure_folder(value)
    return value
