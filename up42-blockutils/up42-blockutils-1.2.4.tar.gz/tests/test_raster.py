import shutil
import tempfile
from pathlib import Path

import pytest
import rasterio as rio
from fake_geo_images.fakegeoimages import FakeGeoImage
from rasterio.enums import ColorInterp
from rio_cogeo import cog_validate

from blockutils.raster import create_multiband_tif, is_empty, to_cog


def test_is_empty():
    tmp_dir = Path(tempfile.mkdtemp())

    # Case for non-empty image
    path_to_test_image, _ = FakeGeoImage(28, 28, 2, "uint16", out_dir=tmp_dir).create()
    assert not is_empty(path_to_test_image)
    # Case for empty image
    path_to_test_image, _ = FakeGeoImage(
        28, 28, 2, "uint16", out_dir=tmp_dir, nodata_fill=28
    ).create()
    assert is_empty(path_to_test_image)

    shutil.rmtree(tmp_dir)


def test_to_cog():
    tmp_dir = Path(tempfile.mkdtemp())

    width = 192
    height = 128
    path_to_test_image, _ = FakeGeoImage(
        width, height, 4, "uint16", out_dir=tmp_dir
    ).create()

    to_cog(path_to_test_image)

    with rio.open(str(path_to_test_image)) as src:
        profile = src.profile
    assert profile["height"] == height
    assert profile["width"] == width
    assert profile["compress"] == "deflate"
    assert profile["blockxsize"] == 128
    assert (
        cog_validate(path_to_test_image)[0] is True
    )

@pytest.mark.parametrize(
    "dtype", ["uint8", "uint16", "uint32", "int16", "int32", "float32", "float64"]
)
def test_to_cog_data_corruption(dtype):
    tmp_dir = Path(tempfile.mkdtemp())

    width = 192
    height = 128

    path_to_test_image, _ = FakeGeoImage(
        width, height, 5, dtype, out_dir=tmp_dir
    ).create()

    with rio.open(str(path_to_test_image), "r+") as src:
        original_values = src.read()
        src.colorinterp = [
            ColorInterp.red,
            ColorInterp.green,
            ColorInterp.blue,
            ColorInterp.alpha,
            ColorInterp.grey,
        ]

    to_cog(path_to_test_image)

    with rio.open(str(path_to_test_image)) as src:
        cog_values = src.read()

    assert original_values.all() == cog_values.all()
    assert (
        cog_validate(path_to_test_image)[0] is True
    )

def test_create_multiband_tif():
    tmp_dir = Path(tempfile.mkdtemp())
    filename_path = Path("/tmp/multi_tif.tif")
    band_descriptions = ["a", "b"]

    width = 192
    height = 128

    path_to_test_image_1, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    path_to_test_image_2, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    create_multiband_tif(
        [path_to_test_image_1, path_to_test_image_2], filename_path, band_descriptions
    )
    with rio.open(filename_path) as src:
        assert src.count == 2
        assert src.width == 192
        assert src.height == 128
        assert src.descriptions == ("a", "b")


def test_create_multiband_tif_different_band_number():
    tmp_dir = Path(tempfile.mkdtemp())
    filename_path = Path("/tmp/multi_tif.tif")
    band_descriptions = ["a", "b", "c", "d"]

    width = 192
    height = 128

    path_to_test_image_1, _ = FakeGeoImage(
        width, height, 3, "uint8", out_dir=tmp_dir
    ).create()

    path_to_test_image_2, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    create_multiband_tif(
        [path_to_test_image_1, path_to_test_image_2], filename_path, band_descriptions
    )
    with rio.open(filename_path) as src:
        assert src.count == 4
        assert src.width == 192
        assert src.height == 128
        assert src.descriptions == ("a", "b", "c", "d")


def test_create_multiband_tif_assertionerror():
    tmp_dir = Path(tempfile.mkdtemp())
    filename_path = Path("/tmp/multi_tif.tif")
    band_descriptions = ["a", "b"]

    width = 192
    height = 128

    path_to_test_image_1, _ = FakeGeoImage(
        width, height, 3, "uint8", out_dir=tmp_dir
    ).create()

    path_to_test_image_2, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    with pytest.raises(AssertionError):
        create_multiband_tif(
            [path_to_test_image_1, path_to_test_image_2],
            filename_path,
            band_descriptions,
        )


def test_create_multiband_tif_no_band_descriptions():
    tmp_dir = Path(tempfile.mkdtemp())
    filename_path = Path("/tmp/multi_tif.tif")

    width = 192
    height = 128

    path_to_test_image_1, _ = FakeGeoImage(
        width, height, 3, "uint8", out_dir=tmp_dir
    ).create()

    path_to_test_image_2, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    create_multiband_tif([path_to_test_image_1, path_to_test_image_2], filename_path)
    with rio.open(filename_path) as src:
        assert src.count == 4
        assert src.width == 192
        assert src.height == 128
        assert not all(src.descriptions)


def test_create_multiband_tif_no_cog():
    tmp_dir = Path(tempfile.mkdtemp())
    filename_path = Path("/tmp/multi_tif.tif")
    band_descriptions = ["a", "b"]

    width = 192
    height = 128

    path_to_test_image_1, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    path_to_test_image_2, _ = FakeGeoImage(
        width, height, 1, "uint8", out_dir=tmp_dir
    ).create()

    create_multiband_tif(
        [path_to_test_image_1, path_to_test_image_2],
        filename_path,
        band_descriptions,
        return_cog=False,
    )
    with rio.open(filename_path) as src:
        assert src.count == 2
        assert src.width == 192
        assert src.height == 128
        assert src.descriptions == ("a", "b")
        assert "compress" not in src.profile
