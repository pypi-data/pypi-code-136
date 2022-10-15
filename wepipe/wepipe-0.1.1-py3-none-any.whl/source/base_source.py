from abc import abstractmethod
from typing import List, Dict, Optional, Any, Iterator

from pydantic import BaseSettings

from wepipe.core.payload import BasePayload
from wepipe.core.workflow.base_store import BaseStore


class BaseSourceConfig(BaseSettings):
    TYPE: str = "Base"

    class Config:
        arbitrary_types_allowed = True


class BaseSource(BaseSettings):
    store: Optional[BaseStore] = None

    def spec(self, **kwargs) -> Dict[str, Any]:
        pass

    def check(self, config: BaseSourceConfig, **kwargs) -> Dict[str, Any]:
        pass

    def discover(self, config: BaseSourceConfig, **kwargs) -> Dict[str, Any]:
        pass    

    def read(self, config: BaseSourceConfig, **kwargs) -> Iterator[BasePayload]:
        pass
    
    @abstractmethod
    def load(self, config: BaseSourceConfig, **kwargs) -> List[BasePayload]:
        pass    

    class Config:
        arbitrary_types_allowed = True
