"""
Quantized version for concat.
"""
from . quant_base_module import *
import operator
from . quant_layer_factory import *


@QuantLayerFactory.register('qconcat', (torch.concat, torch.cat, 'concat', 'cat'))
class QConcat(QBaseModule):
    """
    Quantized version for concat.
    """

    def __init__(self, num_inputs, num_bits=8, disable_quant=False):
        """
        Initialize QConcat.

        Args:

            num_inputs: Number of inputs feature maps.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QConcat,
            self).__init__(
            num_inputs=num_inputs,
            num_outputs=1,
            num_bits=num_bits,
            disable_quant=disable_quant)

    def forward(self, inputs, dim=0, out=None):
        qinputs = []
        for i in range(self.number_inputs):
            m = self.quantize_inputs[i]
            x = inputs[i].clone()
            y = m(x)
            qinputs.append(y)
        qinputs = tuple(qinputs)
        out = torch.cat(qinputs, dim)
        qoutput = self.quantize_outputs[0](out)
        return qoutput

