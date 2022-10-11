"""Module for project directory setup.

Methods:
    create_dirs:                    Creates the main project directory
                                    and the associated subdirectories for the
                                    project.

    check_if_dir_exists:            Checks if the directory about to be created
                                    already exists.
"""
import os


def create_dirs(home_dir: str, directory_name: str) -> str:
    """Create the project directories.

    Creates directories for project files to be inserted.

    Examples:
        Example of use.

    Args:
        home_dir (str):         String value for the path to the
                                home directory.

        directory_name (str):   String value for the name of the
                                directory that is created.
    Returns:
        dir_path (str):         String value for the path to the
                                project's directory
    """
    dir_path = os.path.join(home_dir, directory_name)

    if check_if_dir_exists(dir_path):
        raise FileExistsError(f"Directory {directory_name} already exists")

    os.makedirs(dir_path)
    os.makedirs(os.path.join(dir_path, "data"))
    os.makedirs(os.path.join(dir_path, "data", "database"))
    os.makedirs(os.path.join(dir_path, "data", "excel_src"))
    os.makedirs(os.path.join(dir_path, "data", "duplicates"))
    # os.makedirs(os.path.join(dir_path, "data", "locations"))
    os.makedirs(os.path.join(dir_path, "report"))

    return dir_path


def check_if_dir_exists(dir_path: str) -> bool:
    """Check if directory exists.

    Args:
        dir_path (str):     String with path to the directory to check
                            if it exists.

    Returns:
        dir_exists (bool):  Boolean value representing whether the directory
                            exists or not.
    """
    dir_exists = os.path.exists(dir_path)
    return dir_exists
