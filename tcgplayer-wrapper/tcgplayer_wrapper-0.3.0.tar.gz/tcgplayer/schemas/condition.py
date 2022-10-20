"""
The Condition module.

This module provides the following classes:
- Condition
"""
__all__ = ["Condition"]

from tcgplayer.schemas import BaseModel


class Condition(BaseModel):
    """
    The Condition object contains information for a condition.

    Attributes:
        condition_id: Identifier used by TCGPlayer.
        name:
        abbreviation:
        display_order:
    """

    condition_id: int
    name: str
    abbreviation: str
    display_order: int
