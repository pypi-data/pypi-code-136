from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from functools import lru_cache
from uuid import uuid4

from atoti_core import keyword_only_dataclass


@lru_cache
def _get_process_id() -> str:
    return str(uuid4())


@keyword_only_dataclass
@dataclass(frozen=True)
class Event(ABC):
    process_id: str = field(default_factory=_get_process_id, init=False)
    event_type: str
