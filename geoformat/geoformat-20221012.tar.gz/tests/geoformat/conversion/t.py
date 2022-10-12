from tests.utils.tests_utils import test_dependencies, test_function

from tests.data.geolayers import (
    geolayer_geometry_2d,
    geolayer_geometry_3d,
    geolayer_fr_dept_data_only,
)
from geoformat.conversion.geolayer_conversion import (
    geolayer_to_2d_geolayer,
)
from geoformat.conversion.geometry_conversion import (
    geometry_to_2d_geometry,
    geometry_to_geometry_collection
)

geolayer_to_2d_geolayer_parameters = {
    # 0: {
    #     "input_geolayer": geolayer_fr_dept_data_only,
    #     "return_value": geolayer_fr_dept_data_only,
    # },
    # 1: {
    #     "input_geolayer": geolayer_fr_dept_data_and_geometry,
    #     "return_value": geolayer_fr_dept_data_and_geometry,
    # },
    2: {
        "input_geolayer": geolayer_geometry_3d,
        "return_value": geolayer_geometry_2d,
    },
}


def test_all():
    # geolayer_to_2d_geolayer
    print(test_function(geolayer_to_2d_geolayer, geolayer_to_2d_geolayer_parameters))


if __name__ == "__main__":
    # test_all()
    print(geolayer_to_2d_geolayer(**{
        "input_geolayer": geolayer_fr_dept_data_only,
    }))

    # input_geometry = {'type': 'GeometryCollection25D', 'geometries': [{'type': 'Point25D', 'coordinates': [-115.81, 37.24, -38.654]}, {'type': 'LineString25D', 'coordinates': [[8.919, 44.4074, 254.8], [8.923, 44.4075, -98]]}, {'type': 'Polygon25D', 'coordinates': [[[2.38, 57.322, -76.65], [23.194, -20.28, 145], [-120.43, 19.15, 0.146], [2.38, 57.322, 78.89]], [[-5.21, 23.51, 154.4], [15.21, -10.81], [-20.51, 1.51, -32.6], [-5.21, 23.51, 45.6]]]}, {'type': 'MultiPoint25D', 'coordinates': [[-155.52, 19.61, 78.45], [-156.22, 20.74, 12.65], [-157.97, 21.46, -75.15]]}, {'type': 'MultiLineString25D', 'coordinates': [[[3.75, 9.25, -65.45], [-130.95, 1.52, 45.54]], [[23.15, -34.25, 15.584], [-1.35, -4.65, -98.45], [3.45, 77.95, 78.14]]]}, {'type': 'MultiPolygon25D', 'coordinates': [[[[3.78, 9.28, 123], [-130.91, 1.52, 15.54], [35.12, 72.234, 78.6], [3.78, 9.28, 87.878]]], [[[23.18, -34.29, -45.1515], [-1.31, -4.61, -3.245], [3.41, 77.91, -41.0], [23.18, -34.29, -87.89]]]]}]}
    # # coll = geometry_to_geometry_collection(geometry=input_geometry, bbox=False)
    # print(geometry_to_2d_geometry(input_geometry, bbox=False))
