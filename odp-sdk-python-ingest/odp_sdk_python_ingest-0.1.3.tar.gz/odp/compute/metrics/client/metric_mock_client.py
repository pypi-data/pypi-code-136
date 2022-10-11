from odp.compute.metrics import MetricClient, Counter, Gauge, Distribution
from typing import Optional, List
from numbers import Number
import logging

__all__ = ["MetricMockClient"]

LOG = logging.getLogger(__file__)


class MockCounter(Counter):
    def __init__(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )
        self.value = 0

    def inc(self, n: Number = 1, labels: Optional[List] = None):
        self.value += n

    def dec(self, n: Number = 1, labels: Optional[List] = None):
        self.value -= n


class MockGauge(Gauge):
    def __init__(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )
        super().__init__(namespace, name)
        self.value = 0

    def set(self, value: Number, labels: Optional[List] = None):
        self.value = value


class MockDistribution(Distribution):
    def __init__(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )
        self.value = 0.0

    def update(self, value: Number, labels: Optional[List] = None):
        self.value = value


class MetricMockClient(MetricClient):
    def create_counter(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Counter:
        return MockCounter(namespace, name)

    def create_gauge(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Gauge:
        return MockGauge(namespace, name)

    def create_distribution(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Distribution:
        return MockDistribution(namespace, name)

    def push(self):
        LOG.debug("Fake-pushing metrics")
