from typing import Optional, Sequence, Union

from pydantic import BaseModel, validator

from .docker import Container
from .systemd import Timer


class ScheduledTask(BaseModel):
    task_name: str
    container: Container
    start_timer: Union[Timer, Sequence[Timer]]
    stop_timer: Optional[Union[Timer, Sequence[Timer]]] = None

    @validator("start_timer", "stop_timer")
    def check_iterable(cls, v):
        if v is not None and not isinstance(v, (list, tuple, set)):
            return [v]
        return v
