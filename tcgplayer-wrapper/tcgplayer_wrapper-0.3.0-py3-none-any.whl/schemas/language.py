"""
The Language module.

This module provides the following classes:
- Language
"""
__all__ = ["Language"]

from pydantic import Field

from tcgplayer.schemas import BaseModel


class Language(BaseModel):
    """
    The Language object contains information for a language.

    Attributes:
        language_id: Identifier used by TCGPlayer.
        name:
        abbreviation:
    """

    language_id: int
    name: str
    abbreviation: str = Field(alias="abbr")
