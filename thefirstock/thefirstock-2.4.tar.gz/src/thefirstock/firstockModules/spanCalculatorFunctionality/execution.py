from thefirstock.firstockModules.spanCalculatorFunctionality.functions import *


class FirstockSpanCalculator:
    def __init__(self, exch, instname, symname, expd, optt, strprc, netqty, buyqty, sellqty, product):
        self.spanCalculator = ApiRequests()

        self.exch = exch
        self.instname = instname
        self.symname = symname
        self.expd = expd
        self.optt = optt
        self.strprc = strprc
        self.netqty = netqty
        self.buyqty = buyqty
        self.sellqty = sellqty
        self.product = product

    def firstockSpanCalculator(self):
        result = self.spanCalculator.firstockSpanCalculator(self.exch, self.instname, self.symname, self.expd,
                                                            self.optt, self.strprc, self.netqty, self.buyqty,
                                                            self.sellqty, self.product)
        return result