from abc import abstractmethod
from typing import Any, Dict, List, Optional, Type

from pydantic import Field, BaseSettings

from wepipe.core.payload import BasePayload, TextPayload
from wepipe.core.workflow.base_store import BaseStore


class Convertor(BaseSettings):
    def convert(
        self,
        pipeline_response: Type[BasePayload],
        base_payload: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> dict:
        base_payload = base_payload or dict()
        return (
            {**base_payload, **pipeline_response.to_dict()}
            if base_payload is not None
            else pipeline_response.to_dict()
        )

    class Config:
        arbitrary_types_allowed = True


class BaseDestinationConfig(BaseSettings):
    TYPE: str = "Base"

    @classmethod
    def from_dict(cls, config: Dict[str, Any]):
        pass

    class Config:
        arbitrary_types_allowed = True


class BaseDestination(BaseSettings):
    convertor: Convertor = Field(Convertor())
    store: Optional[BaseStore] = None

    @abstractmethod
    def send_data(
        self, pipeline_responses: List[Type[BasePayload]], config: BaseDestinationConfig, **kwargs
    ):
        pass

    class Config:
        arbitrary_types_allowed = True
