from typing import Any, List, Literal, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


KomputeeFunctionRequest = dict[str, Any]


def Komputee(app: FastAPI):
    origins = [
        "http://localhost:3000",  # only needed for development
        "https://komputee.com"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


class Alert(BaseModel):
    type: Literal["success"] | Literal["info"] | Literal["warning"] | Literal["error"]
    message: str


class Table(BaseModel):
    index: List[str | float | int]
    columns:  List[str | float | int]
    data:  List[List[str | float | int]]
    index_names:  List[str | float | None]
    column_names:  List[str | float | None]


class Series(BaseModel):
    name: Optional[str]
    data: List[float | int]


class LineChart(BaseModel):
    index: List[str | float | int]
    series: List[Series]


class BarChart(BaseModel):
    index: List[str | float | int]
    series: List[Series]


class PieChartElement(BaseModel):
    name: str
    value: float


class PieChart(BaseModel):
    title: str
    subtitle: str
    data: List[PieChartElement]


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


class Gauge(BaseModel):
    value: float
    min: Optional[float]
    max: Optional[float]


class KomputeeFunctionResponse(BaseModel):
    data: dict[str, Alert | Table | LineChart |
               PieChart | BarChart | List[Statistic] | Gauge]
    error: Optional[str] = None
