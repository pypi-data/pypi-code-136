"""
Quantized version for mean layer.
"""
from . quant_base_module import *
from . quant_layer_factory import *


@QuantLayerFactory.register('qmean', (torch.mean, 'mean'))
class QMean(QBaseModule):
    """
    Quantized version for torch.mean.
    """

    def __init__(self,
                 num_bits=8, disable_quant=False):
        """
        Initialize QMean.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QMean,
            self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            disable_quant=disable_quant)

    def forward(self, x, dim, keepdim=False, *, dtype=None, out=None):
        qinput = self.quantize_inputs[0](x)
        output = torch.mean(qinput, dim=dim, keepdim=keepdim, dtype=dtype)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
