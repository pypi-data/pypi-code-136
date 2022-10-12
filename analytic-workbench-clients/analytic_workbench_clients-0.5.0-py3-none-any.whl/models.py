import enum
import uuid
import datetime
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, Field, validator


class State(str, enum.Enum):
    RETRY = "RETRY"
    PREPARING = "PREPARING"
    PENDING = "PENDING"
    WORKING = "WORKING"
    PAWING = "PAWING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REVOKED = "REVOKED"


class SourceType(str, enum.Enum):
    """Used for object creation in `payload.sourceFileName.sourceType`"""

    ADT = "ADT"
    URL = "URL"
    FILEPATH = "FILEPATH"
    FILESTORE = "FILESTORE"


class JobCreateModel(BaseModel):
    userId: str
    payload: Dict[str, Any]
    webData: Dict[str, Any] = Field(default_factory=dict)
    datasetReleaseId: Optional[str] = None
    datasetSchemaId: Optional[str] = None
    projectId: Optional[str] = None
    publish: bool = False

    @validator("userId", "projectId")
    def _validate_uuid(cls, value: Any) -> Union[str, None]:
        if value is not None:
            uuid.UUID(value)
            return value
        return None


class JobSubmitModel(BaseModel):
    executionSlug: Optional[str] = Field(default=None, alias="execution_slug")


class JobModel(JobCreateModel):
    id: Optional[str] = None
    groupId: Optional[str] = None
    errors: List[Any] = Field(default_factory=list)
    created: Optional[datetime.datetime] = None
    modified: Optional[datetime.datetime] = None
    state: State = Field(State.PENDING)
    status: Dict[str, Any] = Field(default_factory=dict)
    deleted: bool = False
    storeTTL: Optional[int] = None
    methodName: Optional[str] = None
    publications: List[Dict[str, Any]] = Field(default_factory=list)


class TaskStatusModel(BaseModel):
    state: State
    status: Dict[str, Any] = Field(default_factory=dict)


class JobResultPath(BaseModel):
    name: str
    size: int
    mimetype: str


class CacheMemberModel(BaseModel):
    id: str = Field(..., alias="guid")
    filename: str
    mimetype: str
    thumbnail: Optional[Dict[str, str]] = None

    @validator("id")
    def _validate_uuid(cls, value: Any) -> Union[str, None]:
        if value is not None:
            uuid.UUID(value)
            return value
        return None
