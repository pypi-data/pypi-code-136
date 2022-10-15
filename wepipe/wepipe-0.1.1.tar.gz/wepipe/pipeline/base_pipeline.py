from abc import abstractmethod
from typing import Any, Iterator, Generator, List, Optional, Type, Union
from collections.abc import Iterable
from itertools import islice
from pydantic import BaseSettings, PrivateAttr

from wepipe.integrate import gpu_util
from wepipe.core.payload import BasePayload
from wepipe.core.workflow.base_store import BaseStore

MAX_LENGTH: int = 512
DEFAULT_BATCH_SIZE_GPU: int = 64
DEFAULT_BATCH_SIZE_CPU: int = 4


class BasePipelineConfig(BaseSettings):
    TYPE: str = "Base"

    def __init__(self, **data: Any):
        super().__init__(**data)

    class Config:
        arbitrary_types_allowed = True


class BasePipeline(BaseSettings):
    _device_id: int = PrivateAttr()
    TYPE: str = "Base"
    store: Optional[BaseStore] = None
    device: str = "auto"
    batch_size: int = -1

    """
        auto: choose gpu if present else use cpu
        cpu: use cpu
        cuda:{id} - cuda device id
    """

    def __init__(self, **data: Any):
        super().__init__(**data)

        self._device_id = gpu_util.get_device_id(self.device)
        if self.batch_size < 0:
            self.batch_size = (
                DEFAULT_BATCH_SIZE_CPU
                if self._device_id == 0
                else DEFAULT_BATCH_SIZE_GPU
            )

    @abstractmethod
    def pipe_input(
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: Optional[BasePipelineConfig] = None,
        **kwargs,
    ) -> List[Type[BasePayload]]:
        pass

    @staticmethod
    def batchify(
        payload_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        batch_size: int,
    ) -> Generator[List[Type[BasePayload]], None, None]:
        if isinstance(payload_list, Generator):
            while batch := list(islice(payload_list, batch_size)):
                yield batch 
        else:
            for index in range(0, len(payload_list), batch_size):
                batch = payload_list[index : index + batch_size]
                yield batch 

    class Config:
        arbitrary_types_allowed = True
