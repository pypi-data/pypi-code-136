"""
Quantized version for avgpooling layer.
"""
from . quant_utils import *
from . quant_layer_factory import *
from . quant_base_module import *


@QuantLayerFactory.register('qavgpool2d', (torch.nn.AvgPool2d,))
class QAvgPool2d(QBaseModule):
    """
    Quantized version for torch.nn.MaxPool2d.
    """

    def __init__(
            self,
            avgpool2d_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QAvgPool2d.

        Args:

            avgpool2d_module: the floating point avgpool2d module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QAvgPool2d, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.ap = nn.AvgPool2d(
            avgpool2d_module.kernel_size,
            stride=avgpool2d_module.stride,
            padding=avgpool2d_module.padding,
            count_include_pad=avgpool2d_module.count_include_pad,
            divisor_override=avgpool2d_module.divisor_override,
            ceil_mode=avgpool2d_module.ceil_mode)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.ap(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
