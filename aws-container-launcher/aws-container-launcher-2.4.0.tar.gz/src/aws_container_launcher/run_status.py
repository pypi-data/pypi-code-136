from enum import Enum


class RunStatus(Enum):
    INITIALIZING = 1
    IN_PROGRESS = 2
    FAILED = 3
    COMPLETED = 4
    UNKNOWN = 6
