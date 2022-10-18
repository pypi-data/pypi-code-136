"""
Quantized version for padding layer.
"""
import torch.nn.functional

from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qpad', (torch.nn.functional.pad,))
class QPad(QBaseModule):
    """
    Quantized version for torch.nn.functional.pad.
    """

    def __init__(
            self,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QPad.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QPad, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(self, x, pad, mode='constant', value=None):
        qinput = self.quantize_inputs[0](x)
        output = torch.nn.functional.pad(x, pad, mode, value)
        qoutput = self.quantize_outputs[0](output)
        return qoutput


@QuantLayerFactory.register('qconstantpad', (torch.nn.ConstantPad2d,))
class QConstantPad(QBaseModule):
    """
    Quantized version for torch.nn.ConstantPad2d.
    """

    def __init__(
            self,
            constantpad_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QConstantPad.

        Args:

            constantpad_module: the floating point ConstantPad2D module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QConstantPad, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.pad = torch.nn.ConstantPad2d(
            padding=constantpad_module.padding,
            value=constantpad_module.value)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.pad(x)
        qoutput = self.quantize_outputs[0](output)
        return qoutput


@QuantLayerFactory.register('qreflectionpad', (torch.nn.ReflectionPad2d,))
class QReflectionPad(QBaseModule):
    """
    Quantized version for torch.nn.ReflectionPad2d.
    """

    def __init__(
            self,
            reflectionpad_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QReflectionPad.

        Args:

            reflectionpad_module: the floating point ReflectionPad2D module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QReflectionPad, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.pad = torch.nn.ReflectionPad2d(padding=reflectionpad_module.padding)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.pad(x)
        qoutput = self.quantize_outputs[0](output)
        return qoutput


@QuantLayerFactory.register('qreplicationpad', (torch.nn.ReplicationPad2d,))
class QReplicationPad(QBaseModule):
    """
    Quantized version for torch.nn.ReplicationPad2d.
    """

    def __init__(
            self,
            replicationpad_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QReplicationPad.

        Args:

            replicationpad_module: the floating point ReplicationPad2D module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QReplicationPad, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.pad = torch.nn.ReplicationPad2d(padding=replicationpad_module.padding)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.pad(x)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
