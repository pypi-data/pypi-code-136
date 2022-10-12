from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSpanCalculator(self, exch, instname, symname, expd, optt, strprc, netqty, buyqty, sellqty, product):
        """
        :return:
        """
        pass
