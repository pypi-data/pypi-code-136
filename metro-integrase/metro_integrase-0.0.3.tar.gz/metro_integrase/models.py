import datetime
import enum
import uuid
from pydantic import BaseModel

# https://github.com/MetroReviews/backend/blob/74c902cc8a10e84796ad779228ea5417fe6ba087/brc/tables.py#L9
class ActionEnum(enum.IntEnum):
    """
Type of action
    """
    CLAIM = 0
    UNCLAIM = 1
    APPROVE = 2
    DENY = 3

class State(enum.IntEnum):
    """
Current bot state
    """
    PENDING = 0
    UNDER_REVIEW = 1
    APPROVED = 2
    DENIED = 3

class ListState(enum.IntEnum):
    """
A lists state
    """
    PENDING_API_SUPPORT = 0
    SUPPORTED = 1
    DEFUNCT = 2
    BLACKLISTED = 3
    UNCONFIRMED_ENROLLMENT = 4

# https://github.com/MetroReviews/backend/blob/64959ddaa0faecfc38007580cc1625412b9b5864/brc/app.py#L109
class List(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None = None
    domain: str | None = None
    state: ListState
    icon: str | None = None


# https://github.com/MetroReviews/backend/blob/74c902cc8a10e84796ad779228ea5417fe6ba087/brc/app.py#L117
class BotPost(BaseModel):
    bot_id: str
    banner: str | None = None
    description: str 
    long_description: str
    website: str | None = None
    invite: str | None = None
    owner: str
    extra_owners: list[str] | None = []
    support: str | None = None
    donate: str | None = None
    library: str | None = None
    nsfw: bool | None = False
    prefix: str | None = None
    tags: list[str] | None = None
    review_note: str | None = None
    cross_add: bool | None = True


class Bot(BotPost):
    state: State
    list_source: uuid.UUID
    added_at: datetime.datetime
    reviewer: str | None = None
    invite_link: str | None = None
    username: str | None = "Unknown"

class ListUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    domain: str | None = None
    claim_bot_api: str | None = None
    unclaim_bot_api: str | None = None
    approve_bot_api: str | None = None
    deny_bot_api: str | None = None
    reset_secret_key: bool = False
    icon: str | None = None

# https://github.com/MetroReviews/backend/blob/main/brc/app.py#L247
class Action(BaseModel):
    id: int
    bot_id: str
    action: ActionEnum
    reason: str
    reviewer: str 
    action_time: datetime.datetime
    list_source: uuid.UUID
