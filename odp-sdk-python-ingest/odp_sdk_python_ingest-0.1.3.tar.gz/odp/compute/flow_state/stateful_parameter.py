import prefect.serialization.task
from prefect import Task, Flow, Parameter
from prefect.core.parameter import JSONSerializableParameterValue, no_default
from prefect.engine.results import PrefectResult
from prefect.utilities.tasks import defaults_from_attrs

from . import Watermark
from .watermark_store import WatermarkStore, get_watermark_store

import logging
from typing import Iterable, Optional, Any, Dict, Callable, Union

__all__ = ["StatefulParameter", "UpdateStatefulParameter", "update_stateful_parameter"]

LOG = logging.getLogger(__name__)


def _key_prefix(key) -> str:
    """Convenience-function returning a key prefixed with flow name and task name

    Args:
        key: Key to be prefixed

    Returns:
        Prefixed key
    """
    flow_id = prefect.context.get("flow_name")

    return f"{flow_id}:PARAMETER:{key}"


class StatefulParameter(Parameter):
    def __init__(
        self,
        name: str = None,
        default: JSONSerializableParameterValue = no_default,
        required: bool = None,
        watermark_store: Optional[WatermarkStore] = None,
        tags: Iterable[str] = None,
    ):
        super().__init__(name=name, default=default, required=required, tags=tags)

        self.watermark_store = watermark_store

    def __repr__(self) -> str:
        return f"<WatermarkedParameter: {self.name}>"

    def _get_watermark_store(self):
        if self.watermark_store is None:
            return get_watermark_store()
        else:
            return self.watermark_store

    def run(self) -> None:
        params = prefect.context.get("parameters") or {}

        watermark_obj = Watermark(
            key=_key_prefix(self.name), value=None, store=self._get_watermark_store()
        )

        if self.name in params:
            watermark_obj.watermark = params[self.name]
            return

        if self.required and watermark_obj.watermark is None:
            err = f"Parameter '{self.name}' was required but not provided."

            LOG.error(err)
            raise prefect.engine.signals.FAIL(err)

        if watermark_obj.watermark is None:
            LOG.info(
                "The parameter '%s' was not set, using default value of '%s' instead",
                self.name,
                self.default,
            )
            watermark_obj.watermark = self.default

        LOG.info(
            "The parameter '%s' was set to '%s'", self.name, watermark_obj.watermark
        )
        return watermark_obj.watermark


class UpdateStatefulParameter(Task):
    def __init__(
        self,
        parameter: StatefulParameter,
        to_value: Union[Any, Callable[[Any], Any]] = None,
        watermark_store: Optional[WatermarkStore] = None,
        tags: Iterable[str] = None,
    ):
        super().__init__(tags=tags, result=PrefectResult(), checkpoint=True)

        self.name = parameter.name
        self.watermark_store = watermark_store or parameter.watermark_store
        self.to_value = to_value

    @defaults_from_attrs("to_value")
    def run(self, state_value: Any, to_value: Union[Any, Callable[[Any], Any]]) -> Any:

        watermark_obj = Watermark(
            key=_key_prefix(self.name),
            value=None,
            store=self.watermark_store or get_watermark_store(),
        )

        if callable(to_value):
            watermark_obj.watermark = to_value(state_value)
        else:
            watermark_obj.watermark = to_value

        LOG.info(
            "The parameter '%s' was set to '%s'", self.name, watermark_obj.watermark
        )
        return watermark_obj.watermark


def update_stateful_parameter(
    parameter: StatefulParameter,
    to_value: Union[Any, Callable[[Any], Any]] = None,
    tags: Iterable[str] = None,
):
    tsk = UpdateStatefulParameter(
        parameter, tags=tags, watermark_store=parameter.watermark_store
    )

    return tsk(state_value=parameter, to_value=to_value)
