import threading
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .execution.networkrun import NetworkRun


thread_local = threading.local()
thread_local.current_run = None


def set_current_run(current_run: 'NetworkRun'):
    thread_local.current_run = current_run


def get_current_run() -> 'Optional[NetworkRun]':
    current_run = getattr(thread_local, 'current_run', None)
    return current_run