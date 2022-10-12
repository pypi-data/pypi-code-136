from dataclasses import dataclass
from typing import Literal, Mapping, Optional, Sequence

from atoti_core import Constant, LevelCoordinates, keyword_only_dataclass

AggregateProviderKey = Literal["bitmap", "leaf"]


@keyword_only_dataclass
@dataclass(frozen=True)
class AggregateProviderDescription:
    key: AggregateProviderKey
    levels_coordinates: Sequence[LevelCoordinates]
    measures_names: Sequence[str]
    filters: Mapping[LevelCoordinates, Sequence[Constant]]
    partitioning: Optional[str]
