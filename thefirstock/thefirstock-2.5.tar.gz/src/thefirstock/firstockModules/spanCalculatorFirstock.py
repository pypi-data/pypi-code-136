from thefirstock.firstockModules.spanCalculatorFunctionality.execution import *


def firstock_SpanCalculator(dataList):
    try:
        spanCalculator = FirstockSpanCalculator(
            dataList=dataList,
        ).firstockSpanCalculator()

        return spanCalculator

    except Exception as e:
        print(e)
