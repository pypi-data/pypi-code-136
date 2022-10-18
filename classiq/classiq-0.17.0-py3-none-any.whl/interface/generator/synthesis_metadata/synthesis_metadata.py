from typing import Optional

import pydantic

from classiq.interface.generator.generation_metadata import GenerationMetadata
from classiq.interface.generator.synthesis_metrics import SynthesisMetrics


class SynthesisMetadata(pydantic.BaseModel):
    execution_metadata: Optional[GenerationMetadata]
    synthesis_metrics: Optional[SynthesisMetrics]
