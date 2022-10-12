import requests
import json
from config import settings
import datamodel as dm


class K2ClientApi:
    INTERNAL_API_BASE_URL = settings["INTERNAL_API_BASE_URL"]
    @staticmethod
    def api_wrapper_client_by_id_get(client_id:str):
        try:
            url = f"{K2ClientApi.INTERNAL_API_BASE_URL}/client_by_id/{client_id}"
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                response = json.loads(response.text)
                strategy = dm.PydanticClient(**(response))
                return strategy
            return False
        except Exception as error:
            print(error)