from datetime import datetime
from enum import Enum
from typing import Any, BinaryIO, Dict, List, Optional

from typing_extensions import NotRequired, TypedDict

__all__ = [
    "Project",
    "JobStatus",
    "Job",
    "JobWithUrl",
    "JobInput",
    "JobWithResults",
]


class Project(TypedDict):
    id: int
    display_name: str


class JobStatus(str, Enum):
    """
    Attributes:
        PROCESSING (str): The document is still processing and does not have results yet.
        PROCESSED (str): The document has been processed and results are available.
        PENDING_REVIEW (str): The document is pending review. The returned job should include a 'content URL'
            linking to the document in the IDP UI where the user can review it.
        ERROR (str): The job has errored for some reason.
        DELETED (str): The job has been deleted.
    """

    PROCESSING = "Processing"
    PROCESSED = "Processed"
    PENDING_REVIEW = "Pending review"
    ERROR = "Error"
    DELETED = "Deleted"


class Job(TypedDict):
    uuid: str
    project_id: int
    status: JobStatus
    created_at: datetime
    processed_at: NotRequired[datetime]
    inputs: List[Dict[str, Any]]


class JobWithUrl(Job):
    content_url: Optional[str]


class JobWithResults(JobWithUrl):
    results: List[Dict[str, Any]]


class JobInput(TypedDict):
    document: BinaryIO
