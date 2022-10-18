from typing import Union

import pydantic
from pydantic import BaseModel

from classiq.interface.generator.finance import FinanceMetadata, FinanceModelMetadata
from classiq.interface.generator.grover_operator import GroverMetadata

_INVALID_METADATA_ERROR_MSG = "Invalid metadata file."
ParamMetadataUnion = Union[GroverMetadata, FinanceMetadata, FinanceModelMetadata]


class GenerationMetadata(BaseModel):
    # Ideally, we would use a "__root__" attribute, but the typescript transpilation
    # does weird things when we use it.
    metadata: ParamMetadataUnion = pydantic.Field(..., discriminator="metadata_type")
