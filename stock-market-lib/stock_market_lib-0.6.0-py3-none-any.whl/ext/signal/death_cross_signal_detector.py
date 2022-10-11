import json

from stock_market.core import Sentiment, Ticker
from stock_market.ext.indicator import MovingAverage
from stock_market.ext.signal import CrossoverSignalDetector


class DeathCrossSignalDetector(CrossoverSignalDetector):
    def __init__(self, identifier, ticker):
        super().__init__(
            identifier,
            f"{DeathCrossSignalDetector.NAME()}({ticker.symbol})",
            ticker,
            MovingAverage(50),
            MovingAverage(200),
            Sentiment.BEARISH,
        )

    @staticmethod
    def NAME():
        return "Death cross"

    def to_json(self):
        return json.dumps({"id": self.id, "ticker": self.ticker.to_json()})

    @staticmethod
    def from_json(json_str):
        json_obj = json.loads(json_str)
        return DeathCrossSignalDetector(
            json_obj["id"], Ticker.from_json(json_obj["ticker"])
        )

    @staticmethod
    def json_schema():
        return {
            "type": "object",
            "properties": {"id": {"type": "integer"}, "ticker": {"type": "string"}},
        }
