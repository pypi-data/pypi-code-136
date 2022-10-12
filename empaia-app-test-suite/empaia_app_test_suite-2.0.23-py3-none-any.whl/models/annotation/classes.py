from enum import Enum
from typing import Any, List, Literal, Optional, Union

from pydantic import UUID4, Field, conlist

from ..commons import ClassValue, DataCreatorType, Id, ItemCount, RestrictedBaseModel


class ClassReferenceType(str, Enum):
    ANNOTATION = "annotation"


# Core model - Used in AppService


class ClassCore(RestrictedBaseModel):
    value: ClassValue = Field(
        example="org.empaia.my_vendor.my_app.v1.classes.non_tumor",
        description="Either a value from EMPAIA App Description or a permitted global class value",
    )
    reference_id: UUID4 = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        description="ID of type UUID4 - ID of referenced annotation",
    )
    reference_type: ClassReferenceType = Field(
        example=ClassReferenceType.ANNOTATION, description='Reference type (must be "annotation")'
    )


# Post models


class PostClass(ClassCore):
    id: Optional[UUID4] = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        description="ID of type UUID4 (only needed in post if external Ids enabled)",
    )
    type: Literal["class"] = Field(example="class", description='Item of type "class"')
    creator_id: Id = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Creator ID")
    creator_type: DataCreatorType = Field(example=DataCreatorType.JOB, description="Creator type")


class PostClassList(RestrictedBaseModel):
    items: List[PostClass] = Field(description="List of classes")


PostClasses = Union[PostClass, PostClassList]


# Full and post response models


class Class(PostClass):
    is_locked: Optional[bool] = Field(example="false", description="Flag to mark a class as immutable")


class ClassListResponse(RestrictedBaseModel):
    item_count: ItemCount = Field(example=12345, description="Count of all items ")
    items: List[Class] = Field(description="List of items")


Classes = Union[Class, ClassListResponse]


class ClassList(ClassListResponse):
    unique_class_values: Optional[List[ClassValue]] = Field(
        example=[
            "org.empaia.my_vendor.my_app.v1.classes.non_tumor",
            "org.empaia.my_vendor.my_app.v1.classes.tumor",
        ],
        description="List of unique class values (for classes matching given filter criteria when returned by query)",
    )


# Query model


class ClassQuery(RestrictedBaseModel):
    creators: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of creator Ids",
    )
    references: Optional[conlist(UUID4, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of annotation Ids (UUID type 4)",
    )
    jobs: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of job Ids",
    )
    classes: Optional[conlist(Any, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of Class Ids (must be of type UUID4)",
    )
