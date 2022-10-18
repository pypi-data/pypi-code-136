import os
from pathlib import Path
import tempfile

import rasterio as rio
from rasterio.transform import from_origin
from mercantile import Tile
import numpy as np
import requests
import pytest

from fake_geo_images.fakegeoimages import FakeGeoImage
from blockutils.wmts import (
    TileMergeHelper,
    MultiTileMergeHelper,
    TileIsEmptyError,
    TileNotFetchedError,
)
from blockutils.exceptions import UP42Error
from blockutils.common import ensure_data_directories_exist

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# pylint: disable=redefined-outer-name
@pytest.fixture(scope="session", autouse=True)
def fixture():
    ensure_data_directories_exist()


@pytest.fixture(params=[True, False])
def fixture_wmts(request):
    def req():
        pass

    def get_wmts(tiles):
        return TileMergeHelper(
            tiles, req=req, parallelize=request.param, polling_cycle=0.1
        )

    return get_wmts


@pytest.fixture()
def fixture_mock_req():
    def mock_req(tile, **req_kwargs):
        del tile
        del req_kwargs
        return requests.Response()

    return mock_req


# pylint: disable=redefined-outer-name
@pytest.fixture()
def tif_files_list():
    td = tempfile.TemporaryDirectory()
    tmp_filepath1, _ = FakeGeoImage(
        xsize=10,
        ysize=10,
        num_bands=1,
        data_type="uint8",
        out_dir=Path(td.name).parent,
    ).create(seed=42)

    tmp_filepath2, _ = FakeGeoImage(
        xsize=10,
        ysize=10,
        num_bands=1,
        data_type="uint8",
        out_dir=Path(td.name).parent,
    ).create(
        seed=42,
        transform=from_origin(1470996, 6914021, 2.0, 2.0),
    )

    tmp_filepath3, _ = FakeGeoImage(
        xsize=10,
        ysize=10,
        num_bands=1,
        data_type="uint8",
        out_dir=Path(td.name).parent,
    ).create(seed=42)

    tmp_filepath4, _ = FakeGeoImage(
        xsize=10,
        ysize=10,
        num_bands=1,
        data_type="uint8",
        out_dir=Path(td.name).parent,
    ).create(
        seed=42,
        transform=from_origin(1470996, 6914021, 2.0, 2.0),
    )
    return tmp_filepath1, tmp_filepath2, tmp_filepath3, tmp_filepath4


@pytest.fixture()
def fixture_mock_process(tif_files_list):
    tmp_filepath1, tmp_filepath2, tmp_filepath3, tmp_filepath4 = tif_files_list

    def mock_process(response, tile):
        del response
        if tile == Tile(x=41955, y=101467, z=18):
            return tmp_filepath1
        if tile == Tile(x=41955, y=101468, z=18):
            return tmp_filepath2
        if tile == Tile(x=41955, y=101469, z=18):
            return tmp_filepath3
        else:
            return tmp_filepath4

    return mock_process


################################################################
# Beginning of test
################################################################
def test_tile_dataset(
    monkeypatch, fixture_wmts, fixture_mock_req, fixture_mock_process
):
    tiles = [Tile(x=41955, y=101467, z=18)]

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", fixture_mock_process)
    with wmts.tile_dataset() as (tile_tif_list, valid_tiles):
        assert len(tile_tif_list) == 1
        assert len(valid_tiles) == 1

    assert not tile_tif_list[0].exists()


def test_tile_dataset_multiple(
    monkeypatch, fixture_wmts, fixture_mock_req, fixture_mock_process
):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", fixture_mock_process)
    with wmts.tile_dataset() as (tile_tif_list, valid_tiles):
        assert len(tile_tif_list) == 2
        assert len(valid_tiles) == 2

    assert not tile_tif_list[0].exists()
    assert not tile_tif_list[1].exists()


def test_tile_dataset_mix(monkeypatch, tif_files_list, fixture_wmts, fixture_mock_req):
    tmp_filepath1, _, _, _ = tif_files_list
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_process(response, tile):
        del response
        if tile == Tile(x=41955, y=101467, z=18):
            return tmp_filepath1
        else:
            raise TileIsEmptyError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", mock_process)
    with wmts.tile_dataset() as (tile_tif_list, valid_tiles):
        assert len(tile_tif_list) == 1
        assert len(valid_tiles) == 1

    assert not tile_tif_list[0].exists()


