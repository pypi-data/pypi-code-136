# pyre-strict
# misc utility functions...

import json
from typing import (
    Dict,
    List,
    Any,
)

__all__: List[str] = []


def export(obj) -> str:  # pyre-ignore
    __all__.append(obj.__name__)
    return obj


@export
class StructuredLogMessage:
    message: str
    kwargs: Dict[str, Any]

    def __init__(self, _message: str, **kwargs) -> None:
        self.message = _message
        self.kwargs = kwargs

    def __str__(self) -> str:
        return (
            f"{self.message} :: {', '.join(k + ': ' + json.dumps(v) for k, v in self.kwargs.items())}"
        )
