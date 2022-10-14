import uuid

import requests.utils


class HTTPRequesterCore:
    def __init__(self,
                 endpoint: str = None):
        self.rpc_endpoint = endpoint

    @staticmethod
    def _get_request_id() -> str:
        return str(uuid.uuid4())

    def _build_request(self,
                       method: str,
                       params):
        request_id = self._get_request_id()
        headers = requests.utils.default_headers()
        headers.update({"Content-Type": "application/json",
                        "User-Agent": "DeenAiR python SDK"})
        json_data = {"jsonrpc": "2.0", "id": request_id, "method": method, "param": params}
        return {"url": self.rpc_endpoint, "json": json_data, "headers": headers}

    @staticmethod
    def _get_response(response):
        return response

