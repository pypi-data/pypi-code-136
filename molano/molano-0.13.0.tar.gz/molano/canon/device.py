# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from datetime import datetime

import pydantic

from .devicetype import DeviceType
from .decimalmeid import DecimalMEID
from .imei import IMEI
from .udid import UDID


class Device(pydantic.BaseModel):
    color: str
    discovered: datetime = pydantic.Field(default_factory=datetime.utcnow)
    battery_serial: str
    imei: list[IMEI] = []
    manufacturer_name: str
    meid: list[DecimalMEID] = []
    model_name: str
    model_number: str
    pesn: list[str] = []
    serial: str
    type: DeviceType
    udid: UDID