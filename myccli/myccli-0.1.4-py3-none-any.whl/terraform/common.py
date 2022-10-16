from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ProviderRequirement:
    name: str
    version: Optional[str] = None


class JSONDocument(dict):
    pass


class JSONDocumentList(list):
    pass


class InlineBlock(dict):
    pass


@dataclass
class TaggedInlineBlock:
    tags: List[str]
    block: InlineBlock


class ETF:
    def render(self) -> str:
        raise NotImplementedError

    def __str__(self):
        return self.render()


class ETFCall(ETF):
    def __init__(self, target: str, args: List[any]):
        self.target = target
        self.args = args

    def render(self) -> str:
        return f'{self.target}({", ".join(self.args)})'


class ETFRaw(ETF):
    def __init__(self, value: str):
        self.value = value

    def render(self) -> str:
        return self.value

    def __str__(self):
        return self.render()


class ETFRawRef(ETF):
    def __init__(self, resource):
        self.resource = resource

    def render(self) -> str:
        return f'{self.resource.kind}.{self.resource.tf_name}'
