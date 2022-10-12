from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property, lru_cache
from threading import Lock
from typing import List, Optional

from atoti_core import ColumnCoordinates, keyword_only_dataclass

from .._java_api import JavaApi
from .._operation import Operation
from .._udaf_utils import (
    LongAggregationOperationVisitor,
    MaxAggregationOperationVisitor,
    MeanAggregationOperationVisitor,
    MinAggregationOperationVisitor,
    MultiplyAggregationOperationVisitor,
    ShortAggregationOperationVisitor,
    SingleValueNullableAggregationOperationVisitor,
    SquareSumAggregationOperationVisitor,
    SumAggregationOperationVisitor,
)
from .._udaf_utils.java_operation_visitor import OperationVisitor
from ..measure_description import MeasureDescription

OPERATION_VISITORS = {
    "SUM": SumAggregationOperationVisitor,
    "MEAN": MeanAggregationOperationVisitor,
    "MULTIPLY": MultiplyAggregationOperationVisitor,
    "MIN": MinAggregationOperationVisitor,
    "MAX": MaxAggregationOperationVisitor,
    "SQ_SUM": SquareSumAggregationOperationVisitor,
    "SHORT": ShortAggregationOperationVisitor,
    "LONG": LongAggregationOperationVisitor,
    "SINGLE_VALUE_NULLABLE": SingleValueNullableAggregationOperationVisitor,
}


@keyword_only_dataclass
@dataclass
class _AtomicCounter:
    """Threadsafe counter to get unique IDs."""

    _value: int = field(default=0, init=False)
    _lock: Lock = field(default_factory=Lock, init=False, repr=False)

    def read_and_increment(self) -> int:
        with self._lock:
            self._value += 1
            return self._value


@lru_cache
def _get_id_provider() -> _AtomicCounter:
    return _AtomicCounter()


@keyword_only_dataclass
@dataclass(frozen=True)
class _UserDefinedAggregateFunction:
    """A class template which builds the sources to compile an AUserDefinedAggregate function at runtime.

    This class parses the combination of operations passed and converts them into Java source code blocks.
    These source code blocks are then compiled using Javassist into a new aggregation function which is then registered on the session.
    """

    _operation: Operation
    _plugin_key: str

    @cached_property
    def _columns(self) -> List[ColumnCoordinates]:
        return self._operation.columns

    @cached_property
    def plugin_key(self) -> str:
        column_names = "".join([column.column_name for column in self._columns])
        return f"{column_names}{_get_id_provider().read_and_increment()}.{self._plugin_key}"

    def register_aggregation_function(self, *, java_api: JavaApi) -> None:
        """Generate the required Java source code blocks and pass them to the Java process to be compiled into a new UserDefinedAggregateFunction."""
        visitor_class = OPERATION_VISITORS[self._plugin_key]
        visitor: OperationVisitor = visitor_class(  # type: ignore[abstract]
            columns=self._columns, java_api=java_api
        )

        java_operation = visitor.build_java_operation(self._operation)
        java_api.register_aggregation_function(
            additional_imports=java_operation.additional_imports,
            additional_methods=java_operation.additional_methods_source_codes,
            contribute_source_code=java_operation.contribute_source_code,
            decontribute_source_code=java_operation.decontribute_source_code,
            merge_source_code=java_operation.merge_source_code,
            terminate_source_code=java_operation.terminate_source_code,
            buffer_types=java_operation.buffer_types,
            output_type=java_operation.output_type,
            plugin_key=self.plugin_key,
        )


@keyword_only_dataclass
@dataclass
class UdafMeasure(MeasureDescription):
    _plugin_key: str
    _operation: Operation

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        udaf = _UserDefinedAggregateFunction(
            _operation=self._operation, _plugin_key=self._plugin_key
        )
        udaf.register_aggregation_function(java_api=java_api)
        return java_api.create_measure(
            cube_name,
            measure_name,
            "ATOTI_UDAF_MEASURE",
            udaf._columns,
            udaf.plugin_key,
            self._plugin_key,
        )
