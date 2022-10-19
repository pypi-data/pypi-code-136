"""cardtrader.schemas package entry file."""
__all__ = ["BaseModel"]

from pydantic import BaseModel as PyModel
from pydantic import Extra


class BaseModel(PyModel):
    """Base model for CardTrader models."""

    class Config:
        """Any extra fields will be ignored, strings will have start/end whitespace stripped."""

        anystr_strip_whitespace = True
        allow_population_by_field_name = True
        extra = Extra.forbid
