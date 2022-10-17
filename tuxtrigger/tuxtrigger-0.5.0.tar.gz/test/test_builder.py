#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT


import json
from requests import Session
from unittest import mock

import pytest

from pathlib import Path
from tuxtrigger.builder import (
    compare_squad_sha,
    squad_metadata_request,
    squad_submit,
    tux_console_build,
    tux_console_plan,
    build_result,
)
from tuxtrigger.exceptions import SquadException, TuxtriggerException, TuxsuiteException

BASE = (Path(__file__) / "..").resolve()

PLAN = BASE / "test_files/planTest.yaml"
PLAN_FAIL = BASE / "test_files/planTestc.yaml"
JSON_PLAN_RESULT = BASE / "test_files/plan_result.json"
JSON_OUT = BASE / "test_files/"

UID = "2CCI3BkwKdqM4wOOwB5xRRxvOha"
FINGERPRINT = "8fa23329efa65477f077d99e145e4087190a55cc"

PARAMS = {
    "git_repo": "https://gitlab.com/Linaro/lkft/mirrors/stable/linux-stable-rc",
    "git_ref": "master",
    "target_arch": "x86_64",
    "toolchain": "gcc-12",
    "kconfig": "tinyconfig",
}
JSON_DATA = {
    "empty": "no_real_values",
    "uid": "1234",
    "git_repo": "https://gitlab.com/no_real_repo",
    "git_ref": "master",
    "git_sha": "6fae37b8a05e58b6103198e89d12dc0d6d472d92",
    "git_describe": "test-rc",
}
JSON_BUILD_DATA = {
    "state": "provisioning",
    "result": "None",
    "uid": "1234",
    "git_repo": "https://gitlab.com/no_real_repo",
    "git_ref": "master",
    "git_describe": "test-rc",
}

JSON_RESPONSE = """{
"count":1,
"git_sha":"1234",
"fingerprint":"8fa23329efa65477f077d99e145e4087190a55cc",
"results":[
{
"metadata":"https://www.example_metadata.pl",
"id":1234
}
]
}"""


class MockedStdout:
    def __init__(self, returncode, stdout, stderr=None) -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


class MockedSession:
    def __init__(self, status_code, content) -> None:
        self.status_code = status_code
        self.content = content


@mock.patch("tuxtrigger.builder.subprocess.run")
@mock.patch("tempfile.NamedTemporaryFile")
def test_tux_console_build(mock_temp_file, mock_run):
    build = MockedStdout(returncode=0, stdout=JSON_DATA)
    mock_run.return_value = build
    with open(BASE / "test_files/test.json", "r") as temp_file:
        mock_temp_file.return_value.__enter__.return_value = temp_file
        result = tux_console_build(**PARAMS)
    assert result == JSON_DATA["uid"]


@mock.patch(
    "tuxtrigger.builder.subprocess.run",
    side_effect=TuxsuiteException("*** Tuxsuite not build repo"),
)
def test_tux_console_build_error(mock_run):
    build = MockedStdout(returncode=1, stdout=None)
    mock_run.return_value = build
    with pytest.raises(TuxsuiteException) as ex:
        tux_console_build(**PARAMS)
    assert "Tuxsuite not build" in str(ex.value)


@mock.patch("tuxtrigger.builder.subprocess.run")
def test_tux_console_plan_error(mock_run, squad_group_good, squad_project_good):
    build = MockedStdout(returncode=1, stdout=JSON_DATA)
    mock_run.return_value = build
    with pytest.raises(TuxtriggerException) as exc_tuxtrigger:
        tux_console_plan(
            None, PLAN, squad_group_good, squad_project_good, JSON_OUT, FINGERPRINT
        )

    assert "*** Not able to submit plan" in str(exc_tuxtrigger)
    with pytest.raises(TuxsuiteException) as exc_tuxsuite:
        tux_console_plan(
            JSON_DATA, PLAN, squad_group_good, squad_project_good, JSON_OUT, FINGERPRINT
        )
    assert "Submiting Plan for example_project_test-rc failed" in str(exc_tuxsuite)


