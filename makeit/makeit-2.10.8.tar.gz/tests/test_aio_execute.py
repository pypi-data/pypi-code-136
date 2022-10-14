import asyncio
import dataclasses
import io
import time

from makeit import Dependency, Target, DataclassTask
from makeit.core import aio_execute_on_change
from tests.utils import InMemoryArtifact


@dataclasses.dataclass
class Multiply(DataclassTask):
    x1: InMemoryArtifact | Dependency
    x2: InMemoryArtifact | Dependency
    res: InMemoryArtifact | Target

    async def a_execute(self):
        await asyncio.sleep(2)

        self.res.put_data(
            self.x1.get_data() * self.x2.get_data()
        )


@dataclasses.dataclass
class Add(DataclassTask):
    x1: InMemoryArtifact | Dependency
    x2: InMemoryArtifact | Dependency
    res: InMemoryArtifact | Target

    async def a_execute(self):
        await asyncio.sleep(1)

        self.res.put_data(
            self.x1.get_data() + self.x2.get_data()
        )


def test_aio_execute_on_change():
    a1 = InMemoryArtifact("a1", 1)
    a2 = InMemoryArtifact("a2", 2)
    a3 = InMemoryArtifact("a3", 3)
    a4 = InMemoryArtifact("a3", 4)

    _i1 = InMemoryArtifact("_i1")
    _i2 = InMemoryArtifact("_i2")

    res = InMemoryArtifact("res")

    # a1 * a2 + a3 * a4
    tasks = [Add(_i1, _i2, res), Multiply(a1, a2, _i1), Multiply(a3, a4, _i2)]

    stream = io.StringIO(initial_value="{}")

    start = time.perf_counter()
    asyncio.run(aio_execute_on_change(tasks, stream), debug=True)
    elapsed = time.perf_counter() - start

    assert elapsed <= 3.2

    assert res.get_data() == a1.get_data() * a2.get_data() + a3.get_data() * a4.get_data()

    start = time.perf_counter()
    asyncio.run(aio_execute_on_change(tasks, stream), debug=True)
    elapsed = time.perf_counter() - start

    assert elapsed <= 0.1
    assert res.get_data() == a1.get_data() * a2.get_data() + a3.get_data() * a4.get_data()
