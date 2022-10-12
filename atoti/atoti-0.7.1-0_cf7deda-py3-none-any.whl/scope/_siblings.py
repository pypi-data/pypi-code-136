from atoti_core import deprecated

from ..hierarchy import Hierarchy
from .siblings_scope import SiblingsScope


def siblings(hierarchy: Hierarchy, *, exclude_self: bool = False) -> SiblingsScope:
    deprecated(
        "Creating a scope with this function is deprecated. Initialize a SiblingsScope directly instead."
    )

    return SiblingsScope(
        hierarchy=hierarchy,
        exclude_self=exclude_self,
    )
