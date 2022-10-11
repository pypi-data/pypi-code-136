from abc import ABC, abstractmethod

from typing import Optional, List
from numbers import Number


__all__ = ["Counter", "Gauge", "Distribution"]


class AbstractMetric(ABC):
    def __init__(
        self,
        namespace: str,
        name: str,
        labels: Optional[List] = None,
        description: Optional[str] = None,
    ):
        self.namespace = namespace
        self.name = name
        self.labels = labels or []
        self.description = description


class Counter(AbstractMetric):
    @abstractmethod
    def inc(self, n: Number = 1, labels: Optional[List] = None):
        pass

    @abstractmethod
    def dec(self, n: Number = 1, labels: Optional[List] = None):
        pass


class Gauge(AbstractMetric):
    @abstractmethod
    def set(self, value: Number, labels: Optional[List] = None):
        pass


class Distribution(AbstractMetric):
    @abstractmethod
    def update(self, value: Number, labels: Optional[List] = None):
        pass
