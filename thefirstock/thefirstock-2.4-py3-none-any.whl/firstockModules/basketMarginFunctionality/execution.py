from thefirstock.firstockModules.basketMarginFunctionality.functions import *


class FirstockBasketMargin:
    def __init__(self, listData):
        self.BasketMargin = ApiRequests()
        self.listData = listData

    def firstockBasketMargin(self):
        result = self.BasketMargin.firstockBasketMargin(self.listData)
        return result
