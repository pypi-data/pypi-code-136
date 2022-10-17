#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import sys
import pytest

from pathlib import Path
import tuxtrigger.__main__ as main_module

BASE = (Path(__file__) / "../..").resolve()

VALUE_DICT = {
    "master": {"sha": "12345", "ref": "refs/master/torvalds"},
    "v5.19": {"sha": "12345", "ref": "refs/v5.19"},
    "for-laurent": {"sha": "12345", "ref": "refs/for-laurent"},
}

UID = "2CCI3BkwKdqM4wOOwB5xRRxvOha"

JSON_OUTPUT = {
    "empty": "no_real_values",
    "uid": "1234",
    "git_repo": "https://gitlab.com/no_real_repo",
    "git_ref": "master",
    "git_describe": "v5.19-rc7",
}

MANIFEST_JSON = {
    "/pub/scm/linux/kernel/git/tomba/linux.git": {
        "owner": "Tomi Valkeinen",
        "description": "Tomi Valkeinen's kernel tree",
        "modified": 1660133218,
        "reference": "/pub/scm/linux/kernel/git/paulg/4.8-rt-patches.git",
        "fingerprint": "8fa23329efa65477f077d99e145e4087190a55cc",
        "forkgroup": "af9f4487-d538-46e5-b148-e18dfb461f8a",
        "head": "ref: refs/heads/master",
    },
    "/pub/scm/linux/kernel/git/torvalds/linux.git": {
        "symlinks": ["/pub/scm/linux/kernel/git/torvalds/linux-2.6.git"],
        "description": "Linux kernel source tree",
        "reference": "/pub/scm/linux/kernel/git/paulg/4.8-rt-patches.git",
        "modified": 1661194011,
        "fingerprint": "2c8d80ee6d795dc6951bbdef466ef19c64ff717d",
        "owner": "Linus Torvalds",
        "head": "ref: refs/heads/master",
        "forkgroup": "af9f4487-d538-46e5-b148-e18dfb461f8a",
    },
}


@pytest.fixture
def argv():
    return ["tuxtrigger"]


@pytest.fixture(autouse=True)
def patch_argv(monkeypatch, argv):
    monkeypatch.setattr(sys, "argv", argv)


