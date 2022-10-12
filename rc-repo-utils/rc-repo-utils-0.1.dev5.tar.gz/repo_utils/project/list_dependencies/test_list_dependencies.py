from os.path import join

from list_dependencies import list_dependencies

from repo_utils import find_definition, get_repository_path


def test_list_def_dependencies():
    deps = list_dependencies("find_definition", "repo_utils")
    assert deps
    assert "find_definition" in deps


def test_parentheses():
    deps = list_dependencies("simulate_definition", "repo_utils")
    assert deps
    assert "find_definition" in deps
    assert "import_from_dir" in deps
    assert "import_definition" in deps


def test_list_recursive_dependencies():
    deps = list_dependencies("enable_installing_dependencies", "repo_utils")
    assert deps
    expected_deps = [
        "find_definition",
        "get_repository_path",
        "list_dependencies",
        "enable_installing_dependencies",
    ]
    for dep in expected_deps:
        assert dep in deps


def test_list_folder_dependencies():
    deps = list_dependencies(find_definition("find_definition"), "repo_utils")
    assert deps
    assert "find_definition" in deps

    deps = list_dependencies(
        join(get_repository_path(), "repo_utils", "project"), "repo_utils"
    )
    assert deps
    expected_deps = [
        "find_definition",
        "get_repository_path",
        "install_def",
        "list_dependencies",
        "start_command_line",
        "test_def",
        "import_from_dir"
    ]
    for dep in expected_deps:
        assert dep in deps


def test_dep_from_import():
    deps = list_dependencies(find_definition("install_def"), "repo_utils")
    assert deps
    assert "find_definition" in deps
    assert "install_def" in deps


def test_multi_imports_on_same_line():
    deps = list_dependencies(find_definition("test_def"), "repo_utils")
    assert deps
    assert "find_definition" in deps
    assert "pytest_on_path" in deps
