from thefirstock.firstockModules.cancelOrderFunctionality.execution import *


def firstock_cancelOrder(norenordno):
    try:
        cancelOrder = FirstockCancelOrder(
            norenordno=norenordno
        ).firstockCancelOrder()

        return cancelOrder

    except Exception as e:
        print(e)
