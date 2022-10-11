from prefect.tasks.gcp.storage import GCSBaseTask
from prefect.utilities.tasks import defaults_from_attrs
from prefect.utilities.gcp import get_storage_client
from google.cloud import storage
from google.cloud.exceptions import NotFound
from fnmatch import fnmatch
from logging import getLogger

from typing import *

LOG = getLogger(__name__)


class GCSList(GCSBaseTask):
    def __init__(
        self,
        bucket: Optional[str] = None,
        glob: Optional[str] = None,
        project: Optional[str] = None,
        **kwargs,
    ):
        self.bucket = bucket
        self.glob = glob
        self.project = project
        super().__init__(bucket=bucket, project=project, nout=True, **kwargs)

    @defaults_from_attrs("bucket", "glob", "project")
    def run(
        self,
        bucket: Optional[str] = None,
        glob: Optional[str] = None,
        project: Optional[str] = None,
        credentials: Optional[Dict] = None,
    ) -> List[str]:
        client = get_storage_client(project=project, credentials=credentials)

        bucket = self._retrieve_bucket(
            client=client, bucket=bucket, create_bucket=False
        )

        blobs = bucket.list_blobs(client=client)
        if glob:
            ret = [blob.name for blob in blobs if fnmatch(blob.name, glob)]
        else:
            ret = [blob.name for blob in blobs]

        LOG.info(f"Returning {len(ret)} files")
        return ret


class GCSDelete(GCSBaseTask):
    def __init__(
        self,
        bucket: str = None,
        blob: str = None,
        project: str = None,
        fail_if_not_found: bool = True,
        request_timeout: Union[float, Tuple[float, float]] = 60,
        **kwargs,
    ):
        self.bucket = bucket
        self.blob = blob
        self.project = project
        self.request_timeout = request_timeout
        self.fail_if_not_found = fail_if_not_found
        super().__init__(bucket=bucket, project=project, nout=True, **kwargs)

    @defaults_from_attrs(
        "bucket",
        "blob",
        "project",
        "request_timeout",
        "fail_if_not_found",
    )
    def run(
        self,
        bucket: str = None,
        blob: str = None,
        project: str = None,
        fail_if_not_found: bool = True,
        credentials: dict = None,
        request_timeout: Union[float, Tuple[float, float]] = 60,
    ) -> str:
        if None in [bucket, blob]:
            raise ValueError("Missing bucket_name or blob")

        client = get_storage_client(project=project, credentials=credentials)

        bucket = client.bucket(bucket)
        blob_ref = storage.Blob(bucket=bucket, name=blob)

        try:
            blob_ref.delete(client)
        except NotFound as e:
            if fail_if_not_found:
                raise e

        return blob
