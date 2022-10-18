"""
Quantized version for softmax layer.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qsoftmax', (torch.nn.Softmax,))
class QSoftmax(QBaseModule):
    """
    Quantized version for torch.nn.Softmax.
    """

    def __init__(
            self,
            softmax_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QSoftmax.

        Args:

            softmax_module: the floating point softmax module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QSoftmax, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        if softmax_module.dim != 1:
            raise Exception("Only supports softmax along channel axis")
        self.softmax = nn.Softmax(dim=softmax_module.dim)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.softmax(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
