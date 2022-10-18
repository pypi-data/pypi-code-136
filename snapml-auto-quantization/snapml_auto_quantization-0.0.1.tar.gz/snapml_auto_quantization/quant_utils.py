"""
Quantization utility functions.
"""
from collections import namedtuple
import numpy as np
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd.function import InplaceFunction, Function
from torch.autograd import Function

QParams = namedtuple('QParams', ['floating_range', 'floating_for_q_zero_point', 'num_bits'])
"""Quantization statistic parameters"""

_DEFAULT_FLATTEN = (1, -1)
_DEFAULT_FLATTEN_GRAD = (0, -1)

DEVICE = torch.device('cpu')
if torch.cuda.is_available():
    DEVICE = torch.device('cuda')


def _deflatten_as(x, x_full):
    shape = list(x.shape) + [1] * (x_full.dim() - x.dim())
    return x.view(*shape)


class QuantizeFunction(Function):
    """
    Forward pass and backward pass for quantization simulation.
    """

    @staticmethod
    def symbolic(g, input, minimum, maximum, per_axis):
        return g.op('QuantizeSnap',
                    input,
                    min_f=minimum,
                    max_f=maximum,
                    per_axis_s=per_axis)

    @staticmethod
    def forward(ctx, input, minimum, maximum, per_axis):
        ctx.input = ctx
        return input.clone()

    @staticmethod
    def backward(ctx, grad_output):
        grad_input = grad_output.clone()
        return grad_input.clone()


class QuantizeSnap(nn.Module):
    """
    Wrapper for applying QuantizeFunction.
    """

    def __init__(self, per_axis='none'):
        super(QuantizeSnap, self).__init__()
        self.per_axis = per_axis

    def forward(self, input, minimum, maximum):
        return QuantizeFunction.apply(input, minimum, maximum, self.per_axis)


def calculate_qparams(
        x,
        num_bits,
        flatten_dims=_DEFAULT_FLATTEN,
        reduce_dim=0,
        reduce_type='full',
        keepdim=False,
        sym=False):
    """
    Calculate quantization statistics.

    Args:

        x: tensor to be quantized.

        num_bits: quantized bits number.

        flatten_dims: dimension of x to be flattened.

        reduce_dim: along which dimension do we reduce the results.

        reduce_type: the reduction type, 'mean' or 'full'.

        keepdim: if keepdim is True, the output tensor is of the same size as input except in the dimension(s) dim where it is of size 1. Otherwise, dim is squeezed (see torch.squeeze()), resulting in the output tensor having 1 (or len(dim)) fewer dimension(s).

        sys: if True, we apply symmetric quantization. 

    Returns:

        Quantization statistic parameters.

    """
    with torch.no_grad():
        x_flat = x.flatten(*flatten_dims)
        if x_flat.dim() == 1:
            min_values = _deflatten_as(x_flat.min(), x)
            max_values = _deflatten_as(x_flat.max(), x)
        else:
            min_values = _deflatten_as(x_flat.min(-1)[0], x)
            max_values = _deflatten_as(x_flat.max(-1)[0], x)
        if reduce_dim is not None:
            if reduce_type == 'mean':
                min_values = min_values.mean(reduce_dim, keepdim=keepdim)
                max_values = max_values.mean(reduce_dim, keepdim=keepdim)
            else:
                min_values = min_values.min(reduce_dim, keepdim=keepdim)[0]
                max_values = max_values.max(reduce_dim, keepdim=keepdim)[0]

        min_values[min_values > 0] = 0
        max_values[max_values < 0] = 0

        floating_range_values = max_values - min_values
        floating_for_q_zero_point = min_values

        if sym:
            mv = (
                torch.stack(
                    (max_values,
                     min_values),
                    dim=0)).abs().max(
                dim=0)[0]
            floating_range_values = mv * 2
            floating_for_q_zero_point = torch.minimum(floating_for_q_zero_point, -mv)

        return QParams(floating_range=floating_range_values, floating_for_q_zero_point=floating_for_q_zero_point,
                       num_bits=num_bits)


def calculate_scale(qparams, signed=False, sym=False):
    """
    Calculate the quantization scale.

    Args:

        qparams: quantization statistics regarding the floating point numbers.

        signed: whether or not we use signed integers for quantization. Default: False.

        sym: whether or not we use symmetric quantization. Default: False.

    Returns:

        quantization scale.
    """
    num_bits = qparams.num_bits
    if sym and num_bits == 8:
        qmin = -(2. ** (num_bits - 1)) if signed else 0.
        qmax = qmin + 2. ** num_bits - 2.
        scale = qparams.floating_range / (qmax - qmin)
    else:
        qmin = -(2. ** (num_bits - 1)) if signed else 0.
        qmax = qmin + 2. ** num_bits - 1.
        scale = qparams.floating_range / (qmax - qmin)

    return scale


