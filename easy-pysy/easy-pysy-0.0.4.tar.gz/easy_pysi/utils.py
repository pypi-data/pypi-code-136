import logging
import threading
import time
from functools import wraps

from typing import Optional, Type
from uuid import uuid4

logger = logging.getLogger(__name__)


class Interval:
    def __init__(self, interval_ms, callback, on_error_callback, daemon=True, *args, **kwargs):
        self.interval_ms = interval_ms
        self.callback = callback
        self.on_error_callback = on_error_callback
        self.daemon = daemon
        self.args = args
        self.kwargs = kwargs

        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=self.daemon)

    def _run(self):
        next_time = time.time() + self.interval_seconds
        while not self.stop_event.wait(next_time - time.time()):
            try:
                next_time += self.interval_seconds
                self.callback(*self.args, **self.kwargs)
            except BaseException as exc:
                self.on_error_callback(exc)

    def start(self):
        if self.thread.is_alive():
            raise RuntimeError('Interval already started')
        self.thread.start()

    def stop(self):
        if not self.thread.is_alive():
            raise RuntimeError('Thread already stopped')
        self.stop_event.set()

    @property
    def interval_seconds(self) -> float:
        return self.interval_ms / 1000.0


def require(condition: bool, message: Optional[str] = None):
    if not condition:
        raise RequirementError(message)


class RequirementError(Exception):
    pass


def uuid() -> str:
    return str(uuid4())


def tri_wave(min_value: int, max_value: int, step: int = 1):
    while True:
        yield from range(min_value, max_value, step)
        yield from range(max_value, min_value, -step)


def float_range(start: float, stop: float, step: float = 1.0, decimals: int = 2):
    for i in range(int(start / step), int(stop / step)):
        yield round(i * step, ndigits=decimals)


def retry(times: int, exception_class: Type = BaseException, sleep=0):
    assert times >= 1, "times should be >= in @retry"

    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            last_exception = None
            while attempt <= times:
                try:
                    return func(*args, **kwargs)
                except exception_class as exc:
                    attempt += 1
                    last_exception = exc
                    if attempt <= times:
                        time.sleep(sleep)
                    else:
                        raise exc
            raise last_exception
        return wrapper
    return decorated
