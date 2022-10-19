from abc import ABC, abstractmethod, abstractproperty


class BasePlugin(ABC):

  @abstractproperty
  def protocol(self) -> str:
    pass

  @abstractmethod
  def get_value(self, key: str):
    pass