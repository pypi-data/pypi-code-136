import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class CreateMetricRequest(BaseModel):
    name: str = Field(
        title="Metric name", description="Name of the metric to be created."
    )
    description: str = Field(
        title="Metric description",
        description="Description of the metric to be created.",
    )
    code: str = Field(
        title="Metric code",
        description="Python code used to calculate a metric value on each logged datapoint. "
        "The last defined function in the code block will be called with a `log` dict, and should "
        "return a number, or `None`.",
    )


class UpdateMetricRequest(BaseModel):
    name: Optional[str] = Field(
        title="Metric name", description="The name of the metric."
    )
    description: Optional[str] = Field(
        title="Metric description",
        description="A description of what the metric measures.",
    )
    code: Optional[str] = Field(
        title="Metric code",
        description="Python code used to calculate a metric value on each logged datapoint.",
    )
    active: Optional[bool] = Field(
        title="Metric active flag",
        description="If enabled, the metric is calculated for every logged datapoint.",
    )


class MetricExperimentResponse(BaseModel):
    id: str
    name: str


class BaseMetricResponse(BaseModel):
    id: str = Field(
        title="Metric ID", description="ID of the metric. Starts with 'metric_'."
    )
    name: str = Field(title="Metric name", description="The name of the metric.")
    description: str = Field(
        title="Metric description",
        description="A description of what the metric measures.",
    )
    code: str = Field(
        title="Metric code",
        description="Python code used to calculate a metric value on each logged datapoint.",
    )
    default: bool = Field(
        title="Metric default flag",
        description="Whether the metric is a global default metric. "
        "Metrics with this flag enabled cannot be deleted or modified.",
    )
    active: bool = Field(
        title="Metric active flag",
        description="If enabled, the metric is calculated for every logged datapoint.",
    )
    created_at: datetime.datetime
    updated_at: datetime.datetime


class MetricResponse(BaseMetricResponse):
    experiments: List[MetricExperimentResponse] = Field(
        title="Experiments using the metric",
        description="List of experiments optimizing for this metric.",
    )
    num_values: int = Field(
        title="Number of values",
        description="Number of datapoints this metric has been calculated on. "
        "This does not include datapoints where the metric returned `None`.",
    )
