import requests
import json
from config import settings
import datamodel as dm
from myutils import *
from static.enums import BarSize, Exchange


class K2BarsApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]
    @staticmethod
    def api_wrapper_last_nbars_get(exchange: Exchange, symbol: str, barsize: BarSize, nbars: int) -> list:
        try:
            url = f"{K2BarsApi.INTERNAL_API_BASE_URL}/bars/{exchange}/{symbol}/{barsize}/nbars={nbars}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)["data"]
                return response
            else:
                return False
        except Exception as error:
            print(error)