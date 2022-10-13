import dataclasses
import pytest

from makeit import execute_on_change, Target, Dependency, MakeItException, DataclassTask
from pathlib import Path


@dataclasses.dataclass
class A(DataclassTask):
    label = "X"

    def execute(self):
        pass


def test_two_tasks_with_same_name():
    with pytest.raises(MakeItException):
        execute_on_change([A(), A()], None)


@dataclasses.dataclass
class B(DataclassTask):
    tar: Path | Target

    def execute(self):
        pass


def test_no_target_created():
    with pytest.raises(MakeItException):
        execute_on_change([B(Path("1"))], None)


@dataclasses.dataclass
class C(DataclassTask):
    dep: Path | Dependency

    def execute(self):
        pass


def test_no_dependency(tmp_path):
    with pytest.raises(MakeItException):
        execute_on_change([
            C(tmp_path / "1.txt")
        ], None)
