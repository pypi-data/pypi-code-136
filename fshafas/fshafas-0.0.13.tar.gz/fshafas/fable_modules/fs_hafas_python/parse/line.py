from __future__ import annotations
from typing import (Optional, Tuple, Literal)
from ...fable_library.array import try_find
from ...fable_library.option import (default_arg, bind)
from ...fable_library.seq import (filter, try_head, empty)
from ...fable_library.util import IEnumerable_1
from ..context import (Context, Profile__get_parseBitmask)
from ..extra_types import (IndexMap_2, IndexMap_2__get_Item_2B595, IndexMap_2__get_Keys)
from ..lib.slug import slugify
from ..lib.transformations import Default_Line
from ..types_hafas_client import (Line, ProductType, Operator)
from ..types_raw_hafas_client import (RawProd, RawProdCtx)
from .common import get_element_at_some

def slug(s: str) -> Optional[str]:
    return slugify(s)


def filter_products(products: IndexMap_2[str, bool]) -> IEnumerable_1[str]:
    def predicate(kv: str, products: IndexMap_2[str, bool]=products) -> bool:
        return IndexMap_2__get_Item_2B595(products, kv)

    return filter(predicate, IndexMap_2__get_Keys(products))


def parse_line(ctx: Context, p: RawProd) -> Line:
    line: Line = Default_Line
    name: Optional[str] = default_arg(p.add_name, p.name)
    id: Optional[str]
    match_value: Optional[RawProdCtx] = p.prod_ctx
    def _arrow428(s: str, ctx: Context=ctx, p: RawProd=p) -> Optional[str]:
        return slug(s)

    id = (None if (name is None) else slug(name)) if (match_value is None) else bind(_arrow428, default_arg(match_value.line_id, name))
    pattern_input: Tuple[Optional[str], Optional[str], Optional[str]]
    match_value_1: Optional[RawProdCtx] = p.prod_ctx
    if match_value_1 is None:
        pattern_input = (None, None, None)

    else: 
        prod_ctx_1: RawProdCtx = match_value_1
        pattern_input = (prod_ctx_1.num, prod_ctx_1.admin, prod_ctx_1.cat_out)

    cat_out: Optional[str] = pattern_input[2]
    def _arrow429(__unit: Literal[None]=None, ctx: Context=ctx, p: RawProd=p) -> Optional[str]:
        cat_out_2: str = cat_out
        return cat_out_2.strip()

    product_name: Optional[str] = (_arrow429() if (cat_out != "") else None) if (cat_out is not None) else None
    def _arrow430(__unit: Literal[None]=None, ctx: Context=ctx, p: RawProd=p) -> IEnumerable_1[str]:
        match_value_2: Optional[int] = p.cls
        if match_value_2 is None:
            return empty()

        else: 
            cls: int = match_value_2 or 0
            return filter_products(Profile__get_parseBitmask(ctx.profile)(ctx)(cls))


    product: Optional[str] = try_head(_arrow430())
    pattern_input_1: Tuple[Optional[str], Optional[str]]
    if product is None:
        pattern_input_1 = (None, None)

    else: 
        kv: str = product
        def predicate(p_1: ProductType, ctx: Context=ctx, p: RawProd=p) -> bool:
            return p_1.id == kv

        match_value_3: Optional[ProductType] = try_find(predicate, ctx.profile.products)
        if match_value_3 is None:
            pattern_input_1 = (None, None)

        else: 
            product_1: ProductType = match_value_3
            pattern_input_1 = (product_1.id, product_1.mode)


    operator: Optional[Operator] = get_element_at_some(p.opr_x, ctx.common.operators)
    return Line(line.type, id, name, pattern_input[1], pattern_input[0], line.additional_name, pattern_input_1[0], True, pattern_input_1[1], line.routes, operator, line.express, line.metro, line.night, line.nr, line.symbol, line.directions, product_name)


__all__ = ["slug", "filter_products", "parse_line"]

