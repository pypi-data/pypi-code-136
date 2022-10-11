from abc import ABC, abstractmethod
from os import getenv
import importlib
import logging

from .metric_client import MetricClient
from .abstract_metric import Gauge, Counter, Distribution

from typing import List, Optional

__all__ = ["Metrics"]

LOG = logging.getLogger(__name__)

DEFAULT_METRIC_CLIENT_CLS = "odp.compute.metrics.client.MetricMockClient"


class Metrics:

    METRICS_CLIENT: MetricClient = None

    @staticmethod
    def _load_metric_client() -> MetricClient:
        try:
            metric_client_packagename = getenv(
                "ODP__METRIC_CLIENT_CLS", DEFAULT_METRIC_CLIENT_CLS
            )
            client_args = [
                x.strip() for x in getenv("ODP__METRIC_CLIENT_ARGS", "").split(",")
            ]
            client_args = [x for x in client_args if x]

            parts = metric_client_packagename.split(".")

            if parts[-1][0].islower():
                client_packagename, client_clsname = ".".join(parts[:-2]), parts[-2]
                client_funcname = parts[-1]
            else:
                client_packagename, client_clsname = ".".join(parts[:-1]), parts[-1]
                client_funcname = None

            client_module = importlib.import_module(client_packagename)
            client_cls = getattr(client_module, client_clsname)

            if client_funcname:
                return getattr(client_cls, client_funcname)(*client_args)
            else:
                return client_cls(*client_args)
        except KeyError as e:
            LOG.exception(f"Failed to load metrics class `{client_cls}'")
            from odp.compute.metrics.client.metric_mock_client import MetricMockClient

            return MetricMockClient()

    @staticmethod
    def _get_metric_client() -> MetricClient:
        if Metrics.METRICS_CLIENT is None:
            Metrics.METRICS_CLIENT = Metrics._load_metric_client()
            LOG.info(
                "Using metrics client: {}".format(Metrics.METRICS_CLIENT.__class__)
            )
        return Metrics.METRICS_CLIENT

    @staticmethod
    def counter(
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Counter:
        client = Metrics._get_metric_client()
        return client.create_counter(namespace, name, labels, description)

    @staticmethod
    def gauge(
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Gauge:
        client = Metrics._get_metric_client()
        return client.create_gauge(namespace, name, labels, description)

    @staticmethod
    def distribution(
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Distribution:
        client = Metrics._get_metric_client()
        return client.create_distribution(namespace, name, labels, description)

    @staticmethod
    def push(raise_on_error=True):
        client = Metrics._get_metric_client()

        try:
            client.push()
        except Exception as e:
            if raise_on_error:
                raise e
            else:
                LOG.warning(
                    f"An exception occurred when attempting to push metrics: {e}",
                    exc_info=True,
                )
