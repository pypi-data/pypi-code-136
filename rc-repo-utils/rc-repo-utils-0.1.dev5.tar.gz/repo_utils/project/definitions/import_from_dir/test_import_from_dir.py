from os.path import join

from repo_utils import find_definition, get_repository_path, import_from_dir


def test_import_same_dir():
    mod = import_from_dir(join(get_repository_path(), "src", "functions"))
    assert mod
