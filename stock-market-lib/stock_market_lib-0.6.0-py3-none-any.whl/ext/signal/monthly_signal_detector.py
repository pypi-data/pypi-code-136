import datetime as dt

from dateutil.relativedelta import relativedelta

from stock_market.common.json_mixins import SingleAttributeJsonMixin
from stock_market.core import Sentiment, Signal, SignalDetector, add_signal


class MonthlySignalDetector(SignalDetector, SingleAttributeJsonMixin):
    JSON_ATTRIBUTE_NAME = "id"
    JSON_ATTRIBUTE_TYPE = "integer"

    def __init__(self, identifier):
        super().__init__(identifier, MonthlySignalDetector.NAME())

    def month_range(self, from_date, to_date):
        while from_date <= to_date:
            yield from_date
            from_date += relativedelta(months=1)

    def detect(self, from_date, to_date, stock_market, sequence):
        if from_date.day != 1:
            from_date = (
                from_date - dt.timedelta(from_date.day - 1) + relativedelta(months=1)
            )
        for date in self.month_range(from_date, to_date):
            sequence = add_signal(
                sequence, Signal(self.id, self.name, Sentiment.NEUTRAL, date)
            )
        return sequence

    def __eq__(self, other):
        return isinstance(other, MonthlySignalDetector)

    @staticmethod
    def NAME():
        return "Monthly"
