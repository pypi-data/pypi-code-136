from typing import List

from bigeye_sdk.client.datawatch_client import DatawatchClient
from bigeye_sdk.generated.com.torodata.models.generated import MetricConfiguration, MetricCreationState


def delete_metrics(client: DatawatchClient, metrics: List[MetricConfiguration]):
    deleatable = [m for m in metrics if m.metric_creation_state != MetricCreationState.METRIC_CREATION_STATE_SUITE]

