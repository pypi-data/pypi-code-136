# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from exchange import injective_explorer_rpc_pb2 as exchange_dot_injective__explorer__rpc__pb2


class InjectiveExplorerRPCStub(object):
    """ExplorerRPC defines gRPC API of explorer data for e.g. Blockchain Explorer
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAccountTxs = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetAccountTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsResponse.FromString,
                )
        self.GetBlocks = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetBlocks',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetBlocksRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetBlocksResponse.FromString,
                )
        self.GetBlock = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetBlock',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetBlockRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetBlockResponse.FromString,
                )
        self.GetValidator = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetValidator',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorResponse.FromString,
                )
        self.GetValidatorUptime = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetValidatorUptime',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeResponse.FromString,
                )
        self.GetTxs = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetTxsResponse.FromString,
                )
        self.GetTxByTxHash = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetTxByTxHash',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashResponse.FromString,
                )
        self.StreamTxs = channel.unary_stream(
                '/injective_explorer_rpc.InjectiveExplorerRPC/StreamTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.StreamTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.StreamTxsResponse.FromString,
                )
        self.StreamBlocks = channel.unary_stream(
                '/injective_explorer_rpc.InjectiveExplorerRPC/StreamBlocks',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.StreamBlocksRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.StreamBlocksResponse.FromString,
                )
        self.GetPeggyDepositTxs = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetPeggyDepositTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsResponse.FromString,
                )
        self.GetPeggyWithdrawalTxs = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetPeggyWithdrawalTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsResponse.FromString,
                )
        self.GetIBCTransferTxs = channel.unary_unary(
                '/injective_explorer_rpc.InjectiveExplorerRPC/GetIBCTransferTxs',
                request_serializer=exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsResponse.FromString,
                )


class InjectiveExplorerRPCServicer(object):
    """ExplorerRPC defines gRPC API of explorer data for e.g. Blockchain Explorer
    """

    def GetAccountTxs(self, request, context):
        """GetAccountTxs returns tranctions involving in an account based upon params.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlocks(self, request, context):
        """GetBlocks returns blocks based upon the request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlock(self, request, context):
        """GetBlock returns block based upon the height or hash
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidator(self, request, context):
        """GetValidator returns validator information on the active chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidatorUptime(self, request, context):
        """GetValidatorUptime returns validator uptime information on the active chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTxs(self, request, context):
        """GetTxs returns transactions based upon the request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTxByTxHash(self, request, context):
        """GetTxByTxHash returns certain transaction information by its tx hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamTxs(self, request, context):
        """StreamTxs returns transactions based upon the request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamBlocks(self, request, context):
        """StreamBlocks returns the latest blocks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeggyDepositTxs(self, request, context):
        """GetPeggyDepositTxs returns the peggy deposit transactions based upon the
        request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeggyWithdrawalTxs(self, request, context):
        """GetPeggyWithdrawalTxs returns the peggy withdrawal transactions based upon
        the request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIBCTransferTxs(self, request, context):
        """GetIBCTransferTxs returns the ibc transfer transactions based upon the
        request params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveExplorerRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAccountTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsResponse.SerializeToString,
            ),
            'GetBlocks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlocks,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetBlocksRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetBlocksResponse.SerializeToString,
            ),
            'GetBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlock,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetBlockRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetBlockResponse.SerializeToString,
            ),
            'GetValidator': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidator,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorResponse.SerializeToString,
            ),
            'GetValidatorUptime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidatorUptime,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeResponse.SerializeToString,
            ),
            'GetTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetTxsResponse.SerializeToString,
            ),
            'GetTxByTxHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTxByTxHash,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashResponse.SerializeToString,
            ),
            'StreamTxs': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.StreamTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.StreamTxsResponse.SerializeToString,
            ),
            'StreamBlocks': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamBlocks,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.StreamBlocksRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.StreamBlocksResponse.SerializeToString,
            ),
            'GetPeggyDepositTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeggyDepositTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsResponse.SerializeToString,
            ),
            'GetPeggyWithdrawalTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeggyWithdrawalTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsResponse.SerializeToString,
            ),
            'GetIBCTransferTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIBCTransferTxs,
                    request_deserializer=exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsRequest.FromString,
                    response_serializer=exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_explorer_rpc.InjectiveExplorerRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveExplorerRPC(object):
    """ExplorerRPC defines gRPC API of explorer data for e.g. Blockchain Explorer
    """

    @staticmethod
    def GetAccountTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetAccountTxs',
            exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetAccountTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetBlocks',
            exchange_dot_injective__explorer__rpc__pb2.GetBlocksRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetBlocksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetBlock',
            exchange_dot_injective__explorer__rpc__pb2.GetBlockRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetValidator',
            exchange_dot_injective__explorer__rpc__pb2.GetValidatorRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetValidatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidatorUptime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetValidatorUptime',
            exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetValidatorUptimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetTxs',
            exchange_dot_injective__explorer__rpc__pb2.GetTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTxByTxHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetTxByTxHash',
            exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetTxByTxHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/StreamTxs',
            exchange_dot_injective__explorer__rpc__pb2.StreamTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.StreamTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/StreamBlocks',
            exchange_dot_injective__explorer__rpc__pb2.StreamBlocksRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.StreamBlocksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeggyDepositTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetPeggyDepositTxs',
            exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetPeggyDepositTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeggyWithdrawalTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetPeggyWithdrawalTxs',
            exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetPeggyWithdrawalTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIBCTransferTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_explorer_rpc.InjectiveExplorerRPC/GetIBCTransferTxs',
            exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsRequest.SerializeToString,
            exchange_dot_injective__explorer__rpc__pb2.GetIBCTransferTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
