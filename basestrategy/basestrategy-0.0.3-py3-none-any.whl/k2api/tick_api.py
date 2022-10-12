import requests
import json
from config import settings
import datamodel as dm
from myutils import *
from static.enums import BarSize, Exchange


class K2TickApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_latest_tick_get(exchange: Exchange, ex_symbol: str) -> list:
        try:
            url = f"{K2TickApi.INTERNAL_API_BASE_URL}/tick/{exchange}/{ex_symbol}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                json_response = json.loads(response.text)
                return dm.PydanticTicks(**json_response)
            else:
                return False
        except Exception as error:
            print(error)
