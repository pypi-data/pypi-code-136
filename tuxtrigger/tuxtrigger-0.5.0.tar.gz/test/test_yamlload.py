#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT


import logging
from unittest import mock
import pytest
from test.test_builder import MockedStdout
from tuxtrigger import yamlload

from tuxtrigger.inputvalidation import YamlValidator
from tuxtrigger.yamlload import (
    yaml_file_read,
    yaml_file_write,
    compare_sha,
)
from pathlib import Path

BASE = (Path(__file__) / "..").resolve()

ERROR_PATH = BASE / "./test_files/error_path.yaml"
HAPPY_PATH = BASE / "./test_files/happy_path.yaml"
FILE_TO_CREATE = BASE / "./test_files/new_file.yaml"
SCRIPT = BASE / ".test_files/test_script.sh"

VALUE_DICT = {
    "v5.19": {
        "sha": "2437f53721bcd154d50224acee23e7dbb8d8c622",
        "ref": "refs/tags/v5.19",
    }
}
VALUE = "v5.19"
RIGHT_KEY = "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"
WRONG_KEY = "/linux-not-existing"


def test_yaml_file_read():
    assert type(yaml_file_read(ERROR_PATH)) == dict


def test_create_repo_list(repo_setup_good):
    assert isinstance(next(repo_setup_good), YamlValidator) is True
    assert repo_setup_good is not None


def test_yaml_file_write(tmpdir):
    test_input = yaml_file_read(ERROR_PATH)
    yaml_file_write(test_input, (tmpdir / "test.yaml"))
    assert (tmpdir / "test.yaml").exists()


def test_compare_sha_correct(correct_archive_read):
    with pytest.raises(KeyError):
        compare_sha(WRONG_KEY, VALUE, VALUE_DICT, correct_archive_read)
    assert compare_sha(RIGHT_KEY, VALUE, VALUE_DICT, correct_archive_read) is True


def test_compare_sha_wrong(wrong_archive_read):
    assert compare_sha(WRONG_KEY, VALUE, VALUE_DICT, wrong_archive_read) is False
    assert compare_sha(RIGHT_KEY, VALUE, VALUE_DICT, wrong_archive_read) is False


@mock.patch("tuxtrigger.yamlload.subprocess.run")
def test_run_lsremote(mock_run):
    ls_remote = MockedStdout(
        returncode=0,
        stdout="0066f1b0e27556381402db3ff31f85d2a2265858        refs/heads/master",
    )
    mock_run.return_value = ls_remote
    assert yamlload.run_lsremote(
        "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git", "master"
    ) == {
        "master": {
            "ref": "refs/heads/master",
            "sha": "0066f1b0e27556381402db3ff31f85d2a2265858",
        }
    }


def test_pre_tux_run(correct_archive_read, caplog):
    with caplog.at_level(logging.INFO):
        yamlload.pre_tux_run(
            None,
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
            "v5.19",
            VALUE_DICT,
            correct_archive_read,
        )

    assert "No script path provided" in caplog.text
