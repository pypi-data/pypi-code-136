import json
from datetime import datetime
from typing import Any, AsyncIterator, Dict, Optional, Tuple
from uuid import UUID

import betterproto
from betterproto.grpc.grpclib_client import MetadataLike
from grpclib.metadata import Deadline
from kilroy_face_py_shared import (
    GeneratedPost,
    GetConfigRequest,
    GetConfigResponse,
    GetConfigSchemaRequest,
    GetConfigSchemaResponse,
    GetMetadataRequest,
    GetMetadataResponse,
    GetPostSchemaRequest,
    GetPostSchemaResponse,
    GetStatusRequest,
    GetStatusResponse,
    PostRequest,
    PostResponse,
    ScoreRequest,
    ScoreResponse,
    ScrapRequest,
    ScrapResponse,
    SetConfigRequest,
    SetConfigResponse,
    Status,
    WatchConfigRequest,
    WatchConfigResponse,
    WatchStatusRequest,
    WatchStatusResponse,
    ResetRequest,
    ResetResponse,
)
from kilroy_face_py_shared.metadata import Metadata


class FaceServiceStub(betterproto.ServiceStub):
    async def get_metadata(
        self,
        get_metadata_request: "GetMetadataRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetMetadataResponse":
        return await self._unary_unary(
            "/kilroy.face.v1alpha.FaceService/GetMetadata",
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
            "/kilroy.face.v1alpha.FaceService/GetPostSchema",
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
            "/kilroy.face.v1alpha.FaceService/GetStatus",
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
            "/kilroy.face.v1alpha.FaceService/WatchStatus",
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
            "/kilroy.face.v1alpha.FaceService/GetConfigSchema",
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
            "/kilroy.face.v1alpha.FaceService/GetConfig",
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
            "/kilroy.face.v1alpha.FaceService/WatchConfig",
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
            "/kilroy.face.v1alpha.FaceService/SetConfig",
            set_config_request,
            SetConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def post(
        self,
        post_request: "PostRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "PostResponse":
        return await self._unary_unary(
            "/kilroy.face.v1alpha.FaceService/Post",
            post_request,
            PostResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def score(
        self,
        score_request: "ScoreRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "ScoreResponse":
        return await self._unary_unary(
            "/kilroy.face.v1alpha.FaceService/Score",
            score_request,
            ScoreResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def scrap(
        self,
        scrap_request: "ScrapRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> AsyncIterator["ScrapResponse"]:
        async for response in self._unary_stream(
            "/kilroy.face.v1alpha.FaceService/Scrap",
            scrap_request,
            ScrapResponse,
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
        metadata: Optional["MetadataLike"] = None,
    ) -> "ResetResponse":
        return await self._unary_unary(
            "/kilroy.face.v1alpha.FaceService/Reset",
            reset_request,
            ResetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class FaceService:
    def __init__(self, *args, **kwargs) -> None:
        self._stub = FaceServiceStub(*args, **kwargs)

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

    async def post(
        self, post: Dict[str, Any], *args, **kwargs
    ) -> Tuple[UUID, Optional[str]]:
        response = await self._stub.post(
            PostRequest(post=GeneratedPost(content=json.dumps(post))),
            *args,
            **kwargs,
        )
        return UUID(response.post_id), response.post_url

    async def score(self, post_id: UUID, *args, **kwargs) -> float:
        response = await self._stub.score(
            ScoreRequest(post_id=str(post_id)), *args, **kwargs
        )
        return response.score

    async def scrap(
        self,
        limit: Optional[int] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        *args,
        **kwargs,
    ) -> AsyncIterator[Tuple[UUID, Dict[str, Any], float]]:
        async for response in self._stub.scrap(
            ScrapRequest(limit=limit, before=before, after=after),
            *args,
            **kwargs,
        ):
            yield (
                response.post.id,
                json.loads(response.post.content),
                response.post.score,
            )

    async def reset(self, *args, **kwargs) -> None:
        await self._stub.reset(ResetRequest(), *args, **kwargs)
