from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

from .bitwise_operators_only import BitwiseOperatorsOnly
from .keyword_only_dataclass import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(eq=False)
class BaseMeasure(BitwiseOperatorsOnly):
    """Measure of a base cube."""

    _name: str

    @property
    def name(self) -> str:
        """Name of the measure."""
        return self._name

    @property
    @abstractmethod
    def folder(self) -> Optional[str]:
        """Folder of the measure."""

    @property
    @abstractmethod
    def visible(self) -> bool:
        """Whether the measure is visible or not."""

    @property
    @abstractmethod
    def description(self) -> Optional[str]:
        """Description of the measure."""

    @property
    @abstractmethod
    def formatter(self) -> Optional[str]:
        """Formatter of the measure."""

    # This is needed otherwise errors like "TypeError: unhashable type: 'Measure'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:  # pylint: disable=useless-super-delegation, no-self-use
        return super().__hash__()
