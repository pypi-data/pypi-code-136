"""
Quantized version for resizing.
"""
from . quant_base_module import *
from . quant_utils import *
from . quant_layer_factory import *


@QuantLayerFactory.register('qresize',
                            (torch.nn.functional.interpolate,))
class QResize(QBaseModule):
    """
    Quantized version for torch.nn.functional.interpolate.
    """

    def __init__(self,
                 num_bits=8, disable_quant=False):
        """
        Initialize QResize.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QResize, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(
            self,
            x,
            size=None,
            scale_factor=None,
            mode='nearest',
            align_corners=None,
            recompute_scale_factor=None,
            antialias=False):
        qinput = self.quantize_inputs[0](x)
        output = torch.nn.functional.interpolate(
            qinput,
            size=size,
            scale_factor=scale_factor,
            mode=mode,
            align_corners=align_corners,
            recompute_scale_factor=recompute_scale_factor,
            antialias=antialias)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
