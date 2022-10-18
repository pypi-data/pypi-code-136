"""
Quantized version for adaptive avg pooling layer.
"""
from . quant_base_module import *
from . quant_utils import *
from . quant_layer_factory import *


@QuantLayerFactory.register('qadaptiveavgpool2d',
                            (torch.nn.functional.adaptive_avg_pool2d,
                             'adaptive_avg_pool2d'))
class QAdaptiveAvgPool2d(QBaseModule):
    """
    Quantized version for torch.nn.functional.adaptive_avg_pool2d.
    """

    def __init__(self,
                 num_bits=8, disable_quant=False):
        """
        Initialize QAdaptiveAvgPool2d.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QAdaptiveAvgPool2d, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(self, x, output_size):
        qinput = self.quantize_inputs[0](x)
        output = torch.nn.functional.adaptive_avg_pool2d(qinput, output_size)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
