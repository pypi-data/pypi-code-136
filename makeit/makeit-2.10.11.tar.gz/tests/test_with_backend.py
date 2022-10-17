import dataclasses
import pathlib
from typing import Any

from makeit import (
    File, Dependency, Target, MD5Checker, TimeChecker
)

from makeit.core import execute, DAG, DictBackend, EARunOnChange

from makeit import DataclassTask


NUM_OF_CALLS = 0


@dataclasses.dataclass
class MakeUpper(DataclassTask):
    input: File | Dependency
    output: File | Target = dataclasses.field(init=False)
    output_meta: File | Target = dataclasses.field(init=False)

    def __post_init__(self):
        self.output = File(f"{self.input.path}out", label=f"{self.input.path.name}out")
        self.output_meta = File(f"{self.input.path}meta", label=f"{self.input.path.name}meta")

    def execute(self):
        self.output.path.write_text(
            self.input.path.read_text().upper()
        )

        self.output_meta.path.write_text(
            self.input.path.as_uri()
        )

        global NUM_OF_CALLS
        NUM_OF_CALLS += 1


def _write_files(tmp_path: pathlib.Path, names: list[str]):
    for name in names:
        (tmp_path / f"{name}.txt").write_text(f"text is written into {name}")


def make_dag(tmp_path: pathlib.Path, checker: Any = MD5Checker()) -> DAG:
    dag = DAG("main")

    for f in tmp_path.glob("*.txt"):
        dag.add(MakeUpper(
            File(f, checker, label=f.name)
        ))

    return dag


def test_full_cycle_on_change(tmp_path):
    global NUM_OF_CALLS
    NUM_OF_CALLS = 0

    _write_files(tmp_path, ["f1", "f2", "f3"])

    dag = make_dag(tmp_path)

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 3
    assert len(list(tmp_path.glob("*.txtout"))) == 3
    assert len(list(tmp_path.glob("*.txtmeta"))) == 3

    _write_files(tmp_path, ["f4", ])

    dag = make_dag(tmp_path)

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 4
    assert len(list(tmp_path.glob("*.txtout"))) == 4
    assert len(list(tmp_path.glob("*.txtmeta"))) == 4

    # run 3
    _write_files(tmp_path, ["f1", "f2"])

    dag = make_dag(tmp_path)

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 4
    assert len(list(tmp_path.glob("*.txtout"))) == 4
    assert len(list(tmp_path.glob("*.txtmeta"))) == 4


def test_full_cycle_modified_time(tmp_path):
    global NUM_OF_CALLS
    NUM_OF_CALLS = 0

    # run 1
    _write_files(tmp_path, ["f1", "f2", "f3"])

    dag = make_dag(tmp_path, TimeChecker(True))

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 3
    assert len(list(tmp_path.glob("*.txtout"))) == 3
    assert len(list(tmp_path.glob("*.txtmeta"))) == 3

    # run 2
    _write_files(tmp_path, ["f4", ])

    dag = make_dag(tmp_path, TimeChecker(True))

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 4
    assert len(list(tmp_path.glob("*.txtout"))) == 4
    assert len(list(tmp_path.glob("*.txtmeta"))) == 4

    # run 3
    _write_files(tmp_path, ["f1", "f2"])

    dag = make_dag(tmp_path, TimeChecker(True))

    execute(dag, DictBackend(tmp_path / "make-it.json"), EARunOnChange, None)

    assert NUM_OF_CALLS == 6
    assert len(list(tmp_path.glob("*.txtout"))) == 4
    assert len(list(tmp_path.glob("*.txtmeta"))) == 4
