from . quant_utils import *


class QBaseModule(nn.Module):
    """
    Quantized version in general. The quantized version of specific modules or non-modules should have it as the base class whenever possible.
    """

    def __init__(
            self,
            num_inputs,
            num_outputs,
            num_bits=8,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(0, -1),
            disable_quant=False,
            per_axis='none'):
        """
        Initialize .

        Args:

            num_inputs: Number of input feature maps.

            num_outputs: Number of output feature maps.

            num_bits: Number of bits for quantization. Default: 8.

            shape_measure: shape of quantization statistics. Defalut: (1, 1, 1, 1).

            flatten_dims: dimensions to be flattened. Default: (0, -1).

            disable_quant: If True, we disable collection of quantization statistics. Default: False.

            per_axis: specify whether there is anything for per-axis quantization. Default: 'none'
        """
        super().__init__()
        self.num_bits = num_bits
        self.quantize_inputs = nn.ModuleList()
        self.number_inputs = num_inputs
        for i in range(num_inputs):
            self.quantize_inputs.append(
                QuantMeasure(
                    self.num_bits,
                    shape_measure=shape_measure,
                    flatten_dims=flatten_dims,
                    disable_quant=disable_quant,
                    per_axis=per_axis))

        self.quantize_outputs = nn.ModuleList()
        self.number_outputs = num_outputs
        for i in range(num_outputs):
            self.quantize_outputs.append(
                QuantMeasure(
                    self.num_bits,
                    shape_measure=shape_measure,
                    flatten_dims=flatten_dims,
                    disable_quant=disable_quant))

        self.disable_quant = disable_quant
