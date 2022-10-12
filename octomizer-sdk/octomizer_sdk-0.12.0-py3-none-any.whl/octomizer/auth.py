"""Helper classes for authenticating via gRPC."""

import collections

import grpc


class _ClientCallDetails(
    collections.namedtuple(
        "_ClientCallDetails", ("method", "timeout", "metadata", "credentials")
    ),
    grpc.ClientCallDetails,
):
    """
    A helper class that allows updating fields of a client call.
    """

    pass


class AuthInterceptor(grpc.UnaryUnaryClientInterceptor):
    """
    This class intercepts outbound gRPC calls and adds an `Authorization: Bearer` header
    carrying an access token.

    :param access_token: The token to send in the `Authorization` header.
    """

    def __init__(self, access_token):
        self.access_token = access_token

    def intercept_unary_unary(self, continuation, client_call_details, request):
        """Invoked by gRPC when issuing a request using this interceptor."""
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.append(("authorization", "Bearer " + self.access_token))
        client_call_details = _ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
        )
        return continuation(client_call_details, request)
