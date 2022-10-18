from kognic.base_clients.cloud_storage import FileResourceClient
from kognic.base_clients.http_client import HttpClient


class IOResource:

    def __init__(self, client: HttpClient, file_client: FileResourceClient):
        super().__init__()
        self._client = client
        self._file_client = file_client
