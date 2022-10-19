import os
import shutil
from unittest import mock
from unittest.mock import mock_open
from pathlib import Path
from datetime import datetime, timedelta

import numpy as np
from geojson import Feature, FeatureCollection
from geojson.geometry import Point, Polygon
from shapely.geometry import shape
from fake_geo_images.fakegeoimages import FakeGeoImage

from blockutils.common import (
    load_query,
    load_params,
    load_metadata,
    get_block_mode,
    BlockModes,
    get_block_info,
    ensure_data_directories_exist,
    setup_test_directories,
    update_extents,
    encode_str_base64,
    decode_str_base64,
    get_timeperiod,
)
from blockutils.logging import get_logger, LOG_FORMAT
from blockutils.stac import STACQuery
from blockutils.exceptions import UP42Error
from blockutils.datapath import set_data_path


def test_setup_test_directories():
    test_dir = Path("/tmp/setup_test_directories")

    # Files that should not be cleaned up
    Path(test_dir / "some_dir").mkdir(parents=True, exist_ok=True)
    with open(test_dir / "some_dir/some.txt", "w", encoding="utf-8") as file:
        file.write("Some")

    # Files that should be cleaned up
    Path(test_dir / "input").mkdir(parents=True, exist_ok=True)
    with open(test_dir / "input/input.txt", "w", encoding="utf-8") as file:
        file.write("Input")

    input_dir, _, _ = setup_test_directories(test_dir)

    assert len(list(test_dir.rglob("*"))) == 5
    assert input_dir == test_dir / "input"
    for subdir in ["input", "output", "quicklooks"]:
        assert Path(test_dir / subdir).exists()
        assert Path(test_dir / subdir).is_dir()
    assert Path(test_dir / "some_dir/some.txt").exists()


def test_load_query():
    os.environ[
        "UP42_TASK_PARAMETERS"
    ] = """
    {
        "intersects": {
          "type": "Point",
          "coordinates": [13.32, 38.205]
        }
    }
    """
    query = load_query()
    assert query.bounds() == (13.32, 38.205, 13.32, 38.205)


def test_load_params():
    # Test for missing parameters key not to cause errors
    os.environ[
        "UP42_TASK_PARAMETERS"
    ] = """
    {
    }
    """
    assert load_params() == {}

    # Test for nothing not to cause errors
    os.environ["UP42_TASK_PARAMETERS"] = ""
    assert load_params() == {}

    # Test that root level parameters are returned when they are not nested in task name
    os.environ[
        "UP42_TASK_PARAMETERS"
    ] = """
    {
        "test_key": "test_value"
    }
    """
    assert "test_key" in load_params()
    assert load_params().get("test_key") == "test_value"


def test_get_logger():
    logger = get_logger("test_logger")
    assert (
        logger.handlers[0].formatter._fmt  # pylint: disable=protected-access
        == LOG_FORMAT
    ), "Incorrect logger or log formatter loaded!"


