import dataclasses

from makeit import execute_on_change, DataclassTask


num_of_executions = 0


@dataclasses.dataclass
class A(DataclassTask):
    def label(self):
        return "X"

    def execute(self):
        global num_of_executions

        num_of_executions += 1


@dataclasses.dataclass
class B(DataclassTask):
    def label(self):
        return "X"

    def execute(self):
        global num_of_executions

        num_of_executions += 1


def test_self_source(tmp_path):
    backend = tmp_path / "makeit.json"

    execute_on_change([A()], backend)
    assert num_of_executions == 1

    execute_on_change([A()], backend)
    assert num_of_executions == 1

    execute_on_change([B()], backend)
    assert num_of_executions == 2

    print(backend.read_text())
