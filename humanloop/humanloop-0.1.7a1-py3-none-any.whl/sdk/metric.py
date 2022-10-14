import inspect
from typing import Callable, Optional, Union

from humanloop.api.models.metric import (
    CreateMetricRequest,
    MetricResponse,
    UpdateMetricRequest,
)
from humanloop.sdk.init import _get_client

# TODO given Metric.id is globally unique, should remove the need for specifying
# project_id as part of update and delete

# TODO pull out the *args, **kwargs validation logic into a separate function to remove duplication


def create_metric(
    project_id: str, name: str, description: str, code: Union[Callable, str]
) -> MetricResponse:
    """Create a metric with name, description and code."""
    client = _get_client()
    code = _process_metric_code(code)
    return client.create_metric(
        project_id=project_id,
        metric=CreateMetricRequest(name=name, description=description, code=code),
    )


def update_metric(
    project_id: str,
    metric_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    code: Optional[str] = None,
    active: Optional[str] = None,
) -> MetricResponse:
    """Update metric definition."""
    client = _get_client()
    if code is not None:
        code = _process_metric_code(code)
    return client.update_metric(
        project_id=project_id,
        metric_id=metric_id,
        request=UpdateMetricRequest(
            name=name,
            description=description,
            code=code,
            active=active,
        ),
    )


def get_metrics(project_id: str) -> MetricResponse:
    """Get metrics for a given project."""
    client = _get_client()
    return client.get_metrics(project_id)


def delete_metric(project_id: str, metric_id: str) -> MetricResponse:
    """Delete metric definition."""
    client = _get_client()
    return client.delete_metric(project_id=project_id, metric_id=metric_id)


def _process_metric_code(code: Union[str, Callable]) -> str:
    """
    Validates that metric is valid for sending to client.
    The client expects a string, so if a function object is provided, it is converted to
    a string.
    TODO add compile and run checks (currently happen server side)
    """
    if isinstance(code, str):
        return code

    if callable(code):
        return inspect.getsource(code)
    else:
        raise ValueError("code is not a callable or a string")
