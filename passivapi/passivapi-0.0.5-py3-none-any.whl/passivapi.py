# SPDX-FileCopyrightText: 2022-present Gareth John <gdjohn@logicalparadox.co.uk>
#
# SPDX-License-Identifier: MIT

import requests
from requests.auth import HTTPBasicAuth

api_protocol = "https"
api_hostname = "www.passivliving.com"


class PassivApi:
    username = None
    password = None
    token = None
    home = None
    home_capabilities_heating = None

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self, username=None, password=None):
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

        url = f"{api_protocol}://{api_hostname}/oauth/token"
        auth = HTTPBasicAuth("trusted", "secret")
        response = requests.post(
            url=url,
            auth=auth,
            json={
                "username": self.username,
                "password": self.password,
                "grant_type": "password",
            },
        )
        self.token = response.json()

    def get_home(self):
        url = f"{api_protocol}://{api_hostname}/api/consumer/v/1/users/{self.username}/home"

        response = requests.get(
            url=url, headers={"Authorization": f"Bearer {self.token['access_token']}"}
        )
        response.raise_for_status()

        self.home = response.json()
        return self.home

    def get_zones(self):
        if self.home is None:
            self.get_home()
        return self.home["zones"]

    def get_heating(self):
        url = f"{api_protocol}://{api_hostname}/api/consumer/v/1/users/{self.username}/home/capabilities/heating"

        response = requests.get(
            url=url, headers={"Authorization": f"Bearer {self.token['access_token']}"}
        )
        response.raise_for_status()

        self.home_capabilities_heating = response.json()

        return self.home_capabilities_heating

    def set_setpoint(self, zone=None, units=None, value=None):
        url = f"{api_protocol}://{api_hostname}/api/consumer/v/1/users/{self.username}/home/capabilities/heating/zones/{zone}/properties/setpoint/status"

        response = requests.put(
            url=url,
            headers={"Authorization": f"Bearer {self.token['access_token']}"},
            json={
                "units": units,
                "value": value,
            },
        )
        response.raise_for_status()

    def get_setpoint(self, zone=None):
        url = f"{api_protocol}://{api_hostname}/api/consumer/v/1/users/{self.username}/home/capabilities/heating/zones/{zone}/properties/setpoint"

        response = requests.get(
            url=url, headers={"Authorization": f"Bearer {self.token['access_token']}"}
        )
        response.raise_for_status()

        return response.json()
