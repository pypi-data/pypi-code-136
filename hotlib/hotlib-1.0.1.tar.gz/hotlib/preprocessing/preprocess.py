# Standard library imports
import os

from .fix_labels import fix_labels
from .georeference import georeference
from .rasterize_labels import rasterize_labels


def preprocess(data_path: str, input_dir: str, image_dir: str, mask_dir: str) -> None:
    """Fully preprocess the input data.

    Args:
        data_path: Path of the directory where all the data are stored.
        input_dir: Name of the directory where the input data are stored.
        image_dir: Name of the directory where the images are stored.
        image_dir: Name of the directory where the masks are stored.
    """
    assert os.path.isdir(
        f"{data_path}/{input_dir}"
    ), "Input data directory wasn't found."
    os.chdir(data_path)

    for sub_dir in os.listdir(input_dir):
        assert os.path.exists(
            f"{input_dir}/{sub_dir}/labels.geojson"
        ), "Label file wasn't found."

        georeference(input_dir, sub_dir, image_dir)
        fix_labels(input_dir, sub_dir, image_dir)
        rasterize_labels(input_dir, sub_dir, mask_dir)
        os.system(f"rm {mask_dir}/{sub_dir}/*.geojson")

