from fastapi import FastAPI
from komputee import Komputee, KomputeeFunctionRequest, KomputeeFunctionResponse, LineChart, Series

app = Komputee(FastAPI())


@app.post("/my-function", response_model=KomputeeFunctionResponse)
async def myFunction(params: KomputeeFunctionRequest):
    return {
        "data": {
            "my-line": LineChart(index=[1, 2, 3], series=[
                Series(data=[1, 2.4, 3], name="series 1"),
            ])
        }
    }
