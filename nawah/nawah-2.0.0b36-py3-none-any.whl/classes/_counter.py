"""Provides 'Counter' dataclass"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Union

if TYPE_CHECKING:
    from nawah.types import NawahDoc


@dataclass(kw_only=True)
class Counter:
    """Counter dataclass serves role as Counter Value Instruction. Callable as value for 'counter'
    should accept only: 'doc'. Callable as value for 'pattern_formatter' should accept any of the
    following args only: 'counter_value', 'doc'"""

    counter: Union[str, Callable[["NawahDoc"], str]]
    pattern_formatter: Union[
        Callable[[int, "NawahDoc"], str],
        Callable[[int], str],
        Callable[["NawahDoc"], str],
        Callable[[], str],
    ]
