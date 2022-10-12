import os
from os.path import join

import git

from repo_utils import def_from_dir


def import_all_defs(
    space_level: int = 1, load_defs: bool = True, search_def: str = None
):
    """Import all modules in the repository and return a dictionary of modules
    keyed by definition name
    if search_def is set, will stop search after finding the provided module name"""
    repo = git.Repo(os.getcwd(), search_parent_directories=True)
    repo_root = repo.working_tree_dir
    src_root = join(repo_root, "src")
    defs = {}
    # Find directories at the space level
    level_offset = len(src_root.split(os.sep)) - 1
    for dirpath, dirs, files in os.walk(src_root):
        dirsplits = dirpath.split(os.sep)
        level_count = len(dirsplits) - level_offset

        if level_count == space_level:
            # Use directories at this level as import spaces (namespaces)
            for dir_name in dirs:
                defs[dir_name] = {}
        elif level_count > space_level:
            if level_count == space_level + 1:
                # Set modules of space we're currently under
                # Note: os.walk is a depth-first search
                space_defs = defs.get(dirsplits[-1])
            # space_name = ntpath.basename(dirpath)
            # space_defs = defs[dir_name]
            # Use the
            # For each directory, find the definition file
            for dir_name in dirs:
                if dir_name.startswith("_"):
                    # e.g. __pycache__
                    continue
                def_path = join(dirpath, dir_name)
                print("def_path", def_path)
                try:
                    if load_defs:
                        # Get function with same name inside module
                        definition = def_from_dir(def_path)
                    else:
                        definition = def_path
                    print("definition", definition)
                    if definition:
                        space_defs[dir_name] = definition
                    if search_def is not None and search_def == dir_name:
                        break
                except FileNotFoundError:
                    pass
    return defs
