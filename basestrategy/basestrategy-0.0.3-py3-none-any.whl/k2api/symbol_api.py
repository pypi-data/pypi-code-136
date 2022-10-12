import requests
import json
from config import settings
import datamodel as dm
from static import *


class K2SymbolApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_symbol_get(source: str, exchange, ex_symbol: str) -> dict:
        __author__ = "Hit Sutariya"

        try:
            url = f"{K2SymbolApi.INTERNAL_API_BASE_URL}/symbol/{source}/{exchange}/{ex_symbol}"
            headers = {"Content-Type": "application/json;"}
            response = requests.get(url, headers=headers)
            json_response = json.loads(response.text)
            if (response.status_code == 200):
                symbol_data = dm.PydanticSymbol(**json_response)
                return symbol_data
            else:
                return False
        except Exception as error:
            raise NotImplementedError("symbol get is not accessable")

    @staticmethod
    def api_wrapper_symbol_by_id_get(id) -> dict:
        __author__ = "Hit Sutariya"

        try:
            url = f'{K2SymbolApi.INTERNAL_API_BASE_URL}/symbol_by_id/{id}'
            headers = {"Content-Type": "application/json;"}
            response = requests.get(url, headers=headers)
            json_response = json.loads(response.text)
            if (response.status_code == 200):
                symbol_data = dm.PydanticSymbol(**json_response)
                return symbol_data
            else:
                return False
        except Exception as error:
            print(error)

    @staticmethod
    def api_wrapper_symbol_post(data: dict) -> dict:
        __author__ = "Hit Sutariya"

        try:
            headers = {"Content-Type": "application/json;"}
            data = json.dumps(data)
            response = requests.post(
                f'{K2SymbolApi.INTERNAL_API_BASE_URL}/symbol', headers=headers, data=data)
            if(response.status_code == 200):
                json_response = json.loads(response.text)
                symbol = dm.PydanticSymbol(**json_response)
                return symbol
            elif(response.status_code == 409):
                return True
            else:
                return False
        except Exception as error:
            raise NotImplementedError("symbol post api is not accessable")
