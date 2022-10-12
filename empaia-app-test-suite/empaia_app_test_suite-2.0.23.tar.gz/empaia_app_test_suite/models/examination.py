from enum import Enum
from typing import List, Optional

from pydantic import UUID4, Field

from .commons import Id, ItemCount, RestrictedBaseModel, Timestamp


class ExaminationState(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class PutExaminationState(RestrictedBaseModel):
    state: ExaminationState = Field(example=ExaminationState.CLOSED, description="Examination state")


class ExaminationCreatorType(str, Enum):
    USER = "USER"


class PostExamination(RestrictedBaseModel):
    case_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Case ID")
    creator_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Creator ID")
    creator_type: ExaminationCreatorType = Field(example=ExaminationCreatorType.USER, description="Creator Type")


class ExaminationApp(RestrictedBaseModel):
    id: Id = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="App ID")
    jobs: List[Id] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="Jobs in this examination",
    )


class Examination(PostExamination):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Examination ID")
    state: ExaminationState = Field(example=ExaminationState.OPEN, description="Examination state")
    created_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")
    updated_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")
    apps: List[ExaminationApp] = Field(
        example=[
            {"id": "b10648a7-340d-43fc-a2d9-4d91cc86f33f", "jobs": ["32520b51-b860-4938-888b-da367ff7b964"]},
        ],
        description="Apps in this examination",
    )


class ExaminationList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=12345, description="Count of items")
    items: List[Examination]


class ExaminationQuery(RestrictedBaseModel):
    cases: Optional[List[Id]] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="Case IDs",
    )
    creator_types: Optional[List[ExaminationCreatorType]] = Field(
        example=[ExaminationCreatorType.USER], description="Examination Creator Type"
    )
    creators: Optional[List[Id]] = Field(
        example=[
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
            "b10648a7-340d-43fc-a2d9-4d91cc86f33f",
        ],
        description="Creator IDs",
    )


class PostScope(RestrictedBaseModel):
    examination_id: UUID4 = Field(example="6b30c43c-eb97-448a-9f8e-15fc0da569f0", description="Examination ID")
    app_id: Id = Field(example="839ba097-f265-4ba0-9412-4b93eea0e6e2", description="App ID")
    user_id: Id = Field(example="02621dcb-e208-449f-9d44-868d092223cf", description="User ID")


class Scope(PostScope):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Scope ID")
    created_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")


class ScopeToken(RestrictedBaseModel):
    """Wrapper for Scope-ID and Access Token, returned on Scope creation and access."""

    access_token: str = Field(
        example="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3NTYzMDAxOC03ZjhmLTQ3YjgtODZmNC0wMTliODhjNjZhMTEiLCJle"
        "HAiOjE2MjQzNTkwNTZ9.CnT0NYwVzyNl05Jp0z4W-qDqKjolQHZxmT9i7SYyBYG6D-5K7jLxm3l4lBLp30rnjYOiZm0TtvskK1lYDh"
        "gKNyXnEhB_O7f6DQuTd9tn8yv8XnK19pj6g8nubFfBho9lYhComb6a3XX3vqLK5pnaXuhC9tFdzsnLkQPoIi2DZ8E",
        description="AccessToken based on JSON Web Tokens. It can be created and passed around to validate requests",
    )
