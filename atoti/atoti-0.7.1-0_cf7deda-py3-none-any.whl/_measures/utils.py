from typing import Any, Iterable, List, Mapping

from .._java_api import JavaApi
from .._py4j_utils import as_java_object, to_java_object_array
from ..measure_description import MeasureDescription


def get_measure_name(
    *, java_api: JavaApi, measure: MeasureDescription, cube_name: str
) -> str:
    """Get the name of the measure from either a measure or its name."""
    return measure._distil(java_api=java_api, cube_name=cube_name)


def convert_measure_args(
    *, java_api: JavaApi, cube_name: str, args: Iterable[Any]
) -> List[Any]:
    """Convert arguments used for creating a measure in Java.

    The ``Measure`` arguments are replaced by their name, and other arguments are
    translated into Java-equivalent objects when necessary.
    """
    return [
        _convert_measure_arg(java_api=java_api, cube_name=cube_name, arg=a)
        for a in args
    ]


def _convert_measure_arg(*, java_api: JavaApi, cube_name: str, arg: Any) -> Any:
    # Replace measures with their name.
    if isinstance(arg, MeasureDescription):
        return get_measure_name(java_api=java_api, measure=arg, cube_name=cube_name)

    # Recursively convert nested args.
    if isinstance(arg, tuple):
        return to_java_object_array(
            convert_measure_args(java_api=java_api, cube_name=cube_name, args=arg),
            gateway=java_api.gateway,
        )
    if isinstance(arg, list):
        return convert_measure_args(java_api=java_api, cube_name=cube_name, args=arg)
    if isinstance(arg, Mapping):
        return {
            _convert_measure_arg(
                java_api=java_api, cube_name=cube_name, arg=key
            ): _convert_measure_arg(java_api=java_api, cube_name=cube_name, arg=value)
            for key, value in arg.items()
        }

    # Nothing smarter to do. Transform the argument to a java array.
    return as_java_object(arg, gateway=java_api.gateway)
