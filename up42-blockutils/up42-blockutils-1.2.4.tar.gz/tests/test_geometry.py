# pylint: disable=redefined-outer-name
import json
import os

import pytest
from geojson.geometry import Polygon
from shapely.geometry import box
import mercantile
from mercantile import Tile
from blockutils.exceptions import UP42Error
from blockutils.geometry import (
    aoi_size_check,
    check_validity,
    count_vertices,
    filter_tiles_intersect_with_geometry,
    get_utm_zone_epsg,
    intersect_geojson_polygons,
    get_query_bbox,
    tiles_to_geom,
)
from blockutils.stac import STACQuery


@pytest.fixture()
def complex_geom():
    _location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(_location_, "mock_data/complex_geom.json"), "rb") as src:
        return json.load(src)


@pytest.fixture()
def multipoly_geom():
    _location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(
        os.path.join(_location_, "mock_data/multi-poly.json"), encoding="utf-8"
    ) as src:
        return json.load(src)


def test_filter_tiles_intersect_with_geometry():

    tile_berlin = Tile(x=70472, y=43010, z=17)
    tile_london = Tile(x=130950, y=87150, z=18)

    polygon_london = Polygon(
        coordinates=[
            [
                [-0.1696014404296875, 51.54249177614476],
                [-0.215606689453125, 51.512588580360244],
                [-0.12153625488281249, 51.47539580264131],
                [-0.100250244140625, 51.505750806437874],
                [-0.1696014404296875, 51.54249177614476],
            ]
        ]
    )

    polygon_berlin = Polygon(
        coordinates=[
            [
                [13.3978271484375, 52.36553758871974],
                [13.74664306640625, 52.36553758871974],
                [13.74664306640625, 52.619725272670266],
                [13.3978271484375, 52.619725272670266],
                [13.3978271484375, 52.36553758871974],
            ]
        ]
    )

    assert (
        list(
            filter_tiles_intersect_with_geometry(
                [tile_berlin, tile_london], polygon_london
            )
        )[0]
        == tile_london
    )
    assert (
        len(
            list(
                filter_tiles_intersect_with_geometry(
                    [tile_berlin, tile_london], polygon_london
                )
            )
        )
        == 1
    )

    assert (
        list(
            filter_tiles_intersect_with_geometry(
                [tile_berlin, tile_london], polygon_berlin
            )
        )[0]
        == tile_berlin
    )
    assert (
        len(
            list(
                filter_tiles_intersect_with_geometry(
                    [tile_berlin, tile_london], polygon_london
                )
            )
        )
        == 1
    )


def test_intersect_geojson_polygons():

    geom1 = Polygon(coordinates=[[[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]]])

    geom2 = Polygon(coordinates=[[[1, 1], [1, 3], [3, 3], [3, 1], [1, 1]]])

    intersection = intersect_geojson_polygons(geom1, geom2)

    expected_geom = {
        "type": "Polygon",
        "coordinates": (((2.0, 2.0), (2.0, 1.0), (1.0, 1.0), (1.0, 2.0), (2.0, 2.0)),),
    }

    assert intersection == expected_geom


