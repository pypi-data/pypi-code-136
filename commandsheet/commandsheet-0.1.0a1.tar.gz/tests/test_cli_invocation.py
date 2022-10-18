from pathlib import Path
from contextlib import contextmanager
from commandsheet.const import XDG_CONFIG_PATH
import subprocess
import pytest


SUCCESS = 0


def test_runas_entrypoint():
    cmd = ('commandsheet', '--help',)
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == SUCCESS


def test_runas_module():
    cmd = ('python3', '-m', 'commandsheet', '--help',)
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == SUCCESS


def test_version_option():
    cmd = ('commandsheet', '--version',)
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == SUCCESS
    assert result.stdout.startswith('commandsheet')


@contextmanager
def no_config_file(path):
    """Temporarily renames the config file to
    make commandsheet think it does not exist,
    enabling us to simulate the scenario where
    the config file wouldn't actually exist.
    """
    exists = Path(path).expanduser().exists()
    original = str(Path(path).expanduser().parent) + '/' + 'commandsheet.ini'
    temp = str(Path(path).expanduser().parent) + '/' + '_commandsheet.ini'
    try:
        if exists:
            Path(original).replace(temp)
        yield
    finally:
        if exists:
            Path(temp).replace(original)


def test_invocation_without_existing_config_file():
    with no_config_file(XDG_CONFIG_PATH):
        cmd = ('commandsheet')
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert not result.returncode == SUCCESS


def test_config_file_option():
    cmd = ('commandsheet', '--config-file', 'example/commandsheet.ini')
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == SUCCESS

    cmd = ('commandsheet', '--config-file', 'invalid/path/to/file.invalid')
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert not result.returncode == SUCCESS

    cmd = ('commandsheet', '--config-file', 'setup.py')
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert not result.returncode == SUCCESS
