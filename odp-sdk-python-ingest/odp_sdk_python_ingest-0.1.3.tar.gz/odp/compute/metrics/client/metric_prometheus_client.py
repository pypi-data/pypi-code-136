from numbers import Number

from odp.compute.metrics import MetricClient, Counter, Gauge, Distribution

import prefect
from prometheus_client import (
    CollectorRegistry,
    Counter as PrometheusCounter,
    Gauge as PrometheusGauge,
    push_to_gateway,
)
from os import getenv
from typing import Optional, List
import logging

__all__ = ["MetricPrometheusClient"]

LOG = logging.getLogger(__file__)


class MetricPrometheusCounter(Counter):
    def __init__(
        self,
        registry: CollectorRegistry,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )
        self._counter = PrometheusCounter(
            name=name,
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )

    def inc(self, n: Number = 1, labels: Optional[List] = None):
        if labels:
            self._counter.labels(*labels).inc(n)
        else:
            self._counter.inc(n)

    def dec(self, n: Number = 1, labels: Optional[List] = None):
        self.inc(-n, labels)


class MetricPrometheusGauge(Gauge):
    def __init__(
        self,
        registry: CollectorRegistry,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )
        self._gauge = PrometheusGauge(
            name=name,
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )

    def set(self, value: Number, labels: Optional[List] = None):
        if labels:
            self._gauge.labels(*labels).set(value)
        else:
            self._gauge.set(value)


class MetricPrometheusDistribution(Distribution):
    def __init__(
        self,
        registry: CollectorRegistry,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        super().__init__(
            namespace=namespace, name=name, labels=labels, description=description
        )

        self._min = None
        self._max = None
        self._mean = None
        self._absmean = None
        self._count = 0
        self._sum = 0
        self._abssum = 0

        self._min_gauge = PrometheusGauge(
            name=name + "_min",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._max_gauge = PrometheusGauge(
            name=name + "_max",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._mean_gauge = PrometheusGauge(
            name=name + "_mean",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._absmean_gauge = PrometheusGauge(
            name=name + "_absmean",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._sum_gauge = PrometheusGauge(
            name=name + "_sum",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._abssum_gauge = PrometheusGauge(
            name=name + "_abssum",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._count_gauge = PrometheusGauge(
            name=name + "_count",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )
        self._value_gauge = PrometheusGauge(
            name=name + "_value",
            documentation=description or "",
            labelnames=labels or [],
            namespace=namespace,
            registry=registry,
        )

    def _update_values(self, value: Number):

        value = float(value)

        self._count += 1
        self._sum += value
        self._abssum += abs(value)
        self._mean = self._sum / self._count
        self._absmean = self._abssum / self._count

        if self._min is None:
            self._min = value
        else:
            self._min = min(self._min, value)

        if self._max is None:
            self._max = value
        else:
            self._max = max(self._max, value)

    @staticmethod
    def _update_metric(metric, value, labels):
        if value is None:
            return

        if labels:
            metric = metric.labels(*labels)
        metric.set(value)

    def update(self, value: Number, labels: Optional[List] = None):
        self._update_values(value)

        self._update_metric(self._min_gauge, self._min, labels)
        self._update_metric(self._max_gauge, self._max, labels)
        self._update_metric(self._mean_gauge, self._mean, labels)
        self._update_metric(self._absmean_gauge, self._absmean, labels)
        self._update_metric(self._sum_gauge, self._sum, labels)
        self._update_metric(self._abssum_gauge, self._abssum, labels)
        self._update_metric(self._count_gauge, self._count, labels)
        self._update_metric(self._value_gauge, value, labels)


class MetricPrometheusClient(MetricClient):
    def __init__(self, pushgateway_url: str, job_name: Optional[str] = None):
        self._pushgateway_url = pushgateway_url
        self._registry = CollectorRegistry()

        self._job = job_name or prefect.context["flow_name"]
        self._run = getenv("PREFECT__CONTEXT__FLOW_RUN_ID", "UNKNOWN_RUN")

    def create_counter(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Counter:
        return MetricPrometheusCounter(
            registry=self._registry,
            namespace=namespace,
            name=name,
            labels=labels,
            description=description,
        )

    def create_gauge(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Gauge:
        return MetricPrometheusGauge(
            registry=self._registry,
            namespace=namespace,
            name=name,
            labels=labels,
            description=description,
        )

    def create_distribution(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Distribution:
        return MetricPrometheusDistribution(
            registry=self._registry,
            namespace=namespace,
            name=name,
            labels=labels,
            description=description,
        )

    def push(self):
        LOG.debug("Pushing metrics to " + self._pushgateway_url)
        push_to_gateway(self._pushgateway_url, job=self._job, registry=self._registry)
