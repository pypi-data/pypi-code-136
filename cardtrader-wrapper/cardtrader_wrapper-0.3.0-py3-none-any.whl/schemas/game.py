"""
The Game module.

This module provides the following classes:
- Game
"""
__all__ = ["Game"]

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Game(BaseModel):
    """
    The Game object contains information for a game.

    Attributes:
        display_name:
        game_id: Identifier used by CardTrader.
        name:
    """

    display_name: str
    game_id: int = Field(alias="id")
    name: str

    @validator("display_name", "name", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
