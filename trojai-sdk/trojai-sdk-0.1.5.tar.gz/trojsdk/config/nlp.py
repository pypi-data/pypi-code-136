from typing import Any, Optional, Union, List, Literal, TypedDict
from dataclasses import dataclass
from trojsdk.config.base import BaseTrojConfig
from trojsdk.config.auth import TrojAuthConfig
from dataclasses_json import dataclass_json, DataClassJsonMixin, Undefined
from dataclasses_jsonschema import JsonSchemaMixin

ALLOWED_SUBTASKS = tuple(["classification"])


"""
#TODO make support checks. Attacks and dataset should not be enforced, and an extra attribute should be added
which is an (optional) instance of a checks config (instantiated from some collection of checks Jsons).
If attacks is None, just the checks are ran. If the check config is None, the attacks must not be None and then
just the attacks are ran. If both are not None, the checks and the attacks are ran, with a special option of
adversarial checks which are special in that they take in the results of the attacks and return checks results.
"""


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class NLPTrojConfig(BaseTrojConfig, DataClassJsonMixin, JsonSchemaMixin):

    """
    NLP-specific config class to hold info about the users run (including dataset and model).
    Inherits from base class and JSON dataclass.
    """

    name: str
    attacks: Any
    dataset: Any
    model: Any
    task_type: str
    random_seed: Optional[int] = None
    save_path: Union[str, None] = None
    subtask: Literal[ALLOWED_SUBTASKS] = None
    custom_evaluator_function: Optional[str] = None
    custom_evaluator_args: Optional[dict] = None
    custom_attacks: Optional[Any] = None
    num_batches_to_run: Optional[int] = None
    auth_config: TrojAuthConfig = None
    integrity_checks: Any = None
    compute_severity: Optional[bool] = True

    def __post_init__(self):
        self.task_type = "nlp"

    def get_schema(self):
        return self.json_schema()
