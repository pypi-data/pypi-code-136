""" Sensospot Data Parser

Parsing the numerical output from Sensovations Sensospot image analysis.
"""

import pathlib
from typing import Tuple, Union, Iterable, Optional

import numpy
import pandas
from defusedxml import ElementTree

from . import columns

PathLike = Union[str, pathlib.Path]


def _search_records_file(folder: PathLike) -> Optional[pathlib.Path]:
    """searches for a the records xml file in a folder

    Args:
        folder:  directory to search

    Returns:
        the path to the settings file or None
    """
    folder_path = pathlib.Path(folder)
    files = (item for item in folder_path.iterdir() if item.suffix == ".xsl")
    xls_files = [path for path in files if not path.name.startswith(".")]
    if len(xls_files) == 1:
        xml_file = xls_files[0].with_suffix(".xml")
        if xml_file.is_file():
            return xml_file
    return None


def _iter_records(records_file: PathLike) -> Iterable[Tuple[str, str]]:
    """parses the information from a records file

    Args:
        records_file: path to the records file

    Yields:
        tuples, filename as first element and the datetime string as second
    """
    records_path = pathlib.Path(records_file)
    tree = ElementTree.parse(records_path)
    for channel_config in tree.findall(".//*[ImageFileName]"):
        image_tag = channel_config.find("ImageFileName")
        image_name = None if image_tag is None else image_tag.text
        datetime_tag = channel_config.find("Timestamp")
        datetime_str = None if datetime_tag is None else datetime_tag.text
        yield image_name, datetime_str


def _parse_records_file(records_file: PathLike) -> pandas.DataFrame:
    """parses the information from a records file

    Args:
        records_file: path to the records file

    Returns:
        pandas data frame with the parsed information
    """
    data = _iter_records(records_file)
    data_frame = pandas.DataFrame(
        data, columns=[columns.ANALYSIS_IMAGE, columns.ANALYSIS_DATETIME]
    )
    data_frame[columns.ANALYSIS_DATETIME] = pandas.to_datetime(
        data_frame[columns.ANALYSIS_DATETIME]
    )
    return data_frame


def add_record_time(
    measurement: pandas.DataFrame, folder: PathLike
) -> pandas.DataFrame:
    """adds the recoding datetime to the data frame

    The returned DataFrame will contain one more column for parsed datetime

    If the parameters could not be foundor do not match up with the
    measurement data, the additional collumn will contain NaN.

    Argumentss:
        measurement: the parsed measurement data
        folder: the folder of the measurement data

    Returns:
        the measurement data with parameters added
    """
    record_path = _search_records_file(folder)
    print(f"PATH: {record_path}")
    if record_path is None:
        print("assuming record path is None")
        measurement[columns.ANALYSIS_DATETIME] = numpy.NAN
        return measurement

    data_frame = _parse_records_file(record_path)
    print(data_frame)
    print(measurement[columns.ANALYSIS_IMAGE].iloc[0])
    return measurement.merge(data_frame, how="left", on=columns.ANALYSIS_IMAGE)
