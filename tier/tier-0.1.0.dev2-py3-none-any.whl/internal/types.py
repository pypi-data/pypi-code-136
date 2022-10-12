# std
from __future__ import annotations
from typing import Dict, List, Union

# types
NoneType = type(None)
AtomicData = Union[NoneType, bool, str, int, float]
DictData = Dict[str, 'Data']
ListData = List['Data']
Data = Union[AtomicData, DictData, ListData]
