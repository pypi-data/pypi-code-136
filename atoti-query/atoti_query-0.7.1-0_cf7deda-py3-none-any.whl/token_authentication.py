from dataclasses import dataclass
from functools import cached_property

from atoti_core import keyword_only_dataclass

from ._http import HttpHeaders
from .auth import Auth


@keyword_only_dataclass
@dataclass(frozen=True, eq=False)
class TokenAuthentication(Auth):
    """Also called "Bearer authentication", this :class:`atoti_query.Auth`, passes the given token to the HTTP :guilabel:`Authorization` header of the request being made."""

    token: str
    token_type: str = "Bearer"

    def __call__(self, url: str) -> HttpHeaders:
        return self._headers

    @cached_property
    def _headers(self) -> HttpHeaders:
        return {"Authorization": f"{self.token_type} {self.token}"}
