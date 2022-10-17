from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List
from dataclasses_json import DataClassJsonMixin, Undefined, config, dataclass_json, CatchAll


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class EventMetaData:
    event_id: str
    event_type: str
    created_at: str
    cloud_id: str
    folder_id: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class TriggerMessage:
    event_metadata: EventMetaData
    details: Dict[str, Any]

    def is_timer(self) -> bool:
        return self.event_metadata.event_type == "yandex.cloud.events.serverless.triggers.TimerMessage"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Event(DataClassJsonMixin):
    http_method: str = field(metadata=config(field_name="httpMethod"))
    headers: Dict[str, Any]
    url: str
    params: Dict[str, Any]
    multi_value_params: Dict[str, Any] = field(metadata=config(field_name="multiValueParams"))
    query_string_parameters: Dict[str, Any] = field(metadata=config(field_name="queryStringParameters"))
    multi_value_query_string_parameters: Dict[str, Any] = field(metadata=config(field_name="multiValueQueryStringParameters"))
    request_context: Dict[str, Any] = field(metadata=config(field_name="requestContext"))
    is_base64_encoded: bool = field(metadata=config(field_name="isBase64Encoded"))

    body: Optional[str] = None
    messages: Optional[List[TriggerMessage]] = None

