from pydantic import BaseModel
from typing import Optional


class Dependency(BaseModel):
    source_id: str
    target_id: str
    name: Optional[str]
