from atoti_core import deprecated

from ..level import Level
from .origin_scope import OriginScope


def origin(*levels: Level) -> OriginScope:
    deprecated(
        "Creating a scope with this function is deprecated. Initialize an OriginScope directly instead."
    )

    return OriginScope(*levels)
