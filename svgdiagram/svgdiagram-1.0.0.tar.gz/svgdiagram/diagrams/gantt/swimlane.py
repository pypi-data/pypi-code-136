from pydantic import BaseModel, Field
from .task import Task
from .milestone import Milestone
from typing import List


class Swimlane(BaseModel):
    name: str
    tasks: List[Task] = Field(default_factory=list)
    milestones: List[Milestone] = Field(default_factory=list)
