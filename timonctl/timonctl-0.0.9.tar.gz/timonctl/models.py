from datetime import datetime
from typing import Dict, Optional
import uuid as uuid_pkg

from pydantic import BaseModel, Json

from .enums import DeploymentAction, DeploymentStatus


class Result(BaseModel):
    status_code: int
    headers: Dict
    message: str = ""
    data: Json


class TimonBaseModel(BaseModel):
    id: uuid_pkg.UUID
    created_at: datetime

    # https://python.tutorialink.com/short-way-to-get-all-field-names-of-a-pydantic-class/
    @classmethod
    def get_field_names(cls, alias=False):
        return list(cls.schema(alias).get("properties").keys())


# blueprint

class BlueprintBase(BaseModel):
    name: Optional[str]
    repository: Optional[str]
    repository_path: Optional[str]
    repository_server: Optional[str]


class Blueprint(TimonBaseModel, BlueprintBase):
    pass


# deployment

class DeploymentBase(BaseModel):
    name: Optional[str]
    template_id: Optional[str]


class Deployment(TimonBaseModel, DeploymentBase):
    action: Optional[DeploymentAction] = DeploymentAction.none
    status: Optional[DeploymentStatus] = DeploymentStatus.none


# environment

class EnvironmentBase(BaseModel):
    name: Optional[str]
    repository: Optional[str]
    repository_path: Optional[str]
    repository_server: Optional[str]


class Environment(TimonBaseModel, EnvironmentBase):
    pass


# log

class LogBase(BaseModel):
    category: Optional[str]


class Log(TimonBaseModel, LogBase):
    pass


class LogWithValue(Log):
    value: Optional[str]


# organisation

class OrganisationBase(BaseModel):
    pass


class Organisation(TimonBaseModel, OrganisationBase):
    pass


# project

class ProjectBase(BaseModel):
    name: Optional[str]


class Project(TimonBaseModel, ProjectBase):
    pass


# template

class TemplateBase(BaseModel):
    blueprint_id: Optional[str]
    blueprint_version: Optional[str]
    environment_id: Optional[str]
    environment_version: Optional[str]
    name: Optional[str]


class TemplateWithInputsBase(TemplateBase):
    inputs: Optional[str]


class Template(TimonBaseModel, TemplateBase):
    pass


class TemplateWithInputs(TimonBaseModel, TemplateWithInputsBase):
    pass


# other

class Token(BaseModel):
    access_token: str
    expires_in: int
    issue_timestamp: int
    organisation_id: str
    project_id: str
    refresh_expires_in: int
    refresh_token: str
    user_id: str
