"""

"""

from abc import ABCMeta, abstractmethod
from pyspark.sql import DataFrame


class Validator(metaclass=ABCMeta):
    """
    Callable validator then ts is valid, before analyze
    """

    @abstractmethod
    def validate(self, ts: DataFrame, time_col_name: str):
        pass
