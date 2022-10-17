from __future__ import annotations
from ..context import Context
from ..lib.slug import slugify
from ..types_hafas_client import Operator
from ..types_raw_hafas_client import RawOp

def slug(s: str) -> str:
    return slugify(s)


default_operator: Operator = Operator("operator", "", "")

def parse_operator(ctx: Context, a: RawOp) -> Operator:
    name: str = a.name.strip()
    return Operator(default_operator.type, slug(name), name)


__all__ = ["slug", "default_operator", "parse_operator"]

