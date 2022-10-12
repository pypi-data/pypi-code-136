from abc import ABC, abstractmethod
from dataclasses import dataclass

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class BaseOrder(ABC):
    """Base class for orders."""

    @property
    @abstractmethod
    def _key(self) -> str:
        ...
