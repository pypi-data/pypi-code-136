from __future__ import annotations

from typing import (
    Any,
    AsyncIterator,
    Callable,
    Collection,
    Dict,
    List,
    Optional,
    Protocol,
    Tuple,
    runtime_checkable,
)
import typing as t

import pandas as pd
import pyarrow as pa

try:
    import tensorflow as tf
except ModuleNotFoundError:
    pass  # Warning is displayed by typing.py

from sarus_data_spec.storage.typing import HasStorage
import sarus_data_spec.protobuf as sp
import sarus_data_spec.query_manager.typing as sqmt
import sarus_data_spec.typing as st


@runtime_checkable
class Manager(st.Referrable[sp.Manager], HasStorage, Protocol):
    """Provide the dataset functionalities"""

    def to_arrow(
        self, dataset: st.Dataset, batch_size: int
    ) -> st.ContextManagerIterator[pa.RecordBatch]:
        """Synchronous method based on async_to_arrow
        that returns an iterator of arrow batches
        for the input dataset"""
        ...

    async def async_to_arrow(
        self, dataset: st.Dataset, batch_size: int
    ) -> AsyncIterator[pa.RecordBatch]:
        """Asynchronous method. It orchestrates how
        the iterator is obtained: it can either be delegated
        via arrow_task and the result polled, or computed directly
        it via the op"""
        ...

    def schema(self, dataset: st.Dataset) -> st.Schema:
        """Synchronous method that returns the schema of a
        dataspec. Based on the asynchronous version"""
        ...

    async def async_schema(self, dataset: st.Dataset) -> st.Schema:
        """Asynchronous method that returns the schema of a
        dataspec. The computation can be either delegated to
        another manager via schema_task and the result polled
        or executed directly via async_schema_ops"""
        ...

    def value(self, scalar: st.Scalar) -> st.DataSpecValue:
        """Synchronous method that returns the value of a
        scalar. Based on the asynchronous version"""
        ...

    async def async_value(self, scalar: st.Scalar) -> st.DataSpecValue:
        """Asynchronous method that returns the value of a
        scalar. The computation can be either delegated to
        another manager via value_task and the result polled
        or executed directly via async_value_ops"""
        ...

    def to_parquet(self, dataset: st.Dataset) -> None:
        """Synchronous parquet caching"""
        ...

    async def async_to_parquet(self, dataset: st.Dataset) -> None:
        """Asynchronous parquet caching"""
        ...

    def parquet_dir(self) -> str:
        ...

    def marginals(self, dataset: st.Dataset) -> st.Marginals:
        ...

    def to_pandas(self, dataset: st.Dataset) -> pd.DataFrame:
        ...

    async def async_to_pandas(self, dataset: st.Dataset) -> pd.DataFrame:
        ...

    def to_tensorflow(self, dataset: st.Dataset) -> tf.data.Dataset:
        ...

    async def async_to_tensorflow(
        self, dataset: st.Dataset
    ) -> tf.data.Dataset:
        ...

    def status(self, dataset: st.DataSpec) -> st.Status:
        """Reference to use to refer to this object."""
        ...

    def size(self, dataset: st.Dataset) -> st.Size:
        ...

    def bounds(self, dataset: st.Dataset) -> st.Bounds:
        ...

    def query_manager(self) -> sqmt.QueryManager:
        ...

    def is_compliant(
        self,
        dataspec: st.DataSpec,
        kind: st.ConstraintKind,
        public_context: List[str],
        epsilon: Optional[float],
    ) -> bool:
        ...

    def variant(
        self,
        dataspec: st.DataSpec,
        kind: st.ConstraintKind,
        public_context: List[str],
        epsilon: Optional[float],
    ) -> Optional[st.DataSpec]:
        ...

    def variants(self, dataspec: st.DataSpec) -> Collection[st.DataSpec]:
        ...

    def variant_constraint(
        self, dataspec: st.DataSpec
    ) -> Optional[st.VariantConstraint]:
        ...

    def set_remote(self, dataspec: st.DataSpec) -> None:
        """Add an Attribute to tag the DataSpec as remotely fetched."""
        ...

    def is_remote(self, dataspec: st.DataSpec) -> bool:
        """Is the dataspec a remotely defined dataset."""
        ...

    def infer_output_type(
        self,
        transform: st.Transform,
        *arguments: st.DataSpec,
        **named_arguments: st.DataSpec,
    ) -> Tuple[str, Callable[[st.DataSpec], None]]:
        ...

    def foreign_keys(self, dataset: st.Dataset) -> Dict[st.Path, st.Path]:
        ...

    async def async_foreign_keys(
        self, dataset: st.Dataset
    ) -> Dict[st.Path, st.Path]:
        ...

    async def async_primary_keys(self, dataset: st.Dataset) -> List[st.Path]:
        ...

    def primary_keys(self, dataset: st.Dataset) -> List[st.Path]:
        ...

    def sql(
        self,
        dataset: st.Dataset,
        query: str,
        dialect: Optional[st.SQLDialect] = None,
    ) -> List[Dict[str, Any]]:
        ...

    def is_big_data(self, dataset: st.Dataset) -> bool:
        ...

    def is_cached(self, dataset: st.Dataset) -> bool:
        """Returns whether a dataspec should be cached
        or not"""
        ...


