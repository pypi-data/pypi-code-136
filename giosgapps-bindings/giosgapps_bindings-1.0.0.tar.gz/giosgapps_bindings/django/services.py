from django.core.exceptions import ObjectDoesNotExist
import os
import requests
import logging

logger = logging.getLogger(__name__)


class GiosgHttpApi:
    CHAT_HOST = os.environ.get('SERVICE_GIOSG_COM', 'https://service.giosg.com')

    def __init__(self, org_id, installation_model, api_key=None, token_type="Token"):
        valid_token_types = ["Token", "Bearer"]
        if token_type not in valid_token_types:
            raise ValueError("Invalid token type '{}', valid values are {}".format(
                token_type, valid_token_types
            ))

        if api_key:
            self.auth_headers = {"Authorization": "{} {}".format(token_type, api_key)}
        else:
            try:
                conf = installation_model.objects.get(installed_org_uuid=org_id)
            except ObjectDoesNotExist:
                raise ValueError("Cannot instantiate Giosg API without persistent token. "
                                 "Either app has not been installed for this org, "
                                 "or the token was not saved on app install.")
            self.auth_headers = {
                "Authorization": "{} {}".format(conf.persistent_token_prefix, conf.persistent_bot_token)
            }

    def get(self, endpoint, params={}, headers={}):
        request_headers = self._get_headers(headers)
        response = requests.get(f"{self.CHAT_HOST}{endpoint}", params=params, headers=request_headers)
        response.raise_for_status()
        return response

    def post(self, endpoint, json, headers={}):
        request_headers = self._get_headers(headers, add_content_type=True)
        response = requests.post(f"{self.CHAT_HOST}{endpoint}", json=json, headers=request_headers)
        response.raise_for_status()
        return response

    def patch(self, endpoint, json, headers={}):
        request_headers = self._get_headers(headers, add_content_type=True)
        response = requests.patch(f"{self.CHAT_HOST}{endpoint}", json=json, headers=request_headers)
        response.raise_for_status()
        return response

    def put(self, endpoint, json, headers={}):
        request_headers = self._get_headers(headers, add_content_type=True)
        response = requests.put(f"{self.CHAT_HOST}{endpoint}", json=json, headers=request_headers)
        response.raise_for_status()
        return response

    def delete(self, endpoint, params={}, headers={}):
        request_headers = self._get_headers(headers)
        response = requests.delete(f"{self.CHAT_HOST}{endpoint}", params=params, headers=request_headers)
        response.raise_for_status()
        return response

    def _get_headers(self, extra_headers={}, add_content_type=False):
        json_headers = {"content-type": "application/json"} if add_content_type else {}
        return dict(self.auth_headers, **json_headers, **extra_headers)
