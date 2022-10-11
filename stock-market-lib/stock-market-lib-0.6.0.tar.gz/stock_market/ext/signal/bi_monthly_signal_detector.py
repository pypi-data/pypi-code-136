import datetime as dt

from dateutil.relativedelta import relativedelta

from stock_market.common.json_mixins import SingleAttributeJsonMixin
from stock_market.core import Sentiment, Signal, SignalDetector, add_signal


class BiMonthlySignalDetector(SignalDetector, SingleAttributeJsonMixin):
    JSON_ATTRIBUTE_NAME = "id"
    JSON_ATTRIBUTE_TYPE = "integer"

    def __init__(self, identifier):
        super().__init__(identifier, BiMonthlySignalDetector.NAME())

    def month_range(self, from_date, to_date):
        while from_date <= to_date:
            yield from_date
            from_date += relativedelta(months=1)

    def detect(self, from_date, to_date, stock_market, sequence):
        start = from_date
        if from_date.day != 1:
            start = from_date - dt.timedelta(from_date.day - 1)

        def create_signal(date):
            return Signal(self.id, self.name, Sentiment.NEUTRAL, date)

        for date in self.month_range(start, to_date + relativedelta(months=1)):
            if date >= from_date and date <= to_date:
                sequence = add_signal(sequence, create_signal(date))
            half_month = date + dt.timedelta(days=14)
            if half_month >= from_date and half_month <= to_date:
                sequence = add_signal(
                    sequence, create_signal(date + dt.timedelta(days=14))
                )

        return sequence

    def __eq__(self, other):
        return isinstance(other, BiMonthlySignalDetector)

    @staticmethod
    def NAME():
        return "Bi-monthly"
