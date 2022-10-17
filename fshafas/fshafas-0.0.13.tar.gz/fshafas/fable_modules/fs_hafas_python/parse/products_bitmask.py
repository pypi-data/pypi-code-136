from __future__ import annotations
from ...fable_library.array import (fold, exists)
from ...fable_library.types import Array
from ..context import Context
from ..extra_types import (IndexMap_2, IndexMap_2__set_Item_541DA560, IndexMap_2__ctor_2B594)
from ..types_hafas_client import ProductType

def parse_bitmask(ctx: Context, bitmask: int) -> IndexMap_2[str, bool]:
    array_1: Array[ProductType] = ctx.profile.products
    def folder(m: IndexMap_2[str, bool], p: ProductType, ctx: Context=ctx, bitmask: int=bitmask) -> IndexMap_2[str, bool]:
        def predicate(b: int, m: IndexMap_2[str, bool]=m, p: ProductType=p) -> bool:
            return (b & bitmask) != 0

        IndexMap_2__set_Item_541DA560(m, p.id, exists(predicate, p.bitmasks))
        return m

    return fold(folder, IndexMap_2__ctor_2B594(False), array_1)


__all__ = ["parse_bitmask"]

