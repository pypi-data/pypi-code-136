"""
The Product module.

This module provides the following classes:
- Product
"""
__all__ = ["Product"]

from typing import Dict, Optional, Union

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Price(BaseModel):
    """
    The Price object contains information used in a product property.

    Attributes:
        cents:
        currency:
        currency_symbol:
        formatted:
    """

    cents: int
    currency: str
    currency_symbol: str
    formatted: str

    @validator("currency", "currency_symbol", "formatted", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None


class Expansion(BaseModel):
    """
    The Expansion object contains information used in a product property.

    Attributes:
        code:
        expansion_id:
        name:
    """

    code: str
    expansion_id: int = Field(alias="id")
    name: str = Field(alias="name_en")

    @validator("code", "name", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None


class User(BaseModel):
    """
    The User object contains information used in a product property.

    Attributes:
        can_sell_sealed_with_ct_zero:
        can_sell_via_hub:
        country_code:
        user_id:
        too_many_request_for_cancel_as_seller:
        user_type:
        username:
        max_sellable_in24h_quantity:
    """

    can_sell_sealed_with_ct_zero: bool
    can_sell_via_hub: bool
    country_code: str
    user_id: int = Field(alias="id")
    too_many_request_for_cancel_as_seller: bool
    user_type: str
    username: str
    max_sellable_in24h_quantity: Optional[int] = None

    @validator("country_code", "user_type", "username", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None


class Product(BaseModel):
    """
    The Product object contains information for a product.

    Attributes:
        blueprint_id: Identifier used by CardTrader.
        bundle_size:
        expansion:
        product_id: Identifier used by CardTrader.
        name:
        on_vacation:
        price:
        price_cents:
        price_currency:
        quantity:
        seller:
        description:
        graded:
        layered_price_cents:
        properties:
        tag:
    """

    blueprint_id: int
    bundle_size: int
    expansion: Expansion
    product_id: int = Field(alias="id")
    name: str = Field(alias="name_en")
    on_vacation: bool
    price: Price
    price_cents: int
    price_currency: str
    quantity: int
    seller: User = Field(alias="user")
    description: Optional[str] = None
    graded: Optional[bool] = None
    layered_price_cents: Optional[int] = None
    properties: Dict[str, Optional[Union[str, bool]]] = Field(
        alias="properties_hash", default_factory=dict
    )
    tag: Optional[str] = None

    @validator("name", "price_currency", "description", "tag", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
