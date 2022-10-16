import socket
from ..requesters.core import HTTPRequesterCore
from .base import BaseProvider
import json
from io import BytesIO
from http.client import HTTPResponse


class FakeSocket:
    def __init__(self, response_bytes):
        self._file = BytesIO(response_bytes)

    def makefile(self, *args, **kwargs):
        return self._file


class HTTPRequester(BaseProvider, HTTPRequesterCore):
    """HTTP requester to optimise interact with the rpc endpoint."""

    # @handle_exceptions(SolanaRpcException, requests.exceptions.RequestException)
    def make_request(self, method: str, params):
        request_kwargs = self._build_request(method=method, params=params)

        host, port = request_kwargs["url"].split(":")
        body = json.dumps(request_kwargs["json"], separators=[",", ":"]).encode()
        headers = f"""POST\r\nContent-Length: {len(body)}\r\n\r\n""".encode()
        payload = headers + body


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.sendall(payload)
        # time.sleep(5)
        sample = s.recv(4096)
        source = FakeSocket(sample)
        response = HTTPResponse(source)

        response.begin()
        content_length = response.getheader("Content-Length")

        total_body = b""
        body_start = sample.split(b"\r\n\r\n")[-1]
        total_body += body_start
        while len(total_body) < int(content_length):
            data = s.recv(4096)
            total_body += data
        s.close()

        response = json.loads(total_body.decode())
        return self._get_response(response=response)
