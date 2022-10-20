"""
The Rarity module.

This module provides the following classes:
- Rarity
"""
__all__ = ["Rarity"]

from tcgplayer.schemas import BaseModel


class Rarity(BaseModel):
    """
    The Rarity object contains information for a rarity.

    Attributes:
        rarity_id: Identifier used by TCGPlayer.
        display_text:
        db_value:
    """

    rarity_id: int
    display_text: str
    db_value: str
