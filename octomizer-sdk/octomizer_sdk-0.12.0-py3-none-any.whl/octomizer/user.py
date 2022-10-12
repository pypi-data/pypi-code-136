from __future__ import annotations

import typing

import grpc
from grpc_status import rpc_status

from octomizer import client
from octoml.octomizer.v1 import error_pb2, octomizer_service_pb2, users_pb2


class UserCreationError(RuntimeError):
    pass


class User:
    def __init__(
        self,
        client: client.OctomizerClient,
        given_name: typing.Optional[str] = None,
        family_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        account_uuid: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        is_own_account_admin: typing.Optional[bool] = None,
        can_accelerate: typing.Optional[bool] = None,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[users_pb2.User] = None,
    ):
        """Creates a new User.

        There are three ways to use this constructor:
          (1) The client passes in a given name, family name, email, account UUID, active flag,
              and permissions object. A new user is created on the service with the given parameters.
          (2) The client passes in a user UUID. An existing user with the given UUID is
              fetched from the service.
          (3) The client provides a fully-populated `users_pb2.User` protobuf message.

        :param client: an instance of the OctoML Platform client. Required.
        :param given_name: the given name of the user.
        :param family_name: the family name of the user.
        :param email: the email of the user.
        :param account_uuid: the UUID corresponding to the account that owns this user.
        :param active: if the user is active (not offboarded).
        :param permissions: the permissions given to the user.
        :param uuid: UUID of a User already existing in the OctoML Platform. If provided,
            no other values other than `client` should be specified.
        :param proto: the underyling protobuf object wrapped by this Model. If provided,
            no other values other than `client` should be specified.
        """
        self._client = client
        if proto is not None:
            # case: proto was supplied by client.
            assert uuid is None
            assert given_name is None
            assert family_name is None
            assert email is None
            assert account_uuid is None
            assert active is None
            assert is_own_account_admin is None
            assert can_accelerate is None
            self._proto = proto
        elif uuid is not None:
            # case: We are fetching an existing user from the service.
            assert given_name is None
            assert family_name is None
            assert email is None
            assert account_uuid is None
            assert active is None
            assert is_own_account_admin is None
            assert can_accelerate is None
            self._proto = self._get_user_by_uuid(uuid)
        else:
            # case: We are creating a new model with the given data.
            assert given_name is not None
            assert family_name is not None
            assert email is not None
            assert account_uuid is not None
            assert active is not None
            assert is_own_account_admin is not None
            assert can_accelerate is not None
            self._proto = self._create(
                given_name,
                family_name,
                email,
                account_uuid,
                active,
                is_own_account_admin,
                can_accelerate,
            )

    @property
    def proto(self) -> users_pb2.User:
        """Return the underlying protobuf describing this User."""
        return self._proto

    @property
    def uuid(self) -> str:
        """Return the UUID for this User."""
        return self._proto.uuid

    @property
    def given_name(self) -> str:
        """Return the given name for this User."""
        return self._proto.given_name

    @property
    def family_name(self) -> str:
        """Return the family name for this User."""
        return self._proto.family_name

    @property
    def account_uuid(self) -> str:
        """Return the account UUID for this User."""
        return self._proto.account_uuid

    @property
    def active(self) -> bool:
        """Return a value for if this User is active (not offboarded)."""
        return self._proto.active

    @property
    def permissions(self) -> users_pb2.Permissions:
        """Returns the permissions this User has."""
        return self._proto.permissions

    def _get_user_by_uuid(self, uuid: str) -> users_pb2.User:
        """Get the user proto for the given UUID from the OctoML Platform.

        :param uuid: the user UUID to retrieve.
        """
        request = octomizer_service_pb2.GetUserRequest(user_uuid=uuid)
        return self._client.stub.GetUser(request)

    def _create(
        self,
        given_name: str,
        family_name: str,
        email: str,
        account_uuid: str,
        active: bool,
        is_own_account_admin: bool = False,
        can_accelerate: bool = True,
    ) -> users_pb2.User:
        """Create a User in the OctoML Platform."""
        userpb = users_pb2.User(
            given_name=given_name,
            family_name=family_name,
            email=email,
            account_uuid=account_uuid,
            active=active,
            permissions=users_pb2.Permissions(
                is_own_account_admin=is_own_account_admin,
                can_accelerate=can_accelerate,
            ),
        )

        request = octomizer_service_pb2.CreateUserRequest(user=userpb)

        try:
            proto = self._client.stub.CreateUser(request)
            return proto
        except grpc.RpcError as rpc_error:
            status = rpc_status.from_call(rpc_error)
            for detail in status.details:
                if detail.Is(error_pb2.ErrorDetails.DESCRIPTOR):
                    info = error_pb2.ErrorDetails()
                    detail.Unpack(info)
                    raise UserCreationError(
                        f"failed to create user: {status.message} {info}"
                    )
            raise rpc_error
