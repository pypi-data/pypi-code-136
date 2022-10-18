"""
Quantized version for PReLU layer.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qprelu2d', (torch.nn.PReLU,))
class QPReLU(QBaseModule):
    """
    Quantized version for torch.nn.PReLU.
    """

    def __init__(
            self,
            prelu_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QPReLU.

        Args:

            prelu_module: the floating point PReLU module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QPReLU, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        if prelu_module.num_parameters != 1:
            raise Exception("PReLU: Only supports 1 for num_parameters")

        self.PReLU = nn.PReLU(
            num_parameters=prelu_module.num_parameters,
            init=prelu_module.init,
            device=prelu_module.device,
            dtype=prelu_module.dtype)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.PReLU(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
