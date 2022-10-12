import time
from typing import Any, Generator, List, Callable
from clients_core.service_clients import E360ServiceClient
from clients_core.exceptions import ClientValueError  # noqa: F401
from pydantic import parse_obj_as
from .models import (
    JobCreateModel,
    JobModel,
    JobResultPath,
    State,
    TaskStatusModel,
    JobSubmitModel,
)


class AWJobsClient(E360ServiceClient):
    """
    Subclasses dataclass `clients_core.service_clients.E360ServiceClient`.

    Args:
        client (clients_core.rest_client.RestClient): an instance of a rest client
        user_id (str): the user_id guid

    """

    service_endpoint = ""
    CHUNK_SIZE = 1024 * 1024  # 1MB

    def create(self, model: JobCreateModel, **kwargs: Any) -> JobModel:
        """
        Create a new AW job.

        Args:
            model: job submission model including the payload
        Raises:
            pydantic.ValidationError: when the model creation fails validation

        """
        response = self.client.post(
            self.service_endpoint,
            json=model.dict(by_alias=True),
            headers=self.service_headers,
            raises=True,
            **kwargs,
        )
        return JobModel.parse_obj(response.json())

    def get_by_id(self, job_id: str, **kwargs: Any) -> JobModel:
        url = f"{job_id}/"
        response = self.client.get(
            url, headers=self.service_headers, raises=True, **kwargs
        )
        return JobModel.parse_obj(response.json())

    def modify(self, job_id: str, patches: List[dict], **kwargs: Any) -> JobModel:
        """Performs a patch method on an existing job id with a patch document"""
        url = f"{self.service_endpoint}/{job_id}/"
        response = self.client.patch(
            url,
            json=patches,
            headers=self.service_headers,
            raises=True,
            **kwargs,
        )
        return JobModel.parse_obj(response.json())

    def update(self, job_id: str, model: JobCreateModel, **kwargs: Any) -> JobModel:
        """Updates the entire job record with a new JobCreateModel payload"""
        url = f"{self.service_endpoint}/{job_id}/"
        response = self.client.put(
            url,
            json=model.dict(by_alias=True),
            headers=self.service_headers,
            raises=True,
            **kwargs,
        )
        return JobModel.parse_obj(response.json())

    def submit_job_by_id(
        self, job_id: str, model: JobSubmitModel = None, **kwargs: Any
    ) -> bool:
        url = f"{job_id}/submit/"
        submit_model = model.dict(by_alias=True) if model else None
        response = self.client.post(
            url, json=submit_model, headers=self.service_headers, raises=True, **kwargs
        )
        return response.ok

    def job_task_status_by_id(self, job_id: str, **kwargs: Any) -> TaskStatusModel:
        url = f"{job_id}/task/"
        response = self.client.get(
            url, headers=self.service_headers, raises=True, **kwargs
        )
        return TaskStatusModel.parse_obj(response.json())

    def job_get_results_by_id(self, job_id: str, **kwargs: Any) -> List[JobResultPath]:
        url = f"{job_id}/results/"
        response = self.client.get(
            url, headers=self.service_headers, raises=True, **kwargs
        )
        return parse_obj_as(List[JobResultPath], response.json())

    def job_get_binary_results_by_name(
        self, job_id: str, name: str, **kwargs: Any
    ) -> Generator[bytes, None, None]:
        url = f"{job_id}/results/{name}/"
        headers = self.service_headers.copy()
        headers.update({"accept": "application/octet-stream"})
        response = self.client.get(
            url, raises=True, stream=True, headers=headers, **kwargs
        )
        return response.iter_content(chunk_size=self.CHUNK_SIZE)

    def submit_job_payload(
        self, model: JobCreateModel, submit_model: JobSubmitModel = None, **kwargs: Any
    ) -> JobModel:
        """
        Submits a job and waits for the method completion then returns job details.
        """
        job = self.create(model, **kwargs)
        if job.id:
            self.submit_job_by_id(job.id, submit_model)
            self.wait_for_job(job.id)
            return self.get_by_id(job.id)
        raise ClientValueError(f"AW job failed to create with model: {model}")

    def wait_for_job(
        self,
        job_id: str,
        sleep_time: float = 5.0,  # 5 seconds
        poll_limit: int = (60 * 60 * 2),  # 2 hours
        callback: Callable[[str], None] = print,
        **kwargs: Any,
    ) -> None:
        """
        Poll Job Status GET endpoint until status is complete

        Args:
            poll_limit: int, seconds for total time to poll for; default 2 hours
            sleep_time: float, seconds interval between the sleeps; default 5 seconds
            callback: function, for feeding updates on the polling status; default <built-in function print>

        """

        max_retries = poll_limit // sleep_time
        for _ in range(1, int(max_retries) + 1):
            time.sleep(sleep_time)
            task = self.job_task_status_by_id(job_id)
            if task.state in (State.SUCCESS, State.FAILED):
                return
            callback(
                f"AW job status: {task.status.get('statusText')} ({sleep_time * _} seconds)"
            )

        raise TimeoutError("Polling limit reached before job completion")
