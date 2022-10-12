from typing import Dict, List
from dataclasses import dataclass
from beam.types import OutputType, PythonVersion, TypeSerializer
from beam.base import (
    BaseConfigClass,
    BaseTriggerConfigClass,
)


@dataclass()
class AppSpecConfiguration(BaseConfigClass):
    name: str
    cpu: str
    gpu: int
    memory: str
    apt_install: PythonVersion
    python_version: List[str]
    python_packages: List[str]
    workspace: str


@dataclass
class WebhookConfiguration(BaseTriggerConfigClass):
    inputs: Dict[str, TypeSerializer]
    handler: str
    trigger_type: str = "webhook"


@dataclass
class CronJobConfiguration(BaseTriggerConfigClass):
    inputs: Dict[str, TypeSerializer]
    cron_schedule: str
    handler: str
    trigger_type: str = "cron_job"


@dataclass
class RestAPIConfiguration(BaseTriggerConfigClass):
    inputs: Dict[str, TypeSerializer]
    outputs: Dict[str, TypeSerializer]
    handler: str
    trigger_type: str = "rest_api"


@dataclass
class FileConfiguration(BaseConfigClass):
    path: str
    name: str
    output_type: OutputType
