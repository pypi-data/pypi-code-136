from thefirstock.firstockModules.singleOrderHistory.execution import *


def firstock_SingleOrderHistory(norenordno):
    try:
        singleOrderHistory = FirstockSingleOrderHistory(
            norenordno=norenordno
        ).firstockSingleOrderHistory()

        return singleOrderHistory

    except Exception as e:
        print(e)
