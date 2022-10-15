from typing import Any, List, Optional, Type, Union, Iterator
from wepipe.pipeline.base_pipeline import (
    BasePipeline,
    BasePipelineConfig,
)
from wepipe.core.payload import BasePayload


class DummyPipelineConfig(BasePipelineConfig):
    TYPE: str = "Dummy"
    dummy_data: Optional[Any] = None

    def __init__(self, **data: Any):
        super().__init__(**data)


class DummyPipeline(BasePipeline):
    def pipe_input(  # type: ignore[override]
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: Optional[DummyPipelineConfig] = None,
        **kwargs,
    ) -> List[Type[BasePayload]]:
        responses = []
        for source_response in source_response_list:
            responses.append(
                source_response
            )
        return responses