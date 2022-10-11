from typing import Union, Iterable, Callable, Any, List

from prefect import task, Task
import prefect

from datetime import timedelta, datetime, date
import time

import logging

__all__ = ["nop", "wait_for", "echo", "decode", "filter_elements", "truncate"]

LOG = logging.getLogger(__name__)


@task()
def nop() -> None:
    pass


@task()
def wait_for(dt: Union[timedelta, float, int]) -> None:
    if isinstance(dt, timedelta):
        dt = dt.seconds

    LOG.debug(f"Waiting for {dt} seconds")
    time.sleep(dt)


@task(log_stdout=True)
def echo(x: str):
    LOG.debug(x)
    print(x)


@task()
def decode(
    data: bytes,
    source_encoding: str,
) -> str:
    return data.decode(source_encoding)


@task(nout=True)
def filter_elements(iterable: Iterable, filter_cb: Callable[[Any], bool]) -> Iterable:
    return [x for x in iterable if filter_cb(x)]


@task(nout=True)
def truncate(lst: List, start_index: int = 0, end_index: int = -1) -> List:
    return lst[start_index:end_index]


@task()
def nonnull(arg, default=None):
    if arg is None:
        ret = default
    else:
        ret = arg

    if callable(ret):
        return ret()
    else:
        return ret


@task()
def sleep_task(secs: float):
    log = prefect.context["logger"]
    log.debug(f"Sleeping for {secs:0.3f} seconds")
    time.sleep(secs)


def today() -> Task:
    return days_ago(0)


def yesterday() -> Task:
    return days_ago(1)


@task()
def days_ago(count: int) -> str:
    return (date.today() - timedelta(days=count)).isoformat()
