from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from atoti_core import keyword_only_dataclass

from ._config import Config
from .key_pair import KeyPair


@keyword_only_dataclass
@dataclass(frozen=True)
class JwtConfig(Config):
    """The JWT configuration.

    Note:
        This requires the :mod:`atoti-plus <atoti_plus>` plugin.

    Atoti+ uses JSON Web Tokens to authenticate communications between its various components (e.g. between the app and the session), but also to authenticate communications with remote user content storages.

    Example:

        >>> config = tt.JwtConfig(
        ...     key_pair=tt.KeyPair(
        ...         public_key="some public key",
        ...         private_key="some private key",
        ...     )
        ... )

    """

    key_pair: KeyPair
    """The key pair used to sign the JWT.

    By default, a random key pair of 2048 bytes will be generated at session creation time.

    Passing a custom JWT key pair is mainly useful for SSO purposes

    Only RSA keys using the PKCS 8 standard are supported.
    Key pairs can be generated using a library like ``pycryptodome`` for example.
    """

    @classmethod
    def _from_mapping(cls, mapping: Mapping[str, Any]) -> JwtConfig:
        data = dict(mapping)
        return cls(
            key_pair=KeyPair._from_mapping(data.pop("key_pair")),
            **data,
        )
