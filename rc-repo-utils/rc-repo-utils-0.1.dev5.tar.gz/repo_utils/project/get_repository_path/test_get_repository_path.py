import os

from get_repository_path import get_repository_path


def test_get_repository_path():
    assert "src" in os.listdir(get_repository_path())