def test_aoi_size_check():

    # intersect/contains smaller 0.05
    geom_smaller_005 = {
        "type": "Polygon",
        "coordinates": [
            [
                [13.302234, 52.511731],
                [13.304494, 52.511867],
                [13.304873, 52.510331],
                [13.302414, 52.510423],
                [13.302234, 52.511731],
            ]
        ],
    }

    # bbox smaller 0.1
    bbox_smaller_01 = [
        13.302234392613173,
        52.50959302910651,
        13.306143628433349,
        52.5118674078128,
    ]

    # intersect/contains larger 1.80
    geom_larger_18 = {
        "type": "Polygon",
        "coordinates": [
            [
                [13.296371, 52.504093],
                [13.318107, 52.502611],
                [13.318107, 52.514373],
                [13.293971, 52.514373],
                [13.296371, 52.504093],
            ]
        ],
    }

    # bbox larger 2.00
    bbox_larger_1 = [
        13.293971177190542,
        52.50261091442014,
        13.318107454106213,
        52.51437370986882,
    ]

    query = STACQuery.from_dict({"intersects": geom_smaller_005})

    assert not aoi_size_check(query, min_sqkm=0.05)
    assert aoi_size_check(query, min_sqkm=0.01)

    query = STACQuery.from_dict({"bbox": bbox_smaller_01})

    assert not aoi_size_check(query, min_sqkm=0.1)
    assert aoi_size_check(query, min_sqkm=0.01)

    query = STACQuery.from_dict({"intersects": geom_larger_18})

    assert not aoi_size_check(query, min_sqkm=0.05, max_sqkm=1.4)
    assert aoi_size_check(query, min_sqkm=0.01, max_sqkm=1.9)

    query = STACQuery.from_dict({"bbox": bbox_larger_1})

    assert not aoi_size_check(query, max_sqkm=1.0)
    assert aoi_size_check(query, min_sqkm=0.6)

    query = STACQuery.from_dict({"ids": ["xyz"]})
    assert aoi_size_check(query, min_sqkm=0.6, ignore_missing_geometry=True)
    with pytest.raises(UP42Error):
        aoi_size_check(query, min_sqkm=0.6)


@pytest.mark.parametrize(
    "lon, lat, epsg_expected",
    [
        (-79.52826976776123, 8.847423357771518, 32617),  # Panama
        (9.95121, 49.79391, 32632),  # Wuerzburg
        (9.767417, 62.765571, 32632),  # Norway special zone
        (12.809028, 79.026583, 32633),  # Svalbard special zone
    ],
)
def test_get_utm_zone_epsg(lat, lon, epsg_expected):
    epsg = get_utm_zone_epsg(lat=lat, lon=lon)

    assert epsg == epsg_expected


def test_count_vertices_multipoly(multipoly_geom):

    expected_output = 53
    result = count_vertices(multipoly_geom)

    assert result == expected_output


def test_count_vertices_complex_geom(complex_geom):

    expected_output = 117
    result = count_vertices(complex_geom)

    assert result == expected_output


@pytest.mark.skip
def test_count_vertices(complex_geometry):
    expected_output = 684
    result = count_vertices(complex_geometry)

    assert result == expected_output


@pytest.mark.skip
def test_check_validity_raises_up42error(complex_geometry):
    with pytest.raises(UP42Error, match=r".*['INPUT_PARAMETERS_ERROR'].*"):
        check_validity(complex_geometry)


@pytest.mark.skip
def test_check_validity_raises_explain_msg(complex_geometry):
    with pytest.raises(UP42Error, match=r".*['Self-intersection'].*"):
        check_validity(complex_geometry)


def test_check_validity_is_valid():
    in_geom = {
        "type": "Polygon",
        "coordinates": [
            [
                [-6.087734007972409, 34.01252928472715],
                [-6.08589, 34.280914],
                [-5.716511362513159, 34.29498787258231],
                [-5.717305, 34.016376],
                [-6.087734007972409, 34.01252928472715],
            ]
        ],
    }

    assert check_validity(in_geom) is None


def test_get_query_bbox_z_coordinates():
    poly = {
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

    query = STACQuery.from_dict(
        {"intersects": poly},
    )
    bbox = get_query_bbox(query)
    assert list(bbox) == [72.048156, 71.267127, 72.113736, 71.288156]


def test_tiles_to_geom():
    tiles = [
        Tile(x=41955, y=101467, z=18),
        Tile(x=41955, y=101468, z=18),
        Tile(x=41955, y=101469, z=18),
    ]
    return_poly = tiles_to_geom(tiles, mercantile)
    for tile in tiles:
        assert return_poly.contains(box(*tuple(mercantile.bounds(tile))))

    assert int(return_poly.area / (box(*tuple(mercantile.bounds(tiles[0])))).area) == 3
