from os.path import exists, join

from repo_utils import find_definition, list_dependencies


def enable_installing_dependencies(path_or_def: str = None, package_name: str = None):
    """
    Create an __init__.py file in the necessary folders so that these are included in the package installation.
    Optionally specify a path from which to determine dependencies,
        so only the required definitions will be installed.

    Args:
        - path_or_def (str): If a string with no /, locate the definition with find_definition
            and identify all dependencies by imports recursively.
            If a directory path, search for imports among all files at that path recursively in subfolders.
            If not provided, the repository root will be used as the path and an init file
                will be created in every directory that has a file with the same name.
        - package_name (str): The package name used when importing (only these imports will be listed).

    Returns:
        - init_filepaths (list of str): Filepaths of init files created.
    """
    init_filepaths = []
    deps = list_dependencies(path_or_def, package_name)
    for dep in deps:
        def_path = find_definition(dep)
        if def_path is None:
            continue
        init_filepath = join(def_path, "__init__.py")
        if not exists(init_filepath):
            with open(init_filepath, "w") as file:
                pass
            init_filepaths.append(init_filepath)
    return init_filepaths
