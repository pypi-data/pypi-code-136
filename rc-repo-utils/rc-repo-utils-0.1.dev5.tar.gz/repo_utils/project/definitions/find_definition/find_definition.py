import os
from os.path import join
import inspect
import git


def find_definition(def_name: str, containing_folder: str=None, namespace: str = None):
    """
    Searches among modules directories and
    returns the directory path that matches def_name
    under the specified namespace directory

    Args:
        - containing_folder (str): Search only within this directory path. Current working directory by default.
        - namespace (str): Within containing_folder, find a folder with this name and search only under this folder.
    """
    if containing_folder is None:
        previous_frame = inspect.currentframe().f_back
        previous_previous_frame = previous_frame.f_back
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_previous_frame)
        if "<frozen" in filename or 'site-packages' in filename:
            (filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
        if 'repo_utils' in filename:
            # When using the repo_utils command line, use repository of the current working directory.
            filename = os.getcwd()
        repo = git.Repo(filename, search_parent_directories=True)
        src_root = repo.working_tree_dir
    else:
        src_root = containing_folder
    # src_root = join(repo_root, repo.name) # subfolder with same name
    # level_offset = len(src_root.split(os.sep)) - 1

    if namespace is None:
        for dir_path, dirs, _ in os.walk(src_root):
            if dir_path == "build" or dir_path.endswith(os.sep + "build"):
                continue
            for dir_name in dirs:
                if dir_name == def_name:
                    return join(dir_path, dir_name)
    else:
        for dir_path, dirs, _ in os.walk(src_root):
            for dir_name in dirs:
                if dir_name == "build":
                    continue
                if not namespace or dir_name == namespace:
                    for space_path, space_dirs, space_files in os.walk(
                        join(dir_path, dir_name)
                    ):
                        for def_dir in space_dirs:
                            if def_dir == def_name:
                                return join(space_path, def_dir)
                    if namespace:
                        break
    return None
