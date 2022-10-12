from thefirstock.firstockModules.getQuotesFunctionality.execution import *


def firstock_getQuotes(exchange, token):
    try:
        getQuotes = FirstockGetQuotes(
            exch=exchange,
            token=token
        ).firstockGetQuotes()

        return getQuotes

    except Exception as e:
        print(e)
