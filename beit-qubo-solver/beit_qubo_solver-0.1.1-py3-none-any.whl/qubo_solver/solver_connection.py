import abc
from copy import deepcopy
import enum
from functools import wraps
import json
from typing import cast, Dict, Optional, Tuple

from beit.runfiles import runfiles
import requests
from requests.status_codes import codes

from beit.qubo_solver.endpoint import APIEndpoint, APIError
from beit.qubo_solver.qubo_instance import QuboInstance, QuboSolution


API_PREFIX = "https://qubo-solver.pro.beit.tech/v1"
RUNFILES = runfiles.Create()

def _schema(path_to_schema: str):
    with open(RUNFILES.Rlocation(path_to_schema)) as schema_file:
        return json.load(schema_file)

class JobError(Exception):
    pass


class JobStatus(enum.Enum):
    PENDING = 0
    DONE = 1
    ERROR = 2


class Job(abc.ABC):
    """
    Represents job posted for remote execution.
    """

    @property
    @abc.abstractmethod
    def status(self) -> JobStatus:
        pass

    @property
    @abc.abstractmethod
    def result(self) -> Optional[Tuple[QuboSolution]]:
        pass

    @abc.abstractmethod
    def request_result(self):
        """Tries to retrieve result of the running job"""
        pass


class SolverConnection(abc.ABC):
    """
        Responsible for creating jobs.
    """

    @abc.abstractmethod
    def create_job(self, qubo_instance) -> Job:
        pass


class AWSJob(Job):
    """Job running on BEIT Qubo Solver"""

    SOLUTION_ENDPOINT = APIEndpoint(
        url=API_PREFIX + "/solution",
        method="POST",
        request_schema=_schema("qubo_solver/schemas/result.json"),
        response_schema=_schema("qubo_solver/schemas/result_response.json"),
    )

    def __init__(self, job_id: str, customer_key: str):
        self._job_id = job_id
        self._customer_key = customer_key
        self._status = JobStatus.PENDING
        self._result: Optional[Tuple[QuboSolution]] = None

    @staticmethod
    def _remember_failure(method):
        @wraps(method)
        def _inner(self, *args, **kwargs):
            try:
                result = method(self, *args, **kwargs)
            except Exception:
                self._status = JobStatus.ERROR
                raise
            self._status = result
            return result
        return _inner
    
    @property
    def result(self) -> Optional[Tuple[QuboSolution]]:
        return deepcopy(self._result)

    @property    
    def status(self) -> JobStatus:
        return self._status

    @_remember_failure
    def request_result(self) -> JobStatus:
        """Tries to retrieve result of the running job"""
        if self._status != JobStatus.PENDING:
            return self._status
        body, response = self.SOLUTION_ENDPOINT.execute(
            {"job_id": self._job_id},
            headers={"x-api-key": self._customer_key}
        )
        if response.status_code != codes.ok:
            raise JobError(f"Something went wrong, API returned code {response.status_code}" + 
                (f" reason given {body['error']}" if 'error' in body else "")
            )
        if body == {}:
            return JobStatus.PENDING
        self._result = cast(Tuple[QuboSolution], tuple(QuboSolution.from_json(sample) for sample in body['samples']))
        return JobStatus.DONE


class AWSSolverConnection(SolverConnection):

    SOLVE_ENDPOINT = APIEndpoint(
        url=API_PREFIX + "/solve",
        method="POST",
        request_schema=_schema("qubo_solver/schemas/solve.json"),
        response_schema=_schema("qubo_solver/schemas/solve_response.json"),
    )

    def __init__(self, customer_key: str):
        self._customer_key = customer_key

    
    def create_job(self, qubo_instance: QuboInstance) -> AWSJob:
        """Creates a job"""
        body, response = self.SOLVE_ENDPOINT.execute(
            {"instance": [{"edge": list(edge), "weight": weight} for edge, weight in qubo_instance.items()]},
            headers={"x-api-key": self._customer_key}
        )
        if response.status_code == codes.created:
            return AWSJob(body['task_key'], self._customer_key)
        raise JobError(
            f"Posting job failed with code {response.status_code}" + 
            f' with message: "{body["error"]}"' if 'error' in body else ""
        )
