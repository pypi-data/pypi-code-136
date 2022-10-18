from typing import Any, Literal, NamedTuple

Builder = str

Target = Literal["docs", "doctrees"]


class Setting(NamedTuple):
    name: str
    value: Any
