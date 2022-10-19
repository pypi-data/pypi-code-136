from typing import Type, Tuple

from ....core.component import ProcessorComponent
from ....core.domain import DomainSpecifier
from ....core.specifier import ProcessorStageSpecifier


class RenameISPSpecifier(ProcessorStageSpecifier):
    """
    ISP that renames files.
    """
    @classmethod
    def description(cls) -> str:
        return "ISP that renames files."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        # works in any domain
        return input_domain

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from ...rename.component import Rename
        return Rename,
