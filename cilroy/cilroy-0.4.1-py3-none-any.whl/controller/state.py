import asyncio
from asyncio import Lock
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, MutableMapping, Optional, Tuple
from uuid import UUID

from kilroy_face_client_py_sdk import FaceService
from kilroy_module_client_py_sdk import MetricData, ModuleService
from kilroy_server_py_utils import Observable

from cilroy.post import PostData
from cilroy.posting import PostScheduler
from cilroy.scoring import ScoreScheduler
from cilroy.status import TrainingStatus


@dataclass
class FaceState:
    service: FaceService


@dataclass
class ModuleState:
    service: ModuleService
    archived_metrics: List[MetricData]
    metrics_stream: Observable[MetricData]
    metrics_task: asyncio.Task


@dataclass
class OfflineState:
    scrap_before: Optional[datetime]
    scrap_after: Optional[datetime]
    scrap_limit: Optional[int]
    max_epochs: Optional[int]
    batch_size: Optional[int]
    posts_cache: MutableMapping[str, Tuple[Dict, float]]


@dataclass
class OnlineState:
    ids_cache: MutableMapping[UUID, UUID]
    post_scheduler: PostScheduler
    post_schedulers_params: Dict[str, Dict[str, Any]]
    score_scheduler: ScoreScheduler
    score_schedulers_params: Dict[str, Dict[str, Any]]
    iterations: int
    batch_size: Optional[int]
    lock: Lock


@dataclass
class FeedState:
    feed: List[PostData]
    length: int
    stream: Observable[PostData]


@dataclass
class State:
    face: FaceState
    module: ModuleState
    offline: OfflineState
    online: OnlineState
    training_task: Optional[asyncio.Task]
    training_status: Observable[TrainingStatus]
    feed: FeedState
