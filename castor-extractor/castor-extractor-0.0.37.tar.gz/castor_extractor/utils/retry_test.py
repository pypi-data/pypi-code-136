from statistics import variance
from time import time
from typing import List

from .retry import MS_IN_SEC, Retry, RetryStrategy


def _within(value: int, min_: int, max_: int) -> bool:
    return value >= min_ and value <= max_


def test_retry_strategy__jitter():
    retry = Retry(count=2, base_ms=1000, jitter_ms=500)
    jitters = [retry.jitter() for _ in range(5)]

    # boundaries
    assert all(_within(j, 250, 750) for j in jitters)
    # randomness
    assert variance(jitters) > 0


def _iterate_base(retry: Retry, count: int) -> List[int]:
    bases: List[int] = []
    for _ in range(3):
        retry.count += 1
        bases.append(retry.base())
    return bases


def test_retry_strategy__base():
    common_args = {"count": 2, "base_ms": 2000, "jitter_ms": 500}
    # default strategy is constant
    retry = Retry(**common_args)
    assert _iterate_base(retry, 3) == [2000, 2000, 2000]
    retry = Retry(**common_args, strategy=RetryStrategy.CONSTANT)
    assert _iterate_base(retry, 3) == [2000, 2000, 2000]
    # linear
    retry = Retry(**common_args, strategy=RetryStrategy.LINEAR)
    assert _iterate_base(retry, 3) == [2000, 4000, 6000]
    # exponential
    retry = Retry(**common_args, strategy=RetryStrategy.EXPONENTIAL)
    assert _iterate_base(retry, 3) == [2000, 4000, 8000]


def test_retry_strategy__check():
    retry = Retry(count=3, base_ms=100, jitter_ms=10)

    before = time()
    assert retry.check()
    assert retry.check()
    assert retry.check()
    after = time()

    assert retry.check() is False
    delta_ms = int((after - before) * MS_IN_SEC)
    assert _within(delta_ms, 315, 345)
