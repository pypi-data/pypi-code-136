from typing import Any, Optional
from pydantic import Field
from wepipe.core.workflow.base_store import BaseStore
from wepipe.pipeline.base_pipeline import BasePipelineConfig, BasePipeline


class AltairPipelineConfig(BasePipelineConfig):
    TYPE: str = "Altair"

    def __init__(self, **data: Any):
        super().__init__(**data)

    class Config:
        arbitrary_types_allowed = True


class AltairPipeline(BasePipeline):
    TYPE: str = "Altair"

    def __init__(self, **data: Any):
        super().__init__(**data)
