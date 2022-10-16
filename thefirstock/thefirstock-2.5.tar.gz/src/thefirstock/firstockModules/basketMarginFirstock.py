from thefirstock.firstockModules.basketMarginFunctionality.execution import *


def firstock_BasketMargin(data, exchange, tradingSymbol, quantity, transactionType, price, product, priceType):
    try:
        placeOrder = FirstockBasketMargin(
            listData=data,
            exchange=exchange,
            tradingSymbol=tradingSymbol,
            quantity=quantity,
            transactionType=transactionType,
            price=price,
            product=product,
            priceType=priceType
        )

        result = placeOrder.firstockBasketMargin()
        return result

    except Exception as e:
        print(e)
