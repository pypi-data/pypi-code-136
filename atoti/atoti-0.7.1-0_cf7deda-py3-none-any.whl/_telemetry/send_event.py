from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from typing import Any, Callable, Union
from urllib.request import Request, urlopen

from atoti_core import get_env_flag

from .event import Event

_ASYNC_EXECUTOR = ThreadPoolExecutor(max_workers=1)

_TELEMETRY_SERVICE_URL = "https://telemetry.atoti.io/events"

_TEST_TELEMETRY_ENV_VAR = "ATOTI_TEST_TELEMETRY"


def send_event(event: Event, /) -> None:
    action: Callable[..., Any] = urlopen
    data = json.dumps({"events": [asdict(event)]}, default=str).encode("utf8")
    payload: Union[Request, str] = Request(
        _TELEMETRY_SERVICE_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    if get_env_flag(_TEST_TELEMETRY_ENV_VAR):
        action = print
        payload = data.decode("utf8")

    # Done in the background to not bother the user.
    _ASYNC_EXECUTOR.submit(
        # https://github.com/microsoft/pylance-release/issues/2025#issuecomment-958612654
        action,  # pyright: ignore[reportGeneralTypeIssues]
        payload,  # pyright: ignore[reportGeneralTypeIssues]
    )
