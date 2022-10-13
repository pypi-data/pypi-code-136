from enum import Enum
from typing import List


class PartnersEnum(Enum):
    BELL_PARTNER = "Bell"
    ROGERS_PARTNER = "Rogers"
    VIDEOTRON_PARTNER = "Videotron"
    SHAW_PARTNER = "Shaw"

    def __str__(self) -> str:
        return str(self.value)


available_partners_list: List[str] = [partner.value for partner in PartnersEnum]
