from thefirstock.firstockModules.modifyOrderFunctionality.execution import *


def firstock_ModifyOrder(quantity, norenordno, triggerPrice, price, exchange, tradingSymbol, priceType):
    try:

        modifyOrder = FirstockModifyOrder(
            qty=quantity,
            norenordno=norenordno,
            trgprc=triggerPrice,
            prc=price,
            exchange=exchange,
            tradingSymbol=tradingSymbol,
            priceType=priceType
        ).firstockModifyOrder()

        return modifyOrder

    except Exception as e:
        print(e)
