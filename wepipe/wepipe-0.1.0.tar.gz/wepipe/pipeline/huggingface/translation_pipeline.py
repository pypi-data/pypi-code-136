from typing import Any, List, Optional, Type, Iterator, Union
from pydantic import PrivateAttr
from transformers import pipeline, Pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

from wepipe.pipeline.huggingface import (
    HuggingfacePipeline,
    HuggingfacePipelineConfig,
    MAX_LENGTH,
)
from wepipe.core.payload import BasePayload, TextPayload


class TranslationPipeline(HuggingfacePipeline):
    _pipeline: Pipeline = PrivateAttr()
    _max_length: int = PrivateAttr()
    TYPE: str = "Translation"
    model_name_or_path: str

    def __init__(self, **data: Any):
        super().__init__(**data)
        tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name_or_path)
        self._pipeline = pipeline(
            "translation", model=model, tokenizer=tokenizer, device=self._device_id
        )
        if hasattr(self._pipeline.model.config, "max_position_embeddings"):
            self._max_length = self._pipeline.model.config.max_position_embeddings
        else:
            self._max_length = MAX_LENGTH

    def pipe_input(
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: Optional[HuggingfacePipelineConfig] = None,
        **kwargs,
    ) -> List[TextPayload]:

        pipeline_output = []

        for batch_responses in self.batchify(source_response_list, self.batch_size):
            texts = [
                source_response.processed_text[: self._max_length]
                for source_response in batch_responses
            ]

            batch_predictions = self._pipeline(texts)

            for prediction, source_response in zip(batch_predictions, batch_responses):
                segmented_data = {
                    "translation_data": {
                        "original_text": source_response.processed_text
                    }
                }
                if source_response.segmented_data:
                    segmented_data = {
                        **segmented_data,
                        **source_response.segmented_data,
                    }

                pipeline_output.append(
                    TextPayload(
                        source_name=source_response.source_name,
                        raw=source_response.raw,
                        processed_text=prediction["translation_text"],
                        segmented_data=segmented_data,                            
                    )
                )

        return pipeline_output
