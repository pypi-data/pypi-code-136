"""
The Printing module.

This module provides the following classes:
- Printing
"""
__all__ = ["Printing"]

from datetime import datetime

from tcgplayer.schemas import BaseModel


class Printing(BaseModel):
    """
    The Printing object contains information for a printing.

    Attributes:
        printing_id: Identifier used by TCGPlayer.
        name:
        display_order:
        modified_on:
    """

    printing_id: int
    name: str
    display_order: int
    modified_on: datetime

    def __init__(self, **data):
        if "." in (modified_on := data["modifiedOn"]):
            data["modifiedOn"] = modified_on[: modified_on.rindex(".")]
        super().__init__(**data)
