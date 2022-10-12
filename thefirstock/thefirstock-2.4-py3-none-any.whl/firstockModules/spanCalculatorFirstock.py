from thefirstock.firstockModules.spanCalculatorFunctionality.execution import *


def firstock_SpanCalculator(exchange, instname, symbolName, expd, optt, strikePrice, netQuantity, buyQuantity,
                            sellQuantity, product):
    try:

        spanCalculator = FirstockSpanCalculator(
            exch=exchange,
            instname=instname,
            symname=symbolName,
            expd=expd,
            optt=optt,
            strprc=strikePrice,
            netqty=netQuantity,
            buyqty=buyQuantity,
            sellqty=sellQuantity,
            product=product
        ).firstockSpanCalculator()

        return spanCalculator

    except Exception as e:
        print(e)
