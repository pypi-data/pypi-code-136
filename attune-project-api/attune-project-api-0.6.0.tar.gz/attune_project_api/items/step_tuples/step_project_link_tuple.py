"""
*
 *  Copyright ServerTribe HQ Pty Ltd 2021
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by
 *  ServerTribe HQ Pty Ltd
 *
"""
from typing import List
from typing import Optional

from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from . import addStepDeclarative
from .step_tuple import StepTupleTypeEnum
from ... import ParameterTuple
from ... import StepTuple
from ...ObjectStorageContext import ObjectStorageContext
from ...RelationField import RelationField
from ...StorageTuple import ItemStorageGroupEnum
from ...StorageTuple import StorageMemberTuple


@addTupleType
class ParameterMappingTuple(StorageMemberTuple):
    """Parameter Mapping Tuple

    Mapping between a parameter in a linked project to a parameter or a literal
    text value in the linking project. At least one of `textValue` or
    `sourceParameterKey` must be set.

    """

    __tupleType__ = "com.servertribe.attune.tuples.ParameterMappingTuple"

    # Literal value for text parameters
    textValue: Optional[str] = TupleField(None)

    # Key of the parameter or literal value in the linking project
    sourceParameterKey: Optional[str] = TupleField("")
    sourceParameter: ParameterTuple = RelationField(
        ForeignClass=ParameterTuple,
        referenceKeyFieldName="sourceParameterKey",
        cascadeOnDelete=False,
        cascadeOnUpdate=False,
    )

    # Key of the parameter in the "linked" to projects blueprint
    targetParameterReference: str = TupleField()

    parameterType: str = TupleField(ParameterTuple.TEXT)


@ObjectStorageContext.registerItemClass
@addStepDeclarative("Project Link")
@addTupleType
class StepProjectLinkTuple(StepTuple):
    __tupleType__ = StepTupleTypeEnum.PROJECT_LINK.value

    projectKey: str = TupleField()
    blueprintKey: str = TupleField()
    pullUrl: str = TupleField()

    parameterMap: List[ParameterMappingTuple] = TupleField([])

    def parameters(self) -> list["ParameterTuple"]:
        return [mapping.sourceParameter for mapping in self.parameterMap]

    def scriptReferences(self) -> list[str]:
        return []

    def verifyParameterMapping(
        self, targetContext: ObjectStorageContext
    ) -> list[int]:
        targetParams = targetContext.getItemMap(ItemStorageGroupEnum.Parameter)
        invalidIndices = set()

        for i, mapping in enumerate(self.parameterMap):
            if mapping.targetParameterReference not in targetParams:
                invalidIndices.add(i)

            if mapping.parameterType != mapping.sourceParameter.type:
                invalidIndices.add(i)

        return list(invalidIndices)
