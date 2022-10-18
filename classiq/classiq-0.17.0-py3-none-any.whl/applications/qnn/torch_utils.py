from collections.abc import Sized
from functools import reduce
from typing import Callable, Optional, Tuple, Union

import torch
import torch.nn as nn
from torch import Tensor

from classiq.exceptions import ClassiqValueError


def get_shape_second_dimension(shape: torch.Size):
    if not isinstance(shape, Sized):
        raise ClassiqValueError("Invalid shape type - must have `__len__`")

    if len(shape) == 1:
        return 1
    elif len(shape) == 2:
        return shape[1]
    else:
        raise ClassiqValueError("Invalid shape dimension - must be 1D or 2D")


def get_shape_first_dimension(shape: torch.Size):
    if not isinstance(shape, Sized):
        raise ClassiqValueError("Invalid shape type - must have `__len__`")

    if len(shape) in (1, 2):
        return shape[0]
    else:
        raise ClassiqValueError("Invalid shape dimension - must be 1D or 2D")


def iter_inputs_weights(
    function: Callable[[Tensor, Tensor], Union[Tensor, float]],
    inputs: Tensor,
    weights: Tensor,
    expected_shape: Optional[Tuple[int, ...]] = None,
    force_single_weight_per_input: bool = False,
) -> Tensor:
    """
    inputs is of shape (batch_size, in_features)
    weights is of shape (out_features, num_weights)
    """
    if force_single_weight_per_input and get_shape_second_dimension(
        inputs.shape
    ) != get_shape_second_dimension(weights.shape):
        raise ClassiqValueError(
            f"Shape mismatch! the 2nd dimension of both the inputs ({get_shape_second_dimension(inputs.shape)}) and the weights ({get_shape_second_dimension(weights.shape)}) should be the same"
        )

    outer_list = []
    for batch_item in inputs:
        inner_list = []
        for out_weight in weights:
            res = function(batch_item, out_weight)
            inner_list.append(res)
        outer_list.append(inner_list)

    # flattened_outer_list = [item for inner_list in outer_list for item in inner_list]
    # result = torch.stack(flattened_outer_list)
    result = torch.tensor(
        outer_list,
        dtype=torch.float,
        requires_grad=(inputs.requires_grad or weights.requires_grad),
    )
    if expected_shape is not None:
        result = result.reshape(*expected_shape)
    return result


def calculate_amount_of_parameters(net: nn.Module) -> int:
    return sum(  # sum over all parameters
        reduce(int.__mul__, i.shape)  # multiply all dimensions
        for i in net.parameters()
    )