def test_stac():  # pylint: disable=too-many-statements
    query = STACQuery.from_json('{ "bbox": [1, 1, 2, 2]}')
    assert query.bounds, "STACQuery not initialized properly from json!"

    query = STACQuery.from_dict({"intersects": Point((1, 1))})
    assert query.bounds() == (
        1.0,
        1.0,
        1.0,
        1.0,
    ), "STACQuery not initialized properly from dict data!"

    query = STACQuery(bbox=(1, 1, 1, 1))
    assert query.bounds() == (
        1.0,
        1.0,
        1.0,
        1.0,
    ), "STACQuery not initialized properly from args!"

    assert query.time is None, "STACQuery's default TIME property should be NONE"
    assert query.limit == 1, "STACQuery's default LIMIT property should be 1"

    query = STACQuery(bbox=(1, 1, 1, 1), limit=-2)
    assert (
        query.limit == 1
    ), "STACQuery's default LIMIT property should be corrected to 1 if negative is given"

    query = STACQuery()
    exception = None
    try:
        query.bounds()
    except UP42Error as ex:
        exception = ex
    assert (
        exception is not None
    ), "STACQuery without an bbox, intersects or contains should throw an error here!"

    assert STACQuery(contains=Point())
    assert STACQuery(intersects=Point())

    exception = None
    try:
        query = STACQuery(bbox=(1, 1, 1, 1), intersects=Point())
    except UP42Error as ex:
        exception = ex
    assert (
        exception is not None
    ), "STACQuery should throw an error if generated with bbox and intersects."

    exception = None
    try:
        query = STACQuery(bbox=(1, 1, 1, 1), contains=Point())
    except UP42Error as ex:
        exception = ex
    assert (
        exception is not None
    ), "STACQuery should throw an error if generated with bbox and contains."

    exception = None
    try:
        query = STACQuery(intersects=Point(), contains=Point())
    except UP42Error as ex:
        exception = ex
    assert (
        exception is not None
    ), "STACQuery should throw an error if generated with intersects and contains."

    assert STACQuery(whatever=1).whatever == 1  # pylint: disable=no-member
    assert (
        STACQuery.from_dict({"whatever": 1}).whatever == 1  # pylint: disable=no-member
    )
    assert STACQuery.from_dict({"bbox": (1, 1, 1, 1)}).bbox == (
        1,
        1,
        1,
        1,
    )  # pylint: disable=no-member

    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49+00:00")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:44.12+00:00")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47")
    assert STACQuery.validate_datetime_str("2019-01-23")
    assert STACQuery.validate_datetime_str(
        "2019-01-23T16:47:49+00:00/2019-01-24T16:47:49+00:00"
    )
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49Z")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49.22Z")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49Z/2019-01-24T16:47:49Z")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47/2019-01-24T16:47")
    assert STACQuery.validate_datetime_str("2019-01-23/2019-01-24")
    assert STACQuery.validate_datetime_str("2019-01-23T16:47:49+0000")
    assert not STACQuery.validate_datetime_str("2019-01-23T16:47:49T")
    assert not STACQuery.validate_datetime_str("12345")
    assert not STACQuery.validate_datetime_str("yo/yoyo")
    assert not STACQuery.validate_datetime_str(
        "2019-01-23T16:47:49+00:00//2019-01-24T16:47:49+00:00"
    )

    assert STACQuery(ids=["abcdef123456789ghi"]).ids == ["abcdef123456789ghi"]

    test_time_series = [
        "2018-01-01T16:47:49/2018-02-01T16:47:49",
        "2018-02-01T16:47:49/2018-03-01T16:47:49",
        "2018-03-01T16:47:49/2018-04-01T16:47:49",
    ]
    assert STACQuery(time_series=test_time_series).time_series == test_time_series


@mock.patch(
    "builtins.open",
    mock_open(
        read_data=open("tests/mock_data/data.json", "r", encoding="utf-8").read()
    ),
)
@mock.patch("os.path.exists", return_value=True)
def test_load_data(mocks_path):  # pylint: disable=W0613
    data: FeatureCollection = load_metadata()
    for feature in data.features:
        assert isinstance(feature, Feature)


