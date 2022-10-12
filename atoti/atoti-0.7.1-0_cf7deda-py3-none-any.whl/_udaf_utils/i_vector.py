from __future__ import annotations

from typing import Literal, Tuple, cast

from atoti_core import get_literal_args

IVectorType = Literal["IVector"]


def _get_i_vector() -> IVectorType:
    arg, *unexpected_args = cast(Tuple[IVectorType, ...], get_literal_args(IVectorType))

    if unexpected_args:
        raise TypeError(
            f"Expected `IVectorType` to have a single arg but has: {len(unexpected_args) + 1}."
        )

    return arg


I_VECTOR = _get_i_vector()
