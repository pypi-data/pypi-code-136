import time
import uuid
from enum import Enum
from typing import Any
from typing import Generic
from typing import Literal
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.message import Message
from gwproto.message import as_enum


class EventBase(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    time_ns: int = Field(default_factory=time.time_ns)
    src: str = ""
    type_name: str = Field(const=True)


EventT = TypeVar("EventT", bound=EventBase)


class StartupEvent(EventBase):
    clean_shutdown: bool
    type_name: Literal["gridworks.event.startup.000"] = "gridworks.event.startup.000"


class ShutdownEvent(EventBase):
    reason: str
    type_name: Literal["gridworks.event.shutdown.000"] = "gridworks.event.shutdown.000"


class Problems(Enum):
    error = "error"
    warning = "warning"


class ProblemEvent(EventBase):
    problem_type: Problems
    summary: str
    details: str = ""
    type_name: Literal["gridworks.event.problem.000"] = "gridworks.event.problem.000"

    @validator("problem_type", pre=True)
    def problem_type_value(cls, v: Any) -> Optional[Problems]:
        return as_enum(v, Problems)


class CommEvent(EventBase):
    ...


class MQTTCommEvent(CommEvent):
    ...


class MQTTConnectFailedEvent(MQTTCommEvent):
    type_name: Literal[
        "gridworks.event.comm.mqtt.connect_failed.000"
    ] = "gridworks.event.comm.mqtt.connect_failed.000"


class MQTTDisconnectEvent(MQTTCommEvent):
    type_name: Literal[
        "gridworks.event.comm.mqtt.disconnect.000"
    ] = "gridworks.event.comm.mqtt.disconnect.000"


class MQTTFullySubscribedEvent(CommEvent):
    type_name: Literal[
        "gridworks.event.comm.mqtt.fully_subscribed.000"
    ] = "gridworks.event.comm.mqtt.fully_subscribed.000"


class EventMessage(Message[EventT], Generic[EventT]):
    ...
