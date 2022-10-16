from typing import Any, Optional
from pydantic import Field

from wepipe.integrate.postprocessor.inference_aggregator import (
    InferenceAggregator,
    InferenceAggregatorConfig,
)
from wepipe.integrate.preprocessor.text_splitter import TextSplitter, TextSplitterConfig
from wepipe.core.workflow.base_store import BaseStore
from wepipe.pipeline.base_pipeline import BasePipelineConfig, BasePipeline

MAX_LENGTH: int = 512
DEFAULT_BATCH_SIZE_GPU: int = 64
DEFAULT_BATCH_SIZE_CPU: int = 4


class HuggingfacePipelineConfig(BasePipelineConfig):
    TYPE: str = "Huggingface"
    use_splitter_and_aggregator: Optional[bool] = False
    splitter_config: Optional[TextSplitterConfig]
    aggregator_config: Optional[InferenceAggregatorConfig]

    def __init__(self, **data: Any):
        super().__init__(**data)

        if self.use_splitter_and_aggregator and not self.splitter_config and not self.aggregator_config:
            raise AttributeError("Need splitter_config and aggregator_config if enabling use_splitter_and_aggregator "
                                 "option")

    class Config:
        arbitrary_types_allowed = True


class HuggingfacePipeline(BasePipeline):
    TYPE: str = "Huggingface"
    batch_size: int = -1
    splitter: TextSplitter = Field(TextSplitter())
    aggregator: InferenceAggregator = Field(InferenceAggregator())

    """
        auto: choose gpu if present else use cpu
        cpu: use cpu
        cuda:{id} - cuda device id
    """

    def __init__(self, **data: Any):
        super().__init__(**data)
