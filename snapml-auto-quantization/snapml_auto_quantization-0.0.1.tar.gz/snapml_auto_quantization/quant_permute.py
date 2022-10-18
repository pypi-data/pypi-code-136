"""
Quantized version for permute layers.
"""
from . quant_utils import *
from . quant_layer_factory import *
from . quant_base_module import *


@QuantLayerFactory.register('qpermute', (torch.permute, 'permute',))
class QPermute(QBaseModule):
    """
    Quantized version for torch.permute.
    """

    def __init__(
            self,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QPermute.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QPermute, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)


    def forward(self, x, dims):
        qinput = self.quantize_inputs[0](x)
        output = torch.permute(qinput, dims)
        qoutput = self.quantize_outputs[0](output)
        return qoutput

