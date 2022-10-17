import dataclasses

import pytest

from makeit.core import execute, DAG, DictBackend, EARunOnChange, EACheckExists
from tests.utils import InMemoryArtifact, Multiply, Add, Nothing


@dataclasses.dataclass
class Calculator:
    a1: InMemoryArtifact
    a2: InMemoryArtifact
    a3: InMemoryArtifact

    i1: InMemoryArtifact

    res: InMemoryArtifact

    dag: DAG

    # a2 * a3 + a1
    m: Multiply
    a: Add
    n: Nothing


@pytest.fixture
def calc():
    a1 = InMemoryArtifact("a1", 7)
    a2 = InMemoryArtifact("a2", 4)
    a3 = InMemoryArtifact("a3", -1)

    _i1 = InMemoryArtifact("_i1")

    res = InMemoryArtifact("res")

    dag = DAG("main")

    # a2 * a3 + a1
    _m = Multiply(a2, a3, _i1)
    _a = Add(_i1, a1, res)
    _n = Nothing()

    dag.add(_m)
    dag.add(_a)
    dag.add(_n)

    return Calculator(a1, a2, a3, _i1, res, dag, _m, _a, _n)


def test_number_of_fingerprint_calls(calc):
    backend = DictBackend(None)

    execute(calc.dag, backend, EARunOnChange, None)

    assert calc.res.get_data() == calc.a2.get_data() * calc.a3.get_data() + calc.a1.get_data()
    assert calc.a1.fingerprint_calls == 1
    assert calc.a2.fingerprint_calls == 1
    assert calc.a3.fingerprint_calls == 1
    assert calc.i1.fingerprint_calls == 1


def test_run_on_change(calc):
    backend = DictBackend(None)

    execute(calc.dag, backend, EARunOnChange, None)
    assert calc.res.get_data() == calc.a2.get_data() * calc.a3.get_data() + calc.a1.get_data()
    assert calc.m.execute_calls == 1
    assert calc.a.execute_calls == 1
    assert calc.n.execute_calls == 1

    calc.a1.put_data(0)

    execute(calc.dag, backend, EARunOnChange, None)
    assert calc.res.get_data() == calc.a2.get_data() * calc.a3.get_data() + calc.a1.get_data()
    assert calc.m.execute_calls == 1
    assert calc.a.execute_calls == 2
    assert calc.n.execute_calls == 1

    calc.a2.put_data(2)
    calc.a3.put_data(-2)

    execute(calc.dag, backend, EARunOnChange, None)
    assert calc.res.get_data() == calc.a2.get_data() * calc.a3.get_data() + calc.a1.get_data()
    assert calc.m.execute_calls == 2
    assert calc.a.execute_calls == 2  # _i1 hasn't changed: 4*(-1) == 2*(-2)
    assert calc.n.execute_calls == 1


def test_check_exists(calc):
    backend = None

    execute(calc.dag, backend, EACheckExists, None)
    assert calc.res.get_data() == calc.a2.get_data() * calc.a3.get_data() + calc.a1.get_data()
    assert calc.m.execute_calls == 1
    assert calc.a.execute_calls == 1
    assert calc.n.execute_calls == 1

    _prev_res = calc.res.get_data()

    calc.a1.put_data(0)

    execute(calc.dag, backend, EACheckExists, None)
    assert calc.res.get_data() == _prev_res
    assert calc.m.execute_calls == 1
    assert calc.a.execute_calls == 1
    assert calc.n.execute_calls == 2

    calc.a2.put_data(2)
    calc.a3.put_data(-2)

    execute(calc.dag, backend, EACheckExists, None)
    assert calc.res.get_data() == _prev_res
    assert calc.m.execute_calls == 1
    assert calc.a.execute_calls == 1
    assert calc.n.execute_calls == 3
