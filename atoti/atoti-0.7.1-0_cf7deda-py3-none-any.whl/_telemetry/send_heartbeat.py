from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta
from typing import Callable

from atoti_core import keyword_only_dataclass

from .event import Event
from .run_with_exponential_backoff import run_with_exponential_backoff
from .send_event import send_event


@keyword_only_dataclass
@dataclass(frozen=True)
class HeartbeatEvent(Event):
    """Triggered periodically to indicate that the process is still running."""

    event_type: str = field(default="heartbeat", init=False)


_FIRST_WAIT_DURATION = timedelta(seconds=30)


def send_heartbeat() -> Callable[[], None]:
    return run_with_exponential_backoff(
        lambda: send_event(HeartbeatEvent()),
        daemon=True,
        first_wait_duration=_FIRST_WAIT_DURATION,
    )
