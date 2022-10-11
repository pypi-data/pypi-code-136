from pydantic import BaseModel, Field
from napari.layers.image import Image
from mikro.api.schema import RepresentationFragment
import uuid


class BaseContainer(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    representation: RepresentationFragment
    with_rois: bool = False
    with_labels: bool = False
