"""
The Blueprint module.

This module provides the following classes:
- Blueprint
"""
__all__ = ["Blueprint"]

from typing import Dict, List, Optional, Union

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Property(BaseModel):
    """
    The Property object contains information used in a blueprint property.

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


class Blueprint(BaseModel):
    """
    The Blueprint object contains information for a blueprint.

    Attributes:
        category_id: Identifier used by CardTrader.
        expansion_id: Identifier used by CardTrader.
        game_id: Identifier used by CardTrader.
        blueprint_id: Identifier used by CardTrader.
        image_url:
        name: Name/Title of the blueprint.
        card_market_id:
        editable_properties:
        fixed_properties:
        scryfall_id:
        tcg_player_id:
        version:
    """

    category_id: int
    expansion_id: int
    game_id: int
    blueprint_id: int = Field(alias="id")
    image_url: str
    name: str
    card_market_id: Optional[int] = None
    editable_properties: List[Property] = Field(default_factory=list)
    fixed_properties: Dict[str, str] = Field(default_factory=dict)
    scryfall_id: Optional[str] = None
    tcg_player_id: Optional[int] = None
    version: Optional[str] = None

    @validator("image_url", "name", "scryfall_id", "version", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
