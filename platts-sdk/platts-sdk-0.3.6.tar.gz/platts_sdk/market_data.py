import requests
import pandas as pd


class MarketData:
    def __init__(self, token_client, as_df=True):
        self.token_client = token_client
        self.as_df = as_df
        return

    def get_current_assessments_by_mdc(self, mdc):
        # must be quotes around mdc
        params = {"filter": f'mdc: "{mdc}"', "pagesize": 10000}

        headers = {
            "Authorization": f"Bearer {self.token_client.token}",
            "appkey": self.token_client.apikey,
        }

        try:
            r = requests.get(
                "https://api.platts.com/market-data/v3/value/current/mdc",
                params=params,
                headers=headers,
            )
            r.raise_for_status()
            if self.as_df:
                data = r.json()
                df = pd.json_normalize(
                    data["results"], record_path=["data"], meta="symbol"
                )
                return df

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
        headers = {
            "Authorization": f"Bearer {self.token_client.token}",
            "appkey": self.token_client.apikey,
        }

        try:
            r = requests.get(
                "https://api.platts.com/market-data/v3/value/current/symbol",
                params=params,
                headers=headers,
            )
            r.raise_for_status()
            if self.as_df:
                data = r.json()
                df = pd.json_normalize(
                    data["results"], record_path=["data"], meta="symbol"
                )
                return df

            return r.json()
        except Exception as err:
            if r.status_code >= 500:
                print(err)
            else:
                print(r.status_code, r.json())
            raise
