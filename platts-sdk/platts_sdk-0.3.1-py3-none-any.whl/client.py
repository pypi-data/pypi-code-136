from functools import lru_cache
import requests
import logging


class Client:
    def __init__(self, username, password, apikey):
        self.un = username
        self.pw = password
        self.apikey = apikey

    @property
    @lru_cache()
    def token(self):
        body = {"username": self.un, "password": self.pw}
        headers = {"appkey": self.apikey}

        try:
            r = requests.post(
                "https://api.platts.com/auth/api", data=body, headers=headers
            )
            r.raise_for_status()
            return r.json()["access_token"]
        except Exception as err:
            if r.status_code >= 500:
                logging.error(f"[{r.status_code}] - {err}")
            else:
                logging.error(f"[{r.status_code}] -  {r.json()}")
            raise

    def get_current_assessments_by_mdc(self, mdc):
        # must be quotes around mdc
        params = {"filter": f'mdc: "{mdc}"', "pagesize": 10000}

        headers = {"Authorization": f"Bearer {self.token}", "appkey": self.apikey}

        try:
            r = requests.get(
                "https://api.platts.com/market-data/v3/value/current/mdc",
                params=params,
                headers=headers,
            )
            r.raise_for_status()
            return r.json()
        except Exception as err:
            if r.status_code >= 500:
                print(err)
            else:
                print(r.status_code, r.json())
            raise

    def get_current_assessments(self, symbols):
        # quotes are required around each symbol
        symbols = ['"' + x + '"' for x in symbols]

        params = {"filter": f"symbol in ({','.join(symbols)})"}
        headers = {"Authorization": f"Bearer {self.token}", "appkey": self.apikey}

        try:
            r = requests.get(
                "https://api.platts.com/market-data/v3/value/current/symbol",
                params=params,
                headers=headers,
            )
            r.raise_for_status()
            return r.json()
        except Exception as err:
            if r.status_code >= 500:
                print(err)
            else:
                print(r.status_code, r.json())
            raise
