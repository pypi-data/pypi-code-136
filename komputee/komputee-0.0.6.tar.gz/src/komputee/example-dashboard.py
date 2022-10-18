from typing import Any
from fastapi import FastAPI
import pandas as pd
from komputee import Komputee, KomputeeFunctionRequest, KomputeeFunctionResponse, PieChart, LineChart, Series, Alert, Statistic, StatisticChange, StatisticProgress, Table, BarChart, Gauge

app = Komputee(FastAPI())


@app.post("/my-function", response_model=KomputeeFunctionResponse)
async def myFunction(params: KomputeeFunctionRequest):

    df = pd.DataFrame({"Weekday": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Store 1": [
                      1, 2, 3, 4, 5], "Store 2": [6, 7, 8, 9, 10]})
    df = df.set_index('Weekday')

    return {
        "data": {
            "my-df": df.to_dict(orient="tight"),  # use tight orientation or
            "my-line-chart": LineChart(index=[1, 2, 3], series=[
                Series(name="Store 1", data=[1, 2, 3]),
            ]),
            "my-bar-chart": BarChart(index=[1, 2, 3], series=[
                Series(name="Store 2", data=[1, 2, 3]),
            ]),
            "my-alert": Alert(message="Hello " + ((" " + params['name']) if params['name'] else '') + " from FastAPI", type="success"),
            "my-statistics": [
                Statistic(name="Store 1", statistic=1, change=StatisticChange(
                    by=1, type="increase"), progress=StatisticProgress(current=1, goal=10, percentage=0.1)),
                Statistic(name="Store 2", statistic=2, change=StatisticChange(
                    by=2, type="decrease"), progress=StatisticProgress(current=2, goal=10, percentage=0.2)),
            ],
            "my-gauge": Gauge(max=10, min=0, value=5),
            "my-pie": PieChart(title="My Pie Chart", subtitle="My Pie Chart Subtitle", data=[
                {"name": "Store 1", "value": 1},
                {"name": "Store 2", "value": 2},
            ]),
        }
    }
