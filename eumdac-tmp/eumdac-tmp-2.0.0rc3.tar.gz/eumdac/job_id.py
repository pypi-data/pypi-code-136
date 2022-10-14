from threading import Lock
from typing import Any, Dict

from eumdac.errors import EumdacError


class JobIdentifactor:
    def __init__(self, total_jobs: int):
        self.current_count = 0
        self.total_jobs = total_jobs
        self._lock = Lock()
        self.registered_objects: Dict[Any, int] = {}

    def register(self, obj: Any) -> None:
        if obj in self.registered_objects:
            raise JobIdError(f"Object '{obj}' already registered.")
        self.registered_objects[obj] = self._make_new_job_id()

    def job_id_str(self, obj: Any) -> str:
        try:
            return f"Job {self.registered_objects[obj]}:"
        except KeyError as exc:
            raise JobIdError(
                f"No Job ID for '{obj}'. Available ones: {list(self.registered_objects.keys())}"
            )

    def _make_new_job_id(self) -> int:
        with self._lock:
            self.current_count += 1
            if self.current_count > self.total_jobs:
                raise JobIdError(
                    "Too many Job IDs requested. "
                    f"Expected a maximum of {self.total_jobs} Job ID requests"
                )
            return self.current_count


class JobIdError(EumdacError):
    pass
