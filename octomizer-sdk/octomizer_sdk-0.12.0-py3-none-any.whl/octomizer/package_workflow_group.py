"""Resource representing a PackageWorkflowGroup."""
from __future__ import annotations

import time
import typing

from octomizer import client, workflow
from octoml.octomizer.v1 import workflows_pb2

DEFAULT_PACKAGE_WORKFLOW_GROUP_TIMEOUT_SECONDS = 1800
"""The default number of seconds to wait for a PackageWorkflowGroup to finish."""

DEFAULT_PACKAGE_WORKFLOW_GROUP_POLL_INTERVAL_SECONDS = 30
"""The default number of seconds to wait between polling for statuses."""


class PackageWorkflowGroupTimeoutError(Exception):
    """Indicates a PackageWorkflowGroup timed out while being awaited."""


class PackageWorkflowGroup:
    """Represents an OctoML PackageWorkflowGroup."""

    def __init__(
        self,
        client: client.OctomizerClient,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[workflows_pb2.PackageWorkflowGroup] = None,
    ):
        """Initializes a new PackageWorkflowGroup.

        :param client: an instance of the OctoML client.
        :param uuid: the id of this PackageWorkflowGroup in the OctoML Platform.
        :param proto: the underyling protobuf object wrapped by this PackageWorkflowGroup.
        """
        self._client = client

        if proto:
            # Proto has been provided.
            self._proto = proto
        elif uuid:
            # Fetch PackageWorkflowGroup by UUID.
            self._proto = self._client.get_package_workflow_group(uuid).proto
        else:
            # This is a new PackageWorkflowGroup builder.
            self._proto = workflows_pb2.PackageWorkflowGroup()
        self._workflows = [
            workflow.Workflow(client, proto=workflow_proto)
            for workflow_proto in self._proto.workflows
        ]

    def __str__(self) -> str:
        return str(self._proto)

    @property
    def uuid(self) -> str:
        """Return the UUID for this PackageWorkflowGroup."""
        return self._proto.uuid

    @property
    def proto(self) -> workflows_pb2.PackageWorkflowGroup:
        """Return the raw representation for this PackageWorkflowGroup."""
        return self._proto

    @property
    def workflows(self) -> typing.List[workflow.Workflow]:
        return self._workflows

    def done(self) -> bool:
        """Returns True if all Workflows have finished."""
        self.refresh()
        return all([workflow.is_terminal() for workflow in self._workflows])

    def refresh(self) -> PackageWorkflowGroup:
        """Get the latest status of this Workflow from the OctoML Platform."""
        self._proto = self._client.get_package_workflow_group(self.uuid).proto
        self._workflows = [
            workflow.Workflow(self._client, proto=workflow_proto)
            for workflow_proto in self._proto.workflows
        ]
        return self

    def wait(  # type: ignore
        self,
        timeout: typing.Optional[int] = DEFAULT_PACKAGE_WORKFLOW_GROUP_TIMEOUT_SECONDS,
        poll_interval: int = DEFAULT_PACKAGE_WORKFLOW_GROUP_POLL_INTERVAL_SECONDS,
        poll_callback: typing.Optional[
            typing.Callable[[PackageWorkflowGroup], None]
        ] = None,
    ) -> bool:
        """Waits until this PackageWorkflowGroup has finished or the given timeout has elapsed.

        :param timeout: the number of seconds to wait for this PackageWorkflowGroup.
        :param poll_interval: the number of seconds to wait between polling for the
            status of this PackageWorkflowGroup.
        :param poll_callback: Optional callback invoked with `self` as an argument each time
            the PackageWorkflowGroup status is polled.
        :return: whether the PackageWorkflowGroup completed or not.
        :raise: PackageWorkflowGroupTimeoutError if timeout seconds elapse before the
            Workflows in the group reach a terminal state.
        """
        start_time = time.time()
        while not self.done():
            assert self._proto is not None
            if poll_callback is not None:
                poll_callback(self)
            if timeout is not None and time.time() - start_time > timeout:
                raise PackageWorkflowGroupTimeoutError(
                    f"Timeout occurred while waiting on group {self._proto.uuid}."
                )
            time.sleep(poll_interval)

        if poll_callback is not None:
            poll_callback(self)
        return self.done()

    def cancel(self) -> PackageWorkflowGroup:
        """Cancel this Workflows in this PackageWorkflowGroup."""
        self._workflows = [wf.cancel() for wf in self._workflows]
        self.refresh()
        return self
