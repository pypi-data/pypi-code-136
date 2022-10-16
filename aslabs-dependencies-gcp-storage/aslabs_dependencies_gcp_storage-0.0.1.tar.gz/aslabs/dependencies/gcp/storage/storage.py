from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
from dataclasses import dataclass
from google.cloud import storage


@dataclass
class StorageClientConfig:
    sa_file: str


def storage_client_resolver(config: Optional[StorageClientConfig]) -> storage.Client:
    if config and config.sa_file:
        return storage.Client.from_service_account_json(config.sa_file)
    else:
        return storage.Client()


T = TypeVar("T")


class StorageClientResolver(ResolverABC):
    def __init__(self):
        self._client = None

    def __call__(self, deps: DependenciesABC) -> T:
        if self._client is None:
            self._client = storage_client_resolver(
                deps.get_optional(StorageClientConfig))
        return self._client

    @property
    def resolved_type(self) -> Type[T]:
        return storage.Client
