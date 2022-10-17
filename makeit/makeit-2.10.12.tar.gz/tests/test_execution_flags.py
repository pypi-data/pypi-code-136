import dataclasses

import pytest

from makeit import execute_on_change, Target, Dependency, DataclassTask, register_type, File
from pathlib import Path


class Convert(DataclassTask):
    in_: Path | Dependency
    out_: Path | Target = None
    label: str = None

    def __post_init__(self):
        self.out_ = self.in_.with_suffix(".csv")
        self.execution_cnt = 0

    def execute(self):
        self.execution_cnt += 1

        self.out_.write_text(
            self.in_.read_text().upper()
        )

    def __repr__(self):
        return self.label


class Combine(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target
    label: str

    def __post_init__(self):
        self.execution_cnt = 0

    def execute(self):
        self.execution_cnt += 1

        self.out_.write_text(
            "".join(_.read_text() for _ in self.in_)
        )

    def __repr__(self):
        return self.label


COMMANDS = [
    # Execute two times -- skips second
    (
        ["write", ("f1.txt", "abc"), ("f2.txt", "dce")],
        ["execute", {}],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 1)],
        ["read", ("f1.csv", "ABC"), ("f2.csv", "DCE"), ("comb.csv", "ABCDCE")],
        ["execute", {}],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 1)],
        ["read", ("f1.csv", "ABC"), ("f2.csv", "DCE"), ("comb.csv", "ABCDCE")],
    ),

    # Test execute all 1.
    (
        ["write", ("f1.txt", "abc"), ("f2.txt", "dce")],
        ["execute", {}],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 1)],

        ["execute", dict(execute_all=True)],
        ["exec", ("c1", 2), ("c2", 2), ("comb", 2)],

        ["execute", {}],
        ["exec", ("c1", 2), ("c2", 2), ("comb", 2)],

        ["execute", dict(execute_all=True)],
        ["exec", ("c1", 3), ("c2", 3), ("comb", 3)],

        ["drop", "comb.csv"],
        ["execute", {}],
        ["exec", ("c1", 3), ("c2", 3), ("comb", 4)],

        ["drop", "comb.csv"],
        ["execute", dict(execute_all=True)],
        ["exec", ("c1", 4), ("c2", 4), ("comb", 5)],
    ),

    # Test targets
    (
        ["write", ("f1.txt", "abc"), ("f2.txt", "dce"), ("f1.csv", "something"), ("f2.csv", "something")],
        ["write", ("comb.csv", "something")],
        ["execute", dict()],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 1)],

        ["write", ("comb.csv", "something")],
        ["execute", dict(test_targets_fingerprints=False)],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 1)],

        ["write", ("comb.csv", "something")],
        ["execute", dict(test_targets_fingerprints=True)],
        ["exec", ("c1", 2), ("c2", 2), ("comb", 2)],

        ["write", ("comb.csv", "something")],
        ["execute", dict(test_targets_fingerprints=True)],
        ["exec", ("c1", 2), ("c2", 2), ("comb", 3)],
    )
]


COMMANDS_CAPTURE = [
    # Test capture
    (
        ["write", ("f1.txt", "abc"), ("f2.txt", "dce"), ("f1.csv", "something"), ("f2.csv", "something")],
        ["write", ("comb.csv", "something")],
        ["execute", dict(capture_only=True)],
        ["exec", ("c1", 0), ("c2", 0), ("comb", 0)],

        ["execute", dict()],
        ["exec", ("c1", 0), ("c2", 0), ("comb", 0)],

        ["drop", "comb.csv"],
        ["execute", dict()],
        ["exec", ("c1", 0), ("c2", 0), ("comb", 1)],
        ["read", ("comb.csv", "somethingsomething")],

        ["execute", dict(execute_all=True)],
        ["exec", ("c1", 1), ("c2", 1), ("comb", 2)],
        ["read", ("f1.csv", "ABC"), ("f2.csv", "DCE"), ("comb.csv", "ABCDCE")]
    ),
]


@pytest.mark.parametrize("commands", COMMANDS + COMMANDS_CAPTURE)
def test_execution_flags(tmp_path, commands):
    register_type(Path, lambda _: File(_, label=_.name))

    f1 = tmp_path / "f1.txt"
    f2 = tmp_path / "f2.txt"

    c1 = Convert(f1, label="task-c1")
    c2 = Convert(f2, label="task-c2")
    comb = Combine(in_=[c1.out_, c2.out_], out_=tmp_path / "comb.csv", label="task-combine")

    id2c = {"c1": c1, "c2": c2, "comb": comb}

    backend = tmp_path / "makeit.json"

    for command in commands:
        match command:
            case ["write", *cmd]:
                for target, what in cmd:
                    (tmp_path / target).write_text(what)
            case ["execute", kwargs]:
                execute_on_change([c1, c2, comb], dag_name=f"{tmp_path.name}", backend=backend, **kwargs)
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

# ----------------------------------------------------------------------------------------------------------------------


@dataclasses.dataclass
class X(DataclassTask):
    in_: list[Path] | Dependency
    out_: list[Path] | Target
    label: str

    executed_cnt: int = dataclasses.field(default=0, repr=False)

    def execute(self):
        txt = "".join([
            _.read_text()
            for _ in self.in_
        ])

        for i, f in enumerate(self.out_):
            f.write_text(f"{self.label}:{i}:[{txt}]")

        self.executed_cnt += 1

    def __repr__(self):
        return self.label


@pytest.mark.parametrize("commands", [
    (
        ["task", ("x", ["a"], ["b"]), ("y", ["a"], ["c"]), ("z", ["b", "c"], [])],
        ["write", ("a", "A")],
        ["execute", {}],
        ["read", ("b", "x:0:[A]"), ("c", "y:0:[A]")],
        ["exec", ("x", 1), ("y", 1), ("z", 1)],
        ["drop", "c"],

        ["execute", {}],
        ["exec", ("x", 1), ("y", 2), ("z", 1)],
    ),
])
def test_execution_flags_2(tmp_path, commands):
    register_type(Path, lambda _: File(_, label=_.name))
    label2task = {}

    backend = tmp_path / "makeit.json"

    for command in commands:
        match command:
            case ["write", *cmd]:
                for target, what in cmd:
                    (tmp_path / target).write_text(what)

            case ["task", *args]:
                for label, in_, out_ in args:
                    assert label not in label2task

                    label2task[label] = X(
                        in_=[tmp_path / _ for _ in in_],
                        out_=[tmp_path / _ for _ in out_],
                        label=label
                    )

            case ["execute", kwargs]:
                execute_on_change(label2task.values(), dag_name=f"{tmp_path.name}", backend=backend, **kwargs)

            case ["exec", *args]:
                for label, val in args:
                    assert label2task[label].executed_cnt == val

            case ["read", *args]:
                for path, val in args:
                    assert (tmp_path / path).read_text() == val

            case ["drop", *args]:
                for c in args:
                    (tmp_path / c).unlink()

            case _:
                raise Exception(f"failed to parse command {command}")
