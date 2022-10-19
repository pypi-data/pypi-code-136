"""
The Expansion module.

This module provides the following classes:
- Expansion
"""
__all__ = ["Expansion"]

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Expansion(BaseModel):
    """
    The Expansion object contains information for an expansion.

    Attributes:
        code:
        game_id: Identifier used by CardTrader.
        expansion_id: Identifier used by CardTrader.
        name:
    """

    code: str
    game_id: int
    expansion_id: int = Field(alias="id")
    name: str

    @validator("code", "name", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
