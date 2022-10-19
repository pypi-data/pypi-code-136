from typing import Type, Tuple

from ....core.component import ProcessorComponent
from ....core.domain import DomainSpecifier
from ....core.specifier import ProcessorStageSpecifier


class LabelPresentISPSpecifier(ProcessorStageSpecifier):
    """
    Specifies the labels-in-region ISP.
    """
    @classmethod
    def description(cls) -> str:
        return "Keeps or discards images depending on whether annotations with certain label(s) are present. " \
               "Checks can be further tightened by defining regions in the image that annotations must overlap with (or not overlap at all)."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from ....domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        if input_domain is ImageObjectDetectionDomainSpecifier:
            return ImageObjectDetectionDomainSpecifier
        else:
            raise Exception(
                f"LabelPresent only handles the "
                f"{ImageObjectDetectionDomainSpecifier.name()} domain"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from ...label_present.component import LabelPresent
        return LabelPresent,
