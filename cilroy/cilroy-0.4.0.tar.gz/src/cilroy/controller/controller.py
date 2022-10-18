import asyncio
import json
import logging
from abc import ABC, abstractmethod
from asyncio import Lock
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Dict,
    List,
    Mapping,
    Set,
    Tuple,
)
from uuid import UUID

from aiostream.aiter_utils import anext
from grpclib.client import Channel
from kilroy_face_client_py_sdk import FaceService
from kilroy_module_client_py_sdk import MetricConfig, MetricData, ModuleService
from kilroy_server_py_utils import (
    Configurable,
    JSONSchema,
    Observable,
    Parameter,
    ReadOnlyObservableWrapper,
    ReadableObservable,
    classproperty,
)

from cilroy.controller.parameters import (
    MaxOfflineEpochsParameter,
    OfflineBatchSizeParameter,
    OnlineBatchSizeParameter,
    OnlineIterationsParameter,
    PostSchedulerParameter,
    ScoreSchedulerParameter,
    ScrapAfterParameter,
    ScrapBeforeParameter,
    ScrapLimitParameter,
    FeedLengthParameter,
)
from cilroy.controller.params import (
    OfflineParams,
    OnlineParams,
    Params,
    FaceParams,
    ModuleParams,
    FeedParams,
)
from cilroy.controller.state import (
    OfflineState,
    OnlineState,
    State,
    FaceState,
    ModuleState,
    FeedState,
)
from cilroy.messages import Status
from cilroy.metadata import Metadata
from cilroy.post import PostData
from cilroy.posting import PostScheduler
from cilroy.scoring import ScoreScheduler
from cilroy.status import TrainingStatus
from cilroy.utils import CachingAsyncIterable, batches

logger = logging.getLogger(__name__)


