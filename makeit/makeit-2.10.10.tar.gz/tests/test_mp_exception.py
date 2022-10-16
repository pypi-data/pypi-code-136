import dataclasses
import math
from pathlib import Path

import pytest

from makeit import mp_execute_on_change, Target, Dependency, register_type, File, DataclassTask
from makeit.core import SimpleReporter, TaskEvent

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


def test_execute_on_change(tmp_path):
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
