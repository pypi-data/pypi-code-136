from thefirstock.firstockModules.basketMarginFunctionality.execution import *


def firstock_BasketMargin(data):
    try:
        placeOrder = FirstockBasketMargin(
            listData=data,
        )

        result = placeOrder.firstockBasketMargin()
        return result

    except Exception as e:
        print(e)
