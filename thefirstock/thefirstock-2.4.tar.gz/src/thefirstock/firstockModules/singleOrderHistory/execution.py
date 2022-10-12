from thefirstock.firstockModules.singleOrderHistory.functions import *


class FirstockSingleOrderHistory:
    def __init__(self, norenordno):
        self.singleOrderHistory = ApiRequests()

        self.norenordno = norenordno

    def firstockSingleOrderHistory(self):
        result = self.singleOrderHistory.firstockSingleOrderHistory(self.norenordno)
        return result
