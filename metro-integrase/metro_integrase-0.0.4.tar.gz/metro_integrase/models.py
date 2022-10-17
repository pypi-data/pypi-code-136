import datetime
import enum
import uuid
from pydantic import BaseModel
from typing import Optional, List as ListT

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
    description: Optional[str] = None
    domain: Optional[str] = None
    state: ListState
    icon: Optional[str] = None


# https://github.com/MetroReviews/backend/blob/74c902cc8a10e84796ad779228ea5417fe6ba087/brc/app.py#L117
class BotPost(BaseModel):
    bot_id: str
    banner: Optional[str] = None
    description: str 
    long_description: str
    website: Optional[str] = None
    invite: Optional[str] = None
    owner: str
    extra_owners: ListT[str] = []
    support: Optional[str] = None
    donate: Optional[str] = None
    library: Optional[str] = None
    nsfw: Optional[bool] = False
    prefix: Optional[str] = None
    tags: Optional[ListT[str]] = None
    review_note: Optional[str] = None
    cross_add: Optional[bool] = True


class Bot(BotPost):
    state: State
    list_source: uuid.UUID
    added_at: datetime.datetime
    reviewer: Optional[str] = None
    invite_link: Optional[str] = None
    username: Optional[str] = "Unknown"

class ListUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    domain: Optional[str] = None
    claim_bot_api: Optional[str] = None
    unclaim_bot_api: Optional[str] = None
    approve_bot_api: Optional[str] = None
    deny_bot_api: Optional[str] = None
    reset_secret_key: bool = False
    icon: Optional[str] = None

# https://github.com/MetroReviews/backend/blob/main/brc/app.py#L247
class Action(BaseModel):
    id: int
    bot_id: str
    action: ActionEnum
    reason: str
    reviewer: str 
    action_time: datetime.datetime
    list_source: uuid.UUID
