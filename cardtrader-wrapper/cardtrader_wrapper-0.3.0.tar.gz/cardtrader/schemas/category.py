"""
The Category module.

This module provides the following classes:
- Category
"""
__all__ = ["Category"]

from typing import List, Optional, Union

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Property(BaseModel):
    """
    The Property object contains information used in a category property.

    Attributes:
        name:
        property_type:
        default_value:
        possible_values:
    """

    name: str
    property_type: str = Field(alias="type")
    default_value: Optional[str] = None
    possible_values: List[Union[str, bool]] = Field(default_factory=list)

    @validator("name", "property_type", "default_value", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None


class Category(BaseModel):
    """
    The Category object contains information for a category.

    Attributes:
        game_id: Identifier used by CardTrader.
        category_id: Identifier used by CardTrader.
        name:
        properties:
    """

    game_id: int
    category_id: int = Field(alias="id")
    name: str
    properties: List[Property] = Field(default_factory=list)

    @validator("name", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
