import hashlib
import importlib
import inspect
import pickle as pkl
import typing as t

import pandas as pd
import pyarrow as pa

from sarus_data_spec.config import ROUTING
from sarus_data_spec.constants import DATA, PUBLIC, USER_COLUMN, WEIGHTS
from sarus_data_spec.manager.asyncio.utils import async_iter
from sarus_data_spec.manager.ops.asyncio.base import (
    BaseDatasetOp,
    BaseScalarOp,
)
from sarus_data_spec.transform import transform_id
import sarus_data_spec.manager.typing as smt
import sarus_data_spec.protobuf as sp
import sarus_data_spec.typing as st


class ExternalOpImplementation:
    def __init__(
        self,
        data: t.Callable,
        allowed_pep_args: t.List[t.Set[str]] = [],
        is_token_preserving: t.Optional[t.Callable] = None,
    ):
        self.data = data
        self.allowed_pep_args = allowed_pep_args
        if is_token_preserving is None:

            def return_false(*args: t.Any, **kwargs: t.Any) -> bool:
                return False

            self.is_token_preserving = return_false
        else:
            self.is_token_preserving = is_token_preserving


class ExternalDatasetOp(BaseDatasetOp):
    def pep_token(
        self, public_context: t.List[str], epsilon: float
    ) -> t.Optional[str]:
        # Get transformation arguments
        (
            op_implementation,
            parent_args,  # usually empty
            parent_kwargs,  # usually {py_args, py_kwargs, ds_args_pos}
        ) = deserialize_external_op(self.dataset)

        if len(op_implementation.allowed_pep_args) == 0:
            return None

        # `transform_args` and `transform_kwargs` contain the arguments that
        # will be passed to the `OpImplementation.data` function. However,
        # DataSpecs still not have been evaluated.
        transform_args, transform_kwargs = reorganize_arguments(
            self.dataset, *parent_args, **parent_kwargs
        )

        # Add name to positional arguments to identify them by their names
        n_args = len(transform_args)
        argument_names = list(
            inspect.signature(op_implementation.data).parameters.keys()
        )
        """
        Example :
        In [1]: def foo(a, b=3):
        ...:     return a+b
        ...:

        In [2]: list(inspect.signature(foo).parameters.keys())
        Out[2]: ['a', 'b']
        """
        for arg_name, arg_val in zip(argument_names[:n_args], transform_args):
            # put all args in kwargs
            transform_kwargs[arg_name] = arg_val

        # Keep only dataspec args and split PEP from non PEP
        dataspec_args = {
            arg_name: arg
            for arg_name, arg in transform_kwargs.items()
            if isinstance(arg, st.DataSpec)
        }
        pep_args = {
            arg_name: arg
            for arg_name, arg in dataspec_args.items()
            if arg.is_pep()
        }
        non_pep_args = {
            arg_name: arg
            for arg_name, arg in dataspec_args.items()
            if arg_name not in pep_args
        }

        # All non PEP args should be public of published
        if not all(
            [
                arg.uuid() in public_context or arg.is_public()
                for arg in non_pep_args.values()
            ]
        ):
            return None

        # The PEP arg combination should be allowed
        if set(pep_args.keys()) not in op_implementation.allowed_pep_args:
            return None

        # All PEP tokens should be equal
        pep_tokens = [arg.pep_token() for arg in pep_args.values()]
        if not all([token == pep_tokens[0] for token in pep_tokens]):
            return None

        # The result is PEP, now check if it's aligned with the input(s)
        input_token = pep_tokens[0]
        assert input_token is not None
        if op_implementation.is_token_preserving(
            *transform_args, **transform_kwargs
        ):
            output_token = input_token
        else:
            h = hashlib.md5()
            h.update(input_token.encode("ascii"))
            h.update(self.dataset.transform().protobuf().SerializeToString())
            output_token = h.hexdigest()

        return output_token

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:

        (
            op_implementation,
            parent_args,
            parent_kwargs,
        ) = deserialize_external_op(self.dataset)

        transform_args, transform_kwargs = reorganize_arguments(
            self.dataset, *parent_args, **parent_kwargs
        )
        computed_args = [await pandas_or_value(arg) for arg in transform_args]
        computed_kwargs = {
            name: await pandas_or_value(arg)
            for name, arg in transform_kwargs.items()
        }

        data_result = await op_implementation.data(
            *computed_args, **computed_kwargs
        )

        if self.dataset.is_pep():
            # TODO compute PEID
            pass

        if isinstance(data_result, pd.DataFrame):
            return async_iter(
                pa.Table.from_pandas(data_result).to_batches(
                    max_chunksize=batch_size
                )
            )

        else:
            raise TypeError(
                f"Cannot convert {type(data_result)} to Arrow batches."
            )


