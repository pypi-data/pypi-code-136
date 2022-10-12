import os
import pathlib
import shutil

from define import define

curr_dir = pathlib.Path(__file__).parent.absolute()


def test_define():
    name = "test_def_test"
    name_dir = os.path.join(curr_dir, "test_def_test")
    # Remove test directory if it's already there
    try:
        shutil.rmtree(name_dir)
    except Exception:
        pass

    define(name_dir)
    # Folder
    assert os.path.exists(name_dir)
    # Definition file
    assert os.path.exists(os.path.join(name_dir, name + ".py"))
    # Test file
    assert os.path.exists(os.path.join(name_dir, "test_" + name + ".py"))

    # Remove test directory
    shutil.rmtree(name_dir)


def test_define_path():
    name_dir = os.path.join(curr_dir, "test_def_test")
    # Remove test directory if it's already there
    try:
        shutil.rmtree(name_dir)
    except Exception:
        pass

    define(name_dir)
    # Folder
    assert os.path.exists(name_dir)
    # Definition file
    assert os.path.exists(os.path.join(name_dir, "test_def_test.py"))
    # Test file
    assert os.path.exists(os.path.join(name_dir, "test_test_def_test.py"))

    # Remove test directory
    shutil.rmtree(name_dir)
