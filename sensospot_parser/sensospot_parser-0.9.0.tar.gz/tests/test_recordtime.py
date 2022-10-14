import pandas
import pytest

from .conftest import EXAMPLE_DIR_WITH_PARAMS, EXAMPLE_DIR_WITH_RECORD


@pytest.fixture
def file_list(example_dir):
    import pathlib

    path = pathlib.Path(example_dir / EXAMPLE_DIR_WITH_RECORD)
    tifs = (i.with_suffix(".tif") for i in path.glob("*.csv"))
    return [i.name for i in tifs]


def test_search_records_file_ok(example_dir):
    from sensospot_parser.recordtime import _search_records_file

    result = _search_records_file(example_dir / EXAMPLE_DIR_WITH_RECORD)

    assert result.suffix == ".xml"


def test_search_records_file_not_found(example_dir):
    from sensospot_parser.recordtime import _search_records_file

    result = _search_records_file(example_dir / EXAMPLE_DIR_WITH_PARAMS)

    assert result is None


def test_iter_records(example_dir):
    from sensospot_parser.recordtime import _iter_records, _search_records_file

    path = _search_records_file(example_dir / EXAMPLE_DIR_WITH_RECORD)

    result = list(_iter_records(path))

    assert (
        result[0][0] == "220307_SN0801_CHECK-01_SL1,11,9,14_MS_1_1_A01_1.tif"
    )
    assert result[0][1] == "3/7/2022 5:31:47 PM"
    assert (
        result[-1][0] == "220307_SN0801_CHECK-01_SL1,11,9,14_MS_1_1_D04_4.tif"
    )
    assert result[-1][1] == "3/7/2022 5:33:41 PM"


def test_parse_records_file(example_dir):
    from sensospot_parser.recordtime import (
        _parse_records_file,
        _search_records_file,
    )

    path = _search_records_file(example_dir / EXAMPLE_DIR_WITH_RECORD)

    result = _parse_records_file(path)

    assert isinstance(result, pandas.DataFrame)
    assert list(result.columns) == ["Analysis.Image", "Analysis.Datetime"]
    assert len(result) == 64


def test_add_record_time_ok(example_dir, file_list):
    from sensospot_parser.recordtime import add_record_time

    df = pandas.DataFrame(file_list, columns=["Analysis.Image"])

    result = add_record_time(df, example_dir / EXAMPLE_DIR_WITH_RECORD)

    assert len(df) == len(result)
    assert list(result.columns) == ["Analysis.Image", "Analysis.Datetime"]
    assert not result["Analysis.Datetime"].hasnans


def test_add_record_time_unknown_file(example_dir, file_list):
    from sensospot_parser.recordtime import add_record_time

    extended_list = file_list + ["unknown file"]
    df = pandas.DataFrame(extended_list, columns=["Analysis.Image"])

    result = add_record_time(df, example_dir / EXAMPLE_DIR_WITH_RECORD)

    assert len(df) == len(result)
    assert list(result.columns) == ["Analysis.Image", "Analysis.Datetime"]
    assert result["Analysis.Datetime"].hasnans


def test_add_record_time_no_record_xml(example_dir, file_list):
    from sensospot_parser.recordtime import add_record_time

    df = pandas.DataFrame(file_list, columns=["Analysis.Image"])

    result = add_record_time(df, example_dir / EXAMPLE_DIR_WITH_PARAMS)

    assert len(df) == len(result)
    assert list(result.columns) == ["Analysis.Image", "Analysis.Datetime"]
    assert result["Analysis.Datetime"].hasnans
