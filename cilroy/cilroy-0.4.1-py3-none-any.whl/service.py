import json
from typing import AsyncIterator, Dict, Tuple

import aiostream
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase
from grpclib.server import Stream

from cilroy.controller import CilroyController
from cilroy.messages import *


class CilroyServiceBase(ServiceBase):
    async def get_face_metadata(
        self, get_face_metadata_request: "GetFaceMetadataRequest"
    ) -> "GetFaceMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_metadata(
        self, get_module_metadata_request: "GetModuleMetadataRequest"
    ) -> "GetModuleMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_face_post_schema(
        self, get_face_post_schema_request: "GetFacePostSchemaRequest"
    ) -> "GetFacePostSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_post_schema(
        self, get_module_post_schema_request: "GetModulePostSchemaRequest"
    ) -> "GetModulePostSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_controller_status(
        self, get_controller_status_request: "GetControllerStatusRequest"
    ) -> "GetControllerStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_controller_status(
        self, watch_controller_status_request: "WatchControllerStatusRequest"
    ) -> AsyncIterator["WatchControllerStatusResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_face_status(
        self, get_face_status_request: "GetFaceStatusRequest"
    ) -> "GetFaceStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_face_status(
        self, watch_face_status_request: "WatchFaceStatusRequest"
    ) -> AsyncIterator["WatchFaceStatusResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_status(
        self, get_module_status_request: "GetModuleStatusRequest"
    ) -> "GetModuleStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_module_status(
        self, watch_module_status_request: "WatchModuleStatusRequest"
    ) -> AsyncIterator["WatchModuleStatusResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_training_status(
        self, get_training_status_request: "GetTrainingStatusRequest"
    ) -> "GetTrainingStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_training_status(
        self, watch_training_status_request: "WatchTrainingStatusRequest"
    ) -> AsyncIterator["WatchTrainingStatusResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_controller_config_schema(
        self,
        get_controller_config_schema_request: "GetControllerConfigSchemaRequest",
    ) -> "GetControllerConfigSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_controller_config(
        self, get_controller_config_request: "GetControllerConfigRequest"
    ) -> "GetControllerConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_controller_config(
        self, watch_controller_config_request: "WatchControllerConfigRequest"
    ) -> AsyncIterator["WatchControllerConfigResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_controller_config(
        self, set_controller_config_request: "SetControllerConfigRequest"
    ) -> "SetControllerConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_face_config_schema(
        self, get_face_config_schema_request: "GetFaceConfigSchemaRequest"
    ) -> "GetFaceConfigSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_face_config(
        self, get_face_config_request: "GetFaceConfigRequest"
    ) -> "GetFaceConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_face_config(
        self, watch_face_config_request: "WatchFaceConfigRequest"
    ) -> AsyncIterator["WatchFaceConfigResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_face_config(
        self, set_face_config_request: "SetFaceConfigRequest"
    ) -> "SetFaceConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_config_schema(
        self, get_module_config_schema_request: "GetModuleConfigSchemaRequest"
    ) -> "GetModuleConfigSchemaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_config(
        self, get_module_config_request: "GetModuleConfigRequest"
    ) -> "GetModuleConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_module_config(
        self, watch_module_config_request: "WatchModuleConfigRequest"
    ) -> AsyncIterator["WatchModuleConfigResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_module_config(
        self, set_module_config_request: "SetModuleConfigRequest"
    ) -> "SetModuleConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def train_offline(
        self, train_offline_request: "TrainOfflineRequest"
    ) -> "TrainOfflineResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def train_online(
        self, train_online_request: "TrainOnlineRequest"
    ) -> "TrainOnlineResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def stop_training(
        self, stop_training_request: "StopTrainingRequest"
    ) -> "StopTrainingResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_metrics_config(
        self,
        get_module_metrics_config_request: "GetModuleMetricsConfigRequest",
    ) -> "GetModuleMetricsConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_module_metrics(
        self, get_module_metrics_request: "GetModuleMetricsRequest"
    ) -> "GetModuleMetricsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_module_metrics(
        self, watch_module_metrics_request: "WatchModuleMetricsRequest"
    ) -> AsyncIterator["WatchModuleMetricsResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_all(
        self, watch_all_request: "WatchAllRequest"
    ) -> AsyncIterator["WatchAllResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reset_controller(
        self, reset_controller_request: "ResetControllerRequest"
    ) -> "ResetControllerResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reset_face(
        self, reset_face_request: "ResetFaceRequest"
    ) -> "ResetFaceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reset_module(
        self, reset_module_request: "ResetModuleRequest"
    ) -> "ResetModuleResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_feed(
        self, get_feed_request: "GetFeedRequest"
    ) -> "GetFeedResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch_feed(
        self, watch_feed_request: "WatchFeedRequest"
    ) -> AsyncIterator["WatchFeedResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_face_metadata(
        self,
        stream: "grpclib.server.Stream[GetFaceMetadataRequest, GetFaceMetadataResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_face_metadata(request)
        await stream.send_message(response)

    async def __rpc_get_module_metadata(
        self,
        stream: "grpclib.server.Stream[GetModuleMetadataRequest, GetModuleMetadataResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_metadata(request)
        await stream.send_message(response)

    async def __rpc_get_face_post_schema(
        self,
        stream: "grpclib.server.Stream[GetFacePostSchemaRequest, GetFacePostSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_face_post_schema(request)
        await stream.send_message(response)

    async def __rpc_get_module_post_schema(
        self,
        stream: "grpclib.server.Stream[GetModulePostSchemaRequest, GetModulePostSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_post_schema(request)
        await stream.send_message(response)

    async def __rpc_get_controller_status(
        self,
        stream: "grpclib.server.Stream[GetControllerStatusRequest, GetControllerStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_controller_status(request)
        await stream.send_message(response)

    async def __rpc_watch_controller_status(
        self,
        stream: "grpclib.server.Stream[WatchControllerStatusRequest, WatchControllerStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_controller_status,
            stream,
            request,
        )

    async def __rpc_get_face_status(
        self,
        stream: "grpclib.server.Stream[GetFaceStatusRequest, GetFaceStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_face_status(request)
        await stream.send_message(response)

    async def __rpc_watch_face_status(
        self,
        stream: "grpclib.server.Stream[WatchFaceStatusRequest, WatchFaceStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_face_status,
            stream,
            request,
        )

    async def __rpc_get_module_status(
        self,
        stream: "grpclib.server.Stream[GetModuleStatusRequest, GetModuleStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_status(request)
        await stream.send_message(response)

    async def __rpc_watch_module_status(
        self,
        stream: "grpclib.server.Stream[WatchModuleStatusRequest, WatchModuleStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_module_status,
            stream,
            request,
        )

    async def __rpc_get_training_status(
        self,
        stream: "grpclib.server.Stream[GetTrainingStatusRequest, GetTrainingStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_training_status(request)
        await stream.send_message(response)

    async def __rpc_watch_training_status(
        self,
        stream: "grpclib.server.Stream[WatchTrainingStatusRequest, WatchTrainingStatusResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_training_status,
            stream,
            request,
        )

    async def __rpc_get_controller_config_schema(
        self,
        stream: "grpclib.server.Stream[GetControllerConfigSchemaRequest, GetControllerConfigSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_controller_config_schema(request)
        await stream.send_message(response)

    async def __rpc_get_controller_config(
        self,
        stream: "grpclib.server.Stream[GetControllerConfigRequest, GetControllerConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_controller_config(request)
        await stream.send_message(response)

    async def __rpc_watch_controller_config(
        self,
        stream: "grpclib.server.Stream[WatchControllerConfigRequest, WatchControllerConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_controller_config,
            stream,
            request,
        )

    async def __rpc_set_controller_config(
        self,
        stream: "grpclib.server.Stream[SetControllerConfigRequest, SetControllerConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_controller_config(request)
        await stream.send_message(response)

    async def __rpc_get_face_config_schema(
        self,
        stream: "grpclib.server.Stream[GetFaceConfigSchemaRequest, GetFaceConfigSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_face_config_schema(request)
        await stream.send_message(response)

    async def __rpc_get_face_config(
        self,
        stream: "grpclib.server.Stream[GetFaceConfigRequest, GetFaceConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_face_config(request)
        await stream.send_message(response)

    async def __rpc_watch_face_config(
        self,
        stream: "grpclib.server.Stream[WatchFaceConfigRequest, WatchFaceConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_face_config,
            stream,
            request,
        )

    async def __rpc_set_face_config(
        self,
        stream: "grpclib.server.Stream[SetFaceConfigRequest, SetFaceConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_face_config(request)
        await stream.send_message(response)

    async def __rpc_get_module_config_schema(
        self,
        stream: "grpclib.server.Stream[GetModuleConfigSchemaRequest, GetModuleConfigSchemaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_config_schema(request)
        await stream.send_message(response)

    async def __rpc_get_module_config(
        self,
        stream: "grpclib.server.Stream[GetModuleConfigRequest, GetModuleConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_config(request)
        await stream.send_message(response)

    async def __rpc_watch_module_config(
        self,
        stream: "grpclib.server.Stream[WatchModuleConfigRequest, WatchModuleConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_module_config,
            stream,
            request,
        )

    async def __rpc_set_module_config(
        self,
        stream: "grpclib.server.Stream[SetModuleConfigRequest, SetModuleConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_module_config(request)
        await stream.send_message(response)

    async def __rpc_train_offline(
        self,
        stream: "grpclib.server.Stream[TrainOfflineRequest, TrainOfflineResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.train_offline(request)
        await stream.send_message(response)

    async def __rpc_train_online(
        self,
        stream: "grpclib.server.Stream[TrainOnlineRequest, TrainOnlineResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.train_online(request)
        await stream.send_message(response)

    async def __rpc_stop_training(
        self,
        stream: "grpclib.server.Stream[StopTrainingRequest, StopTrainingResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.stop_training(request)
        await stream.send_message(response)

    async def __rpc_get_module_metrics_config(
        self,
        stream: "grpclib.server.Stream[GetModuleMetricsConfigRequest, GetModuleMetricsConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_metrics_config(request)
        await stream.send_message(response)

    async def __rpc_get_module_metrics(
        self,
        stream: "grpclib.server.Stream[GetModuleMetricsRequest, GetModuleMetricsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_module_metrics(request)
        await stream.send_message(response)

    async def __rpc_watch_module_metrics(
        self,
        stream: "grpclib.server.Stream[WatchModuleMetricsRequest, WatchModuleMetricsResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_module_metrics,
            stream,
            request,
        )

    async def __rpc_watch_all(
        self,
        stream: "grpclib.server.Stream[WatchAllRequest, WatchAllResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_all,
            stream,
            request,
        )

    async def __rpc_reset_controller(
        self,
        stream: "grpclib.server.Stream[ResetControllerRequest, ResetControllerResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.reset_controller(request)
        await stream.send_message(response)

    async def __rpc_reset_face(
        self,
        stream: "grpclib.server.Stream[ResetFaceRequest, ResetFaceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.reset_face(request)
        await stream.send_message(response)

    async def __rpc_reset_module(
        self,
        stream: "grpclib.server.Stream[ResetModuleRequest, ResetModuleResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.reset_module(request)
        await stream.send_message(response)

    async def __rpc_get_feed(
        self, stream: "grpclib.server.Stream[GetFeedRequest, GetFeedResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_feed(request)
        await stream.send_message(response)

    async def __rpc_watch_feed(
        self,
        stream: "grpclib.server.Stream[WatchFeedRequest, WatchFeedResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch_feed,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/kilroy.cilroy.v1alpha.CilroyService/GetFaceMetadata": grpclib.const.Handler(
                self.__rpc_get_face_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFaceMetadataRequest,
                GetFaceMetadataResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleMetadata": grpclib.const.Handler(
                self.__rpc_get_module_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleMetadataRequest,
                GetModuleMetadataResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetFacePostSchema": grpclib.const.Handler(
                self.__rpc_get_face_post_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFacePostSchemaRequest,
                GetFacePostSchemaResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModulePostSchema": grpclib.const.Handler(
                self.__rpc_get_module_post_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModulePostSchemaRequest,
                GetModulePostSchemaResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetControllerStatus": grpclib.const.Handler(
                self.__rpc_get_controller_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetControllerStatusRequest,
                GetControllerStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchControllerStatus": grpclib.const.Handler(
                self.__rpc_watch_controller_status,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchControllerStatusRequest,
                WatchControllerStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetFaceStatus": grpclib.const.Handler(
                self.__rpc_get_face_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFaceStatusRequest,
                GetFaceStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchFaceStatus": grpclib.const.Handler(
                self.__rpc_watch_face_status,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchFaceStatusRequest,
                WatchFaceStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleStatus": grpclib.const.Handler(
                self.__rpc_get_module_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleStatusRequest,
                GetModuleStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchModuleStatus": grpclib.const.Handler(
                self.__rpc_watch_module_status,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchModuleStatusRequest,
                WatchModuleStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetTrainingStatus": grpclib.const.Handler(
                self.__rpc_get_training_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetTrainingStatusRequest,
                GetTrainingStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchTrainingStatus": grpclib.const.Handler(
                self.__rpc_watch_training_status,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchTrainingStatusRequest,
                WatchTrainingStatusResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetControllerConfigSchema": grpclib.const.Handler(
                self.__rpc_get_controller_config_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetControllerConfigSchemaRequest,
                GetControllerConfigSchemaResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetControllerConfig": grpclib.const.Handler(
                self.__rpc_get_controller_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetControllerConfigRequest,
                GetControllerConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchControllerConfig": grpclib.const.Handler(
                self.__rpc_watch_controller_config,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchControllerConfigRequest,
                WatchControllerConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/SetControllerConfig": grpclib.const.Handler(
                self.__rpc_set_controller_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetControllerConfigRequest,
                SetControllerConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetFaceConfigSchema": grpclib.const.Handler(
                self.__rpc_get_face_config_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFaceConfigSchemaRequest,
                GetFaceConfigSchemaResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetFaceConfig": grpclib.const.Handler(
                self.__rpc_get_face_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFaceConfigRequest,
                GetFaceConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchFaceConfig": grpclib.const.Handler(
                self.__rpc_watch_face_config,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchFaceConfigRequest,
                WatchFaceConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/SetFaceConfig": grpclib.const.Handler(
                self.__rpc_set_face_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetFaceConfigRequest,
                SetFaceConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleConfigSchema": grpclib.const.Handler(
                self.__rpc_get_module_config_schema,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleConfigSchemaRequest,
                GetModuleConfigSchemaResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleConfig": grpclib.const.Handler(
                self.__rpc_get_module_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleConfigRequest,
                GetModuleConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchModuleConfig": grpclib.const.Handler(
                self.__rpc_watch_module_config,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchModuleConfigRequest,
                WatchModuleConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/SetModuleConfig": grpclib.const.Handler(
                self.__rpc_set_module_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetModuleConfigRequest,
                SetModuleConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/TrainOffline": grpclib.const.Handler(
                self.__rpc_train_offline,
                grpclib.const.Cardinality.UNARY_UNARY,
                TrainOfflineRequest,
                TrainOfflineResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/TrainOnline": grpclib.const.Handler(
                self.__rpc_train_online,
                grpclib.const.Cardinality.UNARY_UNARY,
                TrainOnlineRequest,
                TrainOnlineResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/StopTraining": grpclib.const.Handler(
                self.__rpc_stop_training,
                grpclib.const.Cardinality.UNARY_UNARY,
                StopTrainingRequest,
                StopTrainingResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleMetricsConfig": grpclib.const.Handler(
                self.__rpc_get_module_metrics_config,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleMetricsConfigRequest,
                GetModuleMetricsConfigResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetModuleMetrics": grpclib.const.Handler(
                self.__rpc_get_module_metrics,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModuleMetricsRequest,
                GetModuleMetricsResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchModuleMetrics": grpclib.const.Handler(
                self.__rpc_watch_module_metrics,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchModuleMetricsRequest,
                WatchModuleMetricsResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchAll": grpclib.const.Handler(
                self.__rpc_watch_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchAllRequest,
                WatchAllResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/ResetController": grpclib.const.Handler(
                self.__rpc_reset_controller,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResetControllerRequest,
                ResetControllerResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/ResetFace": grpclib.const.Handler(
                self.__rpc_reset_face,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResetFaceRequest,
                ResetFaceResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/ResetModule": grpclib.const.Handler(
                self.__rpc_reset_module,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResetModuleRequest,
                ResetModuleResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/GetFeed": grpclib.const.Handler(
                self.__rpc_get_feed,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetFeedRequest,
                GetFeedResponse,
            ),
            "/kilroy.cilroy.v1alpha.CilroyService/WatchFeed": grpclib.const.Handler(
                self.__rpc_watch_feed,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchFeedRequest,
                WatchFeedResponse,
            ),
        }


class CilroyService(CilroyServiceBase):
    def __init__(self, controller: CilroyController) -> None:
        super().__init__()
        self._controller = controller

    async def get_face_metadata(
        self, get_face_metadata_request: "GetFaceMetadataRequest"
    ) -> "GetFaceMetadataResponse":
        metadata = await self._controller.get_face_metadata()
        return GetFaceMetadataResponse(
            key=metadata.key,
            description=metadata.description,
        )

    async def get_module_metadata(
        self, get_module_metadata_request: "GetModuleMetadataRequest"
    ) -> "GetModuleMetadataResponse":
        metadata = await self._controller.get_module_metadata()
        return GetModuleMetadataResponse(
            key=metadata.key,
            description=metadata.description,
        )

    async def get_face_post_schema(
        self, get_face_post_schema_request: "GetFacePostSchemaRequest"
    ) -> "GetFacePostSchemaResponse":
        schema = await self._controller.get_face_post_schema()
        return GetFacePostSchemaResponse().from_dict({"schema": schema.json()})

    async def get_module_post_schema(
        self, get_module_post_schema_request: "GetModulePostSchemaRequest"
    ) -> "GetModulePostSchemaResponse":
        schema = await self._controller.get_module_post_schema()
        return GetModulePostSchemaResponse().from_dict(
            {"schema": schema.json()}
        )

    async def get_controller_status(
        self, get_controller_status_request: "GetControllerStatusRequest"
    ) -> "GetControllerStatusResponse":
        ready = await self._controller.state.ready.fetch()
        status = Status.STATUS_READY if ready else Status.STATUS_LOADING
        return GetControllerStatusResponse().from_dict({"status": status})

    async def watch_controller_status(
        self, watch_controller_status_request: "WatchControllerStatusRequest"
    ) -> AsyncIterator["WatchControllerStatusResponse"]:
        async for ready in self._controller.state.ready.subscribe():
            status = Status.STATUS_READY if ready else Status.STATUS_LOADING
            yield WatchControllerStatusResponse().from_dict({"status": status})

    async def get_face_status(
        self, get_face_status_request: "GetFaceStatusRequest"
    ) -> "GetFaceStatusResponse":
        status = await self._controller.get_face_status()
        status = Status(value=status.value)
        return GetFaceStatusResponse().from_dict({"status": status})

    async def watch_face_status(
        self, watch_face_status_request: "WatchFaceStatusRequest"
    ) -> AsyncIterator["WatchFaceStatusResponse"]:
        async for status in self._controller.watch_face_status():
            status = Status(value=status.value)
            yield WatchFaceStatusResponse().from_dict({"status": status})

    async def get_module_status(
        self, get_module_status_request: "GetModuleStatusRequest"
    ) -> "GetModuleStatusResponse":
        status = await self._controller.get_module_status()
        status = Status(value=status.value)
        return GetModuleStatusResponse().from_dict({"status": status})

    async def watch_module_status(
        self, watch_module_status_request: "WatchModuleStatusRequest"
    ) -> AsyncIterator["WatchModuleStatusResponse"]:
        async for status in self._controller.watch_module_status():
            status = Status(value=status.value)
            yield WatchModuleStatusResponse().from_dict({"status": status})

    async def get_training_status(
        self, get_training_status_request: "GetTrainingStatusRequest"
    ) -> "GetTrainingStatusResponse":
        status = await self._controller.get_training_status()
        status = await status.fetch()
        return GetTrainingStatusResponse(status=TrainingStatus(status.value))

    async def watch_training_status(
        self, watch_training_status_request: "WatchTrainingStatusRequest"
    ) -> AsyncIterator["WatchTrainingStatusResponse"]:
        status = await self._controller.get_training_status()
        async for status in status.subscribe():
            yield WatchTrainingStatusResponse(
                status=TrainingStatus(status.value)
            )

    async def get_controller_config_schema(
        self,
        get_controller_config_schema_request: "GetControllerConfigSchemaRequest",
    ) -> "GetControllerConfigSchemaResponse":
        schema = self._controller.schema
        return GetControllerConfigSchemaResponse().from_dict(
            {"schema": schema.json()}
        )

    async def get_controller_config(
        self, get_controller_config_request: "GetControllerConfigRequest"
    ) -> "GetControllerConfigResponse":
        config = await self._controller.config.json.fetch()
        return GetControllerConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def watch_controller_config(
        self, watch_controller_config_request: "WatchControllerConfigRequest"
    ) -> AsyncIterator["WatchControllerConfigResponse"]:
        async for config in self._controller.config.json.subscribe():
            yield WatchControllerConfigResponse().from_dict(
                {"config": json.dumps(config)}
            )

    async def set_controller_config(
        self, set_controller_config_request: "SetControllerConfigRequest"
    ) -> "SetControllerConfigResponse":
        config = json.loads(set_controller_config_request.config)
        config = await self._controller.config.set(config)
        return SetControllerConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def get_face_config_schema(
        self, get_face_config_schema_request: "GetFaceConfigSchemaRequest"
    ) -> "GetFaceConfigSchemaResponse":
        schema = await self._controller.get_face_config_schema()
        return GetFaceConfigSchemaResponse().from_dict(
            {"schema": schema.json()}
        )

    async def get_face_config(
        self, get_face_config_request: "GetFaceConfigRequest"
    ) -> "GetFaceConfigResponse":
        config = await self._controller.get_face_config()
        return GetFaceConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def watch_face_config(
        self, watch_face_config_request: "WatchFaceConfigRequest"
    ) -> AsyncIterator["WatchFaceConfigResponse"]:
        async for config in self._controller.watch_face_config():
            yield WatchFaceConfigResponse().from_dict(
                {"config": json.dumps(config)}
            )

    async def set_face_config(
        self, set_face_config_request: "SetFaceConfigRequest"
    ) -> "SetFaceConfigResponse":
        config = json.loads(set_face_config_request.config)
        config = await self._controller.set_face_config(config)
        return SetFaceConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def get_module_config_schema(
        self, get_module_config_schema_request: "GetModuleConfigSchemaRequest"
    ) -> "GetModuleConfigSchemaResponse":
        schema = await self._controller.get_module_config_schema()
        return GetModuleConfigSchemaResponse().from_dict(
            {"schema": schema.json()}
        )

    async def get_module_config(
        self, get_module_config_request: "GetModuleConfigRequest"
    ) -> "GetModuleConfigResponse":
        config = await self._controller.get_module_config()
        return GetModuleConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def watch_module_config(
        self, watch_module_config_request: "WatchModuleConfigRequest"
    ) -> AsyncIterator["WatchModuleConfigResponse"]:
        async for config in self._controller.watch_module_config():
            yield WatchModuleConfigResponse().from_dict(
                {"config": json.dumps(config)}
            )

    async def set_module_config(
        self, set_module_config_request: "SetModuleConfigRequest"
    ) -> "SetModuleConfigResponse":
        config = json.loads(set_module_config_request.config)
        config = await self._controller.set_module_config(config)
        return SetModuleConfigResponse().from_dict(
            {"config": json.dumps(config)}
        )

    async def train_offline(
        self, train_offline_request: "TrainOfflineRequest"
    ) -> "TrainOfflineResponse":
        await self._controller.train_offline()
        return TrainOfflineResponse()

    async def train_online(
        self, train_online_request: "TrainOnlineRequest"
    ) -> "TrainOnlineResponse":
        await self._controller.train_online()
        return TrainOnlineResponse()

    async def stop_training(
        self, pause_training_request: "StopTrainingRequest"
    ) -> "StopTrainingResponse":
        await self._controller.stop_training()
        return StopTrainingResponse()

    async def get_module_metrics_config(
        self,
        get_module_metrics_config_request: "GetModuleMetricsConfigRequest",
    ) -> "GetModuleMetricsConfigResponse":
        metrics = await self._controller.get_module_metrics_config()
        return GetModuleMetricsConfigResponse(
            configs=[
                MetricConfig(
                    id=metric.id,
                    label=metric.label,
                    group=metric.group,
                    config=json.dumps(metric.config),
                )
                for metric in metrics
            ]
        )

    async def get_module_metrics(
        self, get_module_metrics_request: "GetModuleMetricsRequest"
    ) -> "GetModuleMetricsResponse":
        metrics = await self._controller.get_module_metrics()
        return GetModuleMetricsResponse(
            metrics=[
                MetricData(
                    metric_id=metric.metric_id,
                    dataset_id=metric.dataset_id,
                    data=json.dumps(metric.data),
                )
                for metric in metrics
            ]
        )

    async def watch_module_metrics(
        self, watch_module_metrics_request: "WatchModuleMetricsRequest"
    ) -> AsyncIterator["WatchModuleMetricsResponse"]:
        async for metric in self._controller.watch_module_metrics():
            yield WatchModuleMetricsResponse(
                metric=MetricData(
                    metric_id=metric.metric_id,
                    dataset_id=metric.dataset_id,
                    data=json.dumps(metric.data),
                )
            )

    async def watch_all(
        self, watch_all_request: "WatchAllRequest"
    ) -> AsyncIterator["WatchAllResponse"]:
        async def convert(
            method: str, stream: AsyncIterator[betterproto.Message]
        ) -> AsyncIterator[Tuple[str, str]]:
            async for msg in stream:
                yield method, msg.to_json()

        streams = [
            (
                "WatchControllerStatus",
                self.watch_controller_status(WatchControllerStatusRequest()),
            ),
            (
                "WatchFaceStatus",
                self.watch_face_status(WatchFaceStatusRequest()),
            ),
            (
                "WatchModuleStatus",
                self.watch_module_status(WatchModuleStatusRequest()),
            ),
            (
                "WatchTrainingStatus",
                self.watch_training_status(WatchTrainingStatusRequest()),
            ),
            (
                "WatchControllerConfig",
                self.watch_controller_config(WatchControllerConfigRequest()),
            ),
            (
                "WatchFaceConfig",
                self.watch_face_config(WatchFaceConfigRequest()),
            ),
            (
                "WatchModuleConfig",
                self.watch_module_config(WatchModuleConfigRequest()),
            ),
            (
                "WatchModuleMetrics",
                self.watch_module_metrics(WatchModuleMetricsRequest()),
            ),
            (
                "WatchFeed",
                self.watch_feed(WatchFeedRequest()),
            ),
        ]

        combine = aiostream.stream.merge(
            *(convert(method, stream) for method, stream in streams)
        )

        async with combine.stream() as streamer:
            async for method, message in streamer:
                yield WatchAllResponse(method=method, message=message)

    async def reset_controller(
        self, reset_controller_request: "ResetControllerRequest"
    ) -> "ResetControllerResponse":
        await self._controller.init()
        return ResetControllerResponse()

    async def reset_face(
        self, reset_face_request: "ResetFaceRequest"
    ) -> "ResetFaceResponse":
        await self._controller.reset_face()
        return ResetFaceResponse()

    async def reset_module(
        self, reset_module_request: "ResetModuleRequest"
    ) -> "ResetModuleResponse":
        await self._controller.reset_module()
        return ResetModuleResponse()

    async def get_feed(
        self, get_feed_request: "GetFeedRequest"
    ) -> "GetFeedResponse":
        feed = await self._controller.get_feed()
        return GetFeedResponse(
            posts=[
                Post(
                    id=str(post.id),
                    url=post.url,
                    content=json.dumps(post.content),
                    created_at=post.created_at.isoformat().replace(
                        "+00:00", "Z"
                    ),
                )
                for post in feed
            ]
        )

    async def watch_feed(
        self, watch_feed_request: "WatchFeedRequest"
    ) -> AsyncIterator["WatchFeedResponse"]:
        async for post in self._controller.watch_feed():
            yield WatchFeedResponse(
                post=Post(
                    id=str(post.id),
                    url=post.url,
                    content=json.dumps(post.content),
                    created_at=post.created_at.isoformat().replace(
                        "+00:00", "Z"
                    ),
                )
            )
