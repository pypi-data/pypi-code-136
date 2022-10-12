import requests
import json
from config import settings
import datamodel as dm
from static import *


class K2SymbolDataSubscriptionApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_symbol_data_subscription_post(data: dict) -> dict:
        __author__ = "Hit Sutariya"

        try:
            headers = {"Content-Type": "application/json;"}
            data = json.dumps(data)
            response = requests.post(
                f'{K2SymbolDataSubscriptionApi.INTERNAL_API_BASE_URL}/symbol_data_subscription', headers=headers, data=data)
            if (response.status_code == 200):
                json_response = json.loads(response.text)
                symbol_data_subscription = dm.PydanticSymbolDataSubscription(
                    **json_response)
                return symbol_data_subscription
            elif(response.status_code == 409):
                return True
            else:
                return False
        except Exception as error:
            raise NotImplementedError(
                "symbol_data_subscription post api is not accessable")

    @staticmethod
    def api_wrapper_symbol_data_subscription_by_ex_symbol_and_direction_in_get(ex_symbol: str, direction: str) -> dict:
        __author__ = "Hit Sutariya"

        try:
            headers = {"Content-Type": "application/json;"}
            response = requests.get(
                f'{K2SymbolDataSubscriptionApi.INTERNAL_API_BASE_URL}/symbol_data_subscription_by_ex_symbol_and_direction_in/{ex_symbol}/{direction}', headers=headers)

            if (response.status_code == 200):
                json_response = json.loads(response.text)
                symbol_data_subscription = dm.PydanticSymbolDataSubscription(
                    **json_response)

                return symbol_data_subscription
            else:
                return False
        except Exception as error:
            raise NotImplementedError(
                "symbol_data_subscription_by_ex_symbol_and_direction_in get api is not accessable")
