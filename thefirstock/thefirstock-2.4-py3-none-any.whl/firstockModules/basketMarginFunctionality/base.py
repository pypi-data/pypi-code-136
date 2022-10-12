from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockBasketMargin(self, listData):
        """
        :return:
        """
        pass
