from fastapi import FastAPI
from komputee import Komputee, PieChart, PieChartElement, KomputeeFunctionRequest, KomputeeFunctionResponse, LineChart, Series, BarChart, Alert, Gauge, Table
import numpy as np

app = Komputee(FastAPI())


@app.post("/my-function", response_model=KomputeeFunctionResponse)
async def myFunction(params: KomputeeFunctionRequest):
    return {
        "data": {
            "my-line": LineChart(index=np.arange(100).tolist(), series=[
                Series(data=np.arange(100).tolist()),
            ]),
            "my-pie": PieChart(title="My Title", subtitle="", data=[PieChartElement(name="A", value=30), PieChartElement(name="B", value=70)]),
            "my-bar": BarChart(index=[1, 2, 3], series=[
                Series(data=[1, 2, 3], name="first"),
            ]),
            "my-alert": Alert(message="Hello World", style="error"),
            "my-gauge": Gauge(max=200, value=99),
            "my-table": Table(index=[1, 2, 3], columns=[1, 2, 3], data=[[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
        }
    }
