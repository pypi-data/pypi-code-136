import os
from os.path import exists, join

from enable_installing_dependencies import enable_installing_dependencies

from repo_utils import find_definition


def test_enable_installing_dependencies():
    test_path = None

    assert not exists(
        join(find_definition("enable_installing_dependencies"), "__init__.py")
    )
    init_filepaths = enable_installing_dependencies(
        "enable_installing_dependencies", package_name="repo_utils"
    )
    assert exists(
        join(find_definition("enable_installing_dependencies"), "__init__.py")
    )

    for filepath in init_filepaths:
        if exists(filepath):
            os.remove(filepath)
