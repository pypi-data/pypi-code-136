import dataclasses

import pytest

from makeit import Target, execute_on_change, DataclassTask
from pathlib import Path


RAISE = True


@dataclasses.dataclass
class X(DataclassTask):
    label_: str
    tar: Path | Target

    def execute(self):
        if RAISE:
            raise Exception("Failed")

        self.tar.write_text("done")


@dataclasses.dataclass
class Y(DataclassTask):
    tar: Path | Target

    executed = 0

    def execute(self):
        type(self).executed += 1

        self.tar.write_text("done too")


def test_failure_during(tmp_path):
    backend = tmp_path / "makeit.json"

    y_txt = tmp_path / "y.txt"
    x_txt = tmp_path / "x.txt"

    global RAISE

    with pytest.raises(Exception):
        execute_on_change([Y(y_txt), X("x", x_txt)], backend)

    assert Y.executed == 1
    assert y_txt.read_text() == "done too"
    print(backend.read_text())

    RAISE = False

    execute_on_change([Y(y_txt), X("x", x_txt)], backend)
    assert Y.executed == 1
    assert y_txt.read_text() == "done too"
    assert x_txt.read_text() == "done"

    print(backend.read_text())
