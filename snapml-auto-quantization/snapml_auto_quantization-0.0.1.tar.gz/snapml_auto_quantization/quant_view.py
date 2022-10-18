"""
Quantized version for view layers.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qview', (torch.Tensor.view, 'view',))
class QView(QBaseModule):
    """
    Quantized version for torch.reshape.
    """

    def __init__(
            self,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QView.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QView, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(self, x, *argv):
        qinput = self.quantize_inputs[0](x)
        output = qinput.view(*argv)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
