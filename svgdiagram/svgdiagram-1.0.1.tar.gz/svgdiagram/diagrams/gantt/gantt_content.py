from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from .swimlane import Swimlane
from .dependency import Dependency


class GanttContent(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    swimlanes: List[Swimlane] = Field(default_factory=list)
    dependencies: List[Dependency] = Field(default_factory=list)

    def iter_all_swimlane_dates(self):
        for swimlane in self.swimlanes:
            for milestone in swimlane.milestones:
                yield milestone.due_date
            for task in swimlane.tasks:
                yield task.start_date
                yield task.end_date


class GanttGroup(BaseModel):
    group_id: Optional[str]
    swimlane_order: Optional[List[str]]
    swimlanes: List[Swimlane] = Field(default_factory=list)
    dependencies: List[Dependency] = Field(default_factory=list)
