import json

import pandas as pd
import toolz

from .time_series import TimeSeries, merge_time_series


def create_ohlc(dates, *args):
    if len(dates) == 0:
        return None
    return OHLC(dates, *args)


class OHLC:
    """
    Open-high-low-close time series data.
    """

    def __init__(self, dates, open, high, low, close):
        dates = pd.to_datetime(dates).dt.date
        self.__open = TimeSeries(
            "Open", pd.concat([dates, open], axis=1, ignore_index=True)
        )
        self.__high = TimeSeries(
            "High", pd.concat([dates, high], axis=1, ignore_index=True)
        )
        self.__low = TimeSeries(
            "Low", pd.concat([dates, low], axis=1, ignore_index=True)
        )
        self.__close = TimeSeries(
            "Close", pd.concat([dates, close], axis=1, ignore_index=True)
        )

    @staticmethod
    def from_series(dates, open, high, low, close):
        return create_ohlc(dates, open.values, high.values, low.values, close.values)

    @property
    def start(self):
        return self.dates.iloc[0]

    @property
    def end(self):
        return self.dates.iloc[-1]

    @property
    def dates(self):
        return self.open.dates

    @property
    def open(self):
        return self.__open

    @property
    def high(self):
        return self.__high

    @property
    def low(self):
        return self.__low

    @property
    def close(self):
        return self.__close

    def keep_recent_days(self, days):
        assert days < (self.end - self.start).days + 1
        new_open = self.open.keep_recent_days(days)
        if new_open is None:
            return None
        return OHLC.from_series(
            new_open.dates,
            new_open,
            self.high.keep_recent_days(days),
            self.low.keep_recent_days(days),
            self.close.keep_recent_days(days),
        )

    def trim(self, start_date, end_date):
        """Trims the OHCL to only contain values at or after the given start date
        and before the given end date. The end date is not included."""
        new_open = self.open.trim(start_date, end_date)
        if new_open is None:
            return None
        return OHLC.from_series(
            new_open.dates,
            new_open,
            self.high.trim(start_date, end_date),
            self.low.trim(start_date, end_date),
            self.close.trim(start_date, end_date),
        )

    def __eq__(self, other):
        if not isinstance(other, OHLC):
            return False
        if not self.dates.equals(other.dates):
            return False
        return [self.open, self.high, self.low, self.close] == [
            other.open,
            other.high,
            other.low,
            other.close,
        ]

    def __repr__(self):
        return (
            f"OHLC({self.end}, {self.open.values.iloc[-1]:.2f},"
            f" {self.high.values.iloc[-1]:.2f}, {self.low.values.iloc[-1]:.2f},"
            f" {self.close.values.iloc[-1]:.2f})"
        )

    def to_json(self):
        return json.dumps(
            {
                "dates": self.dates.to_json(),
                "open": self.open.to_json(),
                "high": self.high.to_json(),
                "low": self.low.to_json(),
                "close": self.close.to_json(),
            }
        )

    @staticmethod
    def from_json(json_str):
        json_obj = json.loads(json_str)
        dates = pd.read_json(json_obj.pop("dates"), typ="series")
        return OHLC.from_series(dates, **toolz.valmap(TimeSeries.from_json, json_obj))


def merge_ohlcs(first, second):
    if first is None:
        return second
    if second is None:
        return first
    dates = pd.concat([first.dates, second.dates], ignore_index=True)
    dates.drop_duplicates(keep="last", inplace=True)
    return OHLC.from_series(
        dates,
        merge_time_series(first.open, second.open),
        merge_time_series(first.high, second.high),
        merge_time_series(first.low, second.low),
        merge_time_series(first.close, second.close),
    )
