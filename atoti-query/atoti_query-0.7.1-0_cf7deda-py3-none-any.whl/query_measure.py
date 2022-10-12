from dataclasses import dataclass
from typing import Optional

from atoti_core import BaseMeasure, keyword_only_dataclass


@keyword_only_dataclass
@dataclass
class QueryMeasure(BaseMeasure):
    """Measure of a query cube."""

    _visible: bool
    _folder: Optional[str]
    _formatter: Optional[str]
    _description: Optional[str]

    @property
    def folder(self) -> Optional[str]:
        """Folder of the measure."""
        return self._folder

    @property
    def visible(self) -> bool:
        """Whether the measure is visible or not."""
        return self._visible

    @property
    def description(self) -> Optional[str]:
        """Description of the measure."""
        return self._description

    @property
    def formatter(self) -> Optional[str]:
        """Formatter of the measure."""
        return self._formatter
