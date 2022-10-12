import os
from os.path import join
from pathlib import Path
from shutil import move

from repo_utils import find_definition


def rename_def(def_name: str, target_name: str, namespace: str = None):
    """
    Change the name of a definition
    Make any needed changes to its folder, files,
    and any imports of the definition
    The definition with name def_name in namespace will be
    changed to target_name
    Return True if successful, False otherwise (e.g. no definition found)
    """
    def_dir = find_definition(def_name, namespace)
    if def_dir:
        path = Path(def_dir)
        parent_dir = path.parent
        target_dir = os.path.join(parent_dir, target_name)
        if os.path.exists(target_dir):
            print(f"Aborting move since directory exists: {target_dir}")
            return False
        move(def_dir, target_dir)
        # Use new name on all files of the directory
        # Note: This doesn't search files recursively
        # and doesn't include directories
        files = os.listdir(target_dir)
        for filename in files:
            # Replace file names
            source_path = join(target_dir, filename)
            if def_name in filename and os.path.isfile(source_path):
                new_name = filename.replace(def_name, target_name)
                move(source_path, join(target_dir, new_name))
                filename = join(target_dir, new_name)
            # Replace mentions in files
            if os.path.isfile(filename):
                new_text = None
                with open(filename, "r") as file:
                    text = file.read()
                    if text:
                        new_text = text.replace(def_name, target_name)
                if new_text:
                    with open(filename, "w") as file:
                        file.write(new_text)
        return True
    print(f'Definition {def_dir} not found.')
    return False