def test_update_extents():
    ensure_data_directories_exist()
    tmp_dir = Path("/tmp/output")

    # Create two synthetic images
    path_to_test_image_1, _ = FakeGeoImage(
        28, 20, 2, "uint16", out_dir=tmp_dir
    ).create()
    path_to_test_image_2, _ = FakeGeoImage(
        40, 28, 1, "uint16", out_dir=tmp_dir
    ).create()

    # Create FC out of synthetic images with (too) large image extents
    poly_1 = Polygon(
        [
            [
                (13.21, 52.62),
                (13.22, 52.62),
                (13.22, 52.63),
                (13.21, 52.63),
                (13.21, 52.62),
            ]
        ]
    )
    poly_2 = Polygon(
        [
            [
                (14.21, 53.62),
                (14.22, 53.62),
                (14.22, 53.63),
                (14.21, 53.63),
                (14.21, 53.62),
            ]
        ]
    )
    feature_1 = Feature(bbox=shape(poly_1).bounds, geometry=poly_1)
    feature_2 = Feature(bbox=shape(poly_2).bounds, geometry=poly_2)
    set_data_path(feature_1, path_to_test_image_1.name)
    set_data_path(feature_2, path_to_test_image_2.name)
    fc = FeatureCollection([feature_1, feature_2])

    expected_bbox = [13.21418, 52.62515, 13.21468, 52.625375]
    updated_fc = update_extents(fc)
    up_feature_1, up_feature_2 = updated_fc.features

    assert np.allclose(
        np.array(expected_bbox), np.array(up_feature_1["bbox"]), atol=1e-07
    )
    assert np.allclose(
        np.array(expected_bbox),
        np.array(shape(up_feature_2.geometry).bounds),
        atol=1e-04,
    )

    shutil.rmtree(tmp_dir)


@mock.patch.dict("os.environ", {"UP42_JOB_MODE": "DRY_RUN"})
def test_get_block_mode_dry_run():
    assert get_block_mode() == BlockModes.DRY_RUN.value


@mock.patch.dict("os.environ", {"UP42_JOB_MODE": ""})
def test_get_block_mode_unset():
    assert get_block_mode() == BlockModes.DEFAULT.value


@mock.patch.dict("os.environ", {"UP42_JOB_MODE": "DEFAULT"})
def test_get_block_mode_default():
    assert get_block_mode() == BlockModes.DEFAULT.value


def test_get_block_mode_not_set():
    assert get_block_mode() == BlockModes.DEFAULT.value


def test_get_block_info():
    os.environ[
        "UP42_BLOCK_INFO"
    ] = """{
        "blockId":"8487adcd-a4d7-4cb7-b826-75a533e1f330",
        "blockName":"oneatlas-pleiades-fullscene",
        "blockDisplayName":"Pléiades DIMAP Download",
        "blockVersion":"0.7.2",
        "inputCapabilities":[],
        "outputCapabilities":["up42.data_path"],
        "isPublic":true,
        "pricingStrategyUnit":"SQUARE_KM_OUTPUT",
        "pricingStrategyCredits":900,
        "machineName":"SMALL",
        "machineCredits":37}
        """

    block_info_dict = get_block_info()
    assert block_info_dict["pricingStrategyCredits"] == 900


def test_encode_decode_str_base64():

    unencoded_str = (
        '{"type": "service_acc", "priv_key": "--BEGIN KEY--\nMIIEv\n--END KEY--\n"'
    )
    encoded_str = encode_str_base64(unencoded_str)
    assert (
        encoded_str
        == "eyJ0eXBlIjogInNlcnZpY2VfYWNjIiwgInByaXZfa2V5IjogIi0tQkVHSU4gS0VZLS0KTUlJRXYKLS1FTkQgS0VZLS0KIg=="
    )

    restored_str = decode_str_base64(encoded_str)
    assert restored_str == unencoded_str


def test_select_timeperiod():
    test_end_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    test_start_date = test_end_date + timedelta(days=-365)
    test_time = (
        f"{test_start_date.strftime('%Y-%m-%d')}T00:00:00+00:00/"
        f"{test_end_date.strftime('%Y-%m-%d')}T23:59:59+00:00"
    )

    assert get_timeperiod() == test_time
    assert get_timeperiod(duration=365, start=-365) == test_time
    assert (
        get_timeperiod(duration=60, start_date="2019-01-01")
        == "2019-01-01T00:00:00+00:00/2019-03-02T23:59:59+00:00"
    )
    assert (
        get_timeperiod(start_date="2019-01-01", end_date="2019-02-23")
        == "2019-01-01T00:00:00+00:00/2019-02-23T23:59:59+00:00"
    )
