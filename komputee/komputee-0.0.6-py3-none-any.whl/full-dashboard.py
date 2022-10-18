from typing import Any
from fastapi import FastAPI
import pandas as pd
from komputee import Komputee, KomputeeFunctionRequest, KomputeeFunctionResponse, PieChart, LineChart, Series, Alert, Statistic, StatisticChange, StatisticProgress, Table, BarChart, Gauge
import numpy as np

app = Komputee(FastAPI())


@app.post("/my-function", response_model=KomputeeFunctionResponse)
async def myFunction(params: KomputeeFunctionRequest):

    df = pd.DataFrame({"Weekday": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Store 1": np.random.random_integers(
        0, 100, size=5), "Store 2": np.random.random_integers(
        0, 100, size=5)})
    df = df.set_index('Weekday')

    x1 = np.random.random_integers(0, 100)
    x2 = np.random.random_integers(0, 100)

    earnings = Statistic(title="Total Earnings", statistic=x1, change=StatisticChange(
        by=np.random.random_integers(0, 10), type=np.random.choice(["increase", 'decrease'])), progress=StatisticProgress(current=x1, goal=100, percentage=x1/100))

    spending = Statistic(title="Total Spendings", statistic=x2, change=StatisticChange(
        by=np.random.random_integers(0, 10), type="increase"), progress=StatisticProgress(current=x2, goal=100, percentage=x2/100),)

    barData = np.random.normal(0, 5, size=100).cumsum()
    barData = barData + np.abs(barData.min())
    barData = list(barData)

    barChart = BarChart(
        index=list(range(100)),
        series=[
            Series(name="Store 1", data=barData)]
    )

    return {
        "data": {
            "my-earnings": earnings,
            "my-spending": spending,
            "my-gauge": Gauge(value=np.random.random_integers(0, 100), min=0, max=100),
            "my-bar": barChart,
            "my-table": df.to_dict(orient="tight")
        }
    }
