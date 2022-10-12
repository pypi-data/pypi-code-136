from thefirstock.firstockModules.cancelOrderFunctionality.functions import *


class FirstockCancelOrder:
    def __init__(self, norenordno):
        self.cancelOrder = ApiRequests()

        self.norenordno = norenordno

    def firstockCancelOrder(self):
        result = self.cancelOrder.firstockCancelOrder(self.norenordno)
        return result

