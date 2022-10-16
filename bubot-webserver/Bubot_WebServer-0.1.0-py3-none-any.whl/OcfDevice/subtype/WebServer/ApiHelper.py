from bson import json_util as json
from aiohttp import web


class DeviceApi:
    def __init__(self, response, **kwargs):
        self.response = response
        self.db = kwargs.get('db')
        self.filter_fields = {}
        self.list_limit = 1000


class WebResponse:

    @staticmethod
    def json_response(data, *, status: int = 200, headers=None, content_type: str = 'application/json',
                      dumps=json.dumps) -> web.Response:
        text = dumps(data, ensure_ascii=False)
        return web.Response(text=text, status=status, headers=headers, content_type=content_type)

    @staticmethod
    def text_response(text='', *, status: int = 200, headers=None) -> web.Response:
        return web.Response(text=text, status=status, headers=headers)


class WsResponse:
    @staticmethod
    def json_response(data):
        return data
