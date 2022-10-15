import logging
from typing import Any, List, Optional, Type, Iterator, Union

from wepipe.core.payload import BasePayload, TextPayload
from wepipe.pipeline.huggingface.classification_pipeline import (
    ClassificationPipelineConfig,
    ZeroShotClassificationPipeline,
)

logger = logging.getLogger(__name__)


class TransformersSentimentPipelineConfig(ClassificationPipelineConfig):
    TYPE: str = "Sentiment"
    labels: List[str] = ["positive", "negative"]
    multi_class_classification: bool = False


class TransformersSentimentPipeline(ZeroShotClassificationPipeline):
    def pipe_input(  # type: ignore[override]
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: Optional[TransformersSentimentPipelineConfig],
        **kwargs,
    ) -> List[TextPayload]:
        return super().pipe_input(
            source_response_list=source_response_list,
            pipeline_config=pipeline_config,
            add_positive_negative_labels=True,
            **kwargs,
        )
