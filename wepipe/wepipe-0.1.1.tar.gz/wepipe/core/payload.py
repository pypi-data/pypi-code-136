from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from wepipe.integrate.utils import flatten_dict


class BasePayload(BaseModel):
    source_name: Optional[str] = "Undefined"
    raw: Dict[str, Any] = Field({})
    
    def to_dict(self):
        return self.__dict__
    
    class Config:
        arbitrary_types_allowed = True


class RecordPayload(BasePayload):
    processed_text: Optional[str]
    segmented_data: Optional[Dict[str, Any]] = Field({})

    def to_flatten(self):
        return flatten_dict(self.__dict__)
        
    class Config:
        arbitrary_types_allowed = True


class TextPayload(BasePayload):
    processed_text: str
    segmented_data: Dict[str, Any] = Field({})

    def is_contains_classification_payload(self) -> bool:
        if self.segmented_data:
            if "classifier_data" in self.segmented_data:
                return True
        return False

    class Config:
        arbitrary_types_allowed = True


class PlotPayload(BasePayload):
    raw: Optional[str] = "Undefined"
    width: int = 600
    height: int = 300
    plot: Any

    class Config:
        arbitrary_types_allowed = True
