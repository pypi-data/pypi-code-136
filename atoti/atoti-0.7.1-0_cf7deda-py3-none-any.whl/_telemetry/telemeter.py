from __future__ import annotations

from atoti_core import get_env_flag, is_plugin_active

from .import_event import ImportEvent
from .send_event import send_event
from .send_heartbeat import send_heartbeat
from .track_calls import track_calls

_DISABLE_TELEMETRY_ENV_VAR = "ATOTI_DISABLE_TELEMETRY"


def _disabled_by_atoti_plus() -> bool:
    return is_plugin_active("plus")


def _disabled_by_environment_variable() -> bool:
    return get_env_flag(_DISABLE_TELEMETRY_ENV_VAR)


def telemeter() -> None:
    if _disabled_by_atoti_plus() or _disabled_by_environment_variable():
        return

    send_event(ImportEvent())
    send_heartbeat()
    track_calls()
