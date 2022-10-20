"""
The Group module.

This module provides the following classes:
- Group
"""
__all__ = ["Group"]

from datetime import date, datetime
from typing import Optional

from tcgplayer.schemas import BaseModel


class Group(BaseModel):
    """
    The Group object contains information for a group.

    Attributes:
        group_id: Identifier used by TCGPlayer.
        name:
        abbreviation:
        is_supplemental:
        published_on:
        modified_on:
        category_id: Id of the Category this group is a part of.
    """

    group_id: int
    name: str
    abbreviation: Optional[str] = None
    is_supplemental: bool = False
    published_on: date
    modified_on: datetime
    category_id: int

    def __init__(self, **data):
        if "T" in (published_on := data["publishedOn"]):
            data["publishedOn"] = published_on[: published_on.index("T")]
        if "." in (modified_on := data["modifiedOn"]):
            data["modifiedOn"] = modified_on[: modified_on.rindex(".")]
        super().__init__(**data)
