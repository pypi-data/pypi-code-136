from commandsheet.config import config_file_path_exists
from commandsheet.config import is_valid_config_file
from commandsheet.config import config_empty
from commandsheet.config import config_exists
from commandsheet.config import parse_config
from commandsheet.config import Section
from configparser import ConfigParser
from contextlib import contextmanager
from pathlib import Path
from os import chdir
import pytest


@contextmanager
def inside_dir(path):
    old_path = Path.cwd()
    try:
        chdir(path)
        yield
    finally:
        chdir(str(old_path))


def test_section():
    section = Section(name='section', contents=('cmd', 'desc'))
    assert section.name == 'section'
    assert section.contents == ('cmd', 'desc')


def test_config_empty():
    empty_config = ConfigParser()
    not_empty_config = ConfigParser()
    with inside_dir('example'):
        assert config_empty(empty_config)
        not_empty_config.read('commandsheet.ini')
        assert not config_empty(not_empty_config)


def test_config_exists():
    exist_file = 'commandsheet.ini'
    no_exist_file = 'no_exist_commandsheet.ini'
    with inside_dir('example'):
        assert config_exists(exist_file)
        assert not config_exists(no_exist_file)


def test_is_valid_config_file():
    assert is_valid_config_file('commandsheet.ini')
    assert is_valid_config_file('also-valid.ini')
    assert not is_valid_config_file('config.invalid')


def test_config_file_path_exists():
    assert not config_file_path_exists('invalid/path/to/file')
    with inside_dir('example'):
        assert config_file_path_exists('commandsheet.ini')


def test_parse_config():
    with inside_dir('example'):
        not_empty_commandsheet = parse_config('commandsheet.ini')
        assert not_empty_commandsheet != []
        empty_commandsheet = parse_config('')
        assert empty_commandsheet == []
