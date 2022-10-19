from enum import Enum


class ClusterStateType(str, Enum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATION_FAILED = "CREATION_FAILED"
    DELETED = "DELETED"
    LOCKED = "LOCKED"

    def __str__(self) -> str:
        return str(self.value)
