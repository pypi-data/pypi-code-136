from pathlib import Path
import tempfile

import rasterio as rio
from rasterio.windows import Window
from rasterio.transform import from_origin
import numpy as np
import pytest

from fake_geo_images.fakegeoimages import FakeGeoImage
from blockutils.windows import WindowsUtil
from blockutils.logging import get_logger

logger = get_logger(__name__)


@pytest.fixture()
def windows_util_read():
    test_dir = Path(tempfile.mkdtemp())
    test_img, _ = FakeGeoImage(1000, 1000, 1, "uint16", test_dir).create(seed=45)
    return WindowsUtil(rio.open(test_img, "r"))


@pytest.fixture(scope="session")
def windows_util_write():
    test_dir = Path(tempfile.mkdtemp())
    test_img, _ = FakeGeoImage(200, 200, 1, "uint16", test_dir).create(seed=45)
    profile = rio.open(test_img).profile
    return WindowsUtil(rio.open(test_img, "w", **profile))


# Passing fixture as argument for tests
# pylint: disable=redefined-outer-name
def test_windows_regular(windows_util_read):
    windows = windows_util_read.windows_regular()
    list_windows = list(windows)
    assert len(list_windows) == 250
    # Check if one random window remains equal
    one_window = list_windows[5]
    logger.info(one_window)
    assert one_window == Window(0, 20, 1000, 4)


def test_windows_buffered(windows_util_read):
    windows = windows_util_read.windows_buffered(buffer=5)
    list_windows = list(windows)
    assert len(list_windows) == 250
    # Check if one random window is buffered
    one_window = list_windows[5][1]
    assert one_window == Window(0, 15, 1000, 14)


def test_upsample(windows_util_read):
    test_dir = Path(tempfile.mkdtemp())
    test_img_high, _ = FakeGeoImage(800, 800, 1, "uint16", test_dir).create(
        seed=45, transform=from_origin(1470996, 6914001, 0.5, 0.5)
    )
    dst_dataset = rio.open(test_img_high)
    windows = windows_util_read.windows_transformed(
        dst_dataset.transform, dst_dataset.height, dst_dataset.width
    )
    list_windows = list(windows)
    out_ar = windows_util_read.upsample_window_array(
        list_windows[5][0], list_windows[5][1]
    )
    assert out_ar.shape == (1, list_windows[5][1].height, list_windows[5][1].width)


def test_windows_transformed(windows_util_write):
    test_dir = Path(tempfile.mkdtemp())
    test_img_high, _ = FakeGeoImage(800, 800, 1, "uint16", test_dir).create(
        seed=45, transform=from_origin(1470996, 6914001, 0.5, 0.5)
    )
    dst_dataset = rio.open(test_img_high)
    windows = windows_util_write.windows_transformed(
        dst_dataset.transform, dst_dataset.height, dst_dataset.width
    )
    list_windows = list(windows)
    assert len(list_windows) == 10
    # Check if one random window is transformed
    one_window = list_windows[5][1]
    assert one_window == Window(0.0, 400.0, 800.0, 80.0)


def test_limit_window_to_raster_bounds(windows_util_read):
    window = Window(0, 0, 100, 100)
    assert windows_util_read.limit_window_to_raster_bounds(window, 500, 500) == window

    window = Window(50, 50, 100, 100)
    assert windows_util_read.limit_window_to_raster_bounds(window, 500, 500) == window

    window = Window(0, 0, 101, 101)
    assert windows_util_read.limit_window_to_raster_bounds(window, 100, 100) == Window(
        0, 0, 100, 100
    )

    window = Window(-1, -1, 101, 101)
    assert windows_util_read.limit_window_to_raster_bounds(window, 100, 100) == Window(
        0, 0, 100, 100
    )

    window = Window(-1, -1, 100, 100)
    assert windows_util_read.limit_window_to_raster_bounds(window, 100, 100) == Window(
        0, 0, 99, 99
    )


def test_transform_window(windows_util_read):
    window = Window(0, 0, 100, 100)
    out_window = windows_util_read.transform_window(
        window, out_transform=from_origin(1470996, 6914001, 2.0, 2.0)
    )
    assert out_window == window

    out_window = windows_util_read.transform_window(
        window, out_transform=from_origin(1470996, 6914001, 0.5, 0.5)
    )
    assert out_window == Window(0, 0, 400, 400)


def test_crop_array_to_window(windows_util_read):
    np_array = np.ones((1, 55, 55))
    window = Window(0, 0, 50, 50)
    window_buffer = Window(0, 0, 55, 55)

    cropped_array = windows_util_read.crop_array_to_window(
        np_array, window, window_buffer
    )
    assert cropped_array.shape == (1, 50, 50)

    np_array = np.ones((1, 35, 35))
    window = Window.from_slices((25, 50), (25, 50))
    window_buffer = Window.from_slices((20, 55), (20, 55))

    cropped_array = windows_util_read.crop_array_to_window(
        np_array, window, window_buffer
    )
    assert cropped_array.shape == (1, 25, 25)

    np_array = np.ones((1, 524, 536))
    window = Window(col_off=512.0, row_off=0.0, width=512.0, height=512.0)
    window_buffer = Window(col_off=500.0, row_off=0.0, width=536.0, height=524.0)

    cropped_array = windows_util_read.crop_array_to_window(
        np_array, window, window_buffer
    )
    assert cropped_array.shape == (1, 512, 512)

    np_array = np.ones((1, 131, 63))
    window = Window(col_off=1024, row_off=0, width=60, height=128)
    window_buffer = Window(col_off=1021, row_off=0, width=63, height=131)

    cropped_array = windows_util_read.crop_array_to_window(
        np_array, window, window_buffer
    )
    assert cropped_array.shape == (1, 128, 60)


def test_buffer_window(windows_util_read):
    # shape of array is 1000,1000
    window = Window(0, 0, 100, 100)
    assert windows_util_read.buffer_window(window, 5) == Window(0, 0, 105, 105)

    window = Window(50, 50, 100, 100)
    assert windows_util_read.buffer_window(window, 5) == Window(45, 45, 110, 110)

    window = Window(900, 800, 100, 100)
    assert windows_util_read.buffer_window(window, 5) == Window(895, 795, 105, 110)