def test_tile_dataset_all_empty(monkeypatch, fixture_wmts, fixture_mock_req):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_process(response, tile):
        raise TileIsEmptyError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", mock_process)
    with wmts.tile_dataset() as (tile_tif_list, valid_tiles):
        assert not tile_tif_list
        assert not valid_tiles


def test_tile_worker_not_fetching(monkeypatch, fixture_wmts):
    tile_tif_list = []
    valid_tiles = []
    tiles_not_fetched = []
    tiles = [Tile(x=41955, y=101467, z=18)]

    def mock_req(tile, **req_kwargs):
        del tile
        del req_kwargs
        raise TileNotFetchedError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", mock_req)
    wmts.tile_worker(tiles[0], tile_tif_list, valid_tiles, tiles_not_fetched)
    assert len(tiles_not_fetched) == 1


def test_tile_iterator_one_tile_not_fetched(
    monkeypatch, fixture_wmts, fixture_mock_process
):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_req(tile, **req_kwargs):
        del req_kwargs
        if tile == Tile(x=41955, y=101468, z=18):
            raise TileNotFetchedError
        return requests.Response()

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", mock_req)
    monkeypatch.setattr(wmts, "_process", fixture_mock_process)
    with pytest.raises(UP42Error, match=r".*['API_CONNECTION_ERROR'].*"):
        wmts.loop_over_tiles()


def test_tile_iterator_all_tiles_not_fetched_api_error(monkeypatch, fixture_wmts):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_req(tile, **req_kwargs):
        del req_kwargs
        del tile
        raise TileNotFetchedError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", mock_req)
    with pytest.raises(UP42Error, match=r".*['API_CONNECTION_ERROR'].*"):
        wmts.loop_over_tiles()


# pylint: disable=protected-access
def test_process(monkeypatch):
    tile = Tile(x=41955, y=101468, z=18)

    with open(os.path.join(LOCATION, "mock_data/tile_1.png"), "rb") as image:
        img_byte = bytearray(image.read())

    monkeypatch.setattr(requests.models.Response, "content", img_byte)

    temp_tif = TileMergeHelper._process(requests.Response(), tile)
    assert temp_tif.is_file()
    with rio.open(temp_tif) as src:
        assert src.meta["crs"] == {"init": "epsg:3857"}
        assert src.meta["driver"] == "GTiff"


# pylint: disable=protected-access
def test_process_corrupted_response(monkeypatch):
    tile = Tile(x=41955, y=101468, z=18)
    # A corrupted response in bytes because of an extra "`" in the beginning
    img_byte = b"`\x00\x00\x00\x00\x0b\x00\x1f\x00\x00\x00"

    monkeypatch.setattr(requests.models.Response, "content", img_byte)

    with pytest.raises(UP42Error, match=r".*['API_CONNECTION_ERROR'].*"):
        TileMergeHelper._process(requests.Response(), tile)


# pylint: disable=protected-access
def test_process_empty_tile(monkeypatch):
    tile = Tile(x=120835, y=146897, z=18)

    with open(os.path.join(LOCATION, "mock_data/empty_tile.png"), "rb") as image:
        img_byte = bytearray(image.read())

    monkeypatch.setattr(requests.models.Response, "content", img_byte)

    with pytest.raises(TileIsEmptyError):
        TileMergeHelper._process(requests.Response(), tile)


def test_merge_tiles(tif_files_list):
    merged_array, _, temp_meta = TileMergeHelper.merge_tiles(tif_files_list)
    assert merged_array.shape == (1, 20, 10)
    assert temp_meta["width"] == 10
    assert temp_meta["height"] == 10
    for tiffile in tif_files_list:
        os.remove(tiffile)


def test_merge_tiles_empty():
    with pytest.raises(UP42Error, match=r".*[NO_INPUT_ERROR].*"):
        TileMergeHelper.merge_tiles([])


