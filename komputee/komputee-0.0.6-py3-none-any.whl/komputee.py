from typing import Any, List, Literal, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware


class KomputeeFunctionRequest(BaseModel):
    __root__: dict[str, Any]


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
    type: Literal['alert'] = Field(default='alert', const=True)
    style: Union[Literal["success"], Literal["info"],
                 Literal["warning"], Literal["error"]] = Field(default='info')
    message: str = Field(default='Some Message')


class Table(BaseModel):
    type: Literal['table'] = Field(default='table', const=True)
    index: Union[List[str], List[int], List[float]]
    columns: Union[List[str], List[int], List[float]]
    data:  List[Union[List[str], List[int], List[float]]]
    index_names: Union[List[str], List[int], List[float]] = Field(default=[])
    column_names: Union[List[str], List[int], List[float]] = Field(default=[])


class Series(BaseModel):
    name: Optional[str]
    data: Union[List[int], List[float]]


class LineChart(BaseModel):
    type: Literal['line'] = Field(default='line', const=True)
    index: Union[List[str], List[int], List[float]]
    series: List[Series]


class BarChart(BaseModel):
    type: Literal['bar'] = Field(default='bar', const=True)
    index: Union[List[str], List[int], List[float]]
    series: List[Series]


class PieChartElement(BaseModel):
    name: str
    value: float


class PieChart(BaseModel):
    type: Literal['pie'] = Field(default='pie', const=True)
    title: Optional[str]
    subtitle: Optional[str]
    data: List[PieChartElement]


class StatisticChange(BaseModel):
    by: Optional[Union[str, int, float]]
    type: Optional[Union[Literal["increase"], Literal["decrease"]]]


class StatisticProgress(BaseModel):
    current: Union[int, float, str]
    goal: Union[int, float, str]
    percentage: float


class Statistic(BaseModel):
    type: Literal['statistic'] = Field(default='statistic', const=True)
    title: Optional[str]
    statistic: Union[str, int, float]
    change: Optional[StatisticChange]
    progress: Optional[StatisticProgress]


class Gauge(BaseModel):
    type: Literal['gauge'] = Field(default='gauge', const=True)
    value: float = Field(default=33.33)
    min: Optional[float] = Field(default=0)
    max: Optional[float] = Field(default=100)


class KomputeeFunctionResponse(BaseModel):
    data: dict[str, Union[Alert, Table, LineChart,
                          PieChart, BarChart, Statistic, Gauge]]
    error: Optional[str] = None
