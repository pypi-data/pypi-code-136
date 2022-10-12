from dataclasses import dataclass

from atoti_core import keyword_only_dataclass

from ._config import Config


@keyword_only_dataclass
@dataclass(frozen=True)
class KeyPair(Config):
    public_key: str
    """The public key."""

    private_key: str
    """The private key."""
