from functools import partial
from typing import Any, Dict, Iterable, List, Optional, Sequence, cast

import backoff
import httpx
from typing_extensions import Self

from infiniaml_idp_client._common.constants import IDP_URL
from infiniaml_idp_client.models import Job, JobInput, JobStatus, JobWithResults

from .credentials import TokenCredential
from .idp_client import IdpClient
from .paginator import PaginatedItem

__all__ = ("JobClient",)


class JobClient:
    def __init__(
        self,
        project_id: int,
        token_credential: TokenCredential,
        *,
        idp_url: str = IDP_URL,
    ) -> None:
        """Create an IDP JobClient

        Args:
            project_id: The project ID the jobs will be created under
            token_credential: A token credential instance used for authentication
        """
        self._idp_client = IdpClient(token_credential, idp_url)
        self._project_id = project_id

    def __enter__(self) -> Self:
        self._idp_client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._idp_client.__exit__()

    def close(self) -> None:
        self._idp_client.close()

    def _project_path(self) -> str:
        return f"/api/v1/projects/{self._project_id}"

    def _jobs_path(self) -> str:
        return "/".join((self._project_path(), "jobs"))

    def _job_path(self, uuid: str) -> str:
        return "/".join((self._jobs_path(), uuid))

    def create(self, input: JobInput) -> Job:
        """Create a new job

        Args:
            input: Job input that contains the document to
                be processed
        """
        files = {"document": input["document"]}
        data = cast(Dict[str, Any], input)
        data.pop("document")
        resp = self._idp_client.post(
            self._jobs_path(),
            data=data,
            files=files,
        )
        return Job(**resp.json()[0])

    def process(self, input: JobInput, *, max_time: float = float("inf")) -> JobWithResults:
        """Create a new job and wait until it is processed

        Args:
            input: Job input that contains the document to
                be processed
            max_time: The maximum amount of time in seconds this method is allowed to take
                before a ValueError is thrown
        """

        job = self.create(input)

        @backoff.on_exception(backoff.expo, ValueError, max_time=max_time)
        def inner():
            fetched_job = cast(JobWithResults, self.get(job["uuid"]))
            if fetched_job["status"] == JobStatus.PROCESSING:
                raise ValueError("Job is still processing")
            return fetched_job

        return inner()

    def get(self, uuid: str) -> Optional[JobWithResults]:
        """Get a job by its UUID"""
        try:
            resp = self._idp_client.get(self._job_path(uuid))
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 404:
                return None
            raise
        return resp.json()

    @backoff.on_exception(backoff.expo, ValueError, max_tries=20)
    def _get_completed(self, uuid: str):
        resp = self._idp_client.get(self._job_path(uuid))
        if resp.json().get("status") == JobStatus.PROCESSING:
            raise ValueError("Job is still processing")
        return resp.json()

    def _list_impl(
        self,
        page: int,
        count: int,
        *,
        status: Optional[JobStatus] = None,
        uuids: Optional[Iterable[str]] = None,
    ) -> List[Job]:
        params: Dict[str, Any] = {
            "per": count,
            "page": page,
        }
        if status:
            params["status"] = status.value
        if uuids:
            params["uuid"] = list(uuids)
        try:
            resp = self._idp_client.get(self._jobs_path(), params=params)
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 404:
                return []
            raise
        return resp.json()["jobs"]

    def list(
        self,
        *,
        count: int = 10,
        status: Optional[JobStatus] = None,
        uuids: Optional[Iterable[str]] = None,
    ):
        """List jobs with pagination

        Args:
            count: Number of jobs returned per page
            status: Filter for job status
            uuids: Filter for job uuids
        """
        get_page = cast(_GetPage, partial(self._list_impl, count=count, status=status, uuids=uuids))
        return PaginatedItem(_PageIncrementor(get_page))


class _GetPage:
    def __call__(self, *, page: int) -> Sequence[Job]:
        ...


class _PageIncrementor:
    def __init__(self, list_func: _GetPage) -> None:
        self._page = 1
        self._list_func = list_func

    def __call__(self) -> Sequence[Job]:
        job = self._list_func(page=self._page)
        self._page += 1
        return job
