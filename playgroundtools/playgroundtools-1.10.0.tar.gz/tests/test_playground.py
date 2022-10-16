import json
from argparse import Namespace
from pathlib import Path

import pytest

from ..playgroundtools import playground
from ..playgroundtools.exceptions import (
    PGConfigNotFoundError,
    PGDoesNotExistError,
    PGInvalidConfError,
)
from ..playgroundtools.resources import load_file_resource
from .fixtures import raw_config


class TestPlayground:
    """Tests functions in the playground module."""

    @pytest.fixture
    def example_type(self):
        return {
            "package": {
                "folders": ["${name}", "tests"],
                "files": {
                    "setup.cfg": [
                        "[metadata]",
                        "name = ${name}",
                        "version = 0.0.0",
                        "",
                        "[options]",
                        "packages = find:",
                        "include_package_data = True",
                    ],
                    "pyproject.toml": [
                        "[build-system]",
                        'requires = ["setuptools>=61.0.0", "wheel"]',
                        'build-backend = "setuptools.build_meta"',
                    ],
                    "setup.py": [
                        "import setuptools",
                        "",
                        "setuptools.setup()",
                    ],
                    "${name}/__init__.py": [],
                },
                "lib": [
                    "${name}",
                    "${formatter}",
                    "${linter}",
                    "${build}",
                    "${upload}",
                    "isort"
                ],
                "module": "${name}",
                "args": [],
                "format": {
                    "formatter": "black",
                    "build": "build",
                    "upload": "twine",
                    "linter": "flake8"
                }
            }
        }

    @pytest.fixture
    def example_interpolated(self):
        return {
            "verbosity": 1,
            "dir": Path("playground").resolve(),
            "folders": ["playground", "tests", "requirements"],
            "files": {
                "setup.cfg": [
                    "[metadata]",
                    "name = playground",
                    "version = 0.0.0",
                    "",
                    "[options]",
                    "packages = find:",
                    "include_package_data = True",
                ],
                "pyproject.toml": [
                    "[build-system]",
                    'requires = ["setuptools>=61.0.0", "wheel"]',
                    'build-backend = "setuptools.build_meta"',
                ],
                "setup.py": [
                    "import setuptools",
                    "",
                    "setuptools.setup()",
                ],
                "playground/__init__.py": [],
                "requirements/requirements.in": [
                    "playground",
                    "black",
                    "flake8",
                    "build",
                    "twine",
                    "isort",
                ],
            },
            "lib": [
                "playground",
                "black",
                "flake8",
                "isort",
                "build",
                "twine",
            ],
            "settings": {"module": "playground", "args": []},
        }

    def test_get_config(self, raw_config):
        assert playground.get_config() == raw_config

    def test_get_config_invalid(self, raw_config):
        with load_file_resource("config.json") as config_path:
            config_path.unlink()
            with pytest.raises(PGConfigNotFoundError):
                playground.get_config()
            config_path.touch()

    @pytest.mark.parametrize(
        ["args", "clean_config"],
        [
            (
                Namespace(
                    command="new",
                    name="test",
                    type="console",
                    lib=[],
                    verbose=1,
                    options=None
                ),
                {
                    "verbosity": 1,
                    "dir": Path("test").resolve(),
                    "folders": ["requirements"],
                    "files": {
                        "main.py": ["print('Hello, World!')"],
                        "requirements/requirements.in": [],
                    },
                    "lib": [],
                    "settings": {"module": "main", "args": []},
                },
            ),
            (
                Namespace(
                    command="new",
                    name="test/subfolder",
                    type="jupyter",
                    lib=[],
                    verbose=1,
                    options=None
                ),
                {
                    "verbosity": 1,
                    "dir": Path("test/subfolder").resolve(),
                    "folders": ["requirements"],
                    "files": {
                        "dataprep.ipynb": [
                            "{",
                            ' "cells": [',
                            "  {",
                            '   "cell_type": "code",',
                            '   "execution_count": null,',
                            '   "metadata": {},',
                            '   "outputs": [],',
                            '   "source": []',
                            "  }",
                            " ],",
                            ' "metadata": {},',
                            ' "nbformat": 4,',
                            ' "nbformat_minor": 1',
                            "}",
                        ],
                        "analysis.ipynb": [
                            "{",
                            ' "cells": [',
                            "  {",
                            '   "cell_type": "code",',
                            '   "execution_count": null,',
                            '   "metadata": {},',
                            '   "outputs": [],',
                            '   "source": []',
                            "  }",
                            " ],",
                            ' "metadata": {},',
                            ' "nbformat": 4,',
                            ' "nbformat_minor": 1',
                            "}",
                        ],
                        "requirements/requirements.in": [
                            "jupyter",
                            "jupyterlab",
                            "numpy",
                            "pandas",
                            "matplotlib",
                            "faker",
                            "arrow",
                        ],
                    },
                    "lib": [
                        "jupyter",
                        "jupyterlab",
                        "numpy",
                        "pandas",
                        "matplotlib",
                        "faker",
                        "arrow",
                    ],
                    "settings": {
                        "module": "jupyter",
                        "args": ["notebook", "analysis.ipynb"],
                    },
                },
            ),
        ],
    )
    def test_clean_config(self, args, clean_config, raw_config):
        assert playground.clean_config(args, raw_config) == clean_config

    def test_format_config(
        self, example_type, example_interpolated, raw_config
    ):
        config = {**raw_config, **example_type}
        with load_file_resource("config.json") as config_path:
            with open(config_path, "w") as f:
                json.dump(config, f)

        args = Namespace(
            command="new",
            name="playground",
            type="package",
            lib=[],
            verbose=1,
            options=None
        )
        cleaned = playground.clean_config(args, config)
        assert sorted(cleaned) == sorted(example_interpolated)

    def test_clean_config_invalid(self, raw_config):
        modified_config = raw_config
        del modified_config["http"]["folders"]
        with load_file_resource("config.json") as config_path:
            with open(config_path, "w") as f:
                json.dump(modified_config, f)

        args = Namespace(
            command="new",
            name="test",
            type="http",
            lib=[],
            verbose=1,
            options=None
        )

        with pytest.raises(PGInvalidConfError) as err:
            playground.clean_config(args, raw_config)
        assert err.value.args[0] == f"{args.type}.folders"

    def test_get_playground_dir(self, tmp_path):
        args = Namespace(name="test")
        args.name = tmp_path / args.name
        args.name.mkdir()

        assert playground.get_playground_dir(args) == args.name

    def test_get_playground_dir_invalid(self):
        args = Namespace(name="test")

        with pytest.raises(PGDoesNotExistError):
            playground.get_playground_dir(args)
