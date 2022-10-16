from thefirstock.firstockModules.basketMarginFunctionality.functions import *


class FirstockBasketMargin:
    def __init__(self, listData, exchange, tradingSymbol, quantity, transactionType, price, product,
                 priceType):
        self.BasketMargin = ApiRequests()
        self.listData = listData
        self.exchange = exchange
        self.tradingSymbol = tradingSymbol
        self.quantity = quantity
        self.transactionType = transactionType
        self.price = price
        self.product = product
        self.priceType = priceType

    def firstockBasketMargin(self):
        result = self.BasketMargin.firstockBasketMargin(self.listData, self.exchange, self.tradingSymbol, self.quantity,
                                                        self.transactionType, self.price, self.product,
                                                        self.priceType)
        return result
