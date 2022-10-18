from fastapi import BackgroundTasks

from ehelply_microservice_library.integrations.logging import Log
from ehelply_microservice_library.integrations.monitor import Monitor, UsageMQ
from ehelply_microservice_library.utils.ehelply_cloud import (
    ehelply_cloud_access,
    CloudParticipantAuthRequest,
    CloudParticipantResponse,
)


class ManagerBase:
    def __init__(
        self,
            cloud_participant: CloudParticipantResponse | None,
            logger: Log | None, monitor: Monitor | None, background_tasks: BackgroundTasks | None
    ):
        self.cloud_participant: CloudParticipantResponse | None = cloud_participant
        self.logger: Log | None = logger
        self.monitor: Monitor | None = monitor
        self.background_tasks: BackgroundTasks | None = background_tasks

        self.usage: dict[str, int] = {}

    @classmethod
    async def with_auth(
            cls, auth: CloudParticipantAuthRequest,
            logger: Log | None, monitor: Monitor | None, background_tasks: BackgroundTasks | None
    ):
        cloud_participant: CloudParticipantResponse = await ehelply_cloud_access(auth=auth)
        return cls(cloud_participant, logger, monitor, background_tasks)

    def add_usage(self, usage_type: str, amount: int):
        if usage_type in self.usage:
            self.usage[usage_type] += amount
        else:
            self.usage[usage_type] = amount

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.background_tasks and self.monitor and self.cloud_participant:
            for usage_type, amount in self.usage:
                self.background_tasks.add_task(self.monitor.add_usage, UsageMQ(
                    project_uuid=self.cloud_participant.project_uuid,
                    usage_key=usage_type,
                    quantity=amount
                ))
