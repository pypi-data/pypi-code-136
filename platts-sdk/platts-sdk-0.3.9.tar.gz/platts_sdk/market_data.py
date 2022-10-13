from typing import Any
import typing
import pandas as pd

from platts_sdk.tok import TokenClient


class MarketData:
    def __init__(self, token_client: TokenClient, as_df=True):
        self.token_client = token_client
        self.as_df = as_df
        return

    def get_current_assessments_by_mdc(
        self, mdc: str
    ) -> typing.Union[pd.DataFrame, Any]:
        # get the current assessments for all symbols in a MDC (market data category)
        params = {"filter": f'mdc: "{mdc}"', "pagesize": 10000}

        data = self.token_client.get(
            path="/market-data/v3/value/current/mdc",
            params=params,
        )
        if self.as_df:
            return pd.json_normalize(
                data["results"], record_path=["data"], meta="symbol"
            )

        return data

    def get_current_assessments(
        self, symbols: list[str]
    ) -> typing.Union[pd.DataFrame, Any]:
        # get the current assessments for a list of symbols
        symbols = ['"' + x + '"' for x in symbols]
        params = {"filter": f"symbol in ({','.join(symbols)})"}

        data = self.token_client.get(
            "/market-data/v3/value/current/symbol",
            params=params,
        )
        if self.as_df:
            return pd.json_normalize(
                data["results"], record_path=["data"], meta="symbol"
            )

        return data
