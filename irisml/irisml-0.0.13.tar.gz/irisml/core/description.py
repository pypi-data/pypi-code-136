import dataclasses
from typing import Any, Dict, List, Optional
import typing


@dataclasses.dataclass
class TaskDescription:
    task: str
    name: Optional[str] = None  # Optional name for the task. Must be unique in the job. This name will be used for OutputVariable names.
    inputs: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: typing.Dict):
        return cls(**data)


@dataclasses.dataclass
class JobDescription:
    tasks: List[TaskDescription]
    on_error: Optional[List[TaskDescription]]

    @classmethod
    def from_dict(cls, data: typing.Dict):
        c = {'tasks': [TaskDescription.from_dict(t) for t in data['tasks']],
             'on_error': data.get('on_error', None) and [TaskDescription.from_dict(t) for t in data.get('on_error')]}
        return cls(**c)
