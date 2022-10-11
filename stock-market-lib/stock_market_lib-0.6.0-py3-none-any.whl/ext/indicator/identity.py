from stock_market.common.json_mixins import EmptyJsonMixin
from stock_market.core import TimeSeries


class Identity(EmptyJsonMixin):
    def __call__(self, series: TimeSeries):
        return series

    def __eq__(self, other):
        return isinstance(other, Identity)

    def __str__(self):
        return "Identity"

    def lag_days(self):
        return 0
