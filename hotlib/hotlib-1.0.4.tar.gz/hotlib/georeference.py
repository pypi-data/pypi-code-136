# Standard library imports
import os
from glob import glob

from .utils import get_bounding_box, get_prefix


def georeference(input_dir: str, sub_dir: str, out_dir: str, is_mask=False) -> None:
    """Perform georeferencing and remove the fourth band from images (if any).

    If the image has only one band, that fourth band removal part 
    will be skipped.

    Args:
        input_dir: Name of the directory where the input data are stored.
        sub_dir: Name of the sub-directory under the input directory.
        out_dir: Name of the directory where the output data will go.
        is_mask: Whether the image is binary or not.
    """
    os.makedirs(f"{out_dir}/{sub_dir}", exist_ok=True)

    for path in glob(f"{input_dir}/{sub_dir}/*.png"):
        filename = get_prefix(path)
        bounding_box = get_bounding_box(filename)

        process_image = f"""
            gdal_translate \
                -b 1 {'' if is_mask else '-b 2 -b 3'} \
                {input_dir}/{sub_dir}/{filename}.png \
                {out_dir}/{sub_dir}/{filename}.tif \
                -a_ullr {bounding_box} \
                -a_srs EPSG:4326
        """
        os.system(process_image)