class UniformQuantize(InplaceFunction):
    """
    Convert bias term floating numbers to quantized numbers and convert back during forward pass.
    """

    @staticmethod
    def forward(
            ctx,
            input,
            scale=None,
            num_bits=None,
            qparams=None,
            flatten_dims=_DEFAULT_FLATTEN,
            reduce_dim=0,
            dequantize=True,
            signed=False,
            stochastic=False,
            inplace=False,
            sym=False,
            is_bias=False):

        ctx.inplace = inplace

        if ctx.inplace:
            ctx.mark_dirty(input)
            output = input
        else:
            output = input.clone()

        if qparams is None:
            assert num_bits is not None, "either provide qparams of num_bits to quantize"
            qparams = calculate_qparams(
                input,
                num_bits=num_bits,
                flatten_dims=flatten_dims,
                reduce_dim=reduce_dim,
                sym=sym)

        floating_for_q_zero_point = qparams.floating_for_q_zero_point
        num_bits = qparams.num_bits
        if sym and num_bits == 8:
            qmin = -(2. ** (num_bits - 1)) if signed else 0.
            qmax = qmin + 2. ** num_bits - 2.
        else:
            qmin = -(2. ** (num_bits - 1)) if signed else 0.
            qmax = qmin + 2. ** num_bits - 1.

        if scale is None:
            scale = qparams.floating_range / (qmax - qmin)

        with torch.no_grad():
            scale_d = scale.clone().detach()
            scale_d[scale == 0] = 1
            while len(scale.shape) > len(output.shape):  # For tensors used in Linear layers
                scale = scale.squeeze()
                floating_for_q_zero_point = floating_for_q_zero_point.squeeze()
                scale_d = scale_d.squeeze()

            # zero point for bias is always 0
            q_zero_point = 0 if is_bias else (qmin - floating_for_q_zero_point / scale_d)
            output = output / scale_d + q_zero_point
            if stochastic:
                noise = output.new(output.shape).uniform_(-0.5, 0.5)
                output.add_(noise)
            output.clamp_(qmin, qmax).round_()

            if dequantize:
                output = (output - q_zero_point) * scale
        return output.clone()

    @staticmethod
    def backward(ctx, grad_output):
        # straight-through estimator
        grad_input = grad_output
        return grad_input.clone(), None, None, None, None, None, None, None, None, None, None


class UniformQuantizeGrad(InplaceFunction):
    """
    Convert floating numbers to quantized numbers and convert back during backward pass.
    """

    @staticmethod
    def forward(
            ctx,
            input,
            num_bits=None,
            qparams=None,
            flatten_dims=_DEFAULT_FLATTEN_GRAD,
            reduce_dim=0,
            dequantize=True,
            signed=False,
            stochastic=True):
        ctx.num_bits = num_bits
        ctx.qparams = qparams
        ctx.flatten_dims = flatten_dims
        ctx.stochastic = stochastic
        ctx.signed = signed
        ctx.dequantize = dequantize
        ctx.reduce_dim = reduce_dim
        ctx.inplace = False
        return input.clone()

    @staticmethod
    def backward(ctx, grad_output):
        qparams = ctx.qparams
        with torch.no_grad():
            if qparams is None:
                assert ctx.num_bits is not None, "either provide qparams of num_bits to quantize"
                qparams = calculate_qparams(
                    grad_output,
                    num_bits=ctx.num_bits,
                    flatten_dims=ctx.flatten_dims,
                    reduce_dim=ctx.reduce_dim,
                    reduce_type='extreme')

            grad_input = quantize(
                grad_output,
                num_bits=None,
                qparams=qparams,
                flatten_dims=ctx.flatten_dims,
                reduce_dim=ctx.reduce_dim,
                dequantize=True,
                signed=ctx.signed,
                stochastic=ctx.stochastic,
                inplace=False)
        return grad_input.clone(), None, None, None, None, None, None, None


def quantize(
        x,
        scale=None,
        num_bits=None,
        qparams=None,
        flatten_dims=_DEFAULT_FLATTEN,
        reduce_dim=0,
        dequantize=True,
        signed=False,
        stochastic=False,
        inplace=False,
        sym=False,
        is_bias=False,
        doNothing=False):
    """
    Wrapper for applying UniformQuantize on bias term.
    """
    if doNothing:
        return x
    else:
        return UniformQuantize.apply(x, scale, num_bits, qparams, flatten_dims, reduce_dim,
                                     dequantize, signed, stochastic, inplace, sym, is_bias)


