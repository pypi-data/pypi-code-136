import json
import os
import venv
from argparse import Namespace
from pathlib import Path

import pytest

from ..playgroundtools import commands
from ..playgroundtools.exceptions import (
    PGDoesNotExistError,
    PGInvalidConfError,
    PGJSONFormatError,
)
from ..playgroundtools.resources import load_file_resource
from .fixtures import raw_config


class TestPGCommands:
    """Tests the playground-related functions in the commands module."""

    @pytest.fixture
    def example_playground(self, tmp_path):
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
    def existing_playground(self, example_playground):
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

    def test_new(self, example_playground, tmp_path):
        args = Namespace(
            command="new", name="test", type="console", lib=[], verbose=1
        )
        args.name = tmp_path / args.name

        commands.new(args)

        for path in example_playground.values():
            assert path.exists()

    def test_new_invalid(self, tmp_path):
        args = Namespace(
            command="new", name="test", type="test", lib=[], verbose=1
        )

        with pytest.raises(PGInvalidConfError) as err:
            commands.new(args)
        assert err.value.args[0] == args.type

    def test_run(self, existing_playground, tmp_path, request):
        args = Namespace(command="run", name="test", module=None, args=[])
        args.name = tmp_path / args.name

        try:
            commands.run(args)
        finally:
            os.chdir(request.config.invocation_dir)

    def test_run_invalid(self, tmp_path):
        args = Namespace(command="run", name="test", module=None, args=[])
        args.name = tmp_path / args.name

        with pytest.raises(PGDoesNotExistError):
            commands.run(args)

    def test_delete(self, existing_playground, tmp_path):
        args = Namespace(command="delete", name="test")
        args.name = tmp_path / args.name

        commands.delete(args)

        assert not args.name.exists()

    def test_delete_invalid(self, tmp_path):
        args = Namespace(command="run", name="test")
        args.name = tmp_path / args.name

        with pytest.raises(PGDoesNotExistError):
            commands.run(args)


class TestConfCommands:
    """Tests the config-related functions in the commands module."""

    @pytest.fixture
    def example_type(self):
        return {
            "test": {
                "folders": [],
                "files": {"main.py": ["print('test')"]},
                "lib": [],
                "module": ["main"],
                "args": [],
            }
        }

    def test_config_read_all(self, raw_config):
        args = Namespace(command="config", subcommand=None, read=None)
        assert commands.config(args) == raw_config

    def test_config_read(self, raw_config):
        args = Namespace(command="config", subcommand=None, read="api.files")
        assert commands.config(args) == raw_config["api"]["files"]

    def test_config_invalid(self, raw_config):
        args = Namespace(command="config", subcommand=None, read="test")

        with pytest.raises(PGInvalidConfError):
            commands.config(args)

    def test_config_add(self, raw_config, example_type):
        example_type_json = json.dumps(example_type["test"])
        args = Namespace(
            command="config",
            subcommand="add",
            type="test",
            value=example_type_json,
            file=None,
        )
        modified_config = {**raw_config, **example_type}
        assert commands.config(args) == modified_config

    def test_config_add_invalid_format(self, raw_config, example_type):
        example_type_json = [
            '"test": {' '    folders": [],',  # missing open quote
            '    "files": {"main.py": ["print(\'test\')"]},',
            '    "lib": [],',
            '    "module": ["main"],',
            '    "args": [],',
            "}",
        ]
        example_type_json = "".join(example_type_json)
        args = Namespace(
            command="config",
            subcommand="add",
            type="test",
            value=example_type_json,
            file=None,
        )
        with pytest.raises(PGJSONFormatError):
            commands.config(args)

    def test_config_add_file(self, raw_config, example_type, tmp_path):
        example_file = tmp_path / "test.json"
        with open(example_file, "w") as f:
            json.dump(example_type, f)
        modified_config = {**raw_config, **example_type}
        args = Namespace(
            command="config",
            subcommand="add",
            type=None,
            value=None,
            file=example_file,
        )
        assert commands.config(args) == modified_config

    def test_config_add_file_invalid_file(self, tmp_path):
        example_file = tmp_path / "test.json"
        args = Namespace(
            command="config",
            subcommand="add",
            type=None,
            value=None,
            file=example_file,
        )

        with pytest.raises(FileNotFoundError) as err:
            commands.config(args)
        assert Path(err.value.filename) == example_file

    def test_config_delete(self, raw_config, example_type):
        modified_config = {**raw_config, **example_type}
        with load_file_resource("config.json") as config_path:
            with open(config_path, "w") as f:
                json.dump(modified_config, f)
        args = Namespace(
            command="config", subcommand="delete", key="test", file=None
        )
        assert commands.config(args) == raw_config

    def test_config_delete_file(self, raw_config, example_type, tmp_path):
        config = {**raw_config, **example_type}
        example_file = tmp_path / "test.json"
        with load_file_resource("config.json") as config_path:
            with open(config_path, "w") as f:
                json.dump(config, f)
        with open(example_file, "w") as f:
            json.dump(example_type, f)
        args = Namespace(
            command="config", subcommand="delete", key=None, file=example_file
        )
        assert commands.config(args) == raw_config

    def test_config_delete_file_invalid(self, tmp_path):
        example_file = tmp_path / "test.json"
        args = Namespace(
            command="config",
            subcommand="delete",
            key=None,
            value=None,
            file=example_file,
        )

        with pytest.raises(FileNotFoundError) as err:
            commands.config(args)
        assert Path(err.value.filename) == example_file

    def test_config_edit(self, raw_config):
        modified_value = ["api", "api/routers", "api/db"]
        modified_value_json = '["api", "api/routers", "api/db"]'
        args = Namespace(
            command="config",
            subcommand="edit",
            key="api.folders",
            value=modified_value_json,
        )
        modified_config = raw_config
        modified_config["api"]["folders"] = modified_value
        assert commands.config(args) == modified_config

    def test_config_edit_invalid_format(self, raw_config):
        modified_value_json = (
            '["api", "api/routers", "api/db"'  # missing end bracket
        )
        args = Namespace(
            command="config",
            subcommand="edit",
            key="api.folders",
            value=modified_value_json,
        )

        with pytest.raises(PGJSONFormatError):
            commands.config(args)