class CilroyControllerBase(Configurable[State], ABC):
    @staticmethod
    async def _build_face_service(params: FaceParams) -> FaceService:
        return FaceService(Channel(params.host, params.port))

    @classmethod
    async def _build_face_state(cls, params: FaceParams) -> FaceState:
        return FaceState(
            service=await cls._build_face_service(params),
        )

    @staticmethod
    async def _build_module_service(params: ModuleParams) -> ModuleService:
        return ModuleService(Channel(params.host, params.port))

    async def _build_module_state(self, params: ModuleParams) -> ModuleState:
        return ModuleState(
            service=await self._build_module_service(params),
            archived_metrics=[],
            metrics_stream=await Observable.build(),
            metrics_task=asyncio.create_task(self._watch_metrics_task()),
        )

    @staticmethod
    async def _build_offline_state(params: OfflineParams) -> OfflineState:
        return OfflineState(
            max_epochs=params.max_epochs,
            batch_size=params.batch_size,
            scrap_limit=params.scrap_limit,
            scrap_before=params.scrap_before,
            scrap_after=params.scrap_after,
            posts_cache={},
        )

    @classmethod
    async def _build_post_scheduler(
        cls, params: OnlineParams
    ) -> PostScheduler:
        return await cls._build_categorizable(
            PostScheduler,
            params.post_scheduler_type,
            **params.post_schedulers_params.get(
                params.post_scheduler_type, {}
            ),
        )

    @classmethod
    async def _build_score_scheduler(
        cls, params: OnlineParams
    ) -> ScoreScheduler:
        return await cls._build_categorizable(
            ScoreScheduler,
            params.score_scheduler_type,
            **params.score_schedulers_params.get(
                params.score_scheduler_type, {}
            ),
        )

    @classmethod
    async def _build_online_state(cls, params: OnlineParams) -> OnlineState:
        return OnlineState(
            ids_cache={},
            post_scheduler=await cls._build_post_scheduler(params),
            post_schedulers_params=params.post_schedulers_params,
            score_scheduler=await cls._build_score_scheduler(params),
            score_schedulers_params=params.score_schedulers_params,
            iterations=params.iterations,
            batch_size=params.batch_size,
            lock=Lock(),
        )

    @staticmethod
    async def _build_training_status() -> Observable[TrainingStatus]:
        return await Observable.build(TrainingStatus.IDLE)

    @staticmethod
    async def _build_feed_state(params: FeedParams) -> FeedState:
        return FeedState(
            feed=[],
            length=params.length,
            stream=await Observable.build(),
        )

    async def _build_default_state(self) -> State:
        params = Params(**self._kwargs)
        return State(
            face=await self._build_face_state(params.face),
            module=await self._build_module_state(params.module),
            offline=await self._build_offline_state(params.offline),
            online=await self._build_online_state(params.online),
            training_task=None,
            training_status=await self._build_training_status(),
            feed=await self._build_feed_state(params.feed),
        )

    @staticmethod
    async def _save_state_dict(
        directory: Path, state_dict: Dict[str, Any]
    ) -> None:
        with open(directory / "state.json", "w") as f:
            json.dump(state_dict, f)

    @staticmethod
    async def _save_face_state(state: FaceState, directory: Path) -> None:
        pass

    @staticmethod
    async def _save_module_metrics(
        metrics: List[MetricData], directory: Path
    ) -> None:
        serialized = [json.loads(metric.json()) for metric in metrics]
        with open(directory / "metrics.json", "w") as f:
            json.dump([metric for metric in serialized], f)

    @classmethod
    async def _save_module_state(
        cls, state: ModuleState, directory: Path
    ) -> None:
        metrics_directory = directory / "metrics"
        metrics_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_module_metrics(
            state.archived_metrics, metrics_directory
        )

    @staticmethod
    async def _create_offline_state_dict(
        state: OfflineState,
    ) -> Dict[str, Any]:
        return {
            "max_epochs": state.max_epochs,
            "batch_size": state.batch_size,
            "scrap_limit": state.scrap_limit,
            "scrap_before": state.scrap_before.isoformat()
            if state.scrap_before is not None
            else None,
            "scrap_after": state.scrap_after.isoformat()
            if state.scrap_after is not None
            else None,
        }

    @classmethod
    async def _save_offline_state(
        cls, state: OfflineState, directory: Path
    ) -> None:
        state_dict = await cls._create_offline_state_dict(state)
        await cls._save_state_dict(directory, state_dict)

    @staticmethod
    async def _serialize_ids_cache(
        ids_cache: Mapping[UUID, UUID]
    ) -> Dict[str, str]:
        return {str(k): str(v) for k, v in ids_cache.items()}

    @staticmethod
    async def _deserialize_ids_cache(
        ids_cache: Mapping[str, str]
    ) -> Dict[UUID, UUID]:
        return {UUID(k): UUID(v) for k, v in ids_cache.items()}

    @classmethod
    async def _create_online_state_dict(
        cls,
        state: OnlineState,
    ) -> Dict[str, Any]:
        return {
            "ids_cache": await cls._serialize_ids_cache(state.ids_cache),
            "post_scheduler_type": state.post_scheduler.category,
            "post_schedulers_params": state.post_schedulers_params,
            "score_scheduler_type": state.score_scheduler.category,
            "score_schedulers_params": state.score_schedulers_params,
            "iterations": state.iterations,
            "batch_size": state.batch_size,
        }

    @staticmethod
    async def _save_post_scheduler(
        scheduler: PostScheduler, directory: Path
    ) -> None:
        if isinstance(scheduler, Configurable):
            await scheduler.save(directory)

    @staticmethod
    async def _save_score_scheduler(
        scheduler: ScoreScheduler, directory: Path
    ) -> None:
        if isinstance(scheduler, Configurable):
            await scheduler.save(directory)

    @classmethod
    async def _save_online_state(
        cls, state: OnlineState, directory: Path
    ) -> None:
        post_scheduler_dir = directory / "post_scheduler"
        post_scheduler_dir.mkdir(parents=True, exist_ok=True)
        await cls._save_post_scheduler(
            state.post_scheduler, post_scheduler_dir
        )

        score_scheduler_dir = directory / "score_scheduler"
        score_scheduler_dir.mkdir(parents=True, exist_ok=True)
        await cls._save_score_scheduler(
            state.score_scheduler, score_scheduler_dir
        )

        state_dict = await cls._create_online_state_dict(state)
        await cls._save_state_dict(directory, state_dict)

    @classmethod
    async def _save_feed_state(cls, state: FeedState, directory: Path) -> None:
        serialized_feed = [json.loads(post.json()) for post in state.feed]
        state_dict = {
            "feed": serialized_feed,
            "length": state.length,
        }
        await cls._save_state_dict(directory, state_dict)

    @classmethod
    async def _save_state(cls, state: State, directory: Path) -> None:
        face_directory = directory / "face"
        face_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_face_state(state.face, face_directory)

        module_directory = directory / "module"
        module_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_module_state(state.module, module_directory)

        offline_directory = directory / "offline"
        offline_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_offline_state(state.offline, offline_directory)

        online_directory = directory / "online"
        online_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_online_state(state.online, online_directory)

        feed_directory = directory / "feed"
        feed_directory.mkdir(parents=True, exist_ok=True)
        await cls._save_feed_state(state.feed, feed_directory)

    @staticmethod
    async def _load_state_dict(directory: Path) -> Dict[str, Any]:
        with open(directory / "state.json", "r") as f:
            return json.load(f)

    @classmethod
    async def _load_saved_face_state(
        cls, directory: Path, params: FaceParams
    ) -> FaceState:
        return FaceState(service=await cls._build_face_service(params))

    @staticmethod
    async def _load_module_metrics(directory: Path) -> List[MetricData]:
        with open(directory / "metrics.json", "r") as f:
            serialized = json.load(f)
        return [MetricData.parse_obj(metric) for metric in serialized]

    async def _load_saved_module_state(
        self, directory: Path, params: ModuleParams
    ) -> ModuleState:
        return ModuleState(
            service=await self._build_module_service(params),
            archived_metrics=await self._load_module_metrics(
                directory / "metrics"
            ),
            metrics_stream=await Observable.build(),
            metrics_task=asyncio.create_task(self._watch_metrics_task()),
        )

    @classmethod
    async def _load_saved_offline_state(
        cls, directory: Path, params: OfflineParams
    ) -> OfflineState:
        state_dict = await cls._load_state_dict(directory)
        return OfflineState(
            max_epochs=state_dict["max_epochs"],
            batch_size=state_dict["batch_size"],
            scrap_limit=state_dict["scrap_limit"],
            scrap_before=datetime.fromisoformat(state_dict["scrap_before"])
            if state_dict["scrap_before"] is not None
            else None,
            scrap_after=datetime.fromisoformat(state_dict["scrap_after"])
            if state_dict["scrap_after"] is not None
            else None,
            posts_cache={},
        )

    @classmethod
    async def _load_saved_post_scheduler(
        cls,
        directory: Path,
        state_dict: Dict[str, Any],
        params: OnlineParams,
    ) -> PostScheduler:
        return await cls._load_generic(
            directory,
            PostScheduler,
            category=state_dict["post_scheduler_type"],
            default=partial(
                cls._build_post_scheduler,
                params,
            ),
        )

    @classmethod
    async def _load_saved_score_scheduler(
        cls,
        directory: Path,
        state_dict: Dict[str, Any],
        params: OnlineParams,
    ) -> ScoreScheduler:
        return await cls._load_generic(
            directory,
            ScoreScheduler,
            category=state_dict["score_scheduler_type"],
            default=partial(
                cls._build_score_scheduler,
                params,
            ),
        )

    @classmethod
    async def _load_saved_online_state(
        cls, directory: Path, params: OnlineParams
    ) -> OnlineState:
        state_dict = await cls._load_state_dict(directory)
        return OnlineState(
            ids_cache=await cls._deserialize_ids_cache(
                state_dict["ids_cache"]
            ),
            post_scheduler=await cls._load_saved_post_scheduler(
                directory / "post_scheduler",
                state_dict,
                params,
            ),
            post_schedulers_params=state_dict["post_schedulers_params"],
            score_scheduler=await cls._load_saved_score_scheduler(
                directory / "score_scheduler",
                state_dict,
                params,
            ),
            score_schedulers_params=state_dict["score_schedulers_params"],
            iterations=state_dict["iterations"],
            batch_size=state_dict["batch_size"],
            lock=Lock(),
        )

    @classmethod
    async def _load_saved_feed_state(
        cls, directory: Path, params: FeedParams
    ) -> FeedState:
        state_dict = await cls._load_state_dict(directory)
        return FeedState(
            feed=[
                PostData.parse_obj(post) for post in state_dict.get("feed", [])
            ],
            length=state_dict.get("length", params.length),
            stream=await Observable.build(),
        )

    async def _load_saved_state(self, directory: Path) -> State:
        params = Params(**self._kwargs)
        return State(
            face=await self._load_saved_face_state(
                directory / "face", params.face
            ),
            module=await self._load_saved_module_state(
                directory / "module", params.module
            ),
            offline=await self._load_saved_offline_state(
                directory / "offline", params.offline
            ),
            online=await self._load_saved_online_state(
                directory / "online", params.online
            ),
            training_task=None,
            training_status=await self._build_training_status(),
            feed=await self._load_saved_feed_state(
                directory / "feed", params.feed
            ),
        )

    async def cleanup(self) -> None:
        async with self.state.write_lock() as state:
            state.module.metrics_task.cancel()
            try:
                await state.module.metrics_task
            except asyncio.CancelledError:
                pass

    @classproperty
    def parameters(cls) -> Set[Parameter]:
        return {
            ScrapBeforeParameter(),
            ScrapAfterParameter(),
            ScrapLimitParameter(),
            MaxOfflineEpochsParameter(),
            OfflineBatchSizeParameter(),
            PostSchedulerParameter(),
            ScoreSchedulerParameter(),
            OnlineIterationsParameter(),
            OnlineBatchSizeParameter(),
            FeedLengthParameter(),
        }

    @abstractmethod
    async def _watch_metrics_task(self) -> None:
        pass


