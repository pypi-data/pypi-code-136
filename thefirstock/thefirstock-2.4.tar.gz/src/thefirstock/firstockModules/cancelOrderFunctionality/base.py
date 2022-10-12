from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockCancelOrder(self, norenordno):
        """
        :return:
        """
        pass
