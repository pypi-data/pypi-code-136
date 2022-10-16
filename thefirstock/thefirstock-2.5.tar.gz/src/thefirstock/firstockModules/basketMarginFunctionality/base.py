from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockBasketMargin(self, listData, exchange, tradingSymbol, quantity, transactionType, price, product,
                             priceType):
        """
        :return:
        """
        pass
