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

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def login(self):
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

    def get_heating(self):
        url = f"{api_protocol}://{api_hostname}/api/consumer/v/1/users/{self.username}/home/capabilities/heating"

        response = requests.get(
            url=url, headers={"Authorization": f"Bearer {self.token['access_token']}"}
        )
        return response.json()
