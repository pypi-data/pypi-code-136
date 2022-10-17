import asyncio
from enum import Enum, auto

from yarl import URL


class Status(Enum):
    OK = auto()
    BAD_QUERY_STRING = auto()  # missing HTTP get parameter in final url
    REDIRECT = auto()  # response code 3xx
    TEXT_FOUND = auto()
    BAD_STATUS = auto()  # response code not 200
    TIMEOUT = auto()


class BaseStatusAssigner:
    def __init__(self, page_text=None):
        self.page_text = page_text

    @staticmethod
    def preprocess_url(url):
        return url

    async def parse_response(self, response):
        return Status.OK

    @staticmethod
    def handle_exceptions(e):
        raise e


class StatusAssigner(BaseStatusAssigner):

    def __init__(self, page_text=None):
        self.page_text = page_text

    @staticmethod
    def preprocess_url(url):
        return URL(url).update_query(test_query=1)

    @staticmethod
    def _search_query_in_url(url):
        return 'test_query' in url.query

    async def parse_response(self, response):
        if response.status != 200:
            return Status.BAD_STATUS
        if not self._search_query_in_url(response.url):
            return Status.BAD_QUERY_STRING
        if self.page_text and self.page_text in await response.text():
            return Status.TEXT_FOUND
        if response.history:
            return Status.REDIRECT
        return Status.OK

    @staticmethod
    def handle_exceptions(e):
        if isinstance(e, asyncio.exceptions.TimeoutError):
            return Status.TIMEOUT
        else:
            raise e