def test_write_final_merged_image(fixture_wmts):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]
    with tempfile.TemporaryDirectory() as td:
        tmp_filepath, tmp_ar = FakeGeoImage(
            xsize=10,
            ysize=10,
            num_bands=4,
            data_type="uint8",
            out_dir=Path(td),
        ).create(seed=42, file_name="tmp")
        with rio.open(tmp_filepath) as src:
            in_trans = src.transform
            in_meta = src.meta

        img_filename = Path(td) / "final.tif"
        out_arr = np.resize(tmp_ar, (4, 20, 20))

        wmts = fixture_wmts(tiles)
        wmts.write_merged_tiles(img_filename, out_arr, in_trans, in_meta, tile_size=10)
        assert os.path.exists(Path(td) / "final.tif")
        with rio.open(Path(td) / "final.tif") as src:
            assert src.count == 4
            assert src.width == 20
            assert src.transform == in_trans


def test_get_final_image(
    monkeypatch, fixture_wmts, fixture_mock_req, fixture_mock_process
):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", fixture_mock_process)

    output_path = Path("/tmp/output/final.tif")
    valid_tiles = wmts.get_final_image(output_path)
    assert os.path.exists(output_path)
    assert len(valid_tiles) == 2
    with rio.open(output_path) as src:
        assert src.count == 1
        assert src.width == 10
        assert src.height == 20


def test_get_final_image_mix(
    monkeypatch, tif_files_list, fixture_wmts, fixture_mock_req
):
    tmp_filepath1, _, _, _ = tif_files_list
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_process(response, tile):
        del response
        if tile == Tile(x=41955, y=101467, z=18):
            return tmp_filepath1
        else:
            raise TileIsEmptyError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", mock_process)

    output_path = Path("/tmp/output/final.tif")
    valid_tiles = wmts.get_final_image(output_path)
    assert os.path.exists(output_path)
    assert len(valid_tiles) == 1
    with rio.open(output_path) as src:
        assert src.count == 1
        assert src.width == 10
        assert src.height == 10


def test_get_final_image_all_empty(monkeypatch, fixture_wmts, fixture_mock_req):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_process(response, tile):
        del response
        del tile
        raise TileIsEmptyError

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", fixture_mock_req)
    monkeypatch.setattr(wmts, "_process", mock_process)

    output_path = Path("/tmp/output/final.tif")
    with pytest.raises(UP42Error, match=r".*['NO_INPUT_ERROR'].*"):
        _ = wmts.get_final_image(output_path)


def test_get_final_image_with_unfetched_tile(
    monkeypatch, fixture_wmts, fixture_mock_process
):
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def mock_req(tile, **req_kwargs):
        del req_kwargs
        if tile == Tile(x=41955, y=101468, z=18):
            raise TileNotFetchedError
        return requests.Response()

    wmts = fixture_wmts(tiles)
    monkeypatch.setattr(wmts, "req", mock_req)
    monkeypatch.setattr(wmts, "_process", fixture_mock_process)
    with pytest.raises(UP42Error, match=r".*['API_CONNECTION_ERROR'].*"):
        wmts.loop_over_tiles()


# pylint: disable=too-many-locals
def test_get_multiple_tif(
    fixture_wmts, monkeypatch, fixture_mock_req, fixture_mock_process
):
    band_descriptions = ["a", "b"]
    filename_path = Path("/tmp/multi_tif.tif")

    tiles_1 = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]
    tiles_2 = [Tile(x=41955, y=101469, z=18), Tile(x=41955, y=101470, z=18)]

    wmts_1 = fixture_wmts(tiles_1)
    monkeypatch.setattr(wmts_1, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_1, "_process", fixture_mock_process)
    wmts_2 = fixture_wmts(tiles_2)
    monkeypatch.setattr(wmts_2, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_2, "_process", fixture_mock_process)
    tilemergehelper_list = [wmts_1, wmts_2]
    valid_tiles = MultiTileMergeHelper(tilemergehelper_list).get_multiband_tif(
        filename_path, band_descriptions
    )
    assert os.path.exists(filename_path)
    assert isinstance(valid_tiles, dict)
    assert valid_tiles["a"] == [
        Tile(x=41955, y=101467, z=18),
        Tile(x=41955, y=101468, z=18),
    ]
    assert valid_tiles["b"] == [
        Tile(x=41955, y=101469, z=18),
        Tile(x=41955, y=101470, z=18),
    ]
    with rio.open(filename_path) as src:
        assert src.count == 2
        assert src.width == 10
        assert src.height == 20
        assert src.descriptions == ("a", "b")

    os.remove(filename_path)


