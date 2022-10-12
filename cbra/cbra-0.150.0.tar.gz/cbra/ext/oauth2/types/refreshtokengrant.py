"""Declares :class:`ClientCredentialsGrant`"""
import typing

import pydantic

from .basegrant import BaseGrant
from .granttype import GrantType
from .spaceseparatedlist import SpaceSeparatedList


class RefreshTokenGrant(BaseGrant):
    __module__: str = 'cbra.ext.oauth2.types'

    grant_type: typing.Literal[GrantType.refresh_token] = pydantic.Field(
        default=...,
        title="Grant type",
        description="Must be `refresh_token`.",
        example="refresh_token"
    )

    refresh_token: str = pydantic.Field(
        default=...,
        title="Refresh token",
        description=(
            "The refresh token that was previously issued to the "
            "Client."
        )
    )

    scope: SpaceSeparatedList | None = pydantic.Field(
        default=[],
        title="Scope",
        description=(
            "The requested scope that the client wants to obtain an access "
            "token for."
        )
    )