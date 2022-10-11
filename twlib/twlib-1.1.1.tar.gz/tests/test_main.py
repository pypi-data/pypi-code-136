from pathlib import Path

import pytest

from twlib.environment import ROOT_DIR

# noinspection PyProtectedMember
from twlib.main import _convert_heif


# noinspection PyPep8Naming
def test__convert_heif():
    INPUT_FILE = ROOT_DIR / "tests" / "resources" / "input.heic"
    OUTPUT_FILE = ROOT_DIR / "tests" / "resources" / "input.jpg"
    OUTPUT_FILE.unlink(missing_ok=True)

    _convert_heif(input_file=INPUT_FILE, mode="jpg", out_file=None)
    assert Path(OUTPUT_FILE).exists()


# noinspection PyPep8Naming
@pytest.mark.skip("Long running test")
def test__convert_heif_png_custom_path():
    INPUT_FILE = ROOT_DIR / "tests" / "resources" / "input.heic"
    OUTPUT_FILE = Path("/tmp/xxx.png")
    OUTPUT_FILE.unlink(missing_ok=True)

    _convert_heif(input_file=INPUT_FILE, mode="png", out_file=str(OUTPUT_FILE))
    assert Path(OUTPUT_FILE).exists()
