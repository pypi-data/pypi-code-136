import json
import logging

import boto3
import requests

from blam_sdk.sdk_config import SdkConfig

CLIENT_ID = "3m3jp0ri9vpfs8oh3jlngijb7k"


class BlamBaseService:
    def __init__(self, api_path, config: SdkConfig = None):
        if config is None:
            config = SdkConfig.from_file()
        self.config = config
        self._headers = {"Authorization": None}
        self.base_url = f"{self.config.base_url}/{api_path}"
        self.refresh_auth()

    def _check_res(self, res, msg):
        if res.status_code > 299:
            res_body = res.json()
            logging.error(msg)
            logging.error(res_body)
            raise Exception(res_body)

    def _get_url(self, path=""):
        return f"{self.base_url}/{path}"

    def _get(self, path=""):
        res = requests.get(self._get_url(path), headers=self._headers)
        self._check_res(res, f"Get failed")
        return res.json()

    def _put(self, path="", body={}):
        res = requests.put(
            self._get_url(path), data=json.dumps(body), headers=self._headers
        )
        self._check_res(res, f"Put failed")
        return res.json()

    def _post(self, path="", body={}):
        res = requests.post(
            self._get_url(path), data=json.dumps(body), headers=self._headers
        )
        self._check_res(res, f"Post failed")
        return res.json()

    def _delete(self, path=""):
        res = requests.delete(self._get_url(path), headers=self._headers)
        self._check_res(res, f"Delete failed")
        return res.json()

    def refresh_auth(self):
        cidp = boto3.client("cognito-idp", "us-east-1")
        try:
            self.auth_info = cidp.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": self.config.username,
                    "PASSWORD": self.config.password,
                },
                ClientId=CLIENT_ID,
            )["AuthenticationResult"]
            self._headers["Authorization"] = self.auth_info["IdToken"]
        except Exception as e:
            logging.error(e)
            raise Exception("Failed to get auth tokens")
