from typing import Dict

from pydantic import Field

from kognic.io.model.base_serializer import BaseSerializer


class InputJobCreated(BaseSerializer):
    input_uuid: str = Field(alias='internalId')
    files: Dict[str, str]

    def __str__(self):
        return f"{self.__class__.__name__}(input_uuid={self.input_uuid}, files={{...}})"


class CreateInputResponse(BaseSerializer):
    input_uuid: str

    @staticmethod
    def from_input_job_response(input_job: InputJobCreated):
        return CreateInputResponse(input_uuid=input_job.input_uuid)
