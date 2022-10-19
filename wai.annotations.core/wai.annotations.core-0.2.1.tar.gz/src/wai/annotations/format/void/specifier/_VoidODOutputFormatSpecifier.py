from typing import Type

from ....core.domain import DomainSpecifier

from ._VoidOutputFormatSpecifier import VoidOutputFormatSpecifier


class VoidODOutputFormatSpecifier(VoidOutputFormatSpecifier):
    """
    Specifier for the void-writer in the image-object-detection domain.
    """
    @classmethod
    def description(cls) -> str:
        return "Consumes object detection instances without writing them."

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
