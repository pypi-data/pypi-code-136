import multipart
import importlib
import orjson as json
from typing import AsyncGenerator
from panther.status import status_text, is_client_error, is_server_error, is_success


async def _http_response_start(send, /, status_code: int):
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': [
            [b'content-type', b'application/json'],
        ],
    })


async def _http_response_body(send, /, body: any = None):
    if body is None:
        await send({'type': 'http.response.body'})
    else:
        await send({'type': 'http.response.body', 'body': body})


async def builtin_http_response(send, /, *, status_code: int):
    body = json.dumps({'detail': status_text[status_code]})
    await http_response(send, status_code=status_code, body=body)


async def http_response(send, /, *, status_code: int, body: bytes = None):
    if status_code == 204:
        body = None
    elif body == b'null':
        body = None
        if is_success(status_code):
            status_code = 204
    await _http_response_start(send, status_code=status_code)
    await _http_response_body(send, body=body)


async def read_body(receive) -> bytes:
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True
    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)
    return body


async def stream_body(receive) -> AsyncGenerator[bytes, None]:
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True
    while more_body:
        message = await receive()
        yield message.get('body', b'')
        more_body = message.get('more_body', False)


def import_class(_klass: str, /):
    """
    Example:
        Input: panther.db.models.User
        Output: User (The Class)
    """
    seperator = _klass.rfind('.')
    module = importlib.import_module(_klass[:seperator])
    return getattr(module, _klass[seperator + 1:])


def generate_body():
    body = b'----------------------------357352357603906367105786\r\nContent-Disposition: form-data; name="name"\r\n\r\nali\r\n----------------------------357352357603906367105786\r\nContent-Disposition: form-data; name="age"\r\n\r\n25\r\n----------------------------357352357603906367105786--\r\n'
    return body


def simple_app(input_stream):
    ret = []

    def on_field(field):
        ret.append("Parsed field named: %s" % (field.field_name,))

    def on_file(file):
        ret.append("Parsed file named: %s" % (file.field_name,))

    headers = {
        'Content-Type': 'multipart/form-data; boundary=--------------------------776011414554065674436168',
        'Content-Length': '-1',
    }
    multipart.parse_form(headers, input_stream, on_field, on_file)
    ret.append('\n')
    return ret

