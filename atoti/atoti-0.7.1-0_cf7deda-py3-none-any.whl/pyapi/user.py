from dataclasses import dataclass
from typing import Collection

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class User:
    """Info of a user calling a custom HTTP endpoint."""

    name: str
    """Name of the user calling the endpoint."""

    roles: Collection[str]
    """Roles of the user calling the endpoint."""
