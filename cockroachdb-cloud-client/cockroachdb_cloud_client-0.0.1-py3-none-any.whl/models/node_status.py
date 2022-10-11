from enum import Enum


class NodeStatus(str, Enum):
    LIVE = "LIVE"
    NOT_READY = "NOT_READY"

    def __str__(self) -> str:
        return str(self.value)
