import json
import os
import venv
from argparse import Namespace

import pytest

from ..playgroundtools import commands
from .fixtures import raw_config


@pytest.fixture
def example_playground(tmp_path):
    playground_dir = tmp_path / "test"

    reqs_dir = playground_dir / "requirements"
    reqs_path = reqs_dir / "requirements.in"

    venv_path = playground_dir / ".venv"

    main_path = playground_dir / "main.py"

    settings_path = playground_dir / "settings.json"

    return {
        "dir": playground_dir,
        "reqs_dir": reqs_dir,
        "reqs_path": reqs_path,
        "venv": venv_path,
        "file": main_path,
        "settings": settings_path,
    }


@pytest.fixture
def existing_playground(example_playground):
    paths = example_playground

    paths["dir"].mkdir()

    paths["reqs_dir"].mkdir()
    paths["reqs_path"].touch()

    venv.create(paths["venv"], with_pip=True)
    python_path = paths["venv"] / "bin" / "python"
    alt_python_path = paths["venv"] / "Scripts" / "python.exe"
    python = python_path if python_path.exists() else alt_python_path

    paths["file"].touch()
    paths["file"].write_text("print('Hello, World!')\n")

    settings = {"python": str(python), "module": "main", "args": []}
    paths["settings"].touch()
    paths["settings"].write_text(json.dumps(settings, indent=4))


class TestPGCommands:
    """Tests the playground-related functions in the commands module."""

    def test_new(self, example_playground, tmp_path):
        args = Namespace(command="new", name="test", type="console", lib=[])
        args.name = tmp_path / args.name

        commands.new(args)

        for path in example_playground.values():
            assert path.exists()

    def test_run(self, existing_playground, tmp_path, request):
        args = Namespace(command="run", name="test")
        args.name = tmp_path / args.name

        try:
            commands.run(args)
        finally:
            os.chdir(request.config.invocation_dir)

    def test_delete(self, existing_playground, tmp_path):
        args = Namespace(command="delete", name="test")
        args.name = tmp_path / args.name

        commands.delete(args)

        assert not args.name.exists()


class TestConfCommands:
    """Tests the config-related functions in the commands module."""

    def test_config_read_all(self, raw_config):
        args = Namespace(command="config", subcommand=None, read=None)
        assert commands.config(args) == raw_config

    def test_config_read(self, raw_config):
        args = Namespace(command="config", subcommand=None, read="api.files")
        assert commands.config(args) == raw_config["api"]["files"]
