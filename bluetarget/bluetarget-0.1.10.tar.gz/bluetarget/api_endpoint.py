
from typing import Dict

import requests
import json

ENDPOINT = "https://api.deploy.bluetarget.ai"


class APIEndpoint:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get(self, path: str, query: Dict = None):
        response = requests.get(f'{ENDPOINT}/{path}',
                                params=query, headers=self.__headers())

        return response.json(), response.status_code

    def post(self, path: str, body: Dict = None):

        if body != None:
            body = json.dumps(body)

        response = requests.post(f'{ENDPOINT}/{path}',
                                 data=body, headers=self.__headers())

        return response.json(), response.status_code

    def __headers(self):
        return {
            "Authorization": f"api-key {self.api_key}",
            "Content-Type": "application/json"
        }
