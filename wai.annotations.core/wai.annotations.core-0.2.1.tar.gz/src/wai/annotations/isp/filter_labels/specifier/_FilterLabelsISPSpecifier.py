from typing import Type, Tuple

from ....core.component import ProcessorComponent
from ....core.domain import DomainSpecifier
from ....core.specifier import ProcessorStageSpecifier


class FilterLabelsISPSpecifier(ProcessorStageSpecifier):
    """
    Specifies the filter-labels ISP.
    """
    @classmethod
    def description(cls) -> str:
        return "Filters detected objects down to those with specified labels or, "\
               "in case of image classification, removes the label if it doesn't match."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from ....domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        from ....domain.image.classification import ImageClassificationDomainSpecifier
        if input_domain is ImageObjectDetectionDomainSpecifier:
            return ImageObjectDetectionDomainSpecifier
        elif input_domain is ImageClassificationDomainSpecifier:
            return ImageClassificationDomainSpecifier
        else:
            raise Exception(
                f"FilterLabels only handles the "
                f"{ImageObjectDetectionDomainSpecifier.name()}, "
                f"{ImageClassificationDomainSpecifier.name()} domains"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from ...filter_labels.component import FilterLabels
        return FilterLabels,
