# (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.
import axolotls as ax

import functools
# NOTE: functorch requires PyTorch version to be >= 1.12 and < 1.13
from functorch._src import python_key
from functorch._src.aot_autograd import (
    aot_autograd_decompositions,
    KNOWN_TYPES,
    PytreeThunk,
)
import inspect
import torch
import torch.fx as fx
import torch.utils._pytree as pytree
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


def _unpack_vals(values: List[Any]) -> List[Any]:
    unpacked = []
    for val in values:
        if isinstance(val, torch.Tensor) and val.numel() == 0:
            unpacked.append(None)
        else:
            unpacked.append(val)
    return unpacked

def _numeric_column_flatten(col: ax.NumericColumn) -> Tuple[List[Any], pytree.Context]:
    return ([col.values, col.presence or torch.empty(0)], None)


def _numeric_column_unflatten(
    values: List[Any], context: pytree.Context
) -> ax.NumericColumn:
    unpacked = _unpack_vals(values)
    return ax.NumericColumn(values=unpacked[0], presence=unpacked[1])

def _string_column_flatten(
    col: ax.StringColumn,
) -> Tuple[List[Any], pytree.Context]:
    return (
        [
            col.values,
            col.offsets,
        ],
        None,
    )

def _string_column_unflatten(
    values: List[Any], context: pytree.Context
) -> ax.StringColumn:
    unpacked = _unpack_vals(values)
    return ax.StringColumn(
        values=unpacked[0],
        offsets=unpacked[1],
    )


def _list_column_flatten(
    col: ax.ListColumn,
) -> Tuple[List[Any], pytree.Context]:
    return (
        [
            col.values,
            col.offsets,
            col.presence or torch.empty(0),
        ],
        None,
    )


def _list_column_unflatten(
    values: List[Any], context: pytree.Context
) -> ax.ListColumn:
    unpacked = _unpack_vals(values)
    return ax.ListColumn(
        values=unpacked[0],
        offsets=unpacked[1],
        presence=unpacked[2],
    )

def _struct_column_flatten(
    col: ax.StructColumn,
) -> Tuple[List[Any], pytree.Context]:
    return (list(col.field_columns.values()), list(col.field_columns.keys()))


def _struct_column_unflatten(
    values: List[Any], context: pytree.Context
) -> ax.StructColumn:
    return ax.StructColumn(field_columns={key: val for key, val in zip(context, values)})

def register_pytree_nodes() -> None:
    pytree._register_pytree_node(
        ax.NumericColumn, _numeric_column_flatten, _numeric_column_unflatten
    )
    pytree._register_pytree_node(
        ax.ListColumn,
        _list_column_flatten,
        _list_column_unflatten,
    )
    pytree._register_pytree_node(
        ax.StringColumn,
        _string_column_flatten,
        _string_column_unflatten,
    )
    pytree._register_pytree_node(
        ax.StructColumn,
        _struct_column_flatten,
        _struct_column_unflatten,
    )
    
    
class Store:
    val = None

    def set(self, val):
        self.val = val

    def __call__(self):
        return self.val

def fake_signature(fn, nargs):
    """FX gets confused by varargs, de-confuse it"""
    argnames = ",".join(f"arg{i}" for i in range(nargs))
    return eval(f"lambda {argnames}: fn({argnames})", {"fn": fn})


# TODO: This is a temporary fix that should have been coverd in the new 
# version of functorch
def make_fx(f, decomposition_table=None):
    if decomposition_table is None:
        decomposition_table = {}

    @functools.wraps(f)
    def wrapped(*args):
        phs = pytree.tree_map(lambda x: fx.PH, args)
        if (
            not hasattr(inspect.unwrap(f), '__code__') or 
            inspect.unwrap(f).__code__.co_flags & inspect.CO_VARARGS
        ):
            # FX (inspect does not get correct argument count) doesn't 
            # support varargs, so we gotta fake up a wrapper
            # TODO: Would be nice to fix this at the source...
            func = fake_signature(f, len(phs))
        else:
            func = f

        with python_key.pythonkey_decompose(decomposition_table):
            t = python_key.pythonkey_trace(
                python_key.wrap_key(func, args), concrete_args=tuple(phs),
            )
        return t

    return wrapped


def trace(
    fn: Union[torch.nn.Module, Callable[..., Any]],
    decompositions: Optional[Dict] = None,
) -> Tuple[Callable, Store]:

    register_pytree_nodes()

    cached_res = None
    if decompositions is None:
        decompositions = aot_autograd_decompositions

    store = Store()

    @functools.wraps(fn)
    def returned_function(*args, **kwargs):
        nonlocal cached_res
        # Now flatten the tensor args
        tensor_args, tensor_args_spec = pytree.tree_flatten((args, kwargs))

        # Compile the function and save it in the cache
        if cached_res is None:
            out_spec = PytreeThunk()

            def flat_fn(*flat_args):
                # The input are flattened tensor args. Prepare the args in the
                # order that original function expects. Add static args as well.
                # They will appear as tensor constants in the traced graph.
                nonlocal out_spec
                _args, _kwargs = pytree.tree_unflatten(flat_args, tensor_args_spec)
                _tree_out = fn(*_args, **_kwargs)
                _flat_out, _spec = pytree.tree_flatten(_tree_out)
                for i in _flat_out:
                    is_known_type = False
                    for j in KNOWN_TYPES:
                        if isinstance(i, j):
                            is_known_type = True
                            break
                    if not is_known_type:
                        raise RuntimeError(
                            f"Found {type(i)} in output, which is not a known type. "
                            "If this type holds tensors, you need to register a pytree for it. "
                            "See https://github.com/pytorch/functorch/issues/475 for a brief "
                            "explanation why. If you don't need to register a pytree, please "
                            "leave a comment explaining your use case and we'll make this more "
                            "ergonomic to deal with"
                        )
                out_spec.set(_spec)
                return _flat_out

            fw_module = make_fx(flat_fn, decompositions)(*tensor_args)
            cached_res = (fw_module, out_spec)
            store.set(fw_module)

        cached_fx_module, out_spec = cached_res
        out = cached_fx_module(*tensor_args)
        return out_spec.unflatten(out)

    return returned_function, store
