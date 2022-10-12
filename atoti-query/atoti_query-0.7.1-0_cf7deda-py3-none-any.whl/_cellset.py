from __future__ import annotations

from typing import Optional, Sequence, TypedDict, Union

MeasureValue = Optional[Union[float, int, str]]
MemberIdentifier = str


class CellsetHierarchy(TypedDict):
    dimension: str
    hierarchy: str


class CellsetMember(TypedDict):
    captionPath: Sequence[str]
    namePath: Sequence[MemberIdentifier]


class CellsetAxis(TypedDict):
    id: int
    hierarchies: Sequence[CellsetHierarchy]
    positions: Sequence[Sequence[CellsetMember]]


class CellsetCellProperties(TypedDict):
    BACK_COLOR: Optional[Union[int, str]]
    FONT_FLAGS: Optional[int]
    FONT_NAME: Optional[str]
    FONT_SIZE: Optional[int]
    FORE_COLOR: Optional[Union[int, str]]


class CellsetCell(TypedDict):
    formattedValue: str
    ordinal: int
    properties: CellsetCellProperties
    value: MeasureValue


class CellsetDefaultMember(TypedDict):
    captionPath: Sequence[str]
    dimension: str
    hierarchy: str
    path: Sequence[MemberIdentifier]


class Cellset(TypedDict):
    axes: Sequence[CellsetAxis]
    cells: Sequence[CellsetCell]
    cube: str
    defaultMembers: Sequence[CellsetDefaultMember]
