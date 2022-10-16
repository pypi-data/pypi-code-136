import logging
from typing import Any, Dict, List, Optional, Tuple, Type, Iterator, Union
from pydantic import PrivateAttr
from transformers import (
    AutoModelForTokenClassification,
    AutoTokenizer,
    Pipeline,
    pipeline,
)
from wepipe.pipeline.huggingface import (
    HuggingfacePipeline,
    HuggingfacePipelineConfig,
    MAX_LENGTH,
)
from wepipe.core.payload import BasePayload, TextPayload

logger = logging.getLogger(__name__)


class TransformersNERPipeline(HuggingfacePipeline):
    _pipeline: Pipeline = PrivateAttr()
    _max_length: int = PrivateAttr()
    TYPE: str = "NER"
    model_name_or_path: str
    tokenizer_name: Optional[str] = None
    grouped_entities: Optional[bool] = True

    def __init__(self, **data: Any):
        super().__init__(**data)

        model = AutoModelForTokenClassification.from_pretrained(self.model_name_or_path)
        tokenizer = AutoTokenizer.from_pretrained(
            self.tokenizer_name if self.tokenizer_name else self.model_name_or_path,
            use_fast=True,
        )

        self._pipeline = pipeline(
            "ner",
            model=model,
            tokenizer=tokenizer,
            grouped_entities=self.grouped_entities,
            device=self._device_id,
        )

        if hasattr(self._pipeline.model.config, "max_position_embeddings"):
            self._max_length = self._pipeline.model.config.max_position_embeddings
        else:
            self._max_length = MAX_LENGTH

    def _prediction_from_model(self, texts: List[str]) -> List[List[Dict[str, float]]]:
        prediction = self._pipeline(texts)
        return (
            prediction
            if len(prediction) and isinstance(prediction[0], list)
            else [prediction]
        )

    def pipe_input(
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: Optional[HuggingfacePipelineConfig] = None,
        **kwargs,
    ) -> List[TextPayload]:
        pipeline_output: List[TextPayload] = []

        for batch_responses in self.batchify(source_response_list, self.batch_size):
            texts = [
                source_response.processed_text[: self._max_length]
                for source_response in batch_responses
            ]
            batch_predictions = self._prediction_from_model(texts)

            for prediction, source_response in zip(batch_predictions, batch_responses):
                segmented_data = {"ner_data": prediction}
                if source_response.segmented_data:
                    segmented_data = {
                        **segmented_data,
                        **source_response.segmented_data,
                    }

                pipeline_output.append(
                    TextPayload(
                        source_name=source_response.source_name,
                        raw=source_response.raw,
                        processed_text=source_response.processed_text,
                        segmented_data=segmented_data,                        
                    )
                )
        return pipeline_output
