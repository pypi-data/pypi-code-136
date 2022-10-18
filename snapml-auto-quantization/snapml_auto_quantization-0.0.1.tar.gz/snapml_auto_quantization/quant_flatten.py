"""
Quantized version for flatten layer.
"""
from . quant_utils import *
from . quant_layer_factory import *
from . quant_base_module import *


@QuantLayerFactory.register('qflatten_module', (torch.nn.Flatten, ))
class QFlattenModule(QBaseModule):
    """
    Quantized version for torch.nn.Flatten.
    """

    def __init__(
            self,
            flatten_module,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QFlattenModule.

        Args:

            flatten_module: the floating point module.

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QFlattenModule, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)
        self.flatten = nn.Flatten(
            start_dim=flatten_module.start_dim,
            end_dim=flatten_module.end_dim)

    def forward(self, x):
        qinput = self.quantize_inputs[0](x)
        output = self.flatten(qinput)
        qoutput = self.quantize_outputs[0](output)
        return qoutput


@QuantLayerFactory.register('qflatten_non_module', (torch.flatten, 'flatten'))
class QFlattenNonModule(QBaseModule):
    """
    Quantized version for torch.flatten.
    """

    def __init__(
            self,
            num_bits=8,
            disable_quant=False):
        """
        Initialize QFlattenNonModule.

        Args:

            num_bits: Number of bits for quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(QFlattenNonModule, self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant)

    def forward(self, x, start_dim=0, end_dim=-1):
        qinput = self.quantize_inputs[0](x)
        output = torch.flatten(qinput, start_dim=start_dim, end_dim=end_dim)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
