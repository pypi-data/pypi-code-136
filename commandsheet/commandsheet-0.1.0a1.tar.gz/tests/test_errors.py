"""Tests for testing CLI errors."""

from io import StringIO
from contextlib import redirect_stderr
from commandsheet.cli import CustomArgumentParser
from commandsheet.errors import no_config_file_found
from commandsheet.errors import no_config_file_sections_found
from commandsheet.errors import no_config_file_path_exists
from commandsheet.errors import not_a_valid_config_file
import pytest


def test_no_config_file_found():
    parser = CustomArgumentParser()
    with pytest.raises(SystemExit):
        no_config_file_found(parser)


def test_no_config_file_sections_found():
    parser = CustomArgumentParser()
    with pytest.raises(SystemExit):
        no_config_file_sections_found(parser)


def test_no_config_file_path_exists():
    parser = CustomArgumentParser()
    file = '/invalid/path/to/file.ini'
    with pytest.raises(SystemExit):
        no_config_file_path_exists(parser, file=file)


def test_not_a_valid_config_file():
    parser = CustomArgumentParser()
    file = '/path/to/invalid/configfile.invalid'
    with pytest.raises(SystemExit):
        not_a_valid_config_file(parser, file=file)