def quantize_grad(
        x,
        num_bits=None,
        qparams=None,
        flatten_dims=_DEFAULT_FLATTEN_GRAD,
        reduce_dim=0,
        dequantize=True,
        signed=False,
        stochastic=True,
        doNothing=False):
    """
    Wrapper for applying UniformQuantizeGrad.
    """
    if doNothing:
        return x
    else:
        return UniformQuantizeGrad.apply(x, num_bits, qparams, flatten_dims,
                                         reduce_dim, dequantize, signed, stochastic)


class QuantMeasure(nn.Module):
    """
    Perform quantization and accumulate statistics during training or when necessary.
    """

    def __init__(
            self,
            num_bits=8,
            shape_measure=(
                    1,
            ),
            flatten_dims=_DEFAULT_FLATTEN,
            inplace=False,
            dequantize=True,
            stochastic=False,
            momentum=0.1,
            measure=False,
            disable_quant=False,
            per_axis='none'):
        """
        Initialize QuantMeasure.

        Args:

            num_bits: quantized bits number.

            shape_measure: shape for the running quantization statistics. 

            flatten_dims: dimensions along which to reduce the quantization statistics.

            inplace: if True, conduct inplace quantization simulation.

            dequantize: if True, dequantize the quantized number back to floating point number.

            stochastic: if Ture, add smally noise on the quantized number.

            momentum: momentum for accumulating the running quantization statistics.

            measure: if True, accumulate the running quantization statistics.

            disable_quant: if True, we disable quantization statistic collection.  

            per_axis: specify whether there is anything for per-axis quantization. Default: 'none'

        """
        super(QuantMeasure, self).__init__()
        self.register_buffer('running_floating_for_q_zero_point', torch.zeros(
            *shape_measure, device=DEVICE))
        self.register_buffer('running_range', torch.zeros(
            *shape_measure, device=DEVICE))
        self.register_buffer('qparam_scale', torch.zeros(
            *shape_measure, device=DEVICE))
        self.measure = measure
        if self.measure:
            self.register_buffer('num_measured', torch.zeros(1, device=DEVICE))
        self.flatten_dims = flatten_dims
        self.momentum = momentum
        self.dequantize = dequantize
        self.stochastic = stochastic
        self.inplace = inplace
        self.num_bits = num_bits
        self.quant = QuantizeSnap(per_axis=per_axis)
        self.disable_quant = disable_quant

    def forward(self, input, qparams=None, logstr=None):
        if self.training or self.measure:
            if qparams is None:
                qparams = calculate_qparams(
                    input,
                    num_bits=self.num_bits,
                    flatten_dims=self.flatten_dims,
                    reduce_dim=0)
            with torch.no_grad():
                if self.measure:
                    momentum = self.num_measured / (self.num_measured + 1)
                    self.num_measured += 1
                else:
                    momentum = self.momentum
                momentum = torch.tensor(momentum).to(DEVICE)
                self.running_floating_for_q_zero_point.mul_(momentum).add_(
                    qparams.floating_for_q_zero_point * (1 - momentum))
                self.running_range.mul_(momentum).add_(
                    qparams.floating_range * (1 - momentum))
                # the current qparams
                # self.qparam_scale = _calculate_scale(qparams)
                # or the accumulated qparams
                self.qparam_scale = calculate_scale(QParams(
                    floating_range=self.running_range,
                    floating_for_q_zero_point=self.running_floating_for_q_zero_point,
                    num_bits=self.num_bits))
        else:
            qparams = QParams(
                floating_range=self.running_range,
                floating_for_q_zero_point=self.running_floating_for_q_zero_point,
                num_bits=self.num_bits)
        if self.measure:
            return input
        else:
            q_input = quantize(
                input,
                qparams=qparams,
                dequantize=self.dequantize,
                stochastic=self.stochastic,
                inplace=self.inplace,
                doNothing=self.disable_quant)
            q_input = self.quant(q_input, self.running_floating_for_q_zero_point.reshape(
                1).item(), (self.running_floating_for_q_zero_point + self.running_range).reshape(1).item())
            return q_input


def set_measure(model, measure=True):
    """
    Set up QuantMeasure.
    """
    for m in model.children():
        if isinstance(m, QuantMeasure):
            m.measure = measure
            if measure and 'num_measured' not in m.state_dict():
                m.register_buffer('num_measured', torch.zeros(1))
        set_measure(m, measure)
