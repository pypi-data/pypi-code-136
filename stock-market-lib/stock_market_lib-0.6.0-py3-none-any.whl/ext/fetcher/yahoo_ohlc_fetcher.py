import json
import traceback

import requests
import yahoo_fin.stock_info as yf
from simputils.logging import get_logger

from stock_market.common.json_mixins import EmptyJsonMixin
from stock_market.core import OHLC, OHLCFetcher

logger = get_logger(__name__)


class YahooOHLCFetcher(OHLCFetcher, EmptyJsonMixin):
    def __init__(self):
        super().__init__("yahoo")

    def fetch_single(self, start, end, ticker):
        ticker_hist = None
        try:
            ticker_hist = yf.get_data(
                ticker.symbol,
                start_date=start,
                end_date=end,
                interval="1d",
                index_as_date=False,
            )
            ticker_hist = ticker_hist.reset_index()
        except json.decoder.JSONDecodeError:
            logger.warning("Yahoo Finance rate limit encountered!")
            return None
        except AssertionError as e:  # Be flexible in start and end ranges
            logger.warning(
                f"Error during Yahoo Finance data request: {ticker}, {start}, {end}."
            )
            logger.debug(
                f"Assertion error encountered during Yahoo Finance request: {e},\n"
                f" {traceback.format_exc()}"
            )
            return None
        # Occurs when no data could be retrieved for the interval
        # (e.g. only weekend interval, bug in yahoo_fin)
        except KeyError:
            return None
        except requests.exceptions.ConnectionError:
            logger.warning("Connection occurred when contacting Yahoo Finance!")
            return None

        if len(ticker_hist.date) == 0:
            return None
        return OHLC(
            ticker_hist.date,
            ticker_hist.open,
            ticker_hist.high,
            ticker_hist.low,
            ticker_hist.adjclose,
        )

    async def fetch_ohlc(self, requests):
        return [
            (ticker, self.fetch_single(start_date, end_date, ticker))
            for start_date, end_date, ticker in requests
        ]

    def __eq__(self, other):
        return isinstance(other, YahooOHLCFetcher)