# pylint: disable=too-many-locals
def test_get_multiple_tif_without_to_cog(
    fixture_wmts, monkeypatch, fixture_mock_req, fixture_mock_process
):
    band_descriptions = ["a", "b"]
    filename_path = Path("/tmp/multi_tif.tif")

    tiles_1 = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]
    tiles_2 = [Tile(x=41955, y=101469, z=18), Tile(x=41955, y=101470, z=18)]

    wmts_1 = fixture_wmts(tiles_1)
    monkeypatch.setattr(wmts_1, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_1, "_process", fixture_mock_process)
    wmts_2 = fixture_wmts(tiles_2)
    monkeypatch.setattr(wmts_2, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_2, "_process", fixture_mock_process)
    tilemergehelper_list = [wmts_1, wmts_2]
    valid_tiles = MultiTileMergeHelper(tilemergehelper_list).get_multiband_tif(
        filename_path, band_descriptions, return_cog=False
    )
    assert os.path.exists(filename_path)
    assert isinstance(valid_tiles, dict)
    assert valid_tiles["a"] == [
        Tile(x=41955, y=101467, z=18),
        Tile(x=41955, y=101468, z=18),
    ]
    assert valid_tiles["b"] == [
        Tile(x=41955, y=101469, z=18),
        Tile(x=41955, y=101470, z=18),
    ]
    with rio.open(filename_path) as src:
        assert src.count == 2
        assert src.width == 10
        assert src.height == 20
        assert src.descriptions == ("a", "b")
        assert "compress" not in src.profile

    os.remove(filename_path)


def test_get_multiple_tif_passing_no_descriptions(
    fixture_wmts, monkeypatch, fixture_mock_req, fixture_mock_process
):
    filename_path = Path("/tmp/multi_tif.tif")

    tiles_1 = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]
    tiles_2 = [Tile(x=41955, y=101469, z=18), Tile(x=41955, y=101470, z=18)]

    wmts_1 = fixture_wmts(tiles_1)
    monkeypatch.setattr(wmts_1, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_1, "_process", fixture_mock_process)
    wmts_2 = fixture_wmts(tiles_2)
    monkeypatch.setattr(wmts_2, "req", fixture_mock_req)
    monkeypatch.setattr(wmts_2, "_process", fixture_mock_process)
    tilemergehelper_list = [wmts_1, wmts_2]
    valid_tiles = MultiTileMergeHelper(tilemergehelper_list).get_multiband_tif(
        filename_path
    )

    assert os.path.exists(filename_path)
    assert isinstance(valid_tiles, dict)
    assert list(valid_tiles.keys()) == [0, 1]
    assert valid_tiles[0] == [
        Tile(x=41955, y=101467, z=18),
        Tile(x=41955, y=101468, z=18),
    ]
    assert valid_tiles[1] == [
        Tile(x=41955, y=101469, z=18),
        Tile(x=41955, y=101470, z=18),
    ]
    with rio.open(filename_path) as src:
        assert src.count == 2
        assert src.width == 10
        assert src.height == 20
        assert not all(src.descriptions)

    os.remove(filename_path)


def test_from_req_kwargs():
    kwargs_list = [{"polling_cycle": 3}, {"polling_cycle": 0.4}]
    tiles = [Tile(x=41955, y=101467, z=18), Tile(x=41955, y=101468, z=18)]

    def req():
        pass

    def process():
        pass

    new_class = MultiTileMergeHelper.from_req_kwargs(
        tiles, req=req, kwargs_list=kwargs_list, process=process
    )
    assert new_class.tilemergehelper_list[0].polling_cycle == 3
    assert new_class.tilemergehelper_list[1].polling_cycle == 0.4
