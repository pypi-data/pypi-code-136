from datetime import datetime
from typing import Any, Dict, Optional

from cilroy.models import SerializableModel


class FaceParams(SerializableModel):
    host: str = "localhost"
    port: int = 10000


class ModuleParams(SerializableModel):
    host: str = "localhost"
    port: int = 11000


class OfflineParams(SerializableModel):
    scrap_before: Optional[datetime] = None
    scrap_after: Optional[datetime] = None
    scrap_limit: Optional[int] = None
    max_epochs: Optional[int] = None
    batch_size: Optional[int] = None


class OnlineParams(SerializableModel):
    post_scheduler_type: str = "interval"
    post_schedulers_params: Dict[str, Dict[str, Any]] = {}
    score_scheduler_type: str = "interval"
    score_schedulers_params: Dict[str, Dict[str, Any]] = {}
    iterations: int = 1
    batch_size: Optional[int] = None


class FeedParams(SerializableModel):
    length: int = 100


class Params(SerializableModel):
    face: FaceParams = FaceParams()
    module: ModuleParams = ModuleParams()
    offline: OfflineParams = OfflineParams()
    online: OnlineParams = OnlineParams()
    feed: FeedParams = FeedParams()
