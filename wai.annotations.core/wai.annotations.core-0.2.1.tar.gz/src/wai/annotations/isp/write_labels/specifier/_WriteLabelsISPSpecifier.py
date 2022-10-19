from typing import Type, Tuple

from ....core.component import ProcessorComponent
from ....core.domain import DomainSpecifier
from ....core.specifier import ProcessorStageSpecifier


class WriteLabelsISPSpecifier(ProcessorStageSpecifier):
    """
    Specifier for the write-labels inline stream-processor.
    """
    @classmethod
    def description(cls) -> str:
        return "ISP which gathers labels and writes them to disk"

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from wai.common.adams.imaging.locateobjects import LocatedObjects
        from ....domain.classification import Classification
        from ....domain.image.segmentation import ImageSegmentationAnnotation

        if issubclass(input_domain.annotations_type(), (LocatedObjects, Classification, ImageSegmentationAnnotation)):
            return input_domain
        else:
            raise Exception(f"Unsupported annotation-type {input_domain.annotations_type().__name__}")

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from ..component import WriteLabels
        return WriteLabels,
