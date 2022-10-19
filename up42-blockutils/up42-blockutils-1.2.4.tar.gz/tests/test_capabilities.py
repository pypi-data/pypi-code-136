from pathlib import Path
from geojson import Feature, Point
from blockutils.datapath import (
    set_data_path,
    get_data_path,
    get_output_filename_and_path,
)


def test_get_and_set_capability():
    feature = Feature(geometry=Point((1, 1)), properties={})
    set_data_path(feature, 1)
    assert get_data_path(feature) == 1


def test_get_output_filename_and_path():
    # No folder
    simple_file_name = "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(simple_file_name)
    assert output_file_name == simple_file_name
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()

    # With folder
    simple_file_name = "3159422e-6c53-4d97-9186-f52626f56b00/f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(simple_file_name)
    assert output_file_name == simple_file_name
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()

    # No folder, with postfix
    simple_file_name = "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(
        simple_file_name, postfix="test"
    )
    assert output_file_name == "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms_test.tif"
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()

    # With folder, with postfix
    simple_file_name = "3159422e-6c53-4d97-9186-f52626f56b00/f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(
        simple_file_name, postfix="test"
    )
    assert (
        output_file_name == "3159422e-6c53-4d97-9186-f52626f56b00/"
        "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms_test.tif"
    )
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()

    # No folder, with postfix and out_file_format
    simple_file_name = "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(
        simple_file_name, postfix="test", out_file_extension=".geojson"
    )
    assert output_file_name == "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms_test.geojson"
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()

    # No folder, no postfix and out_file_format
    simple_file_name = "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.tif"
    output_file_name, output_file_path = get_output_filename_and_path(
        simple_file_name, out_file_extension=".geojson"
    )
    assert output_file_name == "f4233636-12c6-4db0-aa90-6c08a3a492b5_ms.geojson"
    assert output_file_path == Path("/tmp/output") / output_file_name
    assert output_file_path.parent.exists()
