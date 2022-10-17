from typing import Any, Dict, Literal, Optional, overload

import httpx

from ._http_client_mixin import HttpClientMixin
from .credentials import TokenCredential

__all__ = ("IdpClient",)


class IdpClient(HttpClientMixin):
    """HTTP Client for IDP with authentication"""

    def __init__(self, token_credential: TokenCredential, idp_url: str) -> None:
        self._idp_url = idp_url.rstrip("/")
        self._token_credential = token_credential

    def _assemble_headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = dict(extra) if extra else {}
        token = self._token_credential.get_token()
        headers.update({"Authorization": f"Bearer {token}"})
        return headers

    def _build_url(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> httpx.URL:
        return httpx.URL(
            f"{self._idp_url}{path}",
            params=[(k, v) for k, v in sorted((params or {}).items())],
        )

    def request(
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
        headers = self._assemble_headers(headers)
        resp = self._http_client.request(
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

    def get(self, path: str = "", *, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
        return self.request("GET", path, params=params)

    @overload
    def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    @overload
    def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    def post(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        return self.request(
            "POST",
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )

    @overload
    def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    @overload
    def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        ...

    def put(
        self,
        path: str = "",
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        return self.request(
            "PUT",
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )

    def delete(self, path: str = "") -> httpx.Response:
        return self.request("DELETE", path)
