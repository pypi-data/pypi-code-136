from abc import ABC, abstractmethod
from .abstract_metric import Counter, Gauge, Distribution
from typing import Optional, List

__all__ = ["MetricClient"]


class MetricClient(ABC):
    @abstractmethod
    def create_counter(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Counter:
        pass

    @abstractmethod
    def create_gauge(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Gauge:
        pass

    @abstractmethod
    def create_distribution(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ) -> Distribution:
        pass

    @abstractmethod
    def push(self):
        pass
