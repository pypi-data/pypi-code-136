"""
Quantized version for deconvolution.
"""
from .quant_utils import *
from .quant_layer_factory import *
from .quant_base_module import *


@QuantLayerFactory.register('qdeconv2d', (torch.nn.ConvTranspose2d,))
class QConvTranspose2d(QBaseModule):
    """
    Quantized version for torch.nn.ConvTranspose2d.
    """

    def __init__(
            self,
            deconv2d_module,
            num_bits=8,
            num_bits_weight=8,
            num_bits_grad=8,
            disable_quant=False):
        """
        Initialize QConv2d.

        Args:

            deconv2d_module: the floating point deconv2d module.

            num_bits: Number of bits for quantization. Default: 8.

            num_bits_weight: Number of bits for weights quantization. Default: 8.

            num_bits_grad: Number of bits for gradients quantization. Default: 8.

            disable_quant: If True, we disable collection of quantization statistics. Default: False.
        """
        super(
            QConvTranspose2d,
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
        self.deconv2d = nn.ConvTranspose2d(
            deconv2d_module.in_channels,
            deconv2d_module.out_channels,
            deconv2d_module.kernel_size,
            stride=deconv2d_module.stride,
            padding=deconv2d_module.padding,
            output_padding=deconv2d_module.output_padding,
            dilation=deconv2d_module.dilation,
            groups=deconv2d_module.groups,
            padding_mode=deconv2d_module.padding_mode,
            bias=True if deconv2d_module.bias is not None else False)

        self.weight = self.deconv2d.weight
        self.bias = self.deconv2d.bias
        self.register_buffer('qweight', torch.zeros_like(self.weight))
        self.register_buffer('qbias', torch.zeros_like(self.bias) if self.bias is not None else None)
        self.register_buffer('qweight_scale', torch.ones(deconv2d_module.out_channels, 1, 1, 1))

    def forward(self, input):
        qinput = self.quantize_inputs[0](input)
        weight_qparams = calculate_qparams(
            self.weight.transpose(0, 1), num_bits=self.num_bits_weight, flatten_dims=(
                1, -1), reduce_dim=None, sym=True)

        if not self.disable_quant:
            qweight = quantize(self.weight.transpose(0, 1), qparams=weight_qparams,
                               sym=True, doNothing=self.disable_quant).transpose(0, 1)
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
        output = F.conv_transpose2d(
            qinput,
            qweight,
            qbias,
            stride=self.deconv2d.stride,
            padding=self.deconv2d.padding,
            output_padding=self.deconv2d.output_padding,
            dilation=self.deconv2d.dilation,
            groups=self.deconv2d.groups)
        if self.num_bits_grad is not None:
            output = quantize_grad(
                output, num_bits=self.num_bits_grad, flatten_dims=(
                    1, -1), doNothing=self.disable_quant)

        qoutput = self.quantize_outputs[0](output)
        return qoutput
