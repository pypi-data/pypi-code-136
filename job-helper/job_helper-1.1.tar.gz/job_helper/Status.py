from enum import Enum


class Status(Enum):
    QUEUED = "queued"
    IN_PROGRESS = "in-progress"
    FINISHED = "finished"
    FAILED = "failed"
