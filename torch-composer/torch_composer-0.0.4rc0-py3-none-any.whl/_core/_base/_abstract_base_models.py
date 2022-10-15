
__module_name__ = "_base.py"
__doc__ = """Module for declaring all abstract base class objects."""
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu"])


# -- import packages: --------------------------------------------------------------------
from abc import ABC, abstractmethod
from collections import OrderedDict
import torch


# -- Layer: ------------------------------------------------------------------------------
class BaseLayer(ABC):
    @abstractmethod
    def __name__(self):
        pass

    @abstractmethod
    def __add_activation__(self):
        pass

    @abstractmethod
    def __add_layer__(self):
        pass

    @abstractmethod
    def __add_dropout__(self):
        pass


# -- TorchDict: --------------------------------------------------------------------------
class BaseTorchDict(ABC):
    @abstractmethod
    def __register__(self):
        pass

    @abstractmethod
    def __compose__(self):
        pass

    def __call__(self):
        return OrderedDict(self.__compose__())


# -- NeuralNet: --------------------------------------------------------------------------
class BaseNeuralNet(ABC):
    @abstractmethod
    def __define__(self, **kwargs):
        pass

    def __call__(self) -> torch.nn.Sequential:
        return torch.nn.Sequential(self.__define__())