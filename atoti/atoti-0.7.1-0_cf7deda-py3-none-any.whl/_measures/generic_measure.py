from typing import Any, Optional, Sequence

from .._java_api import JavaApi
from ..measure_description import MeasureDescription
from .utils import convert_measure_args


class GenericMeasure(MeasureDescription):
    """Generic implementation of a MeasureDescription."""

    _plugin_key: str
    _args: Sequence[Any]

    def __init__(self, plugin_key: str, /, *args: Any):
        """Create the measure.

        Args:
            plugin_key: The plugin key of the Java implementation.
            args: The arguments used to create the measure.
                They are directly forwarded to the Java code, except for the ``Measure``
                arguments that are first created on the Java side and replaced by their name.
        """
        self._plugin_key = plugin_key
        self._args = args

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        return java_api.create_measure(
            cube_name,
            measure_name,
            self._plugin_key,
            *convert_measure_args(
                java_api=java_api, cube_name=cube_name, args=self._args
            ),
        )
