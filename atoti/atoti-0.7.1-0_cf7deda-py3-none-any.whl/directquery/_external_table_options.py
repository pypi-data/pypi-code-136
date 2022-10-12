from abc import ABC
from dataclasses import dataclass
from typing import Generic, Mapping, Optional, Sequence, Union

from atoti_core import EMPTY_MAPPING, keyword_only_dataclass

from ..directquery import MultiColumnArrayConversion, MultiRowArrayConversion
from ._external_table import ExternalTableT


@keyword_only_dataclass
@dataclass(frozen=True)
class ExternalTableOptions(Generic[ExternalTableT], ABC):
    _array_conversion: Optional[
        Union[MultiColumnArrayConversion, MultiRowArrayConversion]
    ] = None
    _keys: Optional[Sequence[str]] = None
    _options: Mapping[str, object] = EMPTY_MAPPING
