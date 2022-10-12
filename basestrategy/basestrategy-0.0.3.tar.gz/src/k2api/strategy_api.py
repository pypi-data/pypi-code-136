import requests
import json
from config import settings
import datamodel as dm

class K2StrategyApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]
    @staticmethod
    def api_wrapper_strategy_by_id_get(strategy_id:str):
        try:
            url = f"{K2StrategyApi.INTERNAL_API_BASE_URL}/strategy_by_id/{strategy_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                strategy = dm.PydanticStrategy(**(response))
                return strategy
            return False
        except Exception as error:
            print(error)