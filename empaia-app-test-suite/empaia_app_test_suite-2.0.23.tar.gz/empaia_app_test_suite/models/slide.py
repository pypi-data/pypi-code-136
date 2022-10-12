from typing import List, Optional

from pydantic import Field

from .commons import RestrictedBaseModel


class SlideExtent(RestrictedBaseModel):
    x: int = Field(..., description="Extent in horizontal direction")
    y: int = Field(..., description="Extent in vertical direction")
    z: int = Field(..., description="Number of Z-Stack layers")


class SlideColor(RestrictedBaseModel):
    r: int = Field(..., description="R-value (red channel)")
    g: int = Field(..., description="G-value (green channel)")
    b: int = Field(..., description="B-value (blue channel)")
    a: int = Field(..., description="A-value (alpha channel)")


class SlidePixelSizeNm(RestrictedBaseModel):
    x: float = Field(
        ...,
        description="Pixel size in horizontal direction in nm (finest level, level=0)",
    )
    y: float = Field(
        ...,
        description="Pixel size in vertical direction in nm (finest level, level=0)",
    )
    z: Optional[float] = Field(
        None,
        description="Distance of layers in a Z-Stack in nm",
    )


class SlideChannel(RestrictedBaseModel):
    id: int = Field(..., description="Channel ID")
    name: str = Field(..., description="Dedicated channel name")
    color: SlideColor = Field(..., description="RGBA-value of the image channel")


class SlideLevel(RestrictedBaseModel):
    extent: SlideExtent = Field(..., description="Image extent for this level")
    downsample_factor: float = Field(..., description="Downsample factor for this level")


class SlideInfo(RestrictedBaseModel):
    id: str = Field(..., description="Slide ID")
    channels: Optional[List[SlideChannel]] = Field(None, description="List of channels")
    channel_depth: Optional[int] = Field(8, description="Color depth (bitness) of each channel")
    extent: SlideExtent = Field(..., description="Image extent (finest level, level=0)")
    num_levels: int = Field(..., description="Number of levels in image pyramid")
    pixel_size_nm: SlidePixelSizeNm = Field(..., description="Pixel size in nm  (finest level, level=0)")
    tile_extent: SlideExtent = Field(..., description="Tile extent")
    levels: List[SlideLevel]
    format: str = Field(None, description="Slide format identifier")
    raw_download: bool = Field(False, description="Flag indicating if the raw slide can be downloaded")
