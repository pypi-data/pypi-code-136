"""
The Info module.

This module provides the following classes:
- Info
"""
__all__ = ["Info"]

from pydantic import Field, validator

from cardtrader.schemas import BaseModel


class Info(BaseModel):
    """
    The Info object contains information for an info.

    Attributes:
        info_id: Identifier used by CardTrader.
        name:
        shared_secret:
    """

    info_id: int = Field(alias="id")
    name: str
    shared_secret: str

    @validator("name", "shared_secret", pre=True, check_fields=False)
    def remove_blank_strings(cls, value: str):
        """Pydantic validator to convert str to None or return value."""
        return value if value else None
