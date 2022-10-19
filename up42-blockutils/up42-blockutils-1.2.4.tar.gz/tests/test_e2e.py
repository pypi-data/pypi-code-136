from pathlib import Path
from blockutils.e2e import E2ETest


def test_init():
    e2e = E2ETest("some_block_name")

    assert e2e.image_name == "some_block_name"
    assert e2e.variant == ""

    assert e2e.delete_output == e2e.in_ci
    assert e2e.test_dir == Path("/tmp/e2e_some_block_name")
    assert e2e.expected_exit_code == 0
