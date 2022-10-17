#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT


from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import requests


TIMEOUT = 60


def get_session(retries):
    session = requests.Session()

    retry_strategy = Retry(
        total=retries,
        status_forcelist=[408, 413, 429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "DELETE", "PUT", "TRACE"],
        backoff_factor=1,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def requests_get(*args, **kwargs):
    session = get_session(retries=10)
    return session.get(*args, timeout=TIMEOUT, **kwargs)


def requests_post(*args, **kwargs):
    session = get_session(retries=0)
    return session.post(*args, timeout=TIMEOUT, **kwargs)
