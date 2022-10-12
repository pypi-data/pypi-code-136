import os
import re
from os.path import join, exists

from repo_utils import find_definition, get_repository_path


def list_dependencies(path_or_def: str, package_name: str = None):
    """
    Determine dependencies within a repository or package.

    Args:
        - path_or_def (str): If a string with no /, locate the definition with find_definition
            and identify all dependencies by imports recursively.
            If a directory path, search for imports among all files at that path recursively in subfolders.
        - package_name (str): The package name used when importing (only these imports will be listed).
            If not provided, will use the path set at __meta__.py at the repository root (TODO).

    Returns:
        - dependencies (list): List of unique dependent definitions.
    """
    if path_or_def is None:
        path_or_def = get_repository_path()
    # if package_name is None:
    # exec(read("TODO/__meta__.py"), meta)
    if package_name is None:
        raise TypeError("list_dependencies: You must specify package_name used for imports.")

    filenames_to_search = []
    dependencies = []
    if not exists(path_or_def):
        # path_or_def is a definition name.
        # Search recursively for dependencies
        sub_deps = [path_or_def]
        already_checked = set()
        while len(sub_deps):
            dep = sub_deps.pop()
            if dep in already_checked:
                continue
            def_folder = find_definition(dep)
            if def_folder is None:
                print(f'list_dependencies: Definition {dep} not found.')
                continue
            def_path = join(find_definition(dep), f"{dep}.py")
            file_dependencies = list_file_dependencies(def_path, package_name)
            already_checked.add(dep)
            sub_deps.extend(file_dependencies)
            dependencies.extend(file_dependencies)
    else:
        # path_or_def is a folder path.
        for dirpath, dirs, files in os.walk(path_or_def):
            for filename in files:
                if not filename.endswith(".py"):
                    continue
                filepath = join(dirpath, filename)
                file_dependencies = list_file_dependencies(filepath, package_name)
                dependencies.extend(file_dependencies)
    return list(set(dependencies))


def list_file_dependencies(filepath, package_name):
    """
    Given a filepath, return a list of dependencies based on imports in just that file.

    Returns:
        - dependencies (list): List of dependent definitions in the order in which they were found.

    Implementation:
        1. Include the filename as a dependency if it's the same name as the containing folder.
    """
    dependencies = []
    split_filepath = filepath.split(os.sep)
    # 1. Include the filename as a dependency if it's the same name as the containing folder.
    if len(split_filepath) > 1:
        def_name = split_filepath[-1].strip().split(".")[0]
        if def_name == split_filepath[-2]:
            dependencies.append(split_filepath[-2])
    with open(filepath, "r") as file:
        within_parens = False
        after_slash = False
        for line in file.readlines():
            line = line.strip()
            if not after_slash and not within_parens and not line.startswith("from"):
                continue
            if after_slash or within_parens:
                after_slash = False
                if ')' in line:
                    within_parens = False
                    line = line.replace(')', ' ')
                split_imported = line.split(",")
                for imported in split_imported:
                    imported = imported.strip()
                    if imported:
                        dependencies.append(imported)
            line = line[4:].strip()  # Remove from.
            if line.startswith(package_name) or after_slash or within_parens:
                split_line = line.split("import")
                if len(split_line) > 1:
                    imported = split_line[1].strip()
                    if imported.startswith('('):
                        within_parens = True
                        imported = imported[1:]
                    elif imported.endswith('\\'):
                        after_slash = True
                    split_imported = imported.split(",")
                    for imported in split_imported:
                        imported = imported.strip()
                        if imported:
                            dependencies.append(imported)
    return dependencies
