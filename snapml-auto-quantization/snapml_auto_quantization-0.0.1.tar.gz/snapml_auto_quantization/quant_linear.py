"""
Quantized version for linear layer.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


def linear_biprec(input, weight, bias=None, num_bits_grad=None):
    """
    Conduct biprecision quantization for linear.

    Args:

        input: Input tensor.

        weight: Weight of linear.

        bias: Learnable bias if not None.

        num_bits_grad: Number of bits for gradients quantization. Default: None.

    Returns:

        Quantized result tensor.

    """
    out1 = F.linear(input.detach(), weight, bias)
    out2 = F.linear(input, weight.detach(), bias.detach()
    if bias is not None else None)
    out2 = quantize_grad(out2, num_bits=num_bits_grad)
    return out1 + out2 - out1.detach()


@QuantLayerFactory.register('qlinear', (torch.nn.Linear,))
class QLinear(QBaseModule):
    """
    Quantized version for torch.nn.Linear.
    """

    def __init__(
            self,
            linear_module,
            num_bits=8,
            num_bits_weight=8,
            num_bits_grad=8,
            biprecision=False,
            disable_quant=False):
        """
        Initialize QLinear.

        Args:

            linear_module: the floating point linear module.

            num_bits: Number of bits for quantization. Default: 8.

            num_bits_weight: Number of bits for weights quantization. Default: 8.

            num_bits_grad: Number of bits for gradients quantization. Default: 8.

            biprecision: If True, we use biprecision. Default: False.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QLinear,
            self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1),
            flatten_dims=(0, -1),
            disable_quant=disable_quant)

        self.num_bits_weight = num_bits_weight or num_bits
        self.num_bits_grad = num_bits_grad
        self.biprecision = biprecision
        self.linear = nn.Linear(
            linear_module.in_features,
            linear_module.out_features,
            bias=True if linear_module.bias is not None else False)

        self.weight = self.linear.weight
        self.bias = self.linear.bias
        self.register_buffer('qweight', torch.zeros_like(self.weight))
        self.register_buffer('qbias', torch.zeros_like(self.bias) if self.bias is not None else None)
        self.register_buffer('qweight_scale', torch.ones(1))

    def forward(self, input):
        qinput = self.quantize_inputs[0](input)
        # if flatten_dims=(1, -1), in the final onnx graph, there will be an
        # extra FLatten layer flattening the weights of fc
        weight_qparams = calculate_qparams(
            self.weight, num_bits=self.num_bits_weight, flatten_dims=(
                0, -1), reduce_dim=0, sym=True)

        if not self.disable_quant:
            qweight = quantize(self.weight, qparams=weight_qparams,
                               sym=True, doNothing=self.disable_quant)
            self.qweight.data = qweight.clone()
            self.qweight_scale = calculate_scale(weight_qparams, sym=True)
        else:
            qweight = self.qweight.data.clone()

        if self.bias is not None:
            if not self.disable_quant:
                qbias_scale = self.quantize_inputs[0].qparam_scale * self.qweight_scale
                qbias = quantize(self.bias, scale=qbias_scale, num_bits=32, flatten_dims=(
                    0, -1), signed=True, sym=True, is_bias=True, doNothing=self.disable_quant)
                self.qbias.data = qbias.clone()
            else:
                qbias = self.qbias.data.clone()
        else:
            qbias = None

        if not self.biprecision or self.num_bits_grad is None:
            output = F.linear(qinput, qweight, qbias)
            if self.num_bits_grad is not None:
                output = quantize_grad(
                    output, num_bits=self.num_bits_grad, flatten_dims=(
                        1, -1), doNothing=self.disable_quant)
        else:
            output = linear_biprec(qinput, qweight, qbias, self.num_bits_grad)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
