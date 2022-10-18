"""Central "hub" class for all info about the user's run on a Vision task"""

from dataclasses import dataclass
from typing import Any, Optional, Union, List, Literal, Dict
from trojsdk.config.base import BaseTrojConfig
from trojsdk.core.troj_error import TrojConfigError
from trojsdk.config.auth import TrojAuthConfig
from dataclasses_jsonschema import JsonSchemaMixin
from dataclasses_json import dataclass_json, DataClassJsonMixin, Undefined

ALLOWED_SUBTASKS = tuple(["classification", "object detection", "other"])


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class VisionTrojConfig(BaseTrojConfig, DataClassJsonMixin, JsonSchemaMixin):

    """Vision config class. Stores all relevant info about the user's run. Inherit from base and JSON dataclass"""

    name: str
    attacks: Dict
    dataset: Any
    model: Any
    task_type: str
    framework: str = None
    num_batches_to_run: Optional[int] = None
    random_seed: Optional[int] = None
    subtask: Literal[ALLOWED_SUBTASKS] = None

    custom_evaluator_function: Optional[str] = None
    custom_evaluator_args: Optional[dict] = None
    custom_attacks: Optional[Any] = None

    auth_config: TrojAuthConfig = None
    save_path: Optional[str] = None

    def __post_init__(self):

        """Let the dataset know what the framework is going to be, and create data loader with that info"""

        self.task_type = "vision"

        if self.subtask is not None:
            self.subtask = self.subtask.casefold()
            if self.subtask not in ALLOWED_SUBTASKS:
                raise TrojConfigError(
                    f'Provided subtask "{self.subtask}" not supported. '
                    f"Currently supported subtasks are: {ALLOWED_SUBTASKS}"
                )

        self.dataset.initialize_data_loader(framework=self.framework)
