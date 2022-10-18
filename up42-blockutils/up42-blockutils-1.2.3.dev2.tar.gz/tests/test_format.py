# pylint: disable=C0411
# pylint: disable=line-too-long

import shutil
import sys
import zipfile
from pathlib import Path
from typing import List

import attr
import geojson
import pytest
from blockutils.common import TestDirectoryContext, ensure_data_directories_exist
from blockutils.exceptions import SupportedErrors, UP42Error
from blockutils.format import DimapFile, NetCDFFile, update_jsonfile
from blockutils.geometry import meta_is_equal
from blockutils.logging import get_logger
from blockutils.stac import STACQuery
from geojson import Feature, FeatureCollection, Polygon
from rasterio import Affine
from rasterio.crs import CRS

sys.path.append("..")

logger = get_logger(__name__)

INPUT_BASE = Path("/tmp/input")
DIMAP_ID = "f3092a17-cecc-4bad-9394-5263bc6663b3"
ORDER_ID = "e1d4aabb-bed0-4e17-87f9-4cbffadb0841"


@pytest.fixture(scope="session", autouse=True)
def prepare_test_data():
    with TestDirectoryContext(Path("/tmp")) as test_dir:
        _source_ = Path(__file__).resolve().parent / "mock_data" / f"{DIMAP_ID}.zip"
        # Extract the content of zip file to /tmp/input location
        with zipfile.ZipFile(_source_, "r") as zip_ref:
            zip_ref.extractall(INPUT_BASE)

        yield
        shutil.rmtree(str(INPUT_BASE / DIMAP_ID))


# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods
@attr.s
class DummyDimapFile:
    """
    This class initiate a dummy .DIMAP file.
    """

    # pylint: disable-msg=R0913, R0902
    location = attr.ib()
    file_path = attr.ib()
    feature_collection = attr.ib()
    feature = attr.ib()


@pytest.fixture(scope="session")  # pylint: disable=too-many-locals
def dimap_file():
    """
    This method creats a dummy DIMAP file.
    """

    # Set up the whole dummy input
    ensure_data_directories_exist()
    dimap_path = INPUT_BASE / DIMAP_ID
    order_id_path = dimap_path / ORDER_ID
    with open(dimap_path / "data.json", "rb") as f_p:
        test_featurecollection = geojson.load(f_p)

        test_dimap_file = DummyDimapFile(
            dimap_path,
            order_id_path,
            test_featurecollection,
            test_featurecollection.features[0],
        )
        return test_dimap_file


def test_get_dimap_path(dimap_file):
    expected_path = INPUT_BASE / DIMAP_ID / ORDER_ID
    assert DimapFile()._get_dimap_path(dimap_file.feature) == expected_path


def test_get_data_paths(dimap_file):
    data_paths = DimapFile()._get_data_paths(dimap_file.file_path)
    for mode in ["ms", "pan"]:
        assert mode in data_paths
        assert "base" in data_paths.get(mode)
        assert "metadata" in data_paths.get(mode)
        assert "data" in data_paths.get(mode)
        assert data_paths.get(mode).get("base").exists()
        assert data_paths.get(mode).get("metadata").exists()
        for path in data_paths.get(mode).get("data"):
            assert path.exists()


def test_check_dtype(dimap_file):
    expected_img_type = "uint16"
    assert DimapFile().check_dtype(dimap_file.feature) == expected_img_type


def test_open_xml_file_with_rasterio(dimap_file):
    src = DimapFile().open_xml_file_with_rasterio(
        Path(dimap_file.file_path).joinpath("IMG_PHR1B_MS_001")
    )
    expected_meta = {
        "driver": "DIMAP",
        "dtype": "uint16",
        "nodata": None,
        "width": 271,
        "height": 162,
        "count": 4,
        "crs": CRS.from_epsg(4326),
        "transform": Affine(
            2.957135816487319e-05,
            0.0,
            13.377254435760513,
            0.0,
            -2.9571358164891963e-05,
            52.50660784396914,
        ),
    }

    assert meta_is_equal(src.meta, expected_meta)


# pylint: disable=redefined-outer-name
def test_dimap_file_path(dimap_file):
    expected_dimap_file_path = (
        Path(dimap_file.file_path).joinpath("IMG_PHR1B_MS_001"),
        Path(dimap_file.file_path).joinpath("IMG_PHR1B_P_002"),
    )

    feature_list: List[Feature] = []
    bbox = [2.5, 1.0, 4.0, 5.0]
    x1, y1, x2, y2 = bbox
    geom = Polygon([[(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)]])
    in_properties = {
        "up42.data_path": "f3092a17-cecc-4bad-9394-5263bc6663b3/e1d4aabb-bed0-4e17-87f9-4cbffadb0841"
    }

    feature_list.append(Feature(geometry=geom, bbox=bbox, properties=in_properties))
    fc = FeatureCollection(feature_list)

    assert DimapFile().dimap_file_path(fc.features[0]) == expected_dimap_file_path


