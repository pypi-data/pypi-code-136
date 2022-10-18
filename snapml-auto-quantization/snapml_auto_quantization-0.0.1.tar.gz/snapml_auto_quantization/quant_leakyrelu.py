"""
Quantized version for leaky relu layer.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qleakyrelu2d', (torch.nn.LeakyReLU,))
class QLeakyReLU(QBaseModule):
    """
    Quantized version for torch.nn.LeakyReLU.
    """

    def __init__(
            self,
            leakyrelu_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QLeakyReLU.

        Args:

            leakyrelu_module: the floating point LeakyReLU module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QLeakyReLU, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.LeakyReLU = nn.LeakyReLU(
            negative_slope=leakyrelu_module.negative_slope,
            inplace=leakyrelu_module.inplace)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.LeakyReLU(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
