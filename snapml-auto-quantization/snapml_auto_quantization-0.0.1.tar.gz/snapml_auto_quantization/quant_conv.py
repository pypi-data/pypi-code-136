"""
Quantized version for convolution.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


def conv2d_biprec(
        input,
        weight,
        bias=None,
        stride=1,
        padding=0,
        dilation=1,
        groups=1,
        num_bits_grad=None):
    """
    Conduct biprecision quantization for conv2d.

    Args:

        input: Input tensor.

        weight: Weight of conv2d.

        bias: Learnable bias if not None.

        stride: Stride of the convolution. Default: 1.

        padding: Padding added to all four sides of the input. Default: 0.

        dilation: Spacing between kernel elements. Default: 1.

        groups: Number of blocked connections from input channels to output channels. Default: 1.

        num_bits_grad: Number of bits for gradients quantization. Default: None.

    Returns:

        Quantized result tensor.

    """
    out1 = F.conv2d(input.detach(), weight, bias,
                    stride, padding, dilation, groups)
    out2 = F.conv2d(
        input,
        weight.detach(),
        bias.detach() if bias is not None else None,
        stride,
        padding,
        dilation,
        groups)
    out2 = quantize_grad(out2, num_bits=num_bits_grad, flatten_dims=(1, -1))
    return out1 + out2 - out1.detach()


@QuantLayerFactory.register('qconv2d', (torch.nn.Conv2d,))
class QConv2d(QBaseModule):
    """
    Quantized version for torch.nn.Conv2d.
    """

    def __init__(
            self,
            conv2d_module,
            num_bits=8,
            num_bits_weight=8,
            num_bits_grad=8,
            biprecision=False,
            disable_quant=False):
        """
        Initialize QConv2d.

        Args:

            conv2d_module: the floating point conv2d module.

            num_bits: Number of bits for quantization. Default: 8.

            num_bits_weight: Number of bits for weights quantization. Default: 8.

            num_bits_grad: Number of bits for gradients quantization. Default: 8.

            biprecision: If True, we use biprecision. Default: False.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QConv2d,
            self).__init__(
            num_inputs=1,
            num_outputs=1,
            num_bits=num_bits,
            shape_measure=(1, 1, 1, 1),
            flatten_dims=(1, -1),
            disable_quant=disable_quant,
            per_axis='weight, bias')

        self.num_bits_weight = num_bits_weight or num_bits
        self.num_bits_grad = num_bits_grad
        self.biprecision = biprecision
        self.conv2d = nn.Conv2d(
            conv2d_module.in_channels,
            conv2d_module.out_channels,
            conv2d_module.kernel_size,
            conv2d_module.stride,
            conv2d_module.padding,
            conv2d_module.dilation,
            conv2d_module.groups,
            bias=True if conv2d_module.bias is not None else False)

        self.weight = self.conv2d.weight
        self.bias = self.conv2d.bias
        self.register_buffer('qweight', torch.zeros_like(self.weight))
        self.register_buffer('qbias', torch.zeros_like(self.bias) if self.bias is not None else None)
        self.register_buffer('qweight_scale', torch.ones(conv2d_module.out_channels, 1, 1, 1))

    def forward(self, input):
        qinput = self.quantize_inputs[0](input)
        weight_qparams = calculate_qparams(
            self.weight, num_bits=self.num_bits_weight, flatten_dims=(
                1, -1), reduce_dim=None, sym=True)

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
                    0, -1), reduce_dim=None, signed=True, sym=True, is_bias=True, doNothing=self.disable_quant)
                self.qbias.data = qbias.clone()
            else:
                qbias = self.qbias.data.clone()
        else:
            qbias = None
        if not self.biprecision or self.num_bits_grad is None:
            output = F.conv2d(
                qinput,
                qweight,
                qbias,
                self.conv2d.stride,
                self.conv2d.padding,
                self.conv2d.dilation,
                self.conv2d.groups)
            if self.num_bits_grad is not None:
                output = quantize_grad(
                    output, num_bits=self.num_bits_grad, flatten_dims=(
                        1, -1), doNothing=self.disable_quant)
        else:
            output = conv2d_biprec(
                qinput,
                qweight,
                qbias,
                self.conv2d.stride,
                self.conv2d.padding,
                self.conv2d.dilation,
                self.conv2d.groups,
                num_bits_grad=self.num_bits_grad)
        qoutput = self.quantize_outputs[0](output)
        return qoutput
