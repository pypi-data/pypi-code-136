import json
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)
from uuid import UUID

import betterproto
from aiostream import stream
from betterproto.grpc.grpclib_client import MetadataLike
from grpclib.metadata import Deadline
from kilroy_module_py_shared import (
    FitPostsRequest,
    FitPostsResponse,
    FitScoresRequest,
    FitScoresResponse,
    GenerateRequest,
    GenerateResponse,
    GetConfigRequest,
    GetConfigResponse,
    GetConfigSchemaRequest,
    GetConfigSchemaResponse,
    GetMetadataRequest,
    GetMetadataResponse,
    GetMetricsConfigRequest,
    GetMetricsConfigResponse,
    GetPostSchemaRequest,
    GetPostSchemaResponse,
    GetStatusRequest,
    GetStatusResponse,
    Metadata,
    PostScore,
    RealPost,
    SetConfigRequest,
    SetConfigResponse,
    Status,
    StepRequest,
    StepResponse,
    WatchConfigRequest,
    WatchConfigResponse,
    WatchMetricsRequest,
    WatchMetricsResponse,
    WatchStatusRequest,
    WatchStatusResponse,
    ResetRequest,
    ResetResponse,
)

from kilroy_module_client_py_sdk.metrics import MetricConfig, MetricData


class ModuleServiceStub(betterproto.ServiceStub):
    async def get_metadata(
        self,
        get_metadata_request: "GetMetadataRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetMetadataResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetMetadata",
            get_metadata_request,
            GetMetadataResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_post_schema(
        self,
        get_post_schema_request: "GetPostSchemaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetPostSchemaResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetPostSchema",
            get_post_schema_request,
            GetPostSchemaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_status(
        self,
        get_status_request: "GetStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetStatusResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetStatus",
            get_status_request,
            GetStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_status(
        self,
        watch_status_request: "WatchStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchStatusResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchStatus",
            watch_status_request,
            WatchStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_config_schema(
        self,
        get_config_schema_request: "GetConfigSchemaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetConfigSchemaResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetConfigSchema",
            get_config_schema_request,
            GetConfigSchemaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_config(
        self,
        get_config_request: "GetConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetConfig",
            get_config_request,
            GetConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_config(
        self,
        watch_config_request: "WatchConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchConfigResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchConfig",
            watch_config_request,
            WatchConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def set_config(
        self,
        set_config_request: "SetConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "SetConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/SetConfig",
            set_config_request,
            SetConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def generate(
        self,
        generate_request: "GenerateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["GenerateResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/Generate",
            generate_request,
            GenerateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def fit_posts(
        self,
        fit_posts_request_iterator: Union[
            AsyncIterable["FitPostsRequest"], Iterable["FitPostsRequest"]
        ],
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "FitPostsResponse":
        return await self._stream_unary(
            "/kilroy.module.v1alpha.ModuleService/FitPosts",
            fit_posts_request_iterator,
            FitPostsRequest,
            FitPostsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def fit_scores(
        self,
        fit_scores_request: "FitScoresRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "FitScoresResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/FitScores",
            fit_scores_request,
            FitScoresResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def step(
        self,
        step_request: "StepRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "StepResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/Step",
            step_request,
            StepResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_metrics_config(
        self,
        get_metrics_config_request: "GetMetricsConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetMetricsConfigResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/GetMetricsConfig",
            get_metrics_config_request,
            GetMetricsConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def watch_metrics(
        self,
        watch_metrics_request: "WatchMetricsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["WatchMetricsResponse"]:
        async for response in self._unary_stream(
            "/kilroy.module.v1alpha.ModuleService/WatchMetrics",
            watch_metrics_request,
            WatchMetricsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def reset(
        self,
        reset_request: "ResetRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ResetResponse":
        return await self._unary_unary(
            "/kilroy.module.v1alpha.ModuleService/Reset",
            reset_request,
            ResetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ModuleService:
    def __init__(self, *args, **kwargs) -> None:
        self._stub = ModuleServiceStub(*args, **kwargs)

    async def get_metadata(self, *args, **kwargs) -> Metadata:
        response = await self._stub.get_metadata(
            GetMetadataRequest(), *args, **kwargs
        )
        return Metadata(key=response.key, description=response.description)

    async def get_post_schema(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_post_schema(
            GetPostSchemaRequest(), *args, **kwargs
        )
        return json.loads(response.schema)

    async def get_status(self, *args, **kwargs) -> Status:
        response = await self._stub.get_status(
            GetStatusRequest(), *args, **kwargs
        )
        return response.status

    async def watch_status(self, *args, **kwargs) -> AsyncIterator[Status]:
        async for response in self._stub.watch_status(
            WatchStatusRequest(), *args, **kwargs
        ):
            yield response.status

    async def get_config_schema(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_config_schema(
            GetConfigSchemaRequest(), *args, **kwargs
        )
        return json.loads(response.schema)

    async def get_config(self, *args, **kwargs) -> Dict[str, Any]:
        response = await self._stub.get_config(
            GetConfigRequest(), *args, **kwargs
        )
        return json.loads(response.config)

    async def watch_config(
        self, *args, **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        async for response in self._stub.watch_config(
            WatchConfigRequest(), *args, **kwargs
        ):
            yield json.loads(response.config)

    async def set_config(
        self, config: Dict[str, Any], *args, **kwargs
    ) -> "SetConfigResponse":
        response = await self._stub.set_config(
            SetConfigRequest(config=json.dumps(config)), *args, **kwargs
        )
        return json.loads(response.config)

    async def generate(
        self, quantity: int = 1, dry: bool = False, *args, **kwargs
    ) -> AsyncIterator[Tuple[UUID, Dict[str, Any]]]:
        async for response in self._stub.generate(
            GenerateRequest(quantity=quantity, dry=dry), *args, **kwargs
        ):
            yield UUID(response.post.id), json.loads(response.post.content)

    async def fit_posts(
        self,
        posts: Union[
            AsyncIterable[Tuple[Dict[str, Any], float]],
            Iterable[Tuple[Dict[str, Any], float]],
        ],
        *args,
        **kwargs,
    ) -> None:
        async with stream.iterate(posts).stream() as posts:

            async def to_requests():
                async for post, score in posts:
                    yield FitPostsRequest(
                        post=RealPost(content=json.dumps(post), score=score)
                    )

            await self._stub.fit_posts(to_requests(), *args, **kwargs)

    async def fit_scores(
        self,
        scores: Union[
            AsyncIterable[Tuple[UUID, float]],
            Iterable[Tuple[UUID, float]],
        ],
        *args,
        **kwargs,
    ) -> None:
        async with stream.iterate(scores).stream() as scores:
            request = FitScoresRequest(
                scores=[
                    PostScore(id=str(uid), score=score)
                    async for uid, score in scores
                ]
            )

            await self._stub.fit_scores(request, *args, **kwargs)

    async def step(self, *args, **kwargs) -> None:
        await self._stub.step(StepRequest(), *args, **kwargs)

    async def get_metrics_config(self, *args, **kwargs) -> List[MetricConfig]:
        response = await self._stub.get_metrics_config(
            GetMetricsConfigRequest(), *args, **kwargs
        )

        return [
            MetricConfig(
                id=metric.id,
                label=metric.label,
                group=metric.group,
                config=json.loads(metric.config),
            )
            for metric in response.configs
        ]

    async def watch_metrics(
        self, *args, **kwargs
    ) -> AsyncIterator[MetricData]:
        async for response in self._stub.watch_metrics(
            WatchMetricsRequest(), *args, **kwargs
        ):
            yield MetricData(
                metric_id=response.metric_id,
                dataset_id=response.dataset_id,
                data=json.loads(response.data),
            )

    async def reset(self, *args, **kwargs) -> None:
        await self._stub.reset(ResetRequest(), *args, **kwargs)
