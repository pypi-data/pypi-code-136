from thefirstock.firstockModules.limitFunctionality.functions import *


class FirstockLimits:
    def __init__(self):
        self.limits = ApiRequests()

    def firstockLimits(self):
        result = self.limits.firstockLimits()
        return result
