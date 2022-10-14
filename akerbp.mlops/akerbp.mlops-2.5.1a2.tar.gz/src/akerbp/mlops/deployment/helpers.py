# helpers.py
import shutil
import os
import subprocess
import venv
from importlib import resources as importlib_resources
from pathlib import Path
from typing import Dict
from akerbp.mlops import __version__
from akerbp.mlops.core import config, logger
from akerbp.mlops.core.config import ServiceSettings
from akerbp.mlops.core.exceptions import VirtualEnvironmentError

logging = logger.get_logger(name="mlops_deployment")

env = config.envs.env
service_name = config.envs.service_name


def get_repo_origin() -> str:
    """Get origin of the git repo

    Returns:
        (str): origin
    """
    origin = subprocess.check_output(
        ["git", "remote", "get-url", "--push", "origin"], encoding="UTF-8"
    ).rstrip()
    return origin


def replace_string_file(s_old: str, s_new: str, file: Path) -> None:
    """
    Replaces all occurrences of s_old with s_new in a specifyied file

    Args:
        s_old (str): old string
        s_new (str): new string
        file (Path): file to replace the string in
    """
    with file.open() as f:
        s = f.read()
        if s_old not in s:
            logging.warning(f"Didn't find '{s_old}' in {file}")

    with file.open("w") as f:
        s = s.replace(s_old, s_new)
        f.write(s)


def set_mlops_import(req_file: Path) -> None:
    """Set correct package version in requirements.txt

    Args:
        req_file (Path): path to requirements.txt for the model to deploy
    """
    package_version = __version__
    replace_string_file("MLOPS_VERSION", package_version, req_file)
    logging.info(f"Set akerbp.mlops=={package_version} in requirements.txt")


def to_folder(path: Path, folder_path: Path) -> None:
    """
    Copy folders, files or package data to a given folder.
    Note that if target exists it will be overwritten.

    Args:
        path: supported formats
            - file/folder path (Path): e,g, Path("my/folder")
            - module file (tuple/list): e.g. ("my.module", "my_file"). Module
            path has to be a string, but file name can be a Path object.
        folder_path (Path): folder to copy to
    """
    if isinstance(path, (tuple, list)):
        module_path, file = path
        file = str(file)
        if importlib_resources.is_resource(module_path, file):
            with importlib_resources.path(module_path, file) as file_path:
                shutil.copy(file_path, folder_path)
        else:
            raise ValueError(f"Didn't find {path[1]} in {path[0]}")
    elif path.is_dir():
        shutil.copytree(path, folder_path / path, dirs_exist_ok=True)
    elif path.is_file():
        shutil.copy(path, folder_path)
    else:
        raise ValueError(f"{path} should be a file, folder or package resource")


def copy_to_deployment_folder(lst: Dict, deployment_folder: Path) -> None:
    """
    Copy a list of files/folders to a deployment folder
    Logs the content of the deployment folder as a dictionary with keys being
    directory/subdirectory, and values the corresponding content

    Args:
        lst (dict): key is the nickname of the file/folder (used for
        logging) and the value is the path (see `to_folder` for supported
        formats)
        deployment_folder (Path): Path object for the deployment folder

    """
    for k, v in lst.items():
        if v:
            logging.debug(f"{k} => deployment folder")
            to_folder(v, deployment_folder)
        else:
            logging.warning(f"{k} has no value")
    dirwalk = os.walk(deployment_folder)
    content = {}
    for tup in dirwalk:
        if "__pycache__" in tup[0].split("/"):
            continue
        if (
            len(tup[1]) > 0 and "__pycache__" not in tup[1]
        ):  # includes subdirectories, skip pycache
            content[tup[0]] = tup[1] + tup[-1]
        else:
            content[tup[0]] = tup[-1]
    logging.debug(
        f"Deployment folder {deployment_folder} now contains the following: {content}"
    )


def install_requirements(req_file: str, venv_dir: str, **kwargs) -> None:
    """install model requirements

    Args:
        req_file (str): path to requirements file
    """
    with_deps = kwargs.get("with_deps", True)
    logging.info(f"Install python requirement file {req_file}")
    if with_deps:
        c = ["bin/pip", "install", "-r", os.path.abspath(req_file)]
    else:
        c = ["bin/pip", "install", "--no-deps", "-r", os.path.abspath(req_file)]
    subprocess.run(c, cwd=venv_dir)


def create_venv(venv_name: str) -> str:
    venv_dir = os.path.join(os.getcwd(), venv_name)
    logging.info(f"Creating virtual environment {venv_name}")
    venv.create(venv_dir, with_pip=True)
    if os.path.isdir(venv_dir):
        logging.info(f"Sucsessfully created virtual environment {venv_name}")
    else:
        raise VirtualEnvironmentError("Virtual environment was not created")
    return venv_dir


def delete_venv(venv_name: str) -> None:
    logging.info(f"Deleting virtual environment {venv_name}")
    subprocess.run(["rm", "-rf", os.path.abspath(venv_name)])
    if not os.path.isdir(os.path.abspath(venv_name)):
        logging.info("Virtual environment {venv_name} sucsessfully deleted")
    else:
        raise VirtualEnvironmentError("Virtual environment not deleted")


def set_up_requirements(c: ServiceSettings, **kwargs) -> str:
    """
    Set up a "requirements.txt" file at the top of the deployment folder
    (assumed to be the current directory), update config and install
    dependencies (unless in dev)

    Args:
        c (ServiceSettings): service settings a specified in the config file

    Keyword Args:
        install (bool): Whether to install the dependencies, defaults to True
    """
    logging.info("Create requirement file")
    install_reqs = kwargs.get("install", True)
    with_deps = kwargs.get("with_deps", True)
    unit_testing = kwargs.get("unit_testing", False)
    venv_name = kwargs.get("venv_name", "mlops-venv")
    setup_venv = kwargs.get("setup_venv", False)
    if setup_venv:
        venv_dir = create_venv(venv_name=venv_name)
    else:
        venv_dir = str(os.getcwd())
    set_mlops_import(c.req_file)
    if not unit_testing:
        shutil.copyfile(c.req_file, "requirements.txt")
        c.req_file = "requirements.txt"
    if env != "dev" or install_reqs:
        install_requirements(c.req_file, venv_dir=venv_dir, with_deps=with_deps)
    else:
        logging.info("Skipping installation of requirements.txt")
    return venv_dir  # type: ignore


def deployment_folder_path(model: str) -> Path:
    """Generate path to deployment folder, which is on the form "mlops_<model>"

    Args:
        model (str): model name

    Returns:
        Path: path to the deployment folder
    """
    return Path(f"mlops_{model}")


def rm_deployment_folder(model: str) -> None:
    logging.debug("Delete deployment folder")
    deployment_folder = deployment_folder_path(model)
    if deployment_folder.exists():
        shutil.rmtree(deployment_folder)