@mock.patch("tuxtrigger.builder.subprocess.run")
@mock.patch("tempfile.NamedTemporaryFile")
def test_tux_console_plan(
    mock_temp_file, mock_run, squad_group_good, squad_project_good
):
    build = MockedStdout(returncode=0, stdout=JSON_DATA)
    mock_run.return_value = build
    with open(BASE / "test_files/test.json", "r") as test_file:
        mock_temp_file.return_value.__enter__.return_value = test_file
        fail_plan = tux_console_plan(
            JSON_DATA,
            PLAN_FAIL,
            squad_group_good,
            squad_project_good,
            JSON_OUT,
            FINGERPRINT,
        )
    mock_run.assert_called_with(
        [
            "squad-client",
            "submit-tuxsuite",
            "--group",
            "~non.existing",
            "--project",
            "example_project",
            "--build",
            "test-rc",
            "--backend",
            "tuxsuite.com",
            "--json",
            str(BASE / "test_files/test.json"),
        ],
        stdout=-1,
        stderr=-1,
        text=True,
    )
    assert fail_plan == 0


@mock.patch("tuxtrigger.builder.subprocess.run")
def test_build_result(mock_run):
    build = MockedStdout(returncode=0, stdout=json.dumps(JSON_BUILD_DATA))
    mock_run.return_value = build
    json_output = build_result(UID)
    mock_run.assert_called_once_with(
        ["tuxsuite", "build", "get", UID, "--json"], stdout=-1, stderr=-1, text=True
    )
    assert build_result(None) is None
    assert JSON_BUILD_DATA == json_output


@mock.patch("tuxtrigger.builder.subprocess.run")
def test_build_result_error(mock_run):
    build = MockedStdout(returncode=1, stdout="Oops!")
    mock_run.return_value = build
    with pytest.raises(TuxsuiteException) as exc:
        build_result(UID)
    assert "*** Build result for UID:2CCI3BkwKdqM4wOOwB5xRRxvOha failed" in str(exc)


@mock.patch("tuxtrigger.builder.subprocess.run")
def test_squad_submit(mock_run, squad_env_setup, squad_group_good, squad_project_good):
    mocked_submit = MockedStdout(
        returncode=1, stdout="Ooops!, not working!", stderr="Ooops! Serious Error!"
    )
    mock_run.return_value = mocked_submit
    with pytest.raises(SquadException) as exc:
        squad_submit(
            JSON_DATA,
            squad_group_good,
            squad_project_good,
            JSON_PLAN_RESULT,
            FINGERPRINT,
        )
    assert "*** squad-client not able to pass data" in str(exc)


@mock.patch.object(Session, "get")
def test_squad_sha_request(mock_session):
    session_ok = MockedSession(status_code=200, content=JSON_RESPONSE)
    mock_session.return_value = session_ok
    squad_sha = squad_metadata_request("1111", "tuxtrigger")
    assert squad_sha == ("8fa23329efa65477f077d99e145e4087190a55cc", "1234")


@mock.patch.object(Session, "get")
def test_squad_sha_request_fail(mock_session):
    session_fail = MockedSession(status_code=404, content=(None, None))
    mock_session.return_value = session_fail
    with pytest.raises(SquadException) as exc:
        squad_metadata_request("1112", "tuxtrigger")
    assert "SQUAD response error - (get latest build) 404" in str(exc)

    assert squad_metadata_request(None, None) == (None, None)


@mock.patch("tuxtrigger.builder.squad_metadata_request")
def test_compare_squad_sha(mock_sha):
    mock_sha.return_value = ("1234", "1234")
    assert compare_squad_sha("1111", "tuxtrigger", "1234") is False
    assert compare_squad_sha("1112", "tuxtrigger", "5678") is True


def test_compare_squad_sha_none():
    assert compare_squad_sha(None, None, "1234") is True
