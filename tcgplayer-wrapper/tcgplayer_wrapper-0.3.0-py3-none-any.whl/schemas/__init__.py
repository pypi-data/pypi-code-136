"""tcgplayer.schemas package entry file."""
__all__ = ["BaseModel"]

from pydantic import BaseModel as PyModel
from pydantic import Extra


def to_camel_case(value: str) -> str:
    temp = value.replace("_", " ").title().replace(" ", "")
    return temp[0].lower() + temp[1:]


class BaseModel(PyModel):
    """Base model for TCGPlayer models."""

    class Config:
        """Any extra fields will be ignored, strings will have start/end whitespace stripped."""

        alias_generator = to_camel_case
        anystr_strip_whitespace = True
        allow_population_by_field_name = True
        extra = Extra.forbid
