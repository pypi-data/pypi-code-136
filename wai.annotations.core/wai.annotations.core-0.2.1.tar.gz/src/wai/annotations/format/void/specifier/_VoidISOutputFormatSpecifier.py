from typing import Type

from ....core.domain import DomainSpecifier

from ._VoidOutputFormatSpecifier import VoidOutputFormatSpecifier


class VoidISOutputFormatSpecifier(VoidOutputFormatSpecifier):
    """
    Specifier for the void-writer in the image-segmentation domain.
    """
    @classmethod
    def description(cls) -> str:
        return "Consumes image segmentation instances without writing them."

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.segmentation import ImageSegmentationDomainSpecifier
        return ImageSegmentationDomainSpecifier
