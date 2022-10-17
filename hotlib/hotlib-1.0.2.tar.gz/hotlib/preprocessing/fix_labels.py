import os

import geopandas
from shapely.validation import explain_validity, make_valid


def remove_self_intersection(row):
    """Fix self-intersections in the polygons.

    Some of the polygons may have self-intersections. In that
    case, we transform that geometry to a multi-polygon and
    substitute the original geometry with the largest polygon.
    """
    if explain_validity(row.geometry) == "Valid Geometry":
        return row.geometry

    valid_geom = make_valid(row.geometry)
    if not hasattr(valid_geom, "__len__"):
        return valid_geom

    for polygon in valid_geom.geoms:
        if polygon.area >= row.geometry.area / 2.0:
            return polygon


def fix_labels(input_dir: str, sub_dir: str, out_dir: str) -> None:
    """Fix GeoJSON file so that it doesn't have any self-intersecting polygons.

    Args:
        input_dir: Name of the directory where the input data are stored.
        sub_dir: Name of the sub-directory under the input directory.
        out_dir: Name of the directory where the output data will go.
    """
    os.makedirs(f"{out_dir}/{sub_dir}", exist_ok=True)

    gdf = geopandas.read_file(f"{input_dir}/{sub_dir}/labels.geojson")
    gdf["geometry"] = gdf.apply(remove_self_intersection, axis=1)
    gdf.to_file(f"{input_dir}/{sub_dir}/labels.geojson")
