from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime, date


class Milestone(BaseModel):
    name: str
    due_date: Union[datetime, date]
    done: Optional[str] = False
    id: Optional[str] = None