@runtime_checkable
class HasManager(Protocol):
    """Has a manager."""

    def manager(self) -> Manager:
        """Return a manager (usually a singleton)."""
        ...


T = t.TypeVar("T", covariant=True)


class Computation(t.Protocol[T]):
    """Protocol for classes that perform tasks computations.
    It sets how computations are scheduled and launched
    depending on statuses. A computation is mainly defined by two methods:
     - launch : a method that does not return a value but
     that only has side effects, changing either the storage or the cache
    and that updates statuses during the process
    - result: a method that allows to get the value of the computation
    either by reading the cache/storage or via the ops.

    Furthermore, a computation has a method to monitor task completion.
    """

    task_name: str = ''

    def launch_task(self, dataspec: st.DataSpec) -> None:
        """This methods launches a task in the background
        but returns immediately without waiting for the
        result. It updates the statuses during its process."""
        ...

    async def task_result(self, dataspec: st.DataSpec, **kwargs: t.Any) -> T:
        """Returns the value for the given computed task. It either
        retrieves it from the cache or computes it via the ops."""
        ...

    async def complete_task(self, dataspec: st.DataSpec) -> st.Status:
        """Monitors a task: it launches it if there is no status
        and then polls until it is ready/error"""
        ...


class DelegatedComputation(Computation, t.Protocol[T]):
    def delegate_manager_status(
        self, dataspec: st.DataSpec
    ) -> Optional[st.Status]:
        """While some managers are eager and always execute tasks,
        others are lazy and delegate them. This is an interface
        for a manager to get the status of the eager manager
        that is executing the task"""
        ...


@t.runtime_checkable
class ExternalOpImplementation(t.Protocol):
    """Implementation of an external op.

    An instance of this class shall have three attributes defined.

    The `data` attribute is a function that takes values as arguments and
    returns the dataspec's output value.

    The other attributes are used to compute the PEP status of the output
    dataspec.

    The `allowed_pep_args` is a list of combinations of arguments' names which
    are managed by the Op. The result of the Op will be PEP only if the set of
    PEP arguments passed to the Op are in this list.

    For instance, if we have an op that takes 3 arguments `a`, `b` and `c` and
    the `allowed_pep_args` are [{'a'}, {'b'}, {'a','b'}] then the following
    combinations will yield a PEP output:
        - `a` is a PEP dataspec, `b` and `c` are either not dataspecs or public
          dataspecs
        - `b` is a PEP dataspec, `a` and `c` are either not dataspecs or public
          dataspecs
        - `a` and `b` are PEP dataspecs, `c` is either not a dataspec or a
          public dataspec

    The `is_token_preserving` attribute is a function that takes as input the
    non-evaluated arguments and returns a boolean of whether the PEP output
    token is the same as the PEP input token. An Op that changes the number or
    order of the rows is not token preserving.
    """

    data: t.Callable
    allowed_pep_args: t.List[t.Set[str]]
    is_token_preserving: t.Callable
