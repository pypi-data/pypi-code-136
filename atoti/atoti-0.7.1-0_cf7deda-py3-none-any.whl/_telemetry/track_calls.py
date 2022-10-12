from __future__ import annotations

import functools
import json
import time
from dataclasses import dataclass, field
from datetime import timedelta
from operator import attrgetter
from pathlib import Path
from typing import Callable, Dict, List, Mapping, Optional, TypeVar

from atoti_core import keyword_only_dataclass
from typing_extensions import ParamSpec

from .event import Event
from .get_non_personal_arguments import get_non_personal_arguments
from .get_non_personal_type_name import get_non_personal_type_name
from .send_event import send_event

_TELEMETERED_API_PATH = Path(__file__).parent.parent / "data" / "telemetered-api.json"

_TelemeteredApi = Dict[str, Dict[str, List[str]]]


@keyword_only_dataclass
@dataclass(frozen=True)
class CallEvent(Event):
    """Triggered when a function or method from the public API is called."""

    event_type: str = field(default="call", init=False)
    path: str
    duration: timedelta
    arguments: Mapping[str, str]
    error: Optional[str]


@keyword_only_dataclass
@dataclass
class _CallTracker:
    tracking = False


_P = ParamSpec("_P")
_R = TypeVar("_R")


def _track_function_call(
    function: Callable[_P, _R], call_path: str, /, *args: _P.args, **kwargs: _P.kwargs
) -> _R:
    error_type_name = None
    call_time = time.perf_counter()
    try:
        return function(*args, **kwargs)
    except Exception as error:  # pylint: disable=broad-except
        try:
            error_type_name = get_non_personal_type_name(type(error))
        except:  # pylint: disable=bare-except
            # Do nothing to let the previous error be the one presented to the user.
            ...
        raise error
    finally:
        arguments: Dict[str, str] = {}

        try:
            arguments = get_non_personal_arguments(function, *args, **kwargs)
        except:  # pylint: disable=bare-except
            # Do nothing to not bother the user.
            ...

        duration = timedelta(seconds=time.perf_counter() - call_time)
        call_event = CallEvent(
            path=call_path,
            duration=duration,
            arguments=arguments,
            error=error_type_name,
        )
        send_event(call_event)


def _track_function_calls(
    function: Callable[_P, _R],
    /,
    *,
    call_path: str,
    call_tracker: _CallTracker,
) -> Callable[_P, _R]:
    @functools.wraps(function)
    def function_wrapper(
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _R:
        if call_tracker.tracking:
            return function(*args, **kwargs)

        call_tracker.tracking = True

        try:
            return _track_function_call(function, call_path, *args, **kwargs)
        finally:
            call_tracker.tracking = False

    return function_wrapper


def track_calls() -> None:
    call_tracker = _CallTracker()
    telemetered_api: _TelemeteredApi = json.loads(_TELEMETERED_API_PATH.read_bytes())

    for module_name, path_in_module_to_function_names in telemetered_api.items():
        module = __import__(module_name)
        for (
            path_in_module,
            function_names,
        ) in path_in_module_to_function_names.items():
            container = attrgetter(path_in_module)(module) if path_in_module else module
            for function_name in function_names:
                function = getattr(container, function_name)
                function_tracking_calls = _track_function_calls(
                    function,
                    call_path=f"""{module_name}.{f"{path_in_module}." if path_in_module else ""}{function_name}""",
                    call_tracker=call_tracker,
                )
                setattr(container, function_name, function_tracking_calls)