class CilroyControllerDelegatedBase(CilroyControllerBase, ABC):
    async def get_face_metadata(self) -> Metadata:
        async with self.state.read_lock() as state:
            metadata = await state.face.service.get_metadata()
            return Metadata(key=metadata.key, description=metadata.description)

    async def get_module_metadata(self) -> Metadata:
        async with self.state.read_lock() as state:
            metadata = await state.module.service.get_metadata()
            return Metadata(key=metadata.key, description=metadata.description)

    async def get_face_post_schema(self) -> JSONSchema:
        async with self.state.read_lock() as state:
            return JSONSchema(**await state.face.service.get_post_schema())

    async def get_module_post_schema(self) -> JSONSchema:
        async with self.state.read_lock() as state:
            return JSONSchema(**await state.module.service.get_post_schema())

    async def get_face_status(self) -> Status:
        async with self.state.read_lock() as state:
            status = await state.face.service.get_status()
        return Status(status)

    async def watch_face_status(self) -> AsyncIterable[Status]:
        async with self.state.read_lock() as state:
            service = state.face.service
        async for status in service.watch_status():
            yield Status(status)

    async def get_module_status(self) -> Status:
        async with self.state.read_lock() as state:
            status = await state.module.service.get_status()
        return Status(status)

    async def watch_module_status(self) -> AsyncIterable[Status]:
        async with self.state.read_lock() as state:
            service = state.module.service
        async for status in service.watch_status():
            yield Status(status)

    async def get_face_config_schema(self) -> JSONSchema:
        async with self.state.read_lock() as state:
            return JSONSchema(**await state.face.service.get_config_schema())

    async def get_face_config(self) -> Dict[str, Any]:
        async with self.state.read_lock() as state:
            return await state.face.service.get_config()

    async def watch_face_config(self) -> AsyncIterable[Dict[str, Any]]:
        async with self.state.read_lock() as state:
            service = state.face.service
        async for config in service.watch_config():
            yield config

    async def set_face_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        async with self.state.write_lock() as state:
            return await state.face.service.set_config(config)

    async def get_module_config_schema(self) -> JSONSchema:
        async with self.state.read_lock() as state:
            return JSONSchema(**await state.module.service.get_config_schema())

    async def get_module_config(self) -> Dict[str, Any]:
        async with self.state.read_lock() as state:
            return await state.module.service.get_config()

    async def watch_module_config(self) -> AsyncIterable[Dict[str, Any]]:
        async with self.state.read_lock() as state:
            service = state.module.service
        async for config in service.watch_config():
            yield config

    async def set_module_config(
        self, config: Dict[str, Any]
    ) -> Dict[str, Any]:
        async with self.state.write_lock() as state:
            return await state.module.service.set_config(config)


