"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Oct-2022

memberpress REST API Client plugin for Django - rest api client implementation
"""
# Python stuff
import logging
import inspect
import json
import urllib3
from urllib.parse import urljoin
import requests

# Django stuff
from django.conf import settings
from django.core.cache import cache

# our stuff
from memberpress_client.utils import log_pretrip, log_postrip
from memberpress_client.decorators import request_manager

# disable the following warnings:
# -------------------------------
# /usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:1043:
# InsecureRequestWarning: Unverified HTTPS request is being made to host 'staging.global-communications-academy.com'.
# Adding certificate verification is strongly advised. See: https://urllib3.readtheocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class MemberpressAPIClient:
    _locked = False
    _json = None

    def init(self):
        self._locked = False
        self._json = None

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    @property
    def locked(self):
        return self._locked

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        if type(value) == dict or value is None:
            self.init()
            self._json = value
        else:
            logger.warning("was expecting a value of type dict but receive type {t}".format(t=type(value)))

    @property
    def ready(self):
        return True if not self.locked and self.json and len(self.json) > 0 else False

    def is_valid(self, value) -> bool:
        if type(value) != dict:
            return False
        return True

    def get_url(self, path) -> str:
        return urljoin(settings.MEMBERPRESS_API_BASE_URL, path)

    @property
    def headers(self) -> dict:
        return {
            f"{settings.MEMBERPRESS_API_KEY_NAME}": f"{settings.MEMBERPRESS_API_KEY}",
        }

    @request_manager
    def post(self, path, data=None, host=None, operation="") -> json:
        url = self.get_url(path, host=host)
        log_pretrip(caller=inspect.currentframe().f_code.co_name, url=url, data=data, operation=operation)
        response = requests.post(url, data=data, headers=self.headers)
        log_postrip(caller=inspect.currentframe().f_code.co_name, path=url, response=response, operation=operation)
        response.raise_for_status()
        return response.json()

    @request_manager
    def patch(self, path, data=None, host=None, headers=None, json=True, operation=""):
        url = self.get_url(path, host=host)
        if not headers:
            headers = self.headers

        log_pretrip(caller=inspect.currentframe().f_code.co_name, url=url, data=data, operation=operation)
        response = requests.patch(url, json=data, headers=headers)
        log_postrip(caller=inspect.currentframe().f_code.co_name, path=url, response=response, operation=operation)
        response.raise_for_status()
        if json:
            return response.json()
        return response

    @request_manager
    def get(self, path, params=None, operation="") -> json:
        url = self.get_url(path)
        cache_key = f"MemberpressAPIClient.get:{url}"
        response = cache.get(cache_key)

        if not response and not self.locked:
            # set a lock to prevent multiple calls
            self.lock()

            # purge whatever might have previously existing in the cache, in case our
            # response object raises an exception here ...
            cache.delete(cache_key)

            log_pretrip(caller=inspect.currentframe().f_code.co_name, url=url, data={}, operation=operation)
            response = requests.get(url, params=params, headers=self.headers, verify=False)
            log_postrip(caller=inspect.currentframe().f_code.co_name, path=url, response=response, operation=operation)

            # @request_manager will create verbose log entries for any responses outside of 200-299.
            response.raise_for_status()

            if type(response) not in [dict, list]:
                try:
                    response = response.json()
                except Exception:
                    response = json.dumps(response)

            # caching results iff response is a valid json object.
            cache.set(cache_key, response, settings.MEMBERPRESS_CACHE_EXPIRATION)
            self.unlock()
        return response

    def is_valid_dict(self, response, qc_keys) -> bool:
        if not type(response) == dict:
            logger.warning(
                "is_valid_dict() was expecting a dict but received an object of type: {type}".format(
                    type=type(response)
                )
            )
            return False
        return all(key in response for key in qc_keys)
