from typing import Any, Literal, Optional
from pydantic import BaseModel

KomputeeFunctionRequest = dict[str, Any]


class Alert(BaseModel):
    type: Literal["success"] | Literal["info"] | Literal["warning"] | Literal["error"]
    message: str


class Table(BaseModel):
    index: list[str | float | int]
    columns:  list[str | float | int]
    data:  list[list[str | float | int]]
    index_names:  list[str | float | None]
    column_names:  list[str | float | None]


class Series(BaseModel):
    name: Optional[str]
    data: list[float | int]


class LineChart(BaseModel):
    index: list[str | float | int]
    series: list[Series]


class StatisticChange(BaseModel):
    by: Optional[str | float | int]
    type: Optional[Literal["increase"] | Literal["decrease"]]


class StatisticProgress(BaseModel):
    current: float | int | str
    goal: float | int | str
    percentage: float | int


class Statistic(BaseModel):
    name: str
    statistic: Optional[str | float | int]
    change: Optional[StatisticChange]
    progress: Optional[StatisticProgress]


class KomputeeFunctionResponse(BaseModel):
    data: dict[str, Alert | Table | LineChart | list[Statistic]]
    error: Optional[str] = None