# pylint: disable=redefined-outer-name
def test_netcdf_file_path():
    expected_netcdf_file_path = Path(
        "/tmp/input/84758760-35ec-4047-aea6-526fe9840275/t_mean_2m_3h_C.nc"
    )

    feature_list: List[Feature] = []
    bbox = [2.5, 1.0, 4.0, 5.0]
    x1, y1, x2, y2 = bbox
    geom = Polygon([[(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)]])
    in_properties = {
        "up42.data_path": "84758760-35ec-4047-aea6-526fe9840275/t_mean_2m_3h_C.nc"
    }

    feature_list.append(Feature(geometry=geom, bbox=bbox, properties=in_properties))
    fc = FeatureCollection(feature_list)

    assert NetCDFFile().path_to_nc_file(fc.features[0]) == expected_netcdf_file_path


# pylint: disable=redefined-outer-name
def test_update_jsonfile():
    feature_list: List[Feature] = []
    bbox = [2.5, 1.0, 4.0, 5.0]
    x1, y1, x2, y2 = bbox
    geom = Polygon([[(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)]])
    in_properties = {
        "up42.data_path": "DS_PHR1B_201911300136059_FR1_PX_E139N35_1017_01542/"
        "b80af7d2-a6dd-4893-864f-e051e84846bf_ms.tif"
    }

    feature_list.append(Feature(geometry=geom, bbox=bbox, properties=in_properties))
    fc = FeatureCollection(feature_list)

    expected_dimap_cap = (
        "DS_PHR1B_201911300136059_FR1_PX_E139N35_1017_01542/"
        "b80af7d2-a6dd-4893-864f-e051e84846bf_ms.tif"
    )

    dimap_cap = update_jsonfile(fc.features[0], expected_dimap_cap)["properties"][
        "up42.data_path"
    ]

    assert dimap_cap == expected_dimap_cap


# pylint: disable=redefined-outer-name
def test_get_meta_input(dimap_file):
    mode_p = "pan"
    pan = DimapFile().get_meta_input(dimap_file.feature, mode_p)

    mode_m = "ms"
    ms = DimapFile().get_meta_input(dimap_file.feature, mode_m)

    assert ms.get("count") == 4
    assert pan.get("count") == 1
    assert ms.get("driver") == "DIMAP"
    assert pan.get("driver") == "DIMAP"
    assert ms.get("crs") == pan.get("crs")
    assert ms.get("height") == 162
    assert pan.get("height") == 648
    assert ms.get("width") == 271
    assert pan.get("width") == 1084


# pylint: disable=redefined-outer-name
def test_get_dim_xml_path(dimap_file):
    path = DimapFile().get_dim_xml_path(dimap_file.feature)
    expected_path = (
        Path(dimap_file.file_path).joinpath(
            "IMG_PHR1B_MS_001/DIM_PHR1B_MS_201810161039434_ORT_15007a44-dffa-41fe-c109-0d4fecabd40b-001.XML"
        ),
        Path(dimap_file.file_path).joinpath(
            "IMG_PHR1B_P_002/DIM_PHR1B_P_201810161039434_ORT_15007a44-dffa-41fe-c109-0d4fecabd40b-002.XML"
        ),
    )
    assert path == expected_path


# pylint: disable=redefined-outer-name
def test_read_image_as_raster(dimap_file):
    mode_m = "ms"
    mode_p = "pan"
    ms_np = DimapFile().read_image_as_raster(dimap_file.feature, mode_m)
    pan_np = DimapFile().read_image_as_raster(dimap_file.feature, mode_p)
    logger.info(f"{ms_np.shape}, {pan_np.shape}")
    assert ms_np.shape == (4, 162, 271)
    assert pan_np.shape == (1, 648, 1084)


def test_clip_and_read_image_as_raster(dimap_file):
    query = STACQuery.from_dict(
        {
            "bbox": [
                10.379974365234373,
                52.50340931136868,
                13.380,
                52.50542075023239,
            ]
        }
    )
    clipping_geometry = query.geometry()

    mode_m = "ms"
    mode_p = "pan"
    ms_np, _ = DimapFile().clip_and_read_image_as_raster(
        dimap_file.feature, mode_m, clipping_geometry
    )
    pan_np, _ = DimapFile().clip_and_read_image_as_raster(
        dimap_file.feature, mode_p, clipping_geometry
    )
    logger.info(f"{ms_np.shape}, {pan_np.shape}")
    assert ms_np.shape == (4, 69, 93)
    assert pan_np.shape == (1, 273, 372)


def test_error_on_clipping(dimap_file):
    query = STACQuery.from_dict(
        {
            "bbox": [
                14.379974365234373,
                52.50340931136868,
                14.383257389068604,
                52.50542075023239,
            ]
        }
    )
    clipping_geometry = query.geometry()
    mode_m = "ms"

    with pytest.raises(UP42Error) as excinfo:
        ms_np, _, _, _, _ = DimapFile().clip_and_read_image_as_raster(
            dimap_file.feature, mode_m, clipping_geometry
        )
        assert excinfo.type == SupportedErrors(2)