class CilroyController(CilroyControllerDelegatedBase):
    async def get_training_status(self) -> ReadableObservable[TrainingStatus]:
        async with self.state.read_lock() as state:
            return ReadOnlyObservableWrapper(state.training_status)

    async def _train_offline_loop(
        self, posts: AsyncIterable[Tuple[Dict, float]]
    ) -> None:
        epoch = 0

        while True:
            logger.info(f"Offline training: Epoch {epoch}.")

            async with self.state.read_lock() as state:
                max_epochs = state.offline.max_epochs
                batch_size = state.offline.batch_size
                service = state.module.service

            if max_epochs is not None and epoch >= max_epochs:
                break

            n_batch = 0

            async for batch in batches(posts, batch_size):
                logger.info(
                    f"Offline training: Epoch {epoch}, batch {n_batch}."
                )
                await service.fit_posts(batch)
                await service.step()
                n_batch += 1

            epoch += 1

    async def _train_offline(self) -> None:
        logger.info("Offline training started.")

        async def map_posts(
            _posts: AsyncIterable[Tuple[UUID, Dict, float]]
        ) -> AsyncIterable[Tuple[Dict, float]]:
            async for post_id, post, score in _posts:
                yield post, score

        state = await self.state.value.fetch()
        posts = state.face.service.scrap(
            state.offline.scrap_limit,
            state.offline.scrap_before,
            state.offline.scrap_after,
        )
        posts = map_posts(posts)

        with CachingAsyncIterable(posts, state.offline.posts_cache) as posts:
            await self._train_offline_loop(posts)

        async with self.state.write_lock() as state:
            await state.training_status.set(TrainingStatus.IDLE)
            state.training_task = None

        logger.info("Offline training finished.")

    async def train_offline(self) -> None:
        async with self.state.write_lock() as state:
            if state.training_task is not None:
                raise RuntimeError("Training is already in progress.")
            await state.training_status.set(TrainingStatus.OFFLINE)
            state.training_task = asyncio.create_task(self._train_offline())

    async def _train_online_post_loop(self) -> None:
        async with self.state.read_lock() as state:
            module_service = state.module.service
            face_service = state.face.service
            post_scheduler = state.online.post_scheduler
            lock = state.online.lock

        async for _ in post_scheduler.wait():
            async with lock:
                logger.info("Online training: Creating new post...")

                module_post_id, post = await anext(module_service.generate())
                face_post_id, post_url = await face_service.post(post)

                post_data = PostData(
                    id=face_post_id,
                    url=post_url,
                    content=post,
                    created_at=datetime.utcnow(),
                )

                async with self.state.write_lock() as state:
                    state.online.ids_cache[face_post_id] = module_post_id
                    state.feed.feed = state.feed.feed + [post_data]
                    state.feed.feed = state.feed.feed[-state.feed.length :]
                    await state.feed.stream.set(post_data)

                logger.info(
                    f"Online training: "
                    f"New post with module-side id {str(module_post_id)} and "
                    f"face-side id {str(face_post_id)}."
                )

    async def _train_online_fit_scores(
        self, scores: Dict[UUID, float]
    ) -> None:
        iteration = 0

        while True:
            async with self.state.read_lock() as state:
                iterations = state.online.iterations
                batch_size = state.online.batch_size
                service = state.module.service

            if iteration >= iterations:
                break

            async for batch in batches(scores.items(), batch_size):
                await service.fit_scores(batch)
                await service.step()
            iteration += 1

    async def _train_online_score_loop(self) -> None:
        async with self.state.read_lock() as state:
            face_service = state.face.service
            score_scheduler = state.online.score_scheduler
            lock = state.online.lock

        async for _ in score_scheduler.wait():
            async with lock:
                logger.info("Online training: Scoring posts...")

                async with self.state.read_lock() as state:
                    post_ids = list(state.online.ids_cache.keys())

                scores = await asyncio.gather(
                    *[face_service.score(post_id) for post_id in post_ids]
                )

                async with self.state.read_lock() as state:
                    scores = {
                        state.online.ids_cache.get(post_id): score
                        for post_id, score in zip(post_ids, scores)
                    }

                logger.info("Online training: Fitting scores...")

                await self._train_online_fit_scores(scores)

                async with self.state.write_lock() as state:
                    state.online.ids_cache.clear()

                logger.info("Online training: Scores fitted.")

    async def _train_online(self) -> None:
        logger.info("Online training started.")

        tasks = [
            asyncio.create_task(self._train_online_post_loop()),
            asyncio.create_task(self._train_online_score_loop()),
        ]
        try:
            await asyncio.gather(*tasks)
        finally:
            for task in tasks:
                task.cancel()

        async with self.state.write_lock() as state:
            await state.training_status.set(TrainingStatus.IDLE)
            state.training_task = None

        logger.info("Online training finished.")

    async def train_online(self) -> None:
        async with self.state.write_lock() as state:
            if state.training_task is not None:
                raise RuntimeError("Training is already in progress.")
            await state.training_status.set(TrainingStatus.ONLINE)
            state.training_task = asyncio.create_task(self._train_online())

    async def stop_training(self) -> None:
        async with self.state.write_lock() as state:
            if state.training_task is not None:
                state.training_task.cancel()
                try:
                    await state.training_task
                except asyncio.CancelledError:
                    pass
                except Exception as e:
                    logger.warning("Training task failed.", exc_info=e)
                state.training_task = None
                await state.training_status.set(TrainingStatus.IDLE)
                logger.info("Training stopped.")

    async def get_module_metrics_config(self) -> List[MetricConfig]:
        async with self.state.read_lock() as state:
            return await state.module.service.get_metrics_config()

    async def get_module_metrics(self) -> List[MetricData]:
        async with self.state.read_lock() as state:
            return state.module.archived_metrics

    async def _watch_metrics_task(self) -> None:
        async with self.state.read_lock() as state:
            service: ModuleService = state.module.service

        while True:
            try:
                async for metric in service.watch_metrics():
                    async with self.state.write_lock() as state:
                        state.module.archived_metrics.append(metric)
                        await state.module.metrics_stream.set(metric)
            except asyncio.CancelledError:
                raise
            except Exception as e:
                logger.warning("Metrics stream failed.", exc_info=e)
                await asyncio.sleep(1)

    async def watch_module_metrics(self) -> AsyncIterator[MetricData]:
        async with self.state.read_lock() as state:
            metrics = state.module.metrics_stream
        async for metric in metrics.subscribe():
            yield metric

    async def reset_face(self) -> None:
        async with self.state.write_lock() as state:
            await state.face.service.reset()

    async def reset_module(self) -> None:
        await self.stop_training()
        async with self.state.write_lock() as state:
            await state.module.service.reset()
            state.module.archived_metrics = []
            state.offline.posts_cache.clear()
            state.online.ids_cache.clear()
            state.feed.feed = []

    async def get_feed(self) -> List[PostData]:
        async with self.state.read_lock() as state:
            return state.feed.feed

    async def watch_feed(self) -> AsyncIterator[PostData]:
        async with self.state.read_lock() as state:
            feed = state.feed.stream
        async for post in feed.subscribe():
            yield post
