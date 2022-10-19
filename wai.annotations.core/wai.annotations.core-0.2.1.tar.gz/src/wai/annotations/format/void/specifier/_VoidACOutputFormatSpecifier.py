from typing import Type

from ....core.domain import DomainSpecifier

from ._VoidOutputFormatSpecifier import VoidOutputFormatSpecifier


class VoidACOutputFormatSpecifier(VoidOutputFormatSpecifier):
    """
    Specifier for the void-writer in the audio classification.
    """
    @classmethod
    def description(cls) -> str:
        return "Consumes audio classification instances without writing them."

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.audio.classification import AudioClassificationDomainSpecifier
        return AudioClassificationDomainSpecifier
