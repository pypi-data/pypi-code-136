import pandas as pd

from stock_market.common.json_mixins import SingleAttributeJsonMixin
from stock_market.core.time_series import TimeSeries


class ExponentialMovingAverage(SingleAttributeJsonMixin):
    JSON_ATTRIBUTE_NAME = "period"
    JSON_ATTRIBUTE_TYPE = "integer"

    def __init__(self, period):
        self.period = period

    def __call__(self, series: TimeSeries):
        return TimeSeries(
            f"{self} {series.name}",
            pd.concat(
                [series.dates, series.values.ewm(span=self.period).mean()],
                axis=1,
                ignore_index=True,
            ),
        )

    def __eq__(self, other):
        if not isinstance(other, ExponentialMovingAverage):
            return False
        return self.period == other.period

    def __str__(self):
        return f"EMA({self.period})"

    def lag_days(self):
        return self.period
