from abc import ABC, abstractmethod
from collections import namedtuple
from typing import List

OHLCRequest = namedtuple("OHLCRequest", ["start_date", "end_date", "ticker"])
OHLCResult = namedtuple("OHLCResult", ["ticker", "ohlc"])


class OHLCFetcher(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    async def fetch_ohlc(self, requests: List[OHLCRequest]):
        pass
