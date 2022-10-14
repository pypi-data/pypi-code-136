from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json
from telescope_sdk.common import UserFacingDataType


class CampaignStatus(Enum):
    RUNNING = 'RUNNING'
    PAUSED = 'PAUSED'
    ERROR = 'ERROR'


@dataclass_json
@dataclass
class Campaign(UserFacingDataType):
    name: str
    status: CampaignStatus
    sequence_id: str
    replenish: bool
