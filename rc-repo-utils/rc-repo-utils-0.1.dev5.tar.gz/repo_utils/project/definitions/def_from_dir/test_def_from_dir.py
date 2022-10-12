from def_from_dir import def_from_dir

from repo_utils import find_definition


def test_def_from_dir():
    func = def_from_dir(find_definition("define"))
