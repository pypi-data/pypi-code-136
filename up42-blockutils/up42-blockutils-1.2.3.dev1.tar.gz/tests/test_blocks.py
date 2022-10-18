# Disable redifined names for fixtures
# pylint: disable=redefined-outer-name
import os
import json
from unittest.mock import patch
from pathlib import Path
import copy

import pytest

from geojson import FeatureCollection, Feature
from geojson.geometry import Polygon

from blockutils.blocks import DataBlock, ProcessingBlock
from blockutils.stac import STACQuery
from blockutils.datapath import DATA_PATH
from blockutils.common import TestDirectoryContext
from blockutils.exceptions import UP42Error, SupportedErrors

# pytest: disable=redefined-outer-name
@pytest.fixture()
def a_data_block():
    class ADataBlock(DataBlock):
        def fetch(self, query: STACQuery, dry_run: bool = False) -> FeatureCollection:
            return FeatureCollection((Feature()))

    return ADataBlock


@pytest.fixture()
def a_data_block_with_args():
    class ADataBlockArgs(DataBlock):
        def __init__(self, an_arg=5):
            self.an_arg = an_arg

        def fetch(self, query: STACQuery, dry_run: bool = False) -> FeatureCollection:
            return FeatureCollection((Feature()))

    return ADataBlockArgs


@pytest.fixture()
def a_processing_block():
    class AProcessingBlock(ProcessingBlock):
        def __init__(self, a_var):
            super().__init__()
            self.a_var = a_var

        def process(self, input_fc: FeatureCollection):
            self.a_var = 2
            return input_fc

    return AProcessingBlock


@pytest.fixture()
def metadata():
    return FeatureCollection(
        [
            Feature(
                geometry=Polygon(
                    coordinates=[
                        [
                            [-0.1696014404296875, 51.54249177614476],
                            [-0.215606689453125, 51.512588580360244],
                            [-0.12153625488281249, 51.47539580264131],
                            [-0.100250244140625, 51.505750806437874],
                            [-0.1696014404296875, 51.54249177614476],
                        ]
                    ]
                ),
                properties={
                    "name": "a_name",
                    "date": "a_date",
                    DATA_PATH: "a_file_path.tif",
                    "custom.data": "a_file_path.tif",
                },
            )
        ]
    )


def test_data_block(a_data_block):
    data_block = a_data_block()

    assert issubclass(a_data_block, DataBlock)
    assert data_block.fetch(STACQuery()) == FeatureCollection(Feature())


def test_data_block_with_args(a_data_block_with_args):
    data_block = a_data_block_with_args(15)
    data_block.an_arg = 15

    assert issubclass(a_data_block_with_args, DataBlock)
    assert data_block.fetch(STACQuery()) == FeatureCollection(Feature())


def test_processing_block(a_processing_block):
    processing_block = a_processing_block(1)

    assert issubclass(a_processing_block, ProcessingBlock)
    assert processing_block.process(FeatureCollection(Feature())) == FeatureCollection(
        Feature()
    )


def test_from_dict(a_processing_block):
    params_dict = {"a_var": 5}
    processing_block = a_processing_block.from_dict(params_dict)
    assert processing_block.a_var == 5


def test_get_metadata(a_processing_block, metadata):
    out_fc = a_processing_block.get_metadata(metadata.features[0])
    assert DATA_PATH not in out_fc
    assert "custom.data" not in out_fc
    assert out_fc.get("name") == "a_name"

    exp_out = copy.deepcopy(metadata.features[0])
    exp_out.properties.pop(DATA_PATH)
    exp_out.properties.pop("custom.data")
    assert out_fc == exp_out.properties


@patch.dict(os.environ, {"UP42_TASK_PARAMETERS": "{}"})
def test_run_data_block(a_data_block):
    with TestDirectoryContext(Path("/tmp")) as test_dir:
        a_data_block.run()
        assert (test_dir / "output/data.json").exists()
        with open(test_dir / "output/data.json", encoding="utf-8") as src:
            assert "features" in json.loads(src.read())


@patch.dict(os.environ, {"UP42_TASK_PARAMETERS": "{}"})
def test_run_data_block_with_args(a_data_block_with_args):
    with TestDirectoryContext(Path("/tmp")) as test_dir:
        a_data_block_with_args.run(an_arg=15)
        assert (test_dir / "output/data.json").exists()
        with open(test_dir / "output/data.json", encoding="utf-8") as src:
            assert "features" in json.loads(src.read())


@patch.dict(os.environ, {"UP42_TASK_PARAMETERS": '{"a_var": 5}'})
def test_run_processing_block(a_processing_block):
    with TestDirectoryContext(Path("/tmp")) as test_dir:
        a_processing_block.run()
        assert (test_dir / "output/data.json").exists()
        with open(test_dir / "output/data.json", encoding="utf-8") as src:
            assert json.loads(src.read())["features"] == []


# pylint: disable=no-self-use
@patch.dict(os.environ, {"UP42_TASK_PARAMETERS": '{"a_var": 5}'})
def test_exceptions(a_data_block, a_processing_block):
    class AErrorDataBlock(a_data_block):
        def fetch(self, query: STACQuery, dry_run: bool = False):
            raise UP42Error(SupportedErrors.API_CONNECTION_ERROR)

    class AErrorProcessingBlock(a_processing_block):
        def process(
            self, input_fc: FeatureCollection, process_dir: Path = Path("/tmp")
        ):
            raise UP42Error(SupportedErrors.NO_OUTPUT_ERROR)

    with pytest.raises(SystemExit) as e:
        AErrorDataBlock.run()
    assert e.value.code == SupportedErrors.API_CONNECTION_ERROR.value

    with pytest.raises(SystemExit) as e:
        AErrorProcessingBlock.run()
    assert e.value.code == SupportedErrors.NO_OUTPUT_ERROR.value
