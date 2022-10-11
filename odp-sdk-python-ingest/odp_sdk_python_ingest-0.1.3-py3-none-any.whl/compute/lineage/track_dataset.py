import prefect
from prefect.utilities.tasks import defaults_from_attrs
from dataclasses import dataclass
from typing import Optional


class TrackDataset(prefect.Task):
    pass


@dataclass
class TrackRemoteHttpDataset(TrackDataset):
    url: Optional[str] = None
    method: Optional[str] = None
    mime_type: Optional[str] = None
    encoding: Optional[str] = None
    auth: Optional[bool] = None

    @defaults_from_attrs("url", "method", "mime_type", "encoding", "auth")
    def run(
        self,
        url: Optional[str] = None,
        method: Optional[str] = None,
        mime_type: Optional[str] = None,
        encoding: Optional[str] = None,
        auth: Optional[bool] = None,
    ) -> None:
        return url


class TrackCloudStorage(TrackDataset):
    provider: Optional[str] = None


@dataclass
class TrackAzureStorage(TrackCloudStorage):
    provider = "Azure"
    storage_account: Optional[str] = None
    container: Optional[str] = None
    blob: Optional[str] = None

    @defaults_from_attrs("provider", "storage_account", "container", "blob")
    def run(
        self,
        provider: Optional[str] = None,
        storage_account: Optional[str] = None,
        container: Optional[str] = None,
        blob: Optional[str] = None,
    ) -> str:
        return blob


@dataclass
class TrackDatabase(TrackDataset):
    uri: Optional[str] = None
    schema: Optional[str] = None
    table: Optional[str] = None
    table_ref: Optional[str] = None

    @defaults_from_attrs("uri", "schema", "table", "table_ref")
    def run(
        self,
        uri: Optional[str],
        schema: Optional[str],
        table: Optional[str],
        table_ref: Optional[str],
    ) -> str:
        return table or table_ref


track_remote_http_dataset = TrackRemoteHttpDataset()
track_azure_storage = TrackAzureStorage()
track_database = TrackDatabase()


__all__ = [
    "TrackRemoteHttpDataset",
    "TrackAzureStorage",
    "TrackDatabase",
    "track_remote_http_dataset",
    "track_azure_storage",
    "track_database",
]
