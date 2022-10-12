from pathlib import Path
from typing import Dict
import requests

from tradebot.configs import TradebotConfigs


class TradebotRequests:
    '''
    Performs the essential CRUD requests, using the access token defined in the config file\n
    to perform Bearer authorization.
    '''
    def __init__(self, configs:TradebotConfigs):
        self.__configs = configs

        self.__headers = {
            "Accept": "*/*",
            "Authorization": None, #be sure to update Authorization each time the 'headers' are referenced
            "Content-Type": "application/x-www-form-urlencoded",
        }


    def get(self, url:str, data:Dict=None, params:Dict=None, auth:bool=True):

        if auth:
            self.__headers.update({"Authorization": "Bearer " + self.__configs["access_token"]})

        return requests.get(url, data=data, params=params, headers=self.__headers)


    def post(self, url:str, data:Dict=None, params:Dict=None, auth:bool=True):

        if auth:
            self.__headers.update({"Authorization": "Bearer " + self.__configs["access_token"]})
            
        return requests.post(url, data=data, params=params, headers=self.__headers)