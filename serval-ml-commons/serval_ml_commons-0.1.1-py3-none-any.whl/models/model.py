import abc
from abc import ABC


class Model(ABC):
    def __init__(self, name, **kwargs):
        self.name = name

    @abc.abstractmethod
    def predict(self, x):
        pass

    @abc.abstractmethod
    def fit(self, x, y):
        pass

    @abc.abstractmethod
    def load(self, path):
        pass

    @abc.abstractmethod
    def save(self, path):
        pass
