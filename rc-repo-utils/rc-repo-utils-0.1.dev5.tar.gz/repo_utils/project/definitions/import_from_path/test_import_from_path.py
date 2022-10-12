import types

import git
from import_from_path import import_from_path


def test_import_from_path():
    repo = git.Repo(__file__, search_parent_directories=True)
    repo_root = repo.working_tree_dir
    mod = import_from_path(
        f"{repo_root}/src/functions/project/definitions/define/define.py"
    )
    assert type(mod) == types.ModuleType


def test_import_relative():
    mod = import_from_path("import_from_path")
    assert type(mod) == types.ModuleType
