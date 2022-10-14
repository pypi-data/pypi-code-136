from dataclasses import dataclass

from .common import LocalizedString, DEFAULT_LANG
from .functions import TaskFunction


@dataclass
class TaskSpec:
    id: str
    function: TaskFunction
    name: LocalizedString
    description: LocalizedString
    instruction: LocalizedString

    def __post_init__(self):
        LocalizedString.convert_dataclass(self)
        assert DEFAULT_LANG in self.name.lang_to_text, f'please provide name for {DEFAULT_LANG} language'
