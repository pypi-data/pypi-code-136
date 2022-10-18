from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class ParsedNumber:
    number: Union[int, float]
    number_string: str
    unit: Optional[str]
    prob: Optional[float]
