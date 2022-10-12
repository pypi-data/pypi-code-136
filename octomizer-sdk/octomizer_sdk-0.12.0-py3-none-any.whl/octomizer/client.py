"""Python client for the OctoML Platform API."""

from __future__ import annotations

import json
import os
import typing
from datetime import date, datetime, timezone

import google.protobuf.empty_pb2 as empty_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2
import google.protobuf.timestamp_pb2 as timestamp_pb2
import grpc

from octomizer import (
    model,
    model_variant,
    package_workflow_group,
    project,
    user,
    workflow,
)
from octomizer.auth import AuthInterceptor
from octoml.octomizer.v1 import (
    datarefs_pb2,
    hardware_targets_pb2,
    octomizer_service_pb2,
    octomizer_service_pb2_grpc,
    users_pb2,
)

""" Default value for the OctoML API host, if not specified manually or via the environment."""
OCTOMIZER_API_HOST = "api.octoml.ai"
""" Default value for the OctoML API port, if not specified manually or via the environment."""
OCTOMIZER_API_PORT = 443


class OctomizerClient:
    """A client to the OctoML Platform service.

    :param host: The hostname of the OctoML RPC service. Note that this is typically not
        the same as the hostname used to access the OctoML web interface. The default is
        the value of the environment variable ``OCTOMIZER_API_HOST``. This defaults to
        ``api.octoml.ai`` if not specified.
    :param port: The port of the OctoML RPC serivce. The default is the value of the
        environment variable ``OCTOMIZER_API_PORT``, and defaults to 443.
    :param insecure: whether to create an insecure (non-TLS) channel to the
        gRPC server. This is typically used only for testing.
    :param access_token: An OctoML access token. These can be obtained from the web interface
        or via the ``CreateAccessToken`` RPC call.
    :param check_connection: If True, check that the connection is live when the client is created,
        raising a RuntimeError if the connection cannot be established.
    """

    _PAGE_SIZE = 10

    def __init__(
        self,
        host: typing.Optional[str] = None,
        port: typing.Optional[int] = None,
        insecure: bool = False,
        access_token: typing.Optional[str] = None,
        check_connection: bool = True,
    ):
        self._host = (
            host or os.environ.get("OCTOMIZER_API_HOST", None) or OCTOMIZER_API_HOST
        )
        self._port = port or int(
            os.environ.get("OCTOMIZER_API_PORT", None) or OCTOMIZER_API_PORT
        )
        access_token = access_token or os.environ.get("OCTOMIZER_API_TOKEN", None)

        if insecure:
            channel = grpc.insecure_channel(
                f"{self._host}:{self._port}",
                options=[("grpc.service_config", self._retry_config())],
            )
        else:
            credentials = grpc.ssl_channel_credentials()
            channel = grpc.secure_channel(
                f"{self._host}:{self._port}",
                credentials,
                options=[("grpc.service_config", self._retry_config())],
            )

        if access_token is not None:
            channel = grpc.intercept_channel(channel, AuthInterceptor(access_token))

        self._channel = channel
        self._stub = octomizer_service_pb2_grpc.OctomizerServiceStub(channel)

        if check_connection:
            try:
                # This is done to trigger an exception on client creation, to ensure service
                # liveness and the correct hostname/port/access token were provided.
                _ = self.get_current_user()
            except grpc._channel._InactiveRpcError:
                if access_token is not None:
                    # Obscure token from error message.
                    access_token = access_token[0] + ("*" * (len(access_token) - 1))
                raise RuntimeError(
                    f"Unable to connect to OctoML at {self._host}:{self._port} "
                    f"with the access token {access_token}. Check that the hostname, port, and "
                    "access token are correct, by setting the value of the environment variables "
                    "OCTOMIZER_API_HOST, OCTOMIZER_API_PORT, and/or OCTOMIZER_API_TOKEN."
                )

    def __str__(self) -> str:
        return f"OctomizerClient for <{self._host}:{self._port}>"

    def _retry_config(self):
        return json.dumps(
            {
                "methodConfig": [
                    {
                        # Add a retry policy for GetWorkflow and GetIngestModelStatus because
                        # those APIs are idempotent and designed to be polled.
                        "name": [
                            {
                                "service": "octoml.octomizer.v1.OctomizerService",
                                "method": "GetWorkflow",
                            },
                            {
                                "service": "octoml.octomizer.v1.OctomizerService",
                                "method": "GetIngestModelStatus",
                            },
                        ],
                        "retryPolicy": {
                            "maxAttempts": 5,
                            "initialBackoff": "0.5s",
                            "maxBackoff": "10s",
                            "backoffMultiplier": 2,
                            "retryableStatusCodes": ["UNAVAILABLE"],
                        },
                    }
                ]
            }
        )

    @property
    def channel(self) -> grpc.Channel:
        """Returns the underlying gRPC channel used by this OctomizerClient."""
        return self._channel

    @property
    def stub(self) -> octomizer_service_pb2_grpc.OctomizerServiceStub:
        """Return the underlying gRPC client stub used by this OctomizerClient.
        This is useful for cases where you wish to invoke gRPC calls directly."""
        return self._stub

    @property
    def host(self) -> str:
        """Returns the OctoML host that the OctomizerClient connects to."""
        return self._host

    def get_dataref(self, uuid: str) -> datarefs_pb2.DataRef:
        """Returns the DataRef with the given id.

        :param uuid: the id of the DataRef to get.
        :return: the requested DataRef, if it exists.
        """
        request = octomizer_service_pb2.GetDataRefRequest(dataref_uuid=uuid)
        return self._stub.GetDataRef(request)

    def get_project(self, uuid: str) -> project.Project:
        """Returns the Project with the given id.

        :param uuid: the id of the Project to get.
        :return: the requested Project, if it exists.
        """
        request = octomizer_service_pb2.GetProjectRequest(project_uuid=uuid)
        response = self._stub.GetProject(request)
        return project.Project(client=self, proto=response)

    def list_projects(self) -> typing.Iterator[project.Project]:
        """Returns all Projects associted with the current user.

        :return: all the current user's Projects."""
        page_token = None
        while True:
            request = octomizer_service_pb2.ListProjectsRequest(
                page_size=self._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._stub.ListProjects(request)

            for project_proto in response.projects:
                yield project.Project(client=self, proto=project_proto)

            page_token = response.next_page_token
            if not page_token:
                break

    def get_model(self, uuid: str) -> model.Model:
        """Returns the model with the given id.

        :param uuid: the id of the model to get.
        :return: the requested model, if it exists.
        """
        request = octomizer_service_pb2.GetModelRequest(model_uuid=uuid)
        response = self._stub.GetModel(request)
        return model.Model(client=self, proto=response)

    def delete_model(self, uuid: str):
        """Deletes the model with the given id. This deletes all ModelVariants and Workflows
        associated with a model, and cannot be undone.

        :param uuid: the id of the model to delete.
        """
        request = octomizer_service_pb2.DeleteModelRequest(model_uuid=uuid)
        self._stub.DeleteModel(request)

    def list_models(self) -> typing.Iterator[model.Model]:
        """Returns all Models associated with the current user.

        :return: all the current user's Models.
        """
        page_token = None
        while True:
            request = octomizer_service_pb2.ListProjectModelsRequest(
                project_uuid="-",
                page_size=self._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._stub.ListProjectModels(request)

            for model_proto in response.models:
                yield model.Model(client=self, proto=model_proto)

            page_token = response.next_page_token
            if not page_token:
                break

    def get_model_variant(self, uuid: str) -> model_variant.ModelVariant:
        """Returns the model variant with the given id.

        :param uuid: the id of the model variant to get.
        :return: the requested model variant, if it exists.
        """
        request = octomizer_service_pb2.GetModelVariantRequest(model_variant_uuid=uuid)
        model_variant_proto = self._stub.GetModelVariant(request)
        model = self.get_model(model_variant_proto.model_uuid)
        return model_variant.ModelVariant(
            client=self, model=model, proto=model_variant_proto
        )

    def get_workflow(self, uuid: str) -> workflow.Workflow:
        """Returns the workflow with the given id.

        :param uuid: the id of the workflow to get.
        :return: the requested workflow, if it exists.
        """
        request = octomizer_service_pb2.GetWorkflowRequest(workflow_uuid=uuid)
        workflow_proto = self._stub.GetWorkflow(request)
        return workflow.Workflow(client=self, proto=workflow_proto)

    def cancel_workflow(self, uuid: str) -> workflow.Workflow:
        """Cancels the workflow with the given id.

        :param uuid: the id of the workflow to cancel.
        :return: the requested workflow, if it exists.
        """
        request = octomizer_service_pb2.CancelWorkflowRequest(workflow_uuid=uuid)
        workflow_proto = self._stub.CancelWorkflow(request)

        return workflow.Workflow(client=self, proto=workflow_proto)

    def get_package_workflow_group(
        self, uuid: str
    ) -> package_workflow_group.PackageWorkflowGroup:
        """Retrieves the PackageWorkflowGroup with the given id associated with this Model.

        :param uuid: the id of the PackageWorkflowGroup to retrieve.
        :return: the PackageWorkflowGroup associated with this Model that has the given id.
        """
        request = octomizer_service_pb2.GetPackageWorkflowGroupRequest(
            package_workflow_group_uuid=uuid
        )
        response = self.stub.GetPackageWorkflowGroup(request)
        return package_workflow_group.PackageWorkflowGroup(self, proto=response)

    def get_hardware_targets(self) -> typing.List[hardware_targets_pb2.HardwareTarget]:
        """Gets the available hardware targets for the current user's account.

        :return: the list of hardware targets available to the user's account.
        """
        user = self.get_current_user()
        request = octomizer_service_pb2.GetHardwareTargetsRequest(
            account_uuid=user.account_uuid
        )
        return self.stub.GetHardwareTargets(request).hardware_targets

    def get_current_user(self) -> users_pb2.User:
        """Returns the currently-authenticated user."""
        return self._stub.GetCurrentUser(empty_pb2.Empty())

    def get_user(self, uuid: str) -> users_pb2.User:
        """Returns the user with the given id.

        :param uuid: the id of the user to get.
        :return: the requested user, if it exists.
        """
        request = octomizer_service_pb2.GetUserRequest(user_uuid=uuid)
        return self._stub.GetUser(request)

    def get_account(self, uuid: str) -> users_pb2.Account:
        """Returns the account with the given id.

        :param uuid: the id of the account to get.
        :return: the requested account, if it exists.
        """
        request = octomizer_service_pb2.GetAccountRequest(account_uuid=uuid)
        return self._stub.GetAccount(request)

    def get_account_users(self, uuid: str) -> typing.Iterator[users_pb2.User]:
        """Returns all users associated with the account with the given uuid.

        :param uuid: the id of the account whose users to get.
        :return: all the users in the account
        """
        page_token = None
        while True:
            request = octomizer_service_pb2.GetAccountUsersRequest(
                account_uuid=uuid,
                page_size=self._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._stub.GetAccountUsers(request)

            for user_proto in response.members:
                yield user_proto

            page_token = response.next_page_token
            if not page_token:
                break

    def add_user(
        self,
        given_name: str,
        family_name: str,
        email: str,
        active: bool = True,
        is_own_account_admin: bool = False,
        can_accelerate: bool = True,
        account_uuid: typing.Optional[str] = None,
    ) -> users_pb2.User:
        """Creates and returns a user with the given information

        :param given_name: The given name of the new user.
        :param family_name: The family name of the new user.
        :param email: The email associated to the new user.
        :param active: Whether the new user is active (not offboarded).
        :param is_own_account_admin: Whether the new user is an admin of their own account.
        :param can_accelerate: Whether the new user has the ability to trigger octomizations.
        :param account_uuid: uuid corresponding to the account that the new user should be associated to.
        :return: the newly created user
        """
        if account_uuid is None:
            account_uuid = self.get_current_user().account_uuid

        return user.User(
            client=self,
            given_name=given_name,
            family_name=family_name,
            email=email,
            account_uuid=account_uuid,
            active=active,
            is_own_account_admin=is_own_account_admin,
            can_accelerate=can_accelerate,
        ).proto

    def list_users(
        self, account_uuid: typing.Optional[str] = None
    ) -> typing.Iterator[users_pb2.User]:
        """Returns all users associated with the account with the given uuid.

        :param uuid: the id of the account whose users to get.
        :return: all the users in the account
        """
        if account_uuid is None:
            account_uuid = self.get_current_user().account_uuid

        return self.get_account_users(account_uuid)

    def update_user(
        self,
        user_uuid: str,
        given_name: typing.Optional[str] = None,
        family_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        account_uuid: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        is_own_account_admin: typing.Optional[bool] = None,
        can_accelerate: typing.Optional[bool] = None,
    ) -> users_pb2.User:
        """Updates a user's data with the provided parameters

        :param user_uuid: Uuid corresponding to the user whose information should be updated.
        :param given_name: The new given name for the user.
        :param family_name: The new family name for the user.
        :param email: A new email associated to the user.
        :param account_uuid: The uuid corresponding to the new account that the user should be associated to.
        :param active: A new value for whether the user is active (not offboarded).
        :param is_own_account_admin: A new value for whether the user is an admin of their own account.
        :param can_accelerate: A new value for whether the user has the ability to trigger octomizations.
        :return: the updated user
        """
        target_user = user.User(client=self, uuid=user_uuid).proto
        update_mask_paths = []
        if given_name is not None:
            target_user.given_name = given_name
            update_mask_paths.append("given_name")
        if family_name is not None:
            target_user.family_name = family_name
            update_mask_paths.append("family_name")
        if email is not None:
            target_user.email = email
            update_mask_paths.append("email")
        if account_uuid is not None:
            target_user.account_uuid = account_uuid
            update_mask_paths.append("account_uuid")
        if active is not None:
            target_user.active = active
            update_mask_paths.append("active")
        if is_own_account_admin is not None:
            target_user.permissions.is_own_account_admin = is_own_account_admin
            update_mask_paths.append("permissions.is_own_account_admin")
        if can_accelerate is not None:
            target_user.permissions.can_accelerate = can_accelerate
            update_mask_paths.append("permissions.can_accelerate")

        request = octomizer_service_pb2.UpdateUserRequest(
            user=target_user,
            update_mask=field_mask_pb2.FieldMask(paths=update_mask_paths),
        )

        return self._stub.UpdateUser(request)

    def get_usage(
        self,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        account_uuid: typing.Optional[str] = None,
    ) -> typing.List[octomizer_service_pb2.HardwareUsage]:
        """Returns the usage records associated with the user's account.

        :param start_time: Timestamp of the beginning of when to check usage metrics. The default start_time is the first day of the month.
        :param end_time: Timestamp of the end of when to check usage metrics. The default end_time is the first day of next month.
        :param account_uuid: account_uuid to check account usage against. The default account_uuid is the uuid associated to the active user's account.
        :return: a list of usage records associated with the given account.
        """
        if account_uuid is None:
            account_uuid = self.get_current_user().account_uuid

        start_of_month, end_of_month = self.__get_month_start_and_end()
        start_time_proto = timestamp_pb2.Timestamp()
        end_time_proto = timestamp_pb2.Timestamp()

        if start_time is None:
            start_time_proto.FromDatetime(start_of_month)

        if end_time is None:
            end_time_proto.FromDatetime(end_of_month)

        request = octomizer_service_pb2.GetUsageRequest(
            start_time=start_time_proto,
            end_time=end_time_proto,
            account_uuid=account_uuid,
        )

        return self._stub.GetUsage(request).user_usage

    def __get_month_start_and_end(self) -> typing.Tuple[datetime, datetime]:
        today = date.today()
        start_of_month = today.replace(day=1)
        if start_of_month.month == 12:
            end_of_month = start_of_month.replace(year=start_of_month.year + 1, month=1)
        else:
            end_of_month = start_of_month.replace(month=start_of_month.month + 1)

        start_of_month = datetime(
            year=start_of_month.year,
            month=start_of_month.month,
            day=start_of_month.day,
            tzinfo=timezone.utc,
        )

        end_of_month = datetime(
            year=end_of_month.year,
            month=end_of_month.month,
            day=end_of_month.day,
            tzinfo=timezone.utc,
        )
        return start_of_month, end_of_month
