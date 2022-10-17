from typing import Any, Dict, Literal, Optional, overload

import httpx

from ._http_client_mixin import HttpClientMixin
from .credentials import AsyncTokenCredential

__all__ = ("IdpClient",)


class IdpClient(HttpClientMixin):
    """HTTP Client for IDP with authentication"""

    def __init__(self, token_credential: AsyncTokenCredential, idp_url: str) -> None:
        self._idp_url = idp_url.rstrip("/")
        self._token_credential = token_credential

    async def _assemble_headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = dict(extra) if extra else {}
        token = await self._token_credential.get_token()
        headers.update({"Authorization": f"Bearer {token}"})
        return headers

    def _build_url(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> httpx.URL:
        return httpx.URL(
            f"{self._idp_url}{path}",
            params=[(k, v) for k, v in sorted((params or {}).items())],
        )

    async def request(
        self,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        headers = await self._assemble_headers(headers)
        resp = await self._http_client.request(
            method,
            self._build_url(path, params=params),
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )
        resp.raise_for_status()
        return resp

    async def get(self, path: str = "", *, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
        return await self.request("GET", path, params=params)

    @overload
    async def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    @overload
    async def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    async def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        return await self.request(
            "POST",
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )

    @overload
    async def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    @overload
    async def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    async def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        return await self.request(
            "PUT",
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )

    async def delete(self, path: str = "") -> httpx.Response:
        return await self.request("DELETE", path)
