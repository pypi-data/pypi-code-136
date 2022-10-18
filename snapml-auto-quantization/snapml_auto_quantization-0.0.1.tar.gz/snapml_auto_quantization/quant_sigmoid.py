"""
Quantized version for sigmoid.
"""
import torch.nn

from .quant_base_module import *
from .quant_utils import *
from .quant_layer_factory import *


@QuantLayerFactory.register('qsigmoid', (torch.nn.Sigmoid,))
class QSigmoid(QBaseModule):
    """
    Quantized version for torch.nn.Sigmoid.
    """

    def __init__(self, num_bits=8, disable_quant=False):
        """
        Initialize QSigmoid.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QSigmoid, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = torch.nn.Sigmoid(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
