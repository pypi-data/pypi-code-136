from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import UUID4, Field, conlist, validator

from ..commons import (
    DataCreatorType,
    Description,
    Id,
    IdObject,
    ItemCount,
    Message,
    Name,
    RestrictedBaseModel,
    Viewport,
    validate_reference,
)
from .annotations import (
    AnnotationListResponse,
    ArrowAnnotation,
    ArrowAnnotationCore,
    CircleAnnotation,
    CircleAnnotationCore,
    LineAnnotation,
    LineAnnotationCore,
    NppViewing,
    PointAnnotation,
    PointAnnotationCore,
    PolygonAnnotation,
    PolygonAnnotationCore,
    PostArrowAnnotation,
    PostCircleAnnotation,
    PostLineAnnotation,
    PostPointAnnotation,
    PostPolygonAnnotation,
    PostRectangleAnnotation,
    RectangleAnnotation,
    RectangleAnnotationCore,
)
from .classes import Class, ClassCore, ClassListResponse, PostClass
from .primitives import (
    BoolPrimitive,
    BoolPrimitiveCore,
    FloatPrimitive,
    FloatPrimitiveCore,
    IntegerPrimitive,
    IntegerPrimitiveCore,
    PostBoolPrimitive,
    PostFloatPrimitive,
    PostIntegerPrimitive,
    PostStringPrimitive,
    PrimitiveList,
    StringPrimitive,
    StringPrimitiveCore,
)


class CollectionItemType(str, Enum):
    WSI = "wsi"
    INTEGER = "integer"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    POINT = "point"
    LINE = "line"
    ARROW = "arrow"
    CIRCLE = "circle"
    RECTANGLE = "rectangle"
    POLYGON = "polygon"
    CLASS = "class"
    COLLECTION = "collection"


class CollectionReferenceType(str, Enum):
    ANNOTATION = "annotation"
    WSI = "wsi"


# Item type models


class SlideItem(RestrictedBaseModel):
    id: Id = Field(example="4967bf63-a2a1-421c-8789-bf616953537c", description="WSI ID")
    type: Literal["wsi"] = Field(example="wsi", description="WSI type")


class SlideList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=12345, description="Count of all items")
    items: List[SlideItem] = Field(description="List of items")


# Core model - used by AppService


class CollectionCore(RestrictedBaseModel):
    name: Optional[Name] = Field(example="Collection Name", description="Collection name")
    description: Optional[Description] = Field(example="Collection Description", description="Collection description")
    reference_id: Optional[Id] = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        description="Id of the object referenced by this collection",
    )
    reference_type: Optional[CollectionReferenceType] = Field(
        example=CollectionReferenceType.WSI, description="Refrence type"
    )
    item_type: CollectionItemType = Field(
        example=CollectionItemType.POINT, description="The type of items in the collection"
    )
    items: Optional[
        Union[
            List[PointAnnotationCore],
            List[LineAnnotationCore],
            List[ArrowAnnotationCore],
            List[CircleAnnotationCore],
            List[RectangleAnnotationCore],
            List[PolygonAnnotationCore],
            List[ClassCore],
            List[IntegerPrimitiveCore],
            List[FloatPrimitiveCore],
            List[BoolPrimitiveCore],
            List[StringPrimitiveCore],
            List[SlideItem],
            List[IdObject],
            List[CollectionCore],
        ]
    ] = Field(description="Items of the collection")

    # validator for reference
    @validator("reference_type", always=True, pre=True)
    def check_reference(cls, reference_type, values):
        reference_id = values.get("reference_id")
        validate_reference(reference_id, reference_type)
        return reference_type


CollectionCore.update_forward_refs()


# Post models


class PostCollection(CollectionCore):
    id: Optional[UUID4] = Field(
        example="4967bf63-a2a1-421c-8789-bf616953537c",
        description="ID of type UUID4 (only needed in post if external Ids enabled)",
    )
    type: Literal["collection"] = Field(example="collection", description="Collection type")
    creator_id: Id = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        description="Creator Id",
    )
    creator_type: DataCreatorType = Field(example=DataCreatorType.JOB, description="Creator type")
    items: Optional[
        Union[
            List[PostPointAnnotation],
            List[PostLineAnnotation],
            List[PostArrowAnnotation],
            List[PostCircleAnnotation],
            List[PostRectangleAnnotation],
            List[PostPolygonAnnotation],
            List[PostClass],
            List[PostIntegerPrimitive],
            List[PostFloatPrimitive],
            List[PostBoolPrimitive],
            List[PostStringPrimitive],
            List[SlideItem],
            List[IdObject],
            List[PostCollection],
        ]
    ] = Field(description="Items of the collection")


PostCollection.update_forward_refs()


# Full model


