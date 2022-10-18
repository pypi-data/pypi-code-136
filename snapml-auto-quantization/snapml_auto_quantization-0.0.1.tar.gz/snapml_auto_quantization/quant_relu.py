"""
Quantized version for relu layers.
"""
from . quant_utils import *
from . quant_layer_factory import *
from . quant_base_module import *


@QuantLayerFactory.register('qrelu', (torch.nn.ReLU,))
class QReLU(QBaseModule):
    """
    Quantized version for torch.nn.ReLU.
    """

    def __init__(
            self,
            relu_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QReLU.

        Args:

            relu_module: The floating point relu module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QReLU, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.relu = nn.ReLU(inplace=relu_module.inplace)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.relu(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput


@QuantLayerFactory.register('qrelu6', (torch.nn.ReLU6,))
class QReLU6(QBaseModule):
    """
    Quantized version for torch.nn.ReLU6.
    """

    def __init__(
            self,
            relu6_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QReLU6.

        Args:

            relu6_module: The floating point relu6 module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QReLU6, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.relu6 = nn.ReLU6(inplace=relu6_module.inplace)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.relu6(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
