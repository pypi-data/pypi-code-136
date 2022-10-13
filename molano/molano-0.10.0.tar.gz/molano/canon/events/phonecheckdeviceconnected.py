# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import aorta
import pydantic

from ..device import Device


class PhonecheckDeviceConnected(aorta.Event):
    id: int = pydantic.Field(
        default=...
    )

    device: Device = pydantic.Field(
        default=...
    )

    data: dict[str, Any] = pydantic.Field(
        default=...
    )