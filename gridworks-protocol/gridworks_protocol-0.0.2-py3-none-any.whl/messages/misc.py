from typing import Literal

from pydantic import BaseModel


class Ack(BaseModel):
    acks_message_id: str = ""
    type_name: Literal["gridworks.ack.000"] = "gridworks.ack.000"
