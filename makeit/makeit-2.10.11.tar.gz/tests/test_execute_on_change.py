import dataclasses
import math
from pathlib import Path

from makeit import execute_on_change, Target, Dependency, register_type, File, DataclassTask


@dataclasses.dataclass
class Sum(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target

    executed = 0

    def execute(self):
        self.executed += 1

        values = [
            int(f.read_text())
            for f in self.in_
        ]

        self.out_.write_text(
            f"{sum(values)}"
        )


@dataclasses.dataclass
class Mult(DataclassTask):
    in_: list[Path] | Dependency
    out_: Path | Target

    executed = 0

    def execute(self):
        self.executed += 1

        values = [
            int(f.read_text())
            for f in self.in_
        ]

        self.out_.write_text(
            f"{math.prod(values)}"
        )


def test_execute_on_change(tmp_path):
    register_type(Path, lambda _: File(_))

    f1 = tmp_path / "1.sum1.txt"
    f2 = tmp_path / "2.sum1.txt"
    f3 = tmp_path / "3.sum1.txt"

    f4 = tmp_path / "1.sum2.txt"
    f5 = tmp_path / "2.sum2.txt"
    f6 = tmp_path / "3.sum2.txt"

    for i, _ in enumerate([f1, f2, f3, f4, f5, f6]):
        _.write_text(f"{i+1}")

    o1 = tmp_path / "out1.txt"
    o2 = tmp_path / "out2.txt"

    res = tmp_path / "res.txt"

    a1 = Sum([f1, f2, f3], o1)
    a2 = Sum([f4, f5, f6], o2)

    r = Mult([a1.out_, a2.out_], res)

    # initial run
    execute_on_change([r, a1, a2], tmp_path / "makeit.json", reporter=None)
    assert res.read_text() == f"{(1+2+3)*(4+5+6)}"
    assert a1.executed == a2.executed == r.executed == 1

    # change intermediate file
    o1.write_text("100")
    execute_on_change([r, a1, a2], tmp_path / "makeit.json", reporter=None)

    assert res.read_text() == f"{100 * (4+5+6)}"
    assert (a1.executed == a2.executed == 1) and (r.executed == 2)

    # change leaf file
    f1.write_text("0")
    execute_on_change([r, a1, a2], tmp_path / "makeit.json", reporter=None)

    assert res.read_text() == f"{(0+2+3) * (4 + 5 + 6)}"
    assert (a1.executed == 2) and (a2.executed == 1) and (r.executed == 3)

    # remove target file
    res.unlink()
    execute_on_change([r, a1, a2], tmp_path / "makeit.json", reporter=None)

    assert res.read_text() == f"{(0 + 2 + 3) * (4 + 5 + 6)}"
    assert (a1.executed == 2) and (a2.executed == 1) and (r.executed == 4)

    # modify leaf node, but do not change it
    f1.write_text("0")
    execute_on_change([r, a1, a2], tmp_path / "makeit.json", reporter=None)

    assert res.read_text() == f"{(0 + 2 + 3) * (4 + 5 + 6)}"
    assert (a1.executed == 2) and (a2.executed == 1) and (r.executed == 4)
