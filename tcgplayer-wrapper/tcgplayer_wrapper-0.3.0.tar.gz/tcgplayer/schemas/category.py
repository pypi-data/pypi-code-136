"""
The Category module.

This module provides the following classes:
- Category
"""
__all__ = ["Category"]

from datetime import datetime
from typing import Optional

from tcgplayer.schemas import BaseModel


class Category(BaseModel):
    """
    The Category object contains information for a category.

    Attributes:
        category_id: Identifier used by TCGPlayer.
        name:
        modified_on:
        display_name:
        seo_category_name:
        sealed_label:
        non_sealed_label:
        condition_guide_url:
        is_scannable:
        popularity:
        is_direct:
    """

    category_id: int
    name: str
    modified_on: datetime
    display_name: str
    seo_category_name: str
    sealed_label: Optional[str] = None
    non_sealed_label: Optional[str] = None
    condition_guide_url: str
    is_scannable: bool = False
    popularity: int
    is_direct: bool = False

    def __init__(self, **data):
        if "." in (modified_on := data["modifiedOn"]):
            data["modifiedOn"] = modified_on[: modified_on.rindex(".")]
        super().__init__(**data)
