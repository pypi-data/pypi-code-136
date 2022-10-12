import json
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic.typing import Literal

from .models.annotation.annotations import (
    PostArrowAnnotation,
    PostCircleAnnotation,
    PostLineAnnotation,
    PostPointAnnotation,
    PostPolygonAnnotation,
    PostRectangleAnnotation,
)
from .models.annotation.classes import PostClass
from .models.annotation.primitives import (
    PostBoolPrimitive,
    PostFloatPrimitive,
    PostIntegerPrimitive,
    PostStringPrimitive,
)

for klass in (
    PostPointAnnotation,
    PostLineAnnotation,
    PostArrowAnnotation,
    PostCircleAnnotation,
    PostRectangleAnnotation,
    PostPolygonAnnotation,
    PostIntegerPrimitive,
    PostFloatPrimitive,
    PostBoolPrimitive,
    PostStringPrimitive,
    PostClass,
):
    del klass.__fields__["creator_type"]
    del klass.__fields__["creator_id"]


class ApiDataType(Enum):
    ANNOTATIONS = "annotations"
    PRIMITIVES = "primitives"
    CLASSES = "classes"
    COLLECTIONS = "collections"
    SLIDES = "slides"


class InputParameter(BaseModel):
    input_key: str  # key in ead.inputs
    post_data: dict
    api_data_type: ApiDataType
    reference_ids: List[str]  # multiple if collection


class WsiInput(BaseModel):
    class Config:
        extra = "forbid"

    type: Literal["wsi"]
    id: Optional[str]
    path: str
    tissue: str = "KIDNEY"
    stain: str = "H_AND_E"
    block: str = "block123"


class OptionalForTestSuitePrimitive(BaseModel):
    name: Optional[str]
    creator_type: Optional[str]
    creator_id: Optional[str]


class OptionalForTestSuite(OptionalForTestSuitePrimitive):
    reference_type: Optional[str]


class ClassInput(PostClass, OptionalForTestSuite):
    pass


class IntegerInput(PostIntegerPrimitive, OptionalForTestSuitePrimitive):
    pass


class FloatInput(PostFloatPrimitive, OptionalForTestSuitePrimitive):
    pass


class BoolInput(PostBoolPrimitive, OptionalForTestSuitePrimitive):
    pass


class StringInput(PostStringPrimitive, OptionalForTestSuitePrimitive):
    pass


class PointInput(PostPointAnnotation, OptionalForTestSuite):
    pass


class LineInput(PostLineAnnotation, OptionalForTestSuite):
    pass


class ArrowInput(PostArrowAnnotation, OptionalForTestSuite):
    pass


class CircleInput(PostCircleAnnotation, OptionalForTestSuite):
    pass


class RectangleInput(PostRectangleAnnotation, OptionalForTestSuite):
    pass


class PolygonInput(PostPolygonAnnotation, OptionalForTestSuite):
    pass


class CollectionInput(BaseModel):
    id: Optional[str]
    name: Optional[str]
    reference_type: Optional[str]
    creator_id: Optional[str]
    creator_type: Optional[str]
    is_locked: Optional[bool]
    item_type: Literal[
        "integer",
        "float",
        "bool",
        "string",
        "point",
        "line",
        "arrow",
        "circle",
        "rectangle",
        "polygon",
        "wsi",
        "class",
        "collection",
    ]
    item_count: Optional[int]
    items: Union[
        List[IntegerInput],
        List[FloatInput],
        List[BoolInput],
        List[StringInput],
        List[PointInput],
        List[LineInput],
        List[ArrowInput],
        List[CircleInput],
        List[RectangleInput],
        List[PolygonInput],
        List[WsiInput],
        List[ClassInput],
        List["CollectionInput"],
    ]


CollectionInput.update_forward_refs()


def extend_type_inplace(data: dict):
    if "type" not in data:
        if "items" in data:
            data["type"] = "collection"
            for item in data["items"]:
                extend_type_inplace(item)
        elif "value" in data:
            data["type"] = "class"
        elif "path" in data:
            data["type"] = "wsi"


def parse_input_item(_type: str, _file: str):
    type_model_map = {
        "integer": IntegerInput,
        "float": FloatInput,
        "bool": BoolInput,
        "string": StringInput,
        "point": PointInput,
        "line": LineInput,
        "arrow": ArrowInput,
        "circle": CircleInput,
        "rectangle": RectangleInput,
        "polygon": PolygonInput,
        "wsi": WsiInput,
        "class": ClassInput,
        "collection": CollectionInput,
    }
    with open(_file, encoding="utf-8") as f:
        data = json.load(f)

    extend_type_inplace(data)
    type_model = type_model_map[_type]
    return type_model.parse_obj(data)
