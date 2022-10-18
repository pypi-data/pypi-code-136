"""
Quantized version for mul.
"""
from . quant_base_module import *
import operator
from . quant_layer_factory import *


@QuantLayerFactory.register('qmul', (operator.mul, torch.mul, 'mul'))
class QMul(QBaseModule):
    """
    Quantized version for mul.
    """

    def __init__(self, num_bits=8, disable_quant=False):
        """
        Initialize QMul.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QMul,
            self).__init__(
            num_inputs=2,
            num_outputs=1,
            num_bits=num_bits,
            disable_quant=disable_quant)

    def forward(self, x, y):
        qinput1 = self.quantize_inputs[0](x)
        qinput2 = self.quantize_inputs[1](y)
        output = qinput1 * qinput2
        qoutput = self.quantize_outputs[0](output)
        return qoutput
