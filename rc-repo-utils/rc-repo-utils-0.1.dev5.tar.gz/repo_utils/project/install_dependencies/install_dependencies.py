from repo_utils import list_dependencies, install_def

def install_dependencies(path_or_def: str, package_name: str, run_install_scripts=True):
    """

    Args:
        - path_or_def (str): If a string with no /, locate the definition with find_definition
            and identify all dependencies by imports recursively.
            If a directory path, search for imports among all files at that path recursively in subfolders.
        - package_name (str): The package name used when importing (only these imports will be listed).
            If not provided, will use the path set at __meta__.py at the repository root (TODO).
        - run_install_scripts (bool): If install is False, install.sh and install.py won't be run.

    Returns:
        -
    """
    for dep in list_dependencies(path_or_def, package_name):
        install_def(dep, install=run_install_scripts)
