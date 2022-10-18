"""
Quantized version for maxpooling layer.
"""
from . quant_utils import *
from . quant_layer_factory import *
from . quant_base_module import *


@QuantLayerFactory.register('qmaxpool2d', (torch.nn.MaxPool2d,))
class QMaxPool2d(QBaseModule):
    """
    Quantized version for torch.nn.MaxPool2d.
    """

    def __init__(
            self,
            maxpool2d_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QMaxPool2d.

        Args:

            maxpool2d_module: the floating point maxpool2d module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QMaxPool2d, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

        self.mp = nn.MaxPool2d(
            maxpool2d_module.kernel_size,
            maxpool2d_module.stride,
            maxpool2d_module.padding,
            maxpool2d_module.dilation,
            maxpool2d_module.return_indices,
            maxpool2d_module.ceil_mode)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.mp(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
