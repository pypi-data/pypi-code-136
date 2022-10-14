from pathlib import Path
from shutil import rmtree


def get_full_path(name):
    """Retrieve a playground folder from 'args'."""
    return Path(name).resolve()


def get_venv_dir(playground_dir):
    """Retrieve the virtual environment directory in a playground."""
    return playground_dir / ".venv"


def get_python_path(venv_path):
    """Attempt getting the path to Python in a virtual environment."""
    bin_path = venv_path / "bin"
    if bin_path.exists():
        return bin_path / "python"
    scripts_path = venv_path / "Scripts"
    return scripts_path / "python"


def get_command(python, module, args):
    """Creates a command from a path, module, and arguments."""
    cmd = [str(python), "-m", module, *args]
    return " ".join(cmd)


def remove_if_exists(folder):
    """Remove 'folder' if it exists."""
    if folder.exists():
        rmtree(folder)


def get_key(keys, config):
    if not keys:
        return config
    return get_key(keys[1:], config[keys[0]])


def set_key(keys, value, config):
    if len(keys) == 1:
        config.update({keys[0]: value})
        return config
    key = config[keys[0]]
    return set_key(keys[1:], value, key)


def delete_key(keys, config):
    if len(keys) == 1:
        del config[keys[0]]
        return config
    key = config[keys[0]]
    return delete_key(keys[1:], key)
