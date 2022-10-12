from datetime import timedelta
from threading import Event, Thread
from typing import Callable, Generator, Optional

_DEFAULT_BACKOFF_BASE = 2


def _back_off_exponentially(
    *, base: float = _DEFAULT_BACKOFF_BASE
) -> Generator[float, None, None]:
    step = 0
    while True:
        yield base**step
        step += 1


def run_with_exponential_backoff(
    callback: Callable[[], None],
    /,
    *,
    base: float = _DEFAULT_BACKOFF_BASE,
    daemon: Optional[bool] = None,
    first_wait_duration: timedelta = timedelta(seconds=1),
) -> Callable[[], None]:
    scale = first_wait_duration.total_seconds()
    wait_duration_generator = _back_off_exponentially(base=base)

    stopped = Event()

    def loop() -> None:
        while not stopped.wait(scale * next(wait_duration_generator)):
            callback()

    Thread(target=loop, daemon=daemon).start()

    return stopped.set
