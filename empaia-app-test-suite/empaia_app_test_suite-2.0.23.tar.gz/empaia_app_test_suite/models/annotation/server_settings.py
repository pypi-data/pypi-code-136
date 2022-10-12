from pydantic import Field, StrictInt

from ..commons import RestrictedBaseModel


class AnnotationServiceSettings(RestrictedBaseModel):
    item_limit: StrictInt = Field(
        example=12345,
        description="Number of item that can be returned in a single request.",
    )
    post_limit: StrictInt = Field(
        example=12345,
        description="Number of item that can be posted in a single request.",
    )
