"""
The Product module.

This module provides the following classes:
- Product
"""
__all__ = ["Product"]

from datetime import datetime

from tcgplayer.schemas import BaseModel


class Product(BaseModel):
    """
    The Product object contains information for a product.

    Attributes:
        product_id: Identifier used by TCGPlayer.
        name:
        clean_name:
        image_url:
        category_id: Id of the Category this product is a part of.
        group_id: Id of the Group this product is a part of.
        url:
        modified_on:
    """

    product_id: int
    name: str
    clean_name: str
    image_url: str
    category_id: int
    group_id: int
    url: str
    modified_on: datetime

    def __init__(self, **data):
        if "." in (modified_on := data["modifiedOn"]):
            data["modifiedOn"] = modified_on[: modified_on.rindex(".")]
        super().__init__(**data)
