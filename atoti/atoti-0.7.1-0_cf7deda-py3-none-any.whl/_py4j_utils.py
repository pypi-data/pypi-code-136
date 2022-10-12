import datetime
from typing import Any, Collection, Dict, Iterable, List, Mapping, Optional, Union, cast

from atoti_core import ColumnCoordinates, DataType
from dateutil.parser import isoparse
from py4j.java_collections import JavaArray, JavaMap, ListConverter
from py4j.java_gateway import CallbackServer, JavaClass, JavaGateway, JavaObject

from .type import FLOAT_ARRAY, INT_ARRAY


# No type stubs for py4j, so we ignore this error
def to_java_object_array(
    collection: Collection[Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> JavaArray:
    """Transform the Python collection into a Java array."""
    return to_typed_java_array(
        collection, gateway=gateway, array_type=gateway.jvm.Object
    )


def to_java_map(
    mapping: Mapping[Any, Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> JavaMap:
    """Convert a Python mapping to a JavaMap preserving the order of the keys."""
    return _to_typed_java_map(mapping, gateway=gateway, clazz="java.util.LinkedHashMap")


def to_java_object_map(
    mapping: Mapping[Any, Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> JavaMap:
    """Convert a Python mapping to a JavaMap preserving the order of the keys."""
    return to_java_map(
        {
            as_java_object(key, gateway=gateway): as_java_object(value, gateway=gateway)
            for key, value in mapping.items()
        },
        gateway=gateway,
    )


def _to_typed_java_map(
    to_convert: Mapping[Any, Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
    clazz: str,
) -> JavaMap:
    """Convert to a map of the given type."""
    map_type = JavaClass(clazz, gateway._gateway_client)
    java_map = cast(JavaMap, map_type())
    for key in to_convert:
        java_map[key] = as_java_object(to_convert[key], gateway=gateway)
    return java_map


def to_java_string_array(
    collection: Collection[str],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> JavaArray:
    """Transform the Python collection into a Java array of strings."""
    return to_typed_java_array(
        collection, gateway=gateway, array_type=gateway.jvm.String
    )


def to_java_object_list(
    iterable: Iterable[Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> Any:
    """Transform the Python iterable into a Java list of object."""
    return ListConverter().convert(
        [as_java_object(e, gateway=gateway) for e in iterable], gateway._gateway_client
    )


def to_typed_java_array(
    collection: Collection[Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
    array_type: Any,
) -> JavaArray:
    """Transform to Java array of given type."""
    array = cast(JavaArray, gateway.new_array(array_type, len(collection)))
    if collection:
        for index, elem in enumerate(collection):
            array[index] = as_java_object(elem, gateway=gateway)
    return array


def to_java_date_or_time(
    date: Union[datetime.date, datetime.datetime, datetime.time],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> JavaObject:
    """Transform the Python date into a Java one."""
    if isinstance(date, datetime.datetime):
        if not date.tzinfo:
            return gateway.jvm.java.time.LocalDateTime.parse(  # pyright: ignore
                date.isoformat()
            )
        return gateway.jvm.java.time.ZonedDateTime.parse(  # pyright: ignore
            date.isoformat()
        )
    if isinstance(date, datetime.time):
        if not date.tzinfo:
            return gateway.jvm.java.time.LocalTime.of(  # pyright: ignore
                date.hour,
                date.minute,
                date.second,
                date.microsecond * 1000,
            )
        raise NotImplementedError()
    return gateway.jvm.java.time.LocalDate.of(  # pyright: ignore
        date.year, date.month, date.day
    )


def to_qfs_vector(
    arg: Collection[Any],
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
    data_type: Optional[DataType] = None,
) -> Any:
    vector_package = gateway.jvm.com.qfs.vector.array.impl  # pyright: ignore
    if all(isinstance(x, int) for x in arg):
        if data_type == INT_ARRAY:
            array = to_typed_java_array(
                arg, gateway=gateway, array_type=gateway.jvm.int
            )
            return vector_package.ArrayIntegerVector(array)  # pyright: ignore
        array = to_typed_java_array(arg, gateway=gateway, array_type=gateway.jvm.long)
        return vector_package.ArrayLongVector(array)  # pyright: ignore
    if all(isinstance(x, (float, int)) for x in arg):
        if data_type == FLOAT_ARRAY:
            array = to_typed_java_array(
                [float(x) for x in arg],
                gateway=gateway,
                array_type=gateway.jvm.float,
            )
            return vector_package.ArrayFloatVector(array)  # pyright: ignore
        array = to_typed_java_array(
            [float(x) for x in arg], gateway=gateway, array_type=gateway.jvm.double
        )
        return vector_package.ArrayDoubleVector(array)  # pyright: ignore
    array = to_java_object_array(arg, gateway=gateway)
    return vector_package.ArrayObjectVector(array)  # pyright: ignore


def as_java_object(
    arg: Any,
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
    data_type: Optional[DataType] = None,
) -> Any:
    if isinstance(arg, (datetime.date, datetime.datetime, datetime.time)):
        return to_java_date_or_time(arg, gateway=gateway)
    if isinstance(arg, ColumnCoordinates):
        return to_store_field(arg, gateway=gateway)
    if isinstance(arg, list):
        return to_qfs_vector(arg, gateway=gateway, data_type=data_type)
    return arg


def to_python_object(
    value: Optional[Any],
    /,
) -> Any:
    if value is None or not isinstance(value, JavaObject):
        return value
    if value.getClass().getName() in [
        "java.time.LocalDateTime",
        "java.time.ZonedDateTime",
    ]:
        return isoparse(value.toString())
    if value.getClass().getName() == "java.time.LocalDate":
        return datetime.date.fromisoformat(value.toString())
    if value.getClass().getName() == "java.time.LocalTime":
        return datetime.time.fromisoformat(value.toString())
    raise TypeError(f"Cannot convert object of type {type(value)} to Python.")


def to_python_dict(
    java_map: JavaMap,  # pyright: ignore[reportUnknownParameterType]
) -> Dict[Any, Any]:
    """Convert a Java map to a Python dict."""
    return {
        key: java_map[key] for key in java_map.keySet().toArray()
    }  # pyright: ignore


def to_python_list(
    list_to_convert: JavaObject,  # pyright: ignore[reportUnknownParameterType]
) -> List[Any]:
    """Convert a Java list to a Python list."""
    # ignore types when calling a Java function
    return list(list_to_convert.toArray())  # pyright: ignore


def to_store_field(
    coordinates: ColumnCoordinates,
    /,
    *,
    gateway: JavaGateway,  # pyright: ignore[reportUnknownParameterType]
) -> Any:
    # pylint: disable=invalid-name
    StoreField: Any = gateway.jvm.com.activeviam.database.api.schema.StoreField
    # pylint: enable=invalid-name
    return StoreField(coordinates.table_name, coordinates.column_name)


def patch_databricks_py4j() -> None:
    """Fix Databricks' monkey patching of py4j."""

    # The problematic version of Databricks outputs:
    # >>> print(CallbackServer.start.__qualname__)
    #  _daemonize_callback_server.<locals>.start
    #
    # More generally, it looks like most local monkey patches will have
    # the "locals" string in their name, so it's worth checking.

    if "locals" in CallbackServer.start.__qualname__:
        databricks_start = CallbackServer.start

        # Re-define the start function, adding back the missing code.
        def start(self: Any) -> None:
            databricks_start(self)

            if not hasattr(self, "_listening_address"):
                info = self.server_socket.getsockname()
                self._listening_address = info[0]
                self._listening_port = info[1]

        CallbackServer.start = start
