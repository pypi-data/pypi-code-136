from argparse import Namespace
from pathlib import Path

import pytest

from ..playgroundtools import util


class TestUtil:
    """Tests functions in the util module."""

    @pytest.mark.parametrize(
        ["args", "playground_dir"],
        [
            (Namespace(name="test"), "test"),
            (Namespace(name="test/subfolder"), "test/subfolder"),
            (Namespace(name="../parent_dir"), "../parent_dir"),
            (Namespace(name="./current_dir"), "./current_dir"),
        ],
    )
    def test_get_playground_dir(self, args, playground_dir):
        playground_dir = Path(playground_dir).resolve()
        assert util.get_playground_dir(args) == playground_dir

    @pytest.mark.parametrize(
        ["playground_dir", "venv_path"],
        [
            ("test", "test/.venv/"),
            ("test/subfolder", "test/subfolder/.venv/"),
            ("../parent_dir/test", "../parent_dir/test/.venv/"),
            ("./current_dir/test", "./current_dir/test/.venv/"),
        ],
    )
    def test_get_venv_dir(self, playground_dir, venv_path):
        playground_dir = Path(playground_dir).resolve()
        venv_path = Path(venv_path).resolve()

        assert util.get_venv_dir(playground_dir) == venv_path

    @pytest.mark.parametrize(
        ["python", "module", "args", "cmd"],
        [
            (
                "test/.venv/Scripts/python",
                "main",
                [],
                f"{Path('test/.venv/Scripts/python').resolve()} -m main",
            ),
            (
                "test/.venv/Scripts/python",
                "uvicorn",
                ["main:app", "--reload"],
                (
                    f"{Path('test/.venv/Scripts/python').resolve()} -m"
                    f" uvicorn main:app --reload"
                ),
            ),
            (
                "../parent_dir/.venv/Scripts/python",
                "jupyter",
                ["notebook", "analysis.ipynb"],
                (
                    f"{Path('../parent_dir/.venv/Scripts/python').resolve()} "
                    f"-m jupyter notebook analysis.ipynb"
                ),
            ),
        ],
    )
    def test_get_command(self, python, module, args, cmd):
        python = Path(python).resolve()
        assert util.get_command(python, module, args) == cmd

    @pytest.mark.parametrize(
        ["folder", "exists"],
        [
            ("test", True),
            ("test", False),
            ("test/subfolder", True),
            ("test/subfolder", False),
            ("../parent_dir", True),
            ("./current_dir", True),
        ],
    )
    def test_remove_if_exists(self, folder, exists, tmp_path):
        tmp_path = tmp_path.resolve()
        folder_path = tmp_path / folder
        if exists:
            folder_path.mkdir(parents=True)
        util.remove_if_exists(folder_path)
        assert not folder_path.exists()
