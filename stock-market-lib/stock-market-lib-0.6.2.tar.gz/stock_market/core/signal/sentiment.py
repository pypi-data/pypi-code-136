from enum import Enum

from stock_market.common.json_mixins import SingleAttributeJsonMixin


class Sentiment(SingleAttributeJsonMixin, Enum):
    @classmethod
    @property
    def JSON_ATTRIBUTE_NAME(cls):
        return "value"

    @classmethod
    @property
    def JSON_ATTRIBUTE_TYPE(cls):
        return "string"

    NEUTRAL = "NEUTRAL"
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
