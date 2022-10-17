import dataclasses

import pytest

from makeit import mp_execute_on_change, Target, Dependency, DataclassTask, register_type, File
from pathlib import Path

import time

from .test_execution_flags import COMMANDS


@dataclasses.dataclass
class Convert(DataclassTask):
    in_: Path | Dependency
    tmp_path: Path

    out_: Path | Target = None
    label: str = None

    def __post_init__(self):
        self.out_ = self.in_.with_suffix(".csv")

    def execute(self):
        time.sleep(0.1)

        (self.tmp_path / self.md5(".idx")).write_text(
            str(self.execution_cnt + 1)
        )

        self.out_.write_text(
            self.in_.read_text().upper()
        )

    def __repr__(self):
        return self.label

    @property
    def _exec_path(self):
        return self.tmp_path / self.md5(".idx")

    @property
    def execution_cnt(self):
        if not self._exec_path.is_file():
            return 0

        return int(self._exec_path.read_text())


@dataclasses.dataclass
class Combine(DataclassTask):
    in_: list[Path] | Dependency
    tmp_path: Path

    out_: Path | Target
    label: str

    def execute(self):
        time.sleep(0.1)

        (self.tmp_path / self.md5(".idx")).write_text(
            str(self.execution_cnt + 1)
        )

        self.out_.write_text(
            "".join(_.read_text() for _ in self.in_)
        )

    def __repr__(self):
        return self.label

    @property
    def _exec_path(self):
        return self.tmp_path / self.md5(".idx")

    @property
    def execution_cnt(self):
        if not self._exec_path.is_file():
            return 0

        return int((self.tmp_path / self.md5(".idx")).read_text())



@pytest.mark.parametrize("commands", COMMANDS)
def test_mp_execution_flags(tmp_path, commands):
    print(tmp_path)

    register_type(Path, lambda _: File(_, label=_.name))

    f1 = tmp_path / "f1.txt"
    f2 = tmp_path / "f2.txt"

    c1 = Convert(f1, tmp_path=tmp_path, label="task-c1")
    c2 = Convert(f2, tmp_path=tmp_path, label="task-c2")
    comb = Combine(in_=[c1.out_, c2.out_], tmp_path=tmp_path,
                   out_=tmp_path / "comb.csv", label="task-combine")

    id2c = {"c1": c1, "c2": c2, "comb": comb}

    backend = tmp_path / "makeit.json"

    for command in commands:
        match command:
            case ["write", *cmd]:
                for target, what in cmd:
                    (tmp_path / target).write_text(what)
            case ["execute", kwargs]:
                mp_execute_on_change([c1, c2, comb], dag_name=f"{tmp_path.name}", backend=backend, n_jobs=5, **kwargs)
            case ["exec", *cmd]:
                for c, val in cmd:
                    assert id2c[c].execution_cnt == val
            case ["read", *cmd]:
                for c, val in cmd:
                    assert (tmp_path / c).read_text() == val
            case ["drop", *cmd]:
                for c in cmd:
                    (tmp_path / c) .unlink()
            case _:
                raise Exception(f"failed to parse command {command}")
