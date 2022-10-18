"""
Quantized version for add.
"""
from . quant_base_module import *
import operator
from . quant_layer_factory import *


@QuantLayerFactory.register('qadd', (operator.add, torch.add, 'add'))
class QAdd(QBaseModule):
    """
    Quantized version for add, which can be multiple forms in Pytorch, like x.add_(y), x+y, torch.add(x,y).
    """

    def __init__(self, num_bits=8, disable_quant=False):
        """
        Initialize QAdd.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QAdd,
            self).__init__(
            num_inputs=2,
            num_outputs=1,
            num_bits=num_bits,
            disable_quant=disable_quant)

    def forward(self, x, y):
        qinput1 = self.quantize_inputs[0](x)
        qinput2 = self.quantize_inputs[1](y)
        output = qinput1 + qinput2
        qoutput = self.quantize_outputs[0](output)
        return qoutput
