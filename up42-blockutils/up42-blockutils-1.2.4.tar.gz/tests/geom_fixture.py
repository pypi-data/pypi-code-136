import pytest

import geojson


@pytest.fixture
def point_fixture():
    return geojson.utils.generate_random("Point")


@pytest.fixture
def mpoint_fixture():
    point = geojson.utils.generate_random("Point")
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiPoint([g["coordinates"]]), point
    )


@pytest.fixture
def mpoint_with_z_fixture():
    point = geojson.utils.generate_random("Point")
    point["coordinates"].append(0)
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiPoint([g["coordinates"]]), point
    )


@pytest.fixture
def line_fixture():
    return geojson.utils.generate_random("LineString")


@pytest.fixture
def mline_fixture():
    line = geojson.utils.generate_random("LineString")
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiLineString([g["coordinates"]]), line
    )


@pytest.fixture
def mline_with_z_fixture():
    line = geojson.utils.generate_random("LineString")
    line["coordinates"][0].append(0)
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiLineString([g["coordinates"]]), line
    )


@pytest.fixture
def poly_fixture():
    return geojson.utils.generate_random("Polygon")


@pytest.fixture
def mpoly_fixture():
    poly = geojson.utils.generate_random("Polygon")
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiPolygon([g["coordinates"]]), poly
    )


@pytest.fixture
def mpoly_with_z_fixture():
    poly = geojson.utils.generate_random("Polygon")
    poly["coordinates"][0][0].append(0)
    return geojson.utils.map_geometries(
        lambda g: geojson.MultiPolygon([g["coordinates"]]), poly
    )