class Collection(PostCollection):
    is_locked: Optional[bool] = Field(
        example="false",
        description="Flag to mark a collection as immutable",
    )
    item_count: Optional[ItemCount] = Field(example=42, description="The number of items in the collection")
    items: Optional[
        Union[
            List[PointAnnotation],
            List[LineAnnotation],
            List[ArrowAnnotation],
            List[CircleAnnotation],
            List[RectangleAnnotation],
            List[PolygonAnnotation],
            List[Class],
            List[IntegerPrimitive],
            List[FloatPrimitive],
            List[BoolPrimitive],
            List[StringPrimitive],
            List[SlideItem],
            List[IdObject],
            List[Collection],
        ]
    ] = Field(description="Items of the collection")
    item_ids: Optional[List[UUID4]] = Field(
        description="Ids of items in collection",
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
    )


Collection.update_forward_refs()


class CollectionList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=12345, description="Count of items.")
    items: List[Collection] = Field(description="List of items.")


CollectionItems = Union[
    List[IntegerPrimitive],
    List[FloatPrimitive],
    List[BoolPrimitive],
    List[StringPrimitive],
    List[PointAnnotation],
    List[LineAnnotation],
    List[ArrowAnnotation],
    List[CircleAnnotation],
    List[RectangleAnnotation],
    List[PolygonAnnotation],
    List[Class],
    List[SlideItem],
    List[Collection],
]


# Query model


class CollectionQuery(RestrictedBaseModel):
    creators: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of creator Ids",
    )
    references: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of reference Ids",
    )
    jobs: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of job Ids",
    )
    item_types: Optional[conlist(CollectionItemType, min_items=1)] = Field(
        example=[CollectionItemType.INTEGER, CollectionItemType.FLOAT], description="List of item types"
    )


# Item models


ItemCore = Union[
    PointAnnotationCore,
    LineAnnotationCore,
    ArrowAnnotationCore,
    CircleAnnotationCore,
    RectangleAnnotationCore,
    PolygonAnnotationCore,
    ClassCore,
    IntegerPrimitiveCore,
    FloatPrimitiveCore,
    BoolPrimitiveCore,
    StringPrimitiveCore,
    SlideItem,
    IdObject,
    CollectionCore,
]


ItemListCore = Union[
    List[PointAnnotationCore],
    List[LineAnnotationCore],
    List[ArrowAnnotationCore],
    List[CircleAnnotationCore],
    List[RectangleAnnotationCore],
    List[PolygonAnnotationCore],
    List[ClassCore],
    List[IntegerPrimitiveCore],
    List[FloatPrimitiveCore],
    List[BoolPrimitiveCore],
    List[StringPrimitiveCore],
    List[SlideItem],
    List[IdObject],
    List[CollectionCore],
]


PostItem = Union[
    PostPointAnnotation,
    PostLineAnnotation,
    PostArrowAnnotation,
    PostCircleAnnotation,
    PostRectangleAnnotation,
    PostPolygonAnnotation,
    PostClass,
    PostIntegerPrimitive,
    PostFloatPrimitive,
    PostBoolPrimitive,
    PostStringPrimitive,
    SlideItem,
    IdObject,
    PostCollection,
]


PostItemLists = Union[
    List[PostPointAnnotation],
    List[PostLineAnnotation],
    List[PostArrowAnnotation],
    List[PostCircleAnnotation],
    List[PostRectangleAnnotation],
    List[PostPolygonAnnotation],
    List[PostClass],
    List[PostIntegerPrimitive],
    List[PostFloatPrimitive],
    List[PostBoolPrimitive],
    List[PostStringPrimitive],
    List[SlideItem],
    List[IdObject],
    List[PostCollection],
]


class PostItemList(RestrictedBaseModel):
    items: PostItemLists = Field(description="Item list")


PostItems = Union[PostItem, PostItemList]


class ItemQueryList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=12345, description="Count of all items")
    items: Union[
        List[IntegerPrimitive],
        List[FloatPrimitive],
        List[BoolPrimitive],
        List[StringPrimitive],
        List[PointAnnotation],
        List[LineAnnotation],
        List[ArrowAnnotation],
        List[CircleAnnotation],
        List[RectangleAnnotation],
        List[PolygonAnnotation],
        List[Class],
        List[Collection],
    ] = Field(description="Items returned by item query")


ItemPostResponse = Union[
    Message,
    PointAnnotation,
    LineAnnotation,
    ArrowAnnotation,
    CircleAnnotation,
    RectangleAnnotation,
    PolygonAnnotation,
    AnnotationListResponse,
    IntegerPrimitive,
    FloatPrimitive,
    BoolPrimitive,
    StringPrimitive,
    PrimitiveList,
    Class,
    ClassListResponse,
    SlideItem,
    SlideList,
    Collection,
    CollectionList,
]


# Item query model


class ItemQuery(RestrictedBaseModel):
    references: Optional[conlist(Id, min_items=1)] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="List of reference Ids",
    )
    viewport: Optional[Viewport] = Field(
        example={"x": 180, "y": 240, "width": 1280, "height": 1024},
        description="The viewport (only used for annotations: only annotations within are returned)",
    )
    npp_viewing: Optional[NppViewing] = Field(
        example=[499.0, 7984.0],
        description="Resolution range in npp (nanometer per pixel) to filter annotations (only used for annotations)",
    )