class ExternalScalarOp(BaseScalarOp):
    async def value(self) -> t.Any:

        (
            op_implementation,
            parent_args,
            parent_kwargs,
        ) = deserialize_external_op(self.scalar)

        transform_args, transform_kwargs = reorganize_arguments(
            self.scalar, *parent_args, **parent_kwargs
        )

        computed_args = [await pandas_or_value(arg) for arg in transform_args]
        computed_kwargs = {
            name: await pandas_or_value(arg)
            for name, arg in transform_kwargs.items()
        }

        return await op_implementation.data(*computed_args, **computed_kwargs)


def reorganize_arguments(
    dataspec: st.DataSpec,
    py_args: t.Dict[int, t.Any],
    py_kwargs: t.Dict[str, t.Any],
    ds_args_pos: t.List[int],
) -> t.Tuple:
    """Interleave Python arguments with Dataspec arguments."""
    ds_args, ds_kwargs = dataspec.parents()
    pos_values = {pos: val for pos, val in zip(ds_args_pos, ds_args)}
    kwargs = {**py_kwargs, **ds_kwargs}
    pos_args = {**pos_values, **py_args}
    args = [pos_args[i] for i in range(len(pos_args))]
    return args, kwargs


def deserialize_external_op(
    dataspec: st.DataSpec,
) -> t.Tuple[smt.ExternalOpImplementation, t.Any, t.Mapping[str, t.Any]]:
    """Deserialize Python arguments and fetch the op implementation.

    The op implementation can be either a simple function or an
    ExternalOpImplementation instance. If the op is a function,
    it is considered to be the data implementation and
    we instantiate an `ExternalOpImplementation` from this data
    function.
    """
    transform_name = transform_id(dataspec.transform())
    library, op_name = transform_name.split(".")
    if op_name not in ROUTING["external"][library]:
        raise NotImplementedError(
            f"Routing: {op_name} not in {list(ROUTING['external'][library].keys())}"  # noqa: E501
        )

    transform_spec = dataspec.transform().protobuf().spec
    # args: usually empty
    # kwargs: usually {py_args, py_kwargs, ds_args_pos}
    args = pkl.loads(transform_spec.external.arguments)
    kwargs = pkl.loads(transform_spec.external.named_arguments)

    implementation_name = ROUTING["external"][library][op_name]
    module = importlib.import_module(
        f"sarus_data_spec.manager.ops.asyncio.processor.external.{library}"
    )
    op_implementation = getattr(module, implementation_name)

    if not isinstance(op_implementation, smt.ExternalOpImplementation):
        op_implementation = ExternalOpImplementation(op_implementation)

    return op_implementation, args, kwargs


async def pandas_or_value(x: t.Any) -> t.Any:
    """Compute the value of a DataSpec.

    Return the passed argument if it is not a Dataspec.
    """
    if not isinstance(x, st.DataSpec):
        return x

    if x.prototype() == sp.Dataset:
        dataset = t.cast(st.Dataset, x)
        df: pd.DataFrame = await dataset.async_to_pandas()
        # TODO use `dataset.is_protected()` but we need the schema
        # for that, and it is not yet available in the SDK
        is_protected = set(df.columns) == {
            PUBLIC,
            USER_COLUMN,
            WEIGHTS,
            DATA,
        }
        return await select_pandas_data(df, is_protected)
    else:
        scalar = t.cast(st.Scalar, x)
        return await scalar.async_value()


async def select_pandas_data(
    dataframe: pd.DataFrame, is_protected: bool
) -> pd.DataFrame:
    if is_protected:
        return pd.DataFrame.from_records(dataframe['data'].values)
    return dataframe
