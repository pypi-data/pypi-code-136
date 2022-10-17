# Standard library imports
import math
import os
import re
from typing import Tuple

IMAGE_SIZE = 256


def get_prefix(path: str) -> str:
    """Get filename prefix (without extension) from full path."""
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]


def get_bounding_box(filename: str) -> str:
    """Get the four corners of the OAM image as coordinates.

    This function gives us the limiting values that we will pass to
    the GDAL commands. We need to make sure that the raster image
    that we're generating have the same dimension as the original image.
    Hence, we'll need to fetch these extrema values.

    Returns:
        x_min, y_max, x_max, y_min: This is the format the -a_ullr
            flag of GDAL expects.
    """
    _, *tile_info = re.split("-", filename)
    x_tile, y_tile, zoom = map(int, tile_info)
    top_left = num2deg(x_tile, y_tile, zoom)
    bottom_right = num2deg(x_tile + 1, y_tile + 1, zoom)
    bounding_box = [*top_left, *bottom_right]

    return "".join([f"{x} " for x in bounding_box])


def num2deg(x_tile: int, y_tile: int, zoom: int) -> Tuple[float, float]:
    """Convert coordinates from web mercator to WGS 84."""
    n = 2.0 ** zoom
    lon_deg = x_tile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y_tile / n)))
    lat_deg = math.degrees(lat_rad)

    return lon_deg, lat_deg
