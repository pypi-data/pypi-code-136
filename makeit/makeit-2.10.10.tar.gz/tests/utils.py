import dataclasses
from typing import Any

from makeit import DataclassTask, Dependency, Target

from makeit.core import Artifact


class InMemoryArtifact(Artifact):
    def __init__(self, label, data=None):
        self._label = label
        self._data = data

        self.fingerprint_calls = 0
        self.label_calls = 0

    def modification_time(self):
        raise RuntimeError("Not defined for this type of artifact")

    def fingerprint(self) -> str | None:
        self.fingerprint_calls += 1

        if self._data is None:
            return None

        return f"{hash(self._data)}"

    def exists(self, *args) -> bool:
        return self._data is not None

    def label(self) -> str:
        self.label_calls += 1

        return self._label

    def put_data(self, data: Any):
        self._data = data

    def get_data(self):
        if self._data is None:
            raise KeyError()

        return self._data

    def __repr__(self):
        return f"InMemoryArtifact({self._label})"


@dataclasses.dataclass
class Multiply(DataclassTask):
    x1: InMemoryArtifact | Dependency
    x2: InMemoryArtifact | Dependency
    res: InMemoryArtifact | Target

    dependencies_calls = 0
    targets_calls = 0
    label_calls = 0
    execute_calls = 0

    def label(self) -> str:
        self.label_calls += 1
        return f"{self.x1} * {self.x2} -> {self.res}"

    def execute(self):
        self.execute_calls += 1

        self.res.put_data(
            self.x1.get_data() * self.x2.get_data()
        )

    def dependencies(self):
        self.dependencies_calls += 1

        yield self.x1
        yield self.x2

    def targets(self):
        self.targets_calls += 1

        yield self.res


@dataclasses.dataclass
class Add(DataclassTask):
    x1: InMemoryArtifact | Dependency
    x2: InMemoryArtifact | Dependency
    res: InMemoryArtifact | Target

    dependencies_calls = 0
    targets_calls = 0
    label_calls = 0
    execute_calls = 0

    def label(self) -> str:
        self.label_calls += 1
        return f"{self.x1} + {self.x2} -> {self.res}"

    def execute(self):
        self.execute_calls += 1

        self.res.put_data(
            self.x1.get_data() + self.x2.get_data()
        )

    def dependencies(self):
        self.dependencies_calls += 1

        yield self.x1
        yield self.x2

    def targets(self):
        self.targets_calls += 1

        yield self.res


@dataclasses.dataclass
class Nothing(DataclassTask):
    execute_calls = 0

    def label(self) -> str:
        return "Nothing"

    def execute(self):
        self.execute_calls += 1
