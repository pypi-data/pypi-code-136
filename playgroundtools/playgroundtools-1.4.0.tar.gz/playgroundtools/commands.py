import json
import os
import venv
from shutil import rmtree

from . import ABOUT_TEXT, APP_NAME, VERSION
from .exceptions import set_status
from .playground import clean_config, get_config, set_config
from .util import get_command, get_python_path, get_venv_dir, remove_if_exists

# Functions for the parser


def print_about():
    """Print text about the package."""
    print(ABOUT_TEXT)


def print_version():
    """Print the package version."""
    print(f"{APP_NAME} version {VERSION}")


# Functions for the 'new' command


def new(args, status=None):
    """Create a new playground."""
    raw_config = get_config()
    config = clean_config(args, raw_config)
    vb = config["verbosity"]

    new_playground(config["dir"], verbose=vb, status=status)
    new_folders(config["dir"], config["folders"], verbose=vb, status=status)
    new_files(config["dir"], config["files"], verbose=vb, status=status)
    new_settings(config["dir"], config["settings"], verbose=vb, status=status)
    new_venv(config["dir"], verbose=vb, status=status)
    install_reqs(config["dir"], verbose=vb, status=status)

    set_status("Playground creation successful.", status)


def new_playground(playground_dir, verbose=0, status=None):
    """Create the playground folder."""
    if verbose:
        set_status("Creating the playground folder...", status)
    remove_if_exists(playground_dir)
    playground_dir.mkdir()


def new_folders(playground_dir, folders, verbose=0, status=None):
    """Create all folders for a playground."""
    if verbose:
        set_status("Creating necessary folders...", status)
    for folder in folders:
        folder_path = playground_dir / folder
        if verbose > 1:
            print("\t", end="")
            set_status(f"Creating {folder_path}", status)
        folder_path.mkdir(exist_ok=True)


def new_files(playground_dir, files, verbose=0, status=None):
    """Create all files for a playground."""
    if verbose:
        set_status("Creating necessary files...", status)
    for name, content in files.items():
        file_path = playground_dir / name
        if verbose > 1:
            print("\t", end="")
            set_status(f"Creating {file_path}", status)
        with open(file_path, "w") as f:
            for line in content:
                print(line, file=f)


def new_settings(playground_dir, settings, verbose=0, status=None):
    """Create the settings file for a playground."""
    if verbose:
        set_status("Creating the settings file...", status)
    venv_path = get_venv_dir(playground_dir)
    python_path = get_python_path(venv_path)
    settings = {"python": str(python_path), **settings}

    settings_path = playground_dir / "settings.json"
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)


def new_venv(playground_dir, verbose=0, status=None):
    """Create a virtual environment for a playground."""
    if verbose:
        set_status("Creating the virtual environment...", status)
    venv_path = get_venv_dir(playground_dir)
    venv.create(venv_path, with_pip=True)


def install_reqs(playground_dir, verbose=0, status=None):
    """Install the packages from a playground's requirements file."""
    if verbose:
        set_status("Installing requirements...", status)
    venv_path = get_venv_dir(playground_dir)
    python_path = get_python_path(venv_path)
    reqs_path = playground_dir / "requirements" / "requirements.in"
    os.system(f"{python_path} -m pip install --no-cache-dir -r {reqs_path}")


# Functions for the 'delete' command


def delete(args, status=None):
    """Delete a playground."""
    config = clean_config(args)
    rmtree(config["dir"])

    set_status("Playground deletion successful.", status)


# Functions for the 'run' command


def run(args):
    """Run a playground."""
    config = clean_config(args)
    cmd = get_command(**config["settings"])
    os.chdir(config["dir"])
    os.system(cmd)


# Functions for the 'config' command


def config(args, status=None):
    """Read or modify the configuration."""
    raw_config = get_config()

    config = clean_config(args, raw_config)
    if args.subcommand:
        set_config(config)
        set_status("Configuration modified successfully.", status)
    elif args.read:
        value = config["value"]
        print_json(value)
        return value
    else:
        print_json(config)
    return config


def print_json(value):
    value_json = json.dumps(value, indent=4)
    print(value_json)
