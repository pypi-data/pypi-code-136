import os
import pathlib
import shutil
from os.path import join

from rename_def import rename_def

from repo_utils import define

curr_dir = pathlib.Path(__file__).parent.absolute()


def test_rename_def():
    try:
        shutil.rmtree(join(curr_dir, "target_def"))
    except Exception:
        pass
    define(join(curr_dir, "source_def"))
    result = rename_def("source_def", "target_def", namespace="functions")
    assert result
    assert os.path.isdir(join(curr_dir, "target_def"))
    assert not os.path.isdir(join(curr_dir, "source_def"))
    assert os.path.isfile(join(curr_dir, "target_def", "target_def.py"))

    # Remove test directory
    try:
        shutil.rmtree(join(curr_dir, "target_def"))
    except Exception:
        pass
