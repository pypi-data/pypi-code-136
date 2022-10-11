import datetime
import json

from .ohlc import OHLC
from .ticker import Ticker

"""
A stock market representation starting on a given date with the given tickers.
Optionally ticker OHLCs can be given to instantiate the stock market.
"""


class StockMarket:
    def __init__(self, start_date, tickers, ticker_OHLCs={}):
        self.__start_date = start_date
        self.__tickers = sorted(tickers)
        self.__ticker_OHLCs = ticker_OHLCs

    @property
    def start_date(self):
        return self.__start_date

    @property
    def tickers(self):
        return self.__tickers

    def ohlc(self, ticker):
        return self.__ticker_OHLCs.get(ticker)

    def add_ticker(self, ticker):
        assert ticker not in self.tickers
        return StockMarket(
            self.start_date, self.tickers + [ticker], self.__ticker_OHLCs
        )

    def remove_ticker(self, ticker):
        if ticker not in self.tickers:
            return self
        return StockMarket(
            self.start_date,
            [t for t in self.tickers if t != ticker],
            {k: v for k, v in self.__ticker_OHLCs.items() if k != ticker},
        )

    def update_ticker(self, ticker_OHLC):
        assert ticker_OHLC.ticker in self.tickers
        if ticker_OHLC.ohlc.end < self.start_date:
            return self

        ohlc = ticker_OHLC.ohlc
        if ohlc.start < self.start_date:
            ohlc = ohlc.keep_recent_days((ohlc.end - self.start_date).days + 1)
        assert ohlc.start >= self.start_date
        new_ticker_OHLCs = self.__ticker_OHLCs.copy()
        new_ticker_OHLCs[ticker_OHLC.ticker] = ohlc
        return StockMarket(self.start_date, self.tickers, new_ticker_OHLCs)

    @property
    def date(self):
        if not self.__ticker_OHLCs:
            return self.start_date
        max_date = max(map(lambda ohlc: ohlc.end, self.__ticker_OHLCs.values()))
        assert max_date >= self.start_date
        return max_date

    def __repr__(self):
        return f"StockMarket({self.date}, {self.tickers})"

    def __eq__(self, other):
        if not isinstance(other, StockMarket):
            return False
        if self.start_date != other.start_date:
            return False
        if len(self.tickers) != len(other.tickers):
            return False  # fail quickly
        if sorted(self.tickers) != sorted(other.tickers):
            return False
        if self.date != other.date:
            return False  # fail quickly
        if len(self.__ticker_OHLCs) != len(other.__ticker_OHLCs):
            return False  # fail quickly
        for ticker in self.tickers:
            if self.ohlc(ticker) != other.ohlc(ticker):
                return False
        return True

    def to_json(self):
        return json.dumps(
            {
                "start_date": json.dumps(
                    self.start_date, default=datetime.date.isoformat
                ),
                "tickers": json.dumps([ticker.to_json() for ticker in self.tickers]),
                "ticker_ohlcs": json.dumps(
                    [
                        (t.to_json(), ohlc.to_json())
                        for (t, ohlc) in self.__ticker_OHLCs.items()
                    ]
                ),
            }
        )

    @staticmethod
    def from_json(json_str):
        json_obj = json.loads(json_str)
        sm = StockMarket(
            datetime.date.fromisoformat(json.loads(json_obj["start_date"])),
            [Ticker.from_json(ticker) for ticker in json.loads(json_obj["tickers"])],
        )
        sm.__ticker_OHLCs = {
            Ticker.from_json(t): OHLC.from_json(o)
            for t, o in json.loads(json_obj["ticker_ohlcs"])
        }
        return sm
