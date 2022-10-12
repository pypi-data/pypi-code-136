from functools import lru_cache
import requests
import logging


class TokenClient:
    def __init__(self, username, password, apikey):
        self.token_endpoint = "https://api.platts.com/auth/api"
        self.endpoint = "https://api.plats.com"
        self.un = username
        self.pw = password
        self.apikey = apikey
        return

    @property
    @lru_cache()
    def token(self):
        body = {"username": self.un, "password": self.pw}
        headers = {"appkey": self.apikey}

        try:
            r = requests.post(self.token_endpoint, data=body, headers=headers)
            r.raise_for_status()
            return r.json()["access_token"]
        except Exception as err:
            if r.status_code >= 500:
                logging.error(f"[{r.status_code}] - {err}")
            else:
                logging.error(f"[{r.status_code}] -  {r.json()}")
            raise
