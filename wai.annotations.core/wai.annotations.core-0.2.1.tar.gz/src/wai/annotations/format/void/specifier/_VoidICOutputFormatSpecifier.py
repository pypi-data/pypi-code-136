from typing import Type

from ....core.domain import DomainSpecifier

from ._VoidOutputFormatSpecifier import VoidOutputFormatSpecifier


class VoidICOutputFormatSpecifier(VoidOutputFormatSpecifier):
    """
    Specifier for the void-writer in the image-classification domain.
    """
    @classmethod
    def description(cls) -> str:
        return "Consumes image classification instances without writing them."

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.classification import ImageClassificationDomainSpecifier
        return ImageClassificationDomainSpecifier
