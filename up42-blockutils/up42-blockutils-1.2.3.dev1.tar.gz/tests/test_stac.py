import copy
import geojson

import pytest
from pytest_lazyfixture import lazy_fixture

# pylint: disable=unused-import
from geom_fixture import (
    point_fixture,
    line_fixture,
    poly_fixture,
    mpoint_with_z_fixture,
    mline_with_z_fixture,
    mpoly_with_z_fixture,
)

from blockutils.exceptions import UP42Error
from blockutils.stac import STACQuery


@pytest.fixture
def poly():
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [13.3219228515625, 38.2036553180715],
                [13.32366943359375, 38.2058],
                [13.32366943359375, 38.2036553180715],
                [13.3219228515625, 38.2036553180715],
            ]
        ],
    }


@pytest.fixture
def poly_with_z():
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [72.048156, 71.288156, 0],
                [72.048622, 71.286989, 0],
                [72.073096, 71.276898],
                [72.094072, 71.267127, 0],
                [72.097472, 71.268174, 0],
                [72.113736, 71.278004, 0],
                [72.106981, 71.280291, 0],
                [72.082472, 71.285293, 0],
                [72.048156, 71.288156, 0],
            ]
        ],
    }


# pylint: disable=redefined-outer-name
@pytest.fixture
def query_dict(poly):
    return {
        "limit": 5,
        "intersects": poly,
        "add_panchromatic": True,
    }


def test_stac_from_dict(query_dict):
    q = STACQuery.from_dict(query_dict)
    assert q.limit == 5
    assert q.intersects
    assert q.add_panchromatic
    assert not q.bbox


def test_stac_from_dict_z_coor(monkeypatch, query_dict, poly_with_z):
    monkeypatch.setitem(query_dict, "intersects", poly_with_z)
    q = STACQuery.from_dict(query_dict)
    assert q.intersects == {
        "type": "Polygon",
        "coordinates": [
            [
                [72.048156, 71.288156],
                [72.048622, 71.286989],
                [72.073096, 71.276898],
                [72.094072, 71.267127],
                [72.097472, 71.268174],
                [72.113736, 71.278004],
                [72.106981, 71.280291],
                [72.082472, 71.285293],
                [72.048156, 71.288156],
            ]
        ],
    }


def test_stac_set_param_if_not_exists(query_dict):
    q = STACQuery.from_dict(query_dict)
    q.set_param_if_not_exists("limit", 1)
    assert q.limit == 5
    q.set_param_if_not_exists("some_extra", [1248, 5478])
    assert q.some_extra == [1248, 5478]
    q.set_param_if_not_exists("some_extra", [1])
    assert q.some_extra == [1248, 5478]


def test_stac_get_param_if_exists(query_dict):
    q = STACQuery.from_dict(query_dict)
    q.set_param_if_not_exists("limit", 5)
    assert q.limit == q.get_param_if_exists("limit", 1)
    q.set_param_if_not_exists("some_extra", [1248, 5478])
    assert q.get_param_if_exists("some_extra") == [1248, 5478]
    assert q.get_param_if_exists("some_other_extra", 15) == 15
    assert not q.get_param_if_exists("some_other_extra")


def test_stac_repr(query_dict):
    q = STACQuery.from_dict(query_dict)
    assert str(q) == (
        'STACQuery(ids=None, bbox=None, intersects={"coordinates": [[[13.321923, 38.203655],'
        ' [13.323669, 38.2058], [13.323669, 38.203655], [13.321923, 38.203655]]], "type": "Polygon"},'
        " contains=None, time=None, time_series=None, limit=5)"
    )


def test_post_init(query_dict, poly):
    with pytest.raises(UP42Error, match=r".*[WRONG_INPUT_ERROR].*"):

        STACQuery.from_dict(dict(query_dict, bbox=[1, 2, 3, 4]))
    with pytest.raises(UP42Error, match=r".*[WRONG_INPUT_ERROR].*"):
        STACQuery.from_dict(dict(query_dict, contains=poly))

    q = STACQuery.from_dict(dict(query_dict, limit=-1))
    assert q.limit == 1

    with pytest.raises(UP42Error, match=r".*[WRONG_INPUT_ERROR].*"):
        STACQuery.from_dict(dict(query_dict, time="abc", time_series=["abc", "def"]))

    with pytest.raises(UP42Error, match=r".*[WRONG_INPUT_ERROR].*"):
        STACQuery.from_dict(dict(query_dict, time="abc"))

    with pytest.raises(UP42Error, match=r".*[WRONG_INPUT_ERROR].*"):
        STACQuery.from_dict(dict(query_dict, time_series=["abc", "dfc"]))


