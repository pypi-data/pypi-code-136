import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.firstockModules.spanCalculatorFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockSpanCalculator(self, exch, instname, symname, expd, optt, strprc, netqty, buyqty, sellqty, product):
        """
        :return:
        """
        url = SPANCALCULATOR

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "actid": uid,
            "exchange": exch,
            "instname": instname,
            "symbolName": symname,
            "expd": expd,
            "optt": optt,
            "strikePrice": strprc,
            "netQuantity": netqty,
            "buyQuantity": buyqty,
            "sellQuantity": sellqty,
            "product": product,
            "jKey": jKey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
