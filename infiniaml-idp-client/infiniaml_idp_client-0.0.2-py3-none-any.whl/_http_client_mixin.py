from typing import Any, Optional

import httpx
from typing_extensions import Self


class HttpClientMixin:
    def __enter__(self) -> Self:
        try:
            self._http_client.__enter__()
        except RuntimeError:
            raise RuntimeError(f"Cannot open {self.__class__.__name__} instance more than once")
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    @property
    def _http_client(self) -> httpx.Client:
        http_client: Optional[httpx.Client] = getattr(self, "_inner_http_client", None)
        if http_client is None:
            http_client = httpx.Client()
            setattr(self, "_inner_http_client", http_client)
        elif http_client.is_closed:
            raise RuntimeError(f"Cannot reopen {self.__class__.__name__} instance once it has been closed")
        return http_client

    def close(self) -> None:
        self._http_client.close()