def test_snap_polarimetry():
    params = {"mask": ["sea"], "tcorrection": False, "speckle_filter": False}
    params = STACQuery.from_dict(params, lambda x: True)
    assert params.mask == ["sea"]
    assert not params.tcorrection
    assert not params.speckle_filter

    params.set_param_if_not_exists("calibration_band", ["sigma"])
    params.set_param_if_not_exists("speckle_filter", True)
    params.set_param_if_not_exists("linear_to_db", True)
    params.set_param_if_not_exists("clip_to_aoi", False)
    params.set_param_if_not_exists("mask", None)
    params.set_param_if_not_exists("tcorrection", True)
    params.set_param_if_not_exists("polarisations", ["VV"])

    assert params.mask == ["sea"]
    assert not params.tcorrection
    assert not params.speckle_filter


def test_seeps():
    params = {"bbox": [-75.566883, 40.01013, -75.560703, 40.015257]}
    params = STACQuery.from_dict(params, lambda x: True)

    params.set_param_if_not_exists(
        "time", "1991-07-30T00:00:00+00:00/2016-06-01T23:59:59+00:00"
    )
    params.set_param_if_not_exists("object_types", ["Ships_Rigs", "Scenes"])

    assert params.time == "1991-07-30T00:00:00+00:00/2016-06-01T23:59:59+00:00"
    assert params.object_types == ["Ships_Rigs", "Scenes"]
    assert not params.intersects


def test_handle_z_coordinates_no_z(query_dict):
    out_query = STACQuery.handle_z_coordinate(query_dict)
    assert out_query == query_dict


def test_handle_z_coordinate_null():
    # This is a case for processing blocks which have clipe_to_aoi option, and by default
    # intersects and contains both exist and are None. This need to be revisited when
    # in platfrom we allow passing geometry to the next block.
    query = {
        "bbox": [
            139.768248796463,
            35.672863961845884,
            139.7703194618225,
            35.67472909454745,
        ],
        "ms": "true",
        "intersects": None,
        "contains": None,
        "clip_to_aoi": "true",
    }
    out_query = STACQuery.handle_z_coordinate(query)
    assert not out_query["intersects"]
    assert not out_query["contains"]
    assert out_query == query


@pytest.mark.parametrize(
    "in_geom",
    [
        lazy_fixture("point_fixture"),
        lazy_fixture("line_fixture"),
        lazy_fixture("poly_fixture"),
    ],
)
def test_handle_z_coordinates(in_geom, monkeypatch, query_dict):
    in_geom_with_z = copy.deepcopy(in_geom)
    if "Point" in in_geom["type"]:
        in_geom_with_z["coordinates"].append(0)
    if "LineString" in in_geom["type"]:
        in_geom_with_z["coordinates"][0].append(0)
    if "Polygon" in in_geom["type"]:
        in_geom_with_z["coordinates"][0][0].append(0)
    monkeypatch.setitem(query_dict, "intersects", in_geom_with_z)
    out_query = STACQuery.handle_z_coordinate(query_dict)
    assert out_query["intersects"] == in_geom


@pytest.mark.parametrize(
    "in_geom",
    [
        lazy_fixture("mpoint_with_z_fixture"),
        lazy_fixture("mline_with_z_fixture"),
        lazy_fixture("mpoly_with_z_fixture"),
    ],
)
def test_handle_z_coordinates_multi(in_geom, monkeypatch, query_dict):
    in_geom_with_z = copy.deepcopy(in_geom)

    monkeypatch.setitem(query_dict, "intersects", in_geom_with_z)
    out_query = STACQuery.handle_z_coordinate(query_dict)
    list_coor = list(geojson.utils.coords(out_query["intersects"]))
    for i in list_coor:
        assert len(i) == 2
