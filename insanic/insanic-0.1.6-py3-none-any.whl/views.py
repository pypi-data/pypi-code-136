from typing import Any

from sanic.views import HTTPMethodView

from insanic.http import HTTP_STATUS, Response, response_json
from insanic.serializers import Serializer

__all__ = (
    'View',
)


class View(HTTPMethodView):
    serializer_class: type[Serializer] | None = None

    def ok_response(self, data: Any, http_status: int = HTTP_STATUS.OK) -> Response:  # pylint: disable=no-self-use
        response_data = { 'status': 'ok', 'data': data }
        return response_json(response_data, status=http_status)

    def error_response(self, errors: dict, http_status : int = HTTP_STATUS.BAD_REQUEST) -> Response:  # pylint: disable=no-self-use
        response_data = { 'status': 'error', 'errors': errors }
        return response_json(response_data, status=http_status)

    async def serialized_response(self, data: Any, serializer_class: type[Serializer] | None = None, http_status: int = HTTP_STATUS.OK) -> Response :  # pylint: disable=line-too-long
        serializer_class = serializer_class or self.serializer_class
        if not serializer_class:
            raise NotImplementedError('Serializer class must be specified')

        serializer_kwargs = { 'many': isinstance(data, list) }
        serializer = serializer_class(**serializer_kwargs)
        serialized_data = await serializer.serialize(data)

        return self.ok_response(serialized_data, http_status=http_status)
