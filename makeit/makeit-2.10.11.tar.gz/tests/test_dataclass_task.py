import pytest
import dataclasses

from makeit.core import DataclassTask, register_type, File, Dependency, Target
import makeit.core


def test_dataclass_task_create():
    @dataclasses.dataclass
    class Task(DataclassTask):
        in_1: File | Dependency
        in_2: File | Dependency
        out_: File | Target

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    task = Task(File("1"), File("1.1"), File("2"))

    assert list(_.path.name for _ in task.dependencies()) == ["1", "1.1"]
    assert list(_.path.name for _ in task.targets()) == ["2"]


def test_dataclass_task_list():
    @dataclasses.dataclass
    class Task(DataclassTask):
        in_: list[File] | Dependency
        out_: File | Target

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    task = Task([File("1"), File("1.1")], File("2"))

    assert list(_.path.name for _ in task.dependencies()) == ["1", "1.1"]
    assert list(_.path.name for _ in task.targets()) == ["2"]


def test_dataclass_task_list_target():
    @dataclasses.dataclass
    class Task(DataclassTask):
        out_: list[File] | Target

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    task = Task([File("1"), File("1.1")])

    assert [_.path.name for _ in task.targets()] == ["1", "1.1"]


def test_dataclass_task_registered_type():
    # int -> File
    @dataclasses.dataclass
    class Task(DataclassTask):
        in_: int | Dependency
        in2: list[int] | Dependency

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    register_type(int, lambda _: File(f"x{_}"))

    task = Task(in_=12, in2=[13, 14])

    assert [_.path.name for _ in task.dependencies()] == ["x12", "x13", "x14"]
    assert list(task.targets()) == []


def test_dataclass_task_type_failure():
    # float is not registered as accepted type
    @dataclasses.dataclass
    class Task(DataclassTask):
        in_: float | Dependency

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    with pytest.raises(makeit.MakeItException):
        task = Task(in_=12.3)
        list(task.dependencies())


def test_dataclass_artifact_without_mark():
    # Artifact must have mark | Dependency or | Target
    @dataclasses.dataclass
    class Task(DataclassTask):
        in_: File

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    with pytest.raises(makeit.MakeItException):
        task = Task(File("1"))
        list(task.dependencies())

    with pytest.raises(makeit.MakeItException):
        task = Task(File("1"))
        list(task.targets())


def test_dataclass_with_dependency_inheritance():
    # if artifact is inherited from Dependency
    class DFile(File, Dependency):
        pass

    @dataclasses.dataclass
    class DTask(DataclassTask):
        in_: DFile

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    task = DTask(DFile("1"))
    assert [_.path.name for _ in task.dependencies()] == ["1"]
    assert [_.path.name for _ in task.targets()] == []


def test_dataclass_with_target_inheritance():
    # if artifact is inherited from Target
    class TFile(File, Target):
        pass

    @dataclasses.dataclass
    class TTask(DataclassTask):
        in_: TFile

        depends_on_source_code_of_self = False

        def execute(self):
            pass

    task = TTask(TFile("1"))
    assert [_.path.name for _ in task.dependencies()] == []
    assert [_.path.name for _ in task.targets()] == ["1"]
