import asyncio
import dataclasses

import pytest

from makeit import mp_execute_on_change, execute_on_change, Target, Dependency, DataclassTask, \
    register_type, File, aio_execute_on_change

from pathlib import Path

import time

import random


@dataclasses.dataclass
class Combine(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target

    sleep_sec: float

    def execute(self):
        time.sleep(self.sleep_sec)

        self.out_.write_text(
            "".join(_.read_text() for _ in self.in_)
        )


@dataclasses.dataclass
class CombineAsync(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target

    sleep_sec: float

    async def a_execute(self):
        await asyncio.sleep(self.sleep_sec)

        self.out_.write_text(
            "".join(_.read_text() for _ in self.in_)
        )


@pytest.mark.parametrize(
    "num_tasks, batch_size, task_class, exec_foo, sleep_sec, dag_name",
    [
        (50, 2, Combine, execute_on_change, 0.1, "sequential"),
        (50, 2, Combine, mp_execute_on_change, 0.1, "parallel 1"),
        (100, 2, Combine, mp_execute_on_change, 0.5, "parallel 2"),
        (100, 2, CombineAsync, aio_execute_on_change, 0.5, "async 2")
    ]
)
def test_pyramid_game(tmp_path, num_tasks, batch_size, task_class, exec_foo, sleep_sec, dag_name):
    register_type(Path, lambda _: File(_, label=_.name))

    tasks = []
    inter = [_ for _ in range(num_tasks)]

    answer = "".join(str(_) for _ in inter)

    while len(inter) > 1:
        random.shuffle(inter)

        batch = inter[:batch_size]

        inter = inter[len(batch):]

        t = task_class([], None, sleep_sec=sleep_sec)

        for el in batch:
            if isinstance(el, int):
                _ = tmp_path / f"{el}.txt"
                _.write_text(str(el))

                t.in_.append(_)
            else:
                assert isinstance(el, task_class)

                tasks.append(el)

                t.in_.append(el.out_)

        t.out_ = tmp_path / t.md5(".txt")

        inter.append(t)

    exec_foo(tasks + inter, backend=tmp_path / "makeit.json", dag_name=dag_name)
    assert sorted(inter[0].out_.read_text()) == sorted(answer)