class TestMain:
    def test_start(self, monkeypatch, mocker):
        monkeypatch.setattr(main_module, "__name__", "__main__")
        main = mocker.patch("tuxtrigger.__main__.main", return_value=1)
        exit = mocker.patch("sys.exit")
        main_module.start()
        main.assert_called()
        exit.assert_called_with(1)

    def test_main_version(self, argv, capsys):
        argv.append("-v")
        with pytest.raises(SystemExit):
            main_module.main()
        out, out_err = capsys.readouterr()
        assert "TuxTrigger" in out

    def test_main_correct_data(self, argv, monkeypatch, mocker):
        argv.extend([f"{BASE}/test/test_files/happy_path.yaml"])
        monkeypatch.setattr(main_module, "__name__", "__main__")
        main_manifest = mocker.patch(
            "tuxtrigger.__main__.git_manifest_download",
            return_value=json.dumps(MANIFEST_JSON),
        )
        main_manifest_changed = mocker.patch(
            "tuxtrigger.__main__.manifest_changed", return_value=True
        )
        main_check_squad_project = mocker.patch(
            "tuxtrigger.__main__.check_squad_project", return_value=666
        )
        main_lsremote = mocker.patch(
            "tuxtrigger.__main__.run_lsremote", return_value=VALUE_DICT
        )
        main_build_uid = mocker.patch(
            "tuxtrigger.__main__.tux_console_build", return_value=UID
        )
        main_build_output = mocker.patch(
            "tuxtrigger.__main__.build_result", return_value=JSON_OUTPUT
        )
        main_compare_squad_sha = mocker.patch(
            "tuxtrigger.__main__.compare_squad_sha", return_value=True
        )
        main_tux_console_plan = mocker.patch(
            "tuxtrigger.__main__.tux_console_plan", return_value=0
        )
        main_squad_metadata_request = mocker.patch(
            "tuxtrigger.__main__.squad_metadata_request", return_value=("", "")
        )
        main_tux_console_plan = mocker.patch(
            "tuxtrigger.__main__.tux_console_plan", return_value=0
        )
        exit = mocker.patch("sys.exit")
        main_module.start()
        main_manifest.assert_called()
        main_manifest_changed.assert_called()
        main_check_squad_project.assert_called()
        main_lsremote.assert_called()
        main_build_uid.assert_called()
        main_compare_squad_sha.assert_called()
        main_build_output.assert_called()
        main_squad_metadata_request.assert_called()
        main_tux_console_plan.assert_called()
        exit.assert_called_with(0)

    def test_main_correct_data_yaml(self, argv, monkeypatch, mocker):
        argv.extend([f"{BASE}/test/test_files/happy_path.yaml"])
        argv.append("--sha-compare=yaml")
        monkeypatch.setattr(main_module, "__name__", "__main__")
        main_manifest = mocker.patch(
            "tuxtrigger.__main__.git_manifest_download",
            return_value=json.dumps(MANIFEST_JSON),
        )
        main_manifest_changed = mocker.patch(
            "tuxtrigger.__main__.manifest_changed", return_value=True
        )
        main_check_squad_project = mocker.patch(
            "tuxtrigger.__main__.check_squad_project", return_value=666
        )
        main_lsremote = mocker.patch(
            "tuxtrigger.__main__.run_lsremote", return_value=VALUE_DICT
        )
        main_compare_sha = mocker.patch(
            "tuxtrigger.__main__.compare_sha", return_value=True
        )
        main_build_uid = mocker.patch(
            "tuxtrigger.__main__.tux_console_build", return_value=UID
        )
        main_build_output = mocker.patch(
            "tuxtrigger.__main__.build_result", return_value=JSON_OUTPUT
        )
        main_tux_console_plan = mocker.patch(
            "tuxtrigger.__main__.tux_console_plan", return_value=0
        )
        main_pre_tux_run = mocker.patch(
            "tuxtrigger.__main__.pre_tux_run", return_value=0
        )
        exit = mocker.patch("sys.exit")
        main_module.start()
        main_manifest.assert_called()
        main_manifest_changed.assert_called()
        main_check_squad_project.assert_called()
        main_lsremote.assert_called()
        main_compare_sha.assert_called()
        main_pre_tux_run.assert_called()
        main_build_uid.assert_called()
        main_build_output.assert_called()
        main_tux_console_plan.assert_called()
        exit.assert_called_with(0)

    def test_main_key_error(self, argv):
        argv.extend([f"{BASE}/test/test_files/error_path.yaml"])
        with pytest.raises(Exception):
            main_module.main()
            assert main_module.main() == 1

    def test_main_build_never(self, argv, capsys, monkeypatch, mocker):
        argv.append(f"{BASE}/test/test_files/happy_path.yaml")
        monkeypatch.setattr(main_module, "__name__", "__main__")
        main = mocker.patch("tuxtrigger.__main__.run_lsremote", return_value=VALUE_DICT)
        argv.append("--submit=never")
        argv.append("--sha-compare=yaml")
        main_manifest = mocker.patch(
            "tuxtrigger.__main__.git_manifest_download",
            return_value=json.dumps(MANIFEST_JSON),
        )
        main_manifest_changed = mocker.patch(
            "tuxtrigger.__main__.manifest_changed", return_value=True
        )
        main_check_squad_project = mocker.patch(
            "tuxtrigger.__main__.check_squad_project", return_value=666
        )
        main_module.main()
        out, out_err = capsys.readouterr()
        main_manifest.assert_called()
        main_check_squad_project.assert_called()
        main_manifest_changed.assert_called()
        main.assert_called()
        assert "** Builds suspended **" in out

    def test_main_build_always(self, argv, mocker, monkeypatch):
        argv.append(f"{BASE}/test/test_files/happy_path.yaml")
        argv.append("--submit=always")
        argv.append("--sha-compare=yaml")
        monkeypatch.setattr(main_module, "__name__", "__main__")
        main_manifest = mocker.patch(
            "tuxtrigger.__main__.git_manifest_download",
            return_value=json.dumps(MANIFEST_JSON),
        )
        main_lsremote = mocker.patch(
            "tuxtrigger.__main__.run_lsremote", return_value=VALUE_DICT
        )
        main_build_uid = mocker.patch(
            "tuxtrigger.__main__.tux_console_build", return_value=UID
        )
        main_build_output = mocker.patch(
            "tuxtrigger.__main__.build_result", return_value=JSON_OUTPUT
        )
        main_tux_console_plan = mocker.patch(
            "tuxtrigger.__main__.tux_console_plan", return_value=0
        )
        main_pre_tux_run = mocker.patch(
            "tuxtrigger.__main__.pre_tux_run", return_value=0
        )
        main_check_squad_project = mocker.patch(
            "tuxtrigger.__main__.check_squad_project", return_value=666
        )
        main_module.main()
        main_manifest.assert_called()
        main_check_squad_project.assert_called()
        main_lsremote.assert_called()
        main_pre_tux_run.assert_called()
        main_build_uid.assert_called()
        main_build_output.assert_called()
        main_tux_console_plan.assert_called()
