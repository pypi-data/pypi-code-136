# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from strmprivacy.api.organizations.v1 import organizations_v1_pb2 as strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2


class OrganizationsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InviteUsers = channel.unary_unary(
                '/strmprivacy.api.organizations.v1.OrganizationsService/InviteUsers',
                request_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersRequest.SerializeToString,
                response_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersResponse.FromString,
                )
        self.UpdateUserRoles = channel.unary_unary(
                '/strmprivacy.api.organizations.v1.OrganizationsService/UpdateUserRoles',
                request_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesRequest.SerializeToString,
                response_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/strmprivacy.api.organizations.v1.OrganizationsService/GetUser',
                request_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserRequest.SerializeToString,
                response_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserResponse.FromString,
                )
        self.ListOrganizationMembers = channel.unary_unary(
                '/strmprivacy.api.organizations.v1.OrganizationsService/ListOrganizationMembers',
                request_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersRequest.SerializeToString,
                response_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersResponse.FromString,
                )


class OrganizationsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InviteUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserRoles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrganizationMembers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InviteUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.InviteUsers,
                    request_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersRequest.FromString,
                    response_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersResponse.SerializeToString,
            ),
            'UpdateUserRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserRoles,
                    request_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesRequest.FromString,
                    response_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserRequest.FromString,
                    response_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserResponse.SerializeToString,
            ),
            'ListOrganizationMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrganizationMembers,
                    request_deserializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersRequest.FromString,
                    response_serializer=strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'strmprivacy.api.organizations.v1.OrganizationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrganizationsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InviteUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strmprivacy.api.organizations.v1.OrganizationsService/InviteUsers',
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersRequest.SerializeToString,
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.InviteUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strmprivacy.api.organizations.v1.OrganizationsService/UpdateUserRoles',
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesRequest.SerializeToString,
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.UpdateUserRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strmprivacy.api.organizations.v1.OrganizationsService/GetUser',
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserRequest.SerializeToString,
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrganizationMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strmprivacy.api.organizations.v1.OrganizationsService/ListOrganizationMembers',
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersRequest.SerializeToString,
            strmprivacy_dot_api_dot_organizations_dot_v1_dot_organizations__v1__pb2.ListOrganizationMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
