
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from trove_fm.app.models.person import AppRole
from trove_fm.app.models.profile import PersonProfilePublic


class UserAgent:
    """docstring for UserAgent"""

    client_lookup = {
        "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1":
        "Android",
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.51 Safari/537.36"
        ):
        "Chrome",
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
        ):
        "Edge",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0":
        "Firefox",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko":
        "IE",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148":
        "iOS WebView",
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
        ):
        "Opera",
        (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/15.4 Safari/605.1.15"
        ):
        "Safari",
        "Paw/3.3.6 (Macintosh; OS X/10.15.7) GCDHTTPRequest":
        "Paw",
        "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)":
        "curl",
        "python-requests/2.26.0":
        "python requests"
    }

    user_agent_lookup = {
        "Andorid":
        "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Chrome":
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.51 Safari/537.36"
        ),
        "Edge":
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
        ),
        "Firefox":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
        "IE":
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "iOS WebView":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Opera":
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
        ),
        "Safari":
        (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/15.4 Safari/605.1.15"
        ),
        "Paw":
        "Paw/3.3.6 (Macintosh; OS X/10.15.7) GCDHTTPRequest",
        "curl":
        "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)",
        "python requests":
        "python-requests/2.26.0"
    }

    cookie_clients = ["Andorid", "Chrome", "Edge", "Firefox", "IE", "iOS WebView", "Opera", "Safari"]

    @classmethod
    def get_client(cls, ua_string):
        return cls.client_lookup[ua_string]

    @classmethod
    def get_user_agent(cls, client):
        return cls.user_agent_lookup[client]

    @classmethod
    def from_ua_string(cls, ua_string: str):
        client = cls.get_client(ua_string)
        return cls(client)

    def __init__(self, client: str):
        self.client = client
        self.user_agent = self.get_user_agent(client)
        self.stores_cookies = self.client in self.cookie_clients


class UsualSuspect(object):
    """docstring for UsualSuspect"""

    def __init__(
        self,
        id: Optional[int],
        name_prefix: Optional[str] = None,
        name_first: Optional[str] = None,
        name_last: Optional[str] = None,
        name_suffix: Optional[str] = None,
        email_label: Optional[str] = None,
        username: Optional[EmailStr] = None,
        app_role: Optional[AppRole] = None,
        active: bool = False,
        email_login: bool = None,
        verified: bool = False,
        created_at: datetime = datetime.utcnow(),
        updated_at: datetime = datetime.utcnow(),
        password: str = None,
        salt: str = None,
        profile: Optional[PersonProfilePublic] = None
    ):
        self.id = id
        self.active = active
        self.app_role = app_role
        self.created_at = created_at
        self.updated_at = updated_at
        self.name_prefix = name_prefix
        self.name_first = name_first
        self.name_last = name_last
        self.name_suffix = name_suffix
        self.email_label = email_label
        self.username = username
        self.password = None
        self.email_login = None
        self.verified = False
        self.profile = profile

    def dict(self):
        return self.__dict__
