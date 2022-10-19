from typing import List
from dataclasses import dataclass, field

from argparse import Namespace

@dataclass
class RunningConfig:
    bus_connection: str
    debug: bool = False
    banner: bool = False
    queue_name: List[str] = field(default_factory=lambda: ["default"])

    @classmethod
    def from_cli(cls, parsed: Namespace):
        return cls(**{k: v for k, v in parsed.__dict__.items() if v is not None})

__all__ = ("RunningConfig", )
