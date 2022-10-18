from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID

from pydantic import BaseModel


class PostData(BaseModel):
    id: UUID
    url: Optional[str]
    content: Dict[str, Any]
    created_at: datetime
