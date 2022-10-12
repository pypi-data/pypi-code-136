"""Generic wrapper for Projects in the Octomizer."""
from __future__ import annotations

import typing

from octomizer import client, model
from octoml.octomizer.v1 import octomizer_service_pb2, projects_pb2


class Project:
    """Represents a Project in the Octomizer system."""

    def __init__(
        self,
        client: client.OctomizerClient,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.List[str] = None,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[projects_pb2.Project] = None,
    ):
        """Creates a new Project.

        There are three ways to use this constructor:
          (1) The client passes in a project object, name, description,
              and labels. A new project is created on the service with the given parameters.
          (2) The client passes in a project UUID. An existing project with the given UUID is
              fetched from the service.
          (3) The client provides a fully-populated `projects_pb2.Project` protobuf message.

        :param client: an instance of the Octomizer client. Required.
        :param name: the name of the project. Required.
        :param description: a description of the project.
        :param labels: tags for the Project.
        :param uuid: UUID of a Project already existing in the Octomizer. If provided,
            no other values other than `client` should be specified.
        :param proto: the underyling protobuf object wrapped by this Project. If provided,
            no other values other than `client` should be specified.
        """
        self._client = client

        if proto is not None:
            # assert
            assert name is None
            assert description is None
            assert uuid is None
            assert labels is None
            self._proto = proto
        elif uuid is not None:
            assert name is None
            assert description is None
            assert labels is None
            assert proto is None
            self._proto = self._get_project_by_uuid(uuid)
        else:
            assert name is not None
            assert uuid is None
            self._proto = self._create_project(name, description, labels)

    def __str__(self) -> str:
        return str(self._proto)

    @property
    def proto(self) -> projects_pb2.Project:
        """Return the underlying protobuf describing this Project."""
        return self._proto

    @property
    def uuid(self) -> str:
        """Return the UUID for this Project."""
        return self._proto.uuid

    def _get_project_by_uuid(self, uuid: str) -> projects_pb2.Project:
        """Get the Project protobuf for the given UUID from the Octomizer service.

        :param uuid: the Project UUID to retrieve.
        """
        request = octomizer_service_pb2.GetProjectRequest(project_uuid=uuid)
        return self._client.stub.GetProject(request)

    def _create_project(
        self,
        name: str,
        description: typing.Optional[str],
        labels: typing.Optional[typing.List[str]],
    ) -> projects_pb2.Project:
        project = projects_pb2.Project(
            name=name, description=description, labels=labels
        )
        request = octomizer_service_pb2.CreateProjectRequest(project=project)
        return self._client.stub.CreateProject(request)

    def list_models(
        self,
    ) -> typing.Iterator[model.Model]:
        """Retrieves all Models associated with this Project.

        :return: all Models associated with this Project.
        """
        page_token = None
        while True:
            request = octomizer_service_pb2.ListProjectModelsRequest(
                project_uuid=self.uuid,
                page_size=self._client._PAGE_SIZE,
                page_token=page_token,
            )
            response = self._client.stub.ListProjectModels(request)

            for model_proto in response.models:
                yield model.Model(
                    client=self._client,
                    proto=model_proto,
                    project=self,
                )

            page_token = response.next_page_token
            if not page_token:
                break
