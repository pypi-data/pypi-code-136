from typing import Any, Optional

import httpx
from typing_extensions import Self


class HttpClientMixin:
    async def __aenter__(self) -> Self:
        try:
            await self._http_client.__aenter__()
        except RuntimeError:
            raise RuntimeError(f"Cannot open {self.__class__.__name__} instance more than once")
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    @property
    def _http_client(self) -> httpx.AsyncClient:
        http_client: Optional[httpx.AsyncClient] = getattr(self, "_inner_http_client", None)
        if http_client is None:
            http_client = httpx.AsyncClient()
            setattr(self, "_inner_http_client", http_client)
        elif http_client.is_closed:
            raise RuntimeError(f"Cannot reopen {self.__class__.__name__} instance once it has been closed")
        return http_client

    async def close(self) -> None:
        await self._http_client.aclose()
