from enum import Enum
from typing import List, Optional

from pydantic import UUID4, BaseModel, Field, conint, constr

Id = constr(strip_whitespace=True, min_length=1, max_length=50)
Name = constr(strip_whitespace=True, min_length=1, max_length=200)
Description = constr(strip_whitespace=True, min_length=1, max_length=1000)
ClassValue = constr(strip_whitespace=True, min_length=1, max_length=100)
Timestamp = conint(ge=0)
ItemCount = conint(ge=0)


class DataCreatorType(str, Enum):
    JOB = "job"
    USER = "user"
    SCOPE = "scope"


class DataReferenceType(str, Enum):
    WSI = "wsi"
    ANNOTATION = "annotation"
    COLLECTION = "collection"
    NONE = None


class RestrictedBaseModel(BaseModel):
    """Abstract Super-class not allowing unknown fields in the **kwargs."""

    class Config:
        extra = "forbid"


class Message(RestrictedBaseModel):
    message: str = Field(description="Message used for untyped responses")


class Detail(RestrictedBaseModel):
    detail: str = Field(description="Message used for untyped responses")


class ServiceStatus(RestrictedBaseModel):
    status: str = Field(example="ok", description="Status of service")
    version: str = Field(example="0.3.7", description="Version of service")


class IdObject(RestrictedBaseModel):
    id: Id = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        description="ID (type string) of a single element",
    )


class Viewport(RestrictedBaseModel):
    x: conint(ge=0, strict=True) = Field(
        example=180,
        description="X coordinate of upper left corner of viewport (must be >= 0)",
    )
    y: conint(ge=0, strict=True) = Field(
        example=240,
        description="Y coordinate of upper left corner of viewport (must be >= 0)",
    )
    width: conint(gt=0, strict=True) = Field(example=1280, description="Width of viewport (must be > 0)")
    height: conint(gt=0, strict=True) = Field(example=1024, description="Height of viewport (must be > 0)")


class UniqueReferences(RestrictedBaseModel):
    annotation: Optional[List[UUID4]] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of unique referenced annotation IDs (type UUID4)",
    )
    collection: Optional[List[UUID4]] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of unique referenced collection IDs (type UUID4)",
    )
    wsi: Optional[List[Id]] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of unique referenced WSI IDs (type string)",
    )
    contains_items_without_reference: Optional[bool] = Field(
        example=True,
        description="If true: there are items matching the filter criteria without a reference",
    )


# Shared validator for reference of collection and primitive


def validate_reference(reference_id, reference_type):
    if (not reference_id and reference_type) or (reference_id and not reference_type):
        raise ValueError(
            "The fields reference_id and reference_type must either both be None or set with valid values!"
        )
