import hashlib
from pathlib import Path
from typing import Callable
import OrcFxAPI as ofx


def data_hash(model: ofx.Model, hash_function: Callable = hashlib.md5) -> str:
    """
    returns a hash of the data of in sim file to avoid running the same sim multiple times on separate machines
    :param model: [OrcFxAPI.Model] orcaflex model
    :param hash_function: [Callable] function to calculate hash, must support ``hexdigest()`` (default=hashlib.md5)
    :return: [str] hash
    """
    yml_data = model.SaveDataMem(ofx.DataFileType.Text)
    clean_yaml = b"\r\n".join(
        filter(
            lambda row: not row.startswith(
                (b"# File:", b"# Created:", b"# User:", b"# Machine")
            ),
            yml_data.split(b"\r\n"),
        )
    )
    return hash_function(clean_yaml).hexdigest()


def data_hash_from_path(ofx_path: Path, hash_function: Callable = hashlib.md5) -> str:
    """
    returns a hash of the data of in sim file to avoid running the same sim multiple times on separate machines
    :param ofx_path: [pathlib.Path] path to a sim or data file
    :param hash_function: [Callable] function to calculate hash, must support ``hexdigest()`` (default=hashlib.md5)
    :return: [str] hash
    """
    m = ofx.Model(ofx_path, threadCount=1)
    return data_hash(model=m, hash_function=hash_function)
