from typing import Mapping, Sequence, TypedDict


class _ApiVersion(TypedDict):
    id: str
    restPath: str


class ApiVersion(_ApiVersion, total=False):
    wsPath: str


class ServerApi(TypedDict):
    versions: Sequence[ApiVersion]


class ServerVersions(TypedDict):
    version: int
    serverVersion: str
    apis: Mapping[str, ServerApi]
