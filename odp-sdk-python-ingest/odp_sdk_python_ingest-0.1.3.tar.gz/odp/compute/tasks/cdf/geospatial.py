from dataclasses import dataclass, fields
from typing import ClassVar
from cognite.experimental.data_classes.geospatial import FeatureType


@dataclass
class ExampleFeature(object):

    obj_id: int
    name: str
    address: Optional[str] = None


def feature_type_from_dataclass(cls: ClassVar):

    attributes = {}
    for field in fields(cls):
        attribute_name = field.name

        if isinstance(field.type, str):
            attribute_type = "string"
        if isinstance(field.type, int):
            attribute_type = "long"
        else:
            raise ValueError(f"Invalid type: {field.type}")


if __name__ == "__main__":
    for field in fields(ExampleFeature):
        print(field)
