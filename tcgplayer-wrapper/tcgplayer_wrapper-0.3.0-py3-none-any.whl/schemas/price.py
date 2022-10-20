"""
The Price module.

This module provides the following classes:
- Price
"""
__all__ = ["Price"]

from typing import Optional

from tcgplayer.schemas import BaseModel


class Price(BaseModel):
    """
    The Price object contains information for a price.

    Attributes:
        product_id: Identifier used by TCGPlayer.
        low_price:
        mid_price:
        high_price:
        market_price:
        direct_low_price:
        sub_type_name:
    """

    product_id: int
    low_price: Optional[float] = None
    mid_price: Optional[float] = None
    high_price: Optional[float] = None
    market_price: Optional[float] = None
    direct_low_price: Optional[float] = None
    sub_type_name: str
