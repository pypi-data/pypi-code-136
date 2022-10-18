import json
from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass(kw_only=True)
class AbstractConfig(ABC):
    name: str
    reshaper: List[str]
    plotter: List[str]
    filename: str
    experiment_class = None  # type: ignore
    experiment_module: str

    def to_json(self) -> str:
        """return a dictionary of instance variables"""
        return json.dumps(vars(self), indent=4)
