#      A python library for getting Load Shedding schedules.
#      Copyright (C) 2021  Werner Pieterson
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from typing import Any, Dict, List

import certifi
import urllib3


class SePushError(Exception):
    pass


ESKOM = "eskom"
CITY_OF_CAPE_TOWN = "capetown"


class SePush:
    base_url = "https://us-central1-sepush-app.cloudfunctions.net/sepush-serverless-business-api-staging-http/business/2.0"
    # base_url = "https://developer.sepush.co.za/business/2.0"
    token = ""

    def __init__(self, token=None):
        if token:
            self.token = token

    def areas_search(self, text: str) -> List[Dict]:
        url = f"{self.base_url}/areas_search?text={text}"
        data = _call(url, self.token)
        return json.loads(data)

    def area(self, area_id: str) -> List[Dict]:
        url = f"{self.base_url}/area?id={area_id}"
        data = _call(url, self.token)
        return json.loads(data)

    def check_allowance(self) -> Dict:
        url = f"{self.base_url}/api_allowance"
        data = _call(url, self.token)
        return json.loads(data)

    def status(self) -> int:
        url = f"{self.base_url}/status"
        data = _call(url, self.token)
        return json.loads(data)


def _call(url: str, token: str) -> Any:
    try:
        with urllib3.PoolManager(retries=urllib3.Retry(total=3), ca_certs=certifi.where()) as conn:
            headers = {"Token": token}
            print("\nurl: ", url)
            r = conn.request('GET', url, headers=headers)
            if r.status != 200:
                raise urllib3.response.HTTPError(r.status)
            print("\ndata: ", r.data)
            return r.data
    except Exception as e:
        raise SePushError(f"SePush is unreachable. Check your connection.") from e
