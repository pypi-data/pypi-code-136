from pathlib import Path
from typing import Dict
import requests

from tradebot.configs import TradebotConfigs


__headers = {
    "Accept": "*/*",
    "Authorization": None, #be sure to update Authorization each time the 'headers' are referenced
    "Content-Type": "application/x-www-form-urlencoded",
}

__this_dir = Path(__file__).parent
__config_file = Path(__this_dir, "configs/configs.json")
__configs = TradebotConfigs(__config_file)


def auth_get_request(url:str, data:Dict=None, params:Dict=None):
    global __headers, __configs

    __headers.update({"Authorization": "Bearer " + __configs["access_token"]})
    return requests.get(url, data=data, params=params, headers=__headers)


def auth_post_request(url:str, data:Dict=None, params:Dict=None):
    global __headers, __configs

    __headers.update({"Authorization": "Bearer " + __configs["access_token"]})
    return requests.post(url, data=data, params=params)