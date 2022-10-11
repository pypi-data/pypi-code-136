import datetime
import json

from stock_market.core.ticker import Ticker

from .sentiment import Sentiment


class Signal:
    def __init__(self, identifier, name, sentiment, date, tickers=None):
        self.__id = identifier
        self.__name = name
        self.__sentiment = sentiment
        self.__date = date
        self.__tickers = [] if tickers is None else tickers

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def sentiment(self):
        return self.__sentiment

    @property
    def date(self):
        return self.__date

    @property
    def tickers(self):
        return self.__tickers

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (
            f"Signal(id={self.id}, name={self.name}, sentiment={self.sentiment},"
            f" date={self.date}), tickers={self.tickers}"
        )

    def __eq__(self, other):
        if not isinstance(other, Signal):
            return False

        assert (self.id == other.id) == (self.name == other.name)
        return (self.id, self.date, self.sentiment, self.tickers) == (
            other.id,
            other.date,
            other.sentiment,
            other.tickers,
        )

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "sentiment": json.dumps(self.sentiment.value),
                "date": json.dumps(self.date, default=datetime.date.isoformat),
                "tickers": json.dumps([t.to_json() for t in self.tickers]),
            }
        )

    @staticmethod
    def from_json(json_str):
        json_obj = json.loads(json_str)
        return Signal(
            json_obj["id"],
            json_obj["name"],
            Sentiment(json.loads(json_obj["sentiment"])),
            datetime.date.fromisoformat(json.loads(json_obj["date"])),
            [Ticker.from_json(t) for t in json.loads(json_obj["tickers"])],
        )

    @staticmethod
    def json_schema():
        return {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "sentiment": {"type": "string"},
                "date": {"type": "string", "format": "date"},
                "tickers": {"type": "list"},
            },
        }
