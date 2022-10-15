from abc import ABCMeta, abstractmethod


class BaseConfig(metaclass=ABCMeta):
    @abstractmethod
    def get_config(self):
        pass
