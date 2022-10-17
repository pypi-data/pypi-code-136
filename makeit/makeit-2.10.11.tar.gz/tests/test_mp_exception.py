import dataclasses
import json
import math
from pathlib import Path

import pytest

from makeit import mp_execute_on_change, execute_on_change, Target, Dependency, register_type, File, DataclassTask
from makeit.core import SimpleReporter, TaskEvent, MakeItException, ChildProcessException

import time


@dataclasses.dataclass
class Sum(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target

    def execute(self):
        values = [
            int(f.read_text())
            for f in self.in_
        ]

        self.out_.write_text(
            f"{sum(values)}"
        )

        time.sleep(1)


class CustomException(Exception):
    pass


class Custom(SimpleReporter):
    def report_task_event(self, event: TaskEvent, task_name: str, reason: str):
        if event == TaskEvent.DONE:
            raise CustomException("Done!")
        else:
            super(Custom, self).report_task_event(event, task_name, reason)


def test_exception_in_parent_process(tmp_path):
    """ Ctrl-C, for example """
    f1 = tmp_path / "1.sum1.txt"
    f2 = tmp_path / "2.sum1.txt"
    f3 = tmp_path / "3.sum1.txt"

    for i, _ in enumerate([f1, f2, f3]):
        _.write_text(f"{i + 1}")

    o1 = tmp_path / "out1.txt"

    a1 = Sum([f1, f2, f3], o1)

    with pytest.raises(CustomException):
        mp_execute_on_change([a1, ], tmp_path / "makeit.json", n_jobs=3, reporter=Custom())

    # on the next run "SKIP" will be emitted -- no exception will be raised -- should work fine
    mp_execute_on_change([a1, ], tmp_path / "makeit.json", n_jobs=3, reporter=Custom())


@dataclasses.dataclass
class X(DataclassTask):
    ix: int = dataclasses.field(repr=False)
    w_dir: Path = dataclasses.field(repr=False)
    out: Path | Target = None

    execution_cnt = 0

    def __post_init__(self):
        self.out = self.w_dir / f"{self.ix}.txt"

    def execute(self):
        self.out.write_text(f"text={self.ix}")
        self.__class__.execution_cnt += 1


@dataclasses.dataclass
class Y(DataclassTask):
    in_: Path | Dependency
    sleep_time: float
    out_: Path | Target = None

    execution_cnt = 0

    def __post_init__(self):
        self.out_ = self.in_.with_suffix(".out")

    def execute(self):
        if self.in_.name == "1.txt":
            raise RuntimeError("Failure!")

        self.__class__.execution_cnt += 1

        time.sleep(self.sleep_time)

        self.out_.write_text(self.in_.read_text().upper())


def test_exception_in_child_process(tmp_path):
    x_tasks = [
        X(ix=_, w_dir=tmp_path) for _ in range(20)
    ]

    y_tasks = [
        Y(in_=_.out, sleep_time=100) for _ in x_tasks
    ]

    backend = tmp_path / "makeit.json"

    start = time.perf_counter()
    with pytest.raises(ChildProcessException):
        mp_execute_on_change(x_tasks + y_tasks, backend)
    elapsed = time.perf_counter() - start

    assert elapsed <= 2

    content = json.loads(backend.read_text())

    assert "main" in content

    # check that not all task need to be recalculated -- something should be registered in the backend
    execute_on_change(x_tasks, backend)
    assert X.execution_cnt < len(x_tasks)


