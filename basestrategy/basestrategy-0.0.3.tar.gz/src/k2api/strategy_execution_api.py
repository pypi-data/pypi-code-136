import json
import requests
from config import settings
import datamodel as dm


class K2StrategyExecutionApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]

    @staticmethod
    def api_wrapper_strategy_execution_get(strategy_execution_id):
        try:
            url = f"{K2StrategyExecutionApi.INTERNAL_API_BASE_URL}/strategy_execution/{strategy_execution_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                strategy = dm.PydanticStrategyExecution(**(response))
                return strategy
            return False
        except Exception as error:
            print(error)

    @staticmethod
    def api_wrapper_strategy_execution_post(client_id, strategy_id, strategy_execution_stage):
        try:
            url = f"{K2StrategyExecutionApi.INTERNAL_API_BASE_URL}/strategy_execution"
            headers = {"Content-Type": "application/json"}
            data = {"client_id": client_id, "strategy_id": strategy_id,
                    "stage": strategy_execution_stage}
            data = json.dumps(data)
            response = requests.post(url, data, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                strategy = dm.PydanticStrategyExecution(**(response))
                return strategy
            return False
        except Exception as error:
            print(error)

    @staticmethod
    def api_wrapper_strategy_execution_put(use):
        try:
            url = f"{K2StrategyExecutionApi.INTERNAL_API_BASE_URL}/strategy_execution"
            headers = {"Content-Type": "application/json"}
            data = json.dumps(use, default=str)
            response = requests.put(url, data, headers=headers)
            if (response.status_code == 200):
                return response
            else:
                return False
        except Exception as error:
            print('error', error)
